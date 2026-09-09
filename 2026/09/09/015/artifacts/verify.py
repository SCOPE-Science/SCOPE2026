"""Independent replay verifier (stdlib + numpy only).
Replays committed Meringer GENREG shortcode files raw_{n}_3_3.scd:
 (1) checks decode counts 19/85/509/4060/41301, 3-regularity, connectivity;
 (2) recomputes lambda2 with Weyl residual enclosure of width<=1e-6;
 (3) re-derives Ramanujan verdicts vs 2*sqrt(2) with zero ambiguous cases;
 (4) verifies per-n maximal-gap extremal identity (unique min-lambda2) and prints table.
Usage: python3 verify.py  (run from output/artifacts/ or anywhere; resolves sibling files)
"""
import os, math, numpy as np
D=os.path.dirname(os.path.abspath(__file__))
RB=2*math.sqrt(2)
def decode(path,n):
    vals=list(open(path,'rb').read()); m=3*n//2
    assert vals[0]==0
    pos=1; first=vals[pos:pos+m]; pos+=m; codes=[first]; prev=first
    while pos<len(vals):
        pre=vals[pos]; pos+=1; suf=vals[pos:pos+(m-pre)]; pos+=len(vals[pos:pos+(m-pre)][:0])+(m-pre)
        code=prev[:pre]+suf; codes.append(code); prev=code
    return codes
def adj_of(code,n):
    pos=0; adj=[[] for _ in range(n)]; deg=[0]*n
    for i in range(n):
        for k in range(3-deg[i]):
            j=code[pos]-1; pos+=1
            assert j>i; adj[i].append(j); adj[j].append(i); deg[j]+=1
    assert pos==len(code) and all(len(a)==3 for a in adj)
    return adj
EXP={10:19,12:85,14:509,16:4060,18:41301}
ok=True
for n,exp in EXP.items():
    codes=decode(os.path.join(D,f'raw_{n}_3_3.scd'),n)
    assert len(codes)==exp,(n,len(codes))
    nram=0; minl=1e9; mini=-1; maxw=0; second=1e9
    lam=[]
    for gi,c in enumerate(codes):
        adj=adj_of(c,n)
        seen={0}; st=[0]
        while st:
            v=st.pop()
            for w_ in adj[v]:
                if w_ not in seen: seen.add(w_); st.append(w_)
        assert len(seen)==n,(n,gi,'disconnected')
        A=np.zeros((n,n))
        for i in range(n):
            for j in adj[i]: A[i,j]=1.0
        wa,V=np.linalg.eigh(A); w=np.sort(wa)[::-1]
        assert abs(w[0]-3.0)<1e-9
        E=A-(V*wa)@V.T; rad=float(np.sqrt(np.sum(E*E)))+1e-12
        maxw=max(maxw,2*rad)
        assert 2*rad<=1e-6
        assert (3.0-1e-12)-(w[1]+rad)>0
        lo,hi=w[1]-rad,w[1]+rad
        assert not (lo<=RB<=hi),(n,gi,'ambiguous')
        if hi<=RB: nram+=1
        lam.append(float(w[1]))
        if w[1]<minl: minl=float(w[1]); mini=gi
    second=min(v for v in lam if abs(v-minl)>=1e-9)
    ties=[i for i,v in enumerate(lam) if abs(v-minl)<1e-9]
    print(f"n={n}: count={len(codes)} Ramanujan={nram}/{len(codes)} minlam2={minl:.10f} idx1={mini+1} unique={len(ties)==1} margin={second-minl:.6f} maxwidth={maxw:.2e}")
    assert len(ties)==1
print("VERIFY_OK")
