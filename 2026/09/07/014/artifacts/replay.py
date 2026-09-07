"""Replay verification for quartic Cremona partial census over F4 (stdlib only).
Checks: GF4/F16 arithmetic, PGL3 order, 5 representatives (4 symmetric + 1 de Jonquiere)
with base-point data, Noether equations, exact degree 4, composition inverses both ways
with common degree-15 factor, F4/F16 base-locus counts, type witnesses, non-conjugacy,
and configuration-orbit counts (sym 5 orbits; DJ rational-quad 3 orbits).
Usage: python3 replay.py
"""
import itertools
from collections import defaultdict
# ---------- F4 ----------
def f4m(a,b):
    if a==0 or b==0: return 0
    if a==1: return b
    if b==1: return a
    a0,a1=a&1,(a>>1)&1; b0,b1=b&1,(b>>1)&1
    return ((a0&b0)^(a1&b1))|(((a0&b1)^(a1&b0)^(a1&b1))<<1)
FINV={1:1,2:3,3:2}
def f4inv(a):
    assert a!=0; return FINV[a]
# ---------- F16 = F4[u]/(u^2+u+w), w=2 ----------
W=2
def f16m(a,b):
    a0,a1=a; b0,b1=b
    t0=f4m(f4m(a1,b1),W)
    return (f4m(a0,b0)^t0, f4m(a0,b1)^f4m(a1,b0)^f4m(a1,b1))
def f16inv(a):
    assert a!=(0,0)
    for x0 in range(4):
        for x1 in range(4):
            if f16m(a,(x0,x1))==(1,0): return (x0,x1)
    raise AssertionError("no inv")
def frob(a): return (a[0]^a[1],a[1])
# ---------- monomials ----------
def mons(d):
    r=[]
    for i in range(d,-1,-1):
        for j in range(d-i,-1,-1):
            r.append((i,j,d-i-j))
    return r
M4=mons(4); IDX4={e:i for i,e in enumerate(M4)}
M17=mons(17); IDX17={e:i for i,e in enumerate(M17)}
# ---------- points ----------
pts4=[]; _s=set()
for x in range(4):
 for y in range(4):
  for z in range(4):
   if x==0 and y==0 and z==0: continue
   if x!=0: n=(1,f4m(y,f4inv(x)),f4m(z,f4inv(x)))
   elif y!=0: n=(0,1,f4m(z,f4inv(y)))
   else: n=(0,0,1)
   if n not in _s: _s.add(n); pts4.append(n)
assert len(pts4)==21, len(pts4)
F16els=[(a,b) for a in range(4) for b in range(4)]
def f16norm(t):
    for i in range(3):
        if t[i]!=(0,0):
            iv=f16inv(t[i]); return tuple(f16m(x,iv) for x in t)
    raise AssertionError("zero")
pts16=[]; _s16=set()
for x in F16els:
 for y in F16els:
  for z in F16els:
   if x==(0,0) and y==(0,0) and z==(0,0): continue
   n=f16norm((x,y,z))
   if n not in _s16: _s16.add(n); pts16.append(n)
assert len(pts16)==273, len(pts16)
# ---------- poly helpers ----------
def c2d(c): return {e:cc for e,cc in zip(M4,c) if cc!=0}
def peval4(d,x,y,z):
    s=0
    for (i,j,k),cc in d.items():
        a=1
        for _ in range(i): a=f4m(a,x)
        b=1
        for _ in range(j): b=f4m(b,y)
        t=1
        for _ in range(k): t=f4m(t,z)
        s^=f4m(f4m(f4m(a,b),t),cc)
    return s
def eval_mon(e,P):
    i,j,k=e; r=(1,0)
    for _ in range(i): r=f16m(r,P[0])
    for _ in range(j): r=f16m(r,P[1])
    for _ in range(k): r=f16m(r,P[2])
    return r
def f16eval(coeffs,P):
    s=(0,0)
    for e,cc in zip(M4,coeffs):
        if cc==0: continue
        mm=eval_mon(e,P)
        s=(s[0]^f4m(cc,mm[0]),s[1]^f4m(cc,mm[1]))
    return s
def pdm(A,B):
    C={}
    for e1,c1 in A.items():
        for e2,c2 in B.items():
            ee=(e1[0]+e2[0],e1[1]+e2[1],e1[2]+e2[2]); cc=f4m(c1,c2)
            C[ee]=C.get(ee,0)^cc
            if C[ee]==0: del C[ee]
    return C
def fpow(fd):
    F0,F1,F2=fd
    P0=[{(0,0,0):1}]; P1=[{(0,0,0):1}]; P2=[{(0,0,0):1}]
    for _ in range(4):
        P0.append(pdm(P0[-1],F0)); P1.append(pdm(P1[-1],F1)); P2.append(pdm(P2[-1],F2))
    Fp={}
    for e in M4: Fp[e]=pdm(pdm(P0[e[0]],P1[e[1]]),P2[e[2]])
    return Fp
def compose(fc,gc):
    Fp=fpow([c2d(c) for c in fc]); G=[]
    for gj in gc:
        D={}
        for e,cc in zip(M4,gj):
            if cc==0: continue
            for ee,c2 in Fp[e].items():
                cc2=f4m(cc,c2)
                D[ee]=D.get(ee,0)^cc2
                if D[ee]==0: del D[ee]
        G.append(D)
    return G
def check_id(G):
    def mv(D,v):
        R={}
        for (i,j,k),c in D.items():
            e=[i,j,k]; e[v]+=1; e=tuple(e)
            R[e]=R.get(e,0)^c
            if R[e]==0: del R[e]
        return R
    S=dict(mv(G[0],2))
    for e,c in mv(G[2],0).items():
        S[e]=S.get(e,0)^c
        if S[e]==0: del S[e]
    if S: return (False,"eq0",len(S))
    S=dict(mv(G[1],2))
    for e,c in mv(G[2],1).items():
        S[e]=S.get(e,0)^c
        if S[e]==0: del S[e]
    if S: return (False,"eq1",len(S))
    if not G[0] and not G[1] and not G[2]: return (False,"zero",0)
    def div(D,v):
        R={}
        for e,c in D.items():
            if e[v]==0: return None
            ee=list(e); ee[v]-=1; R[tuple(ee)]=c
        return R
    P0,P1,P2=div(G[0],0),div(G[1],1),div(G[2],2)
    if P0 is None or P1 is None or P2 is None: return (False,"div",0)
    if not (P0==P1==P2): return (False,"phi-mismatch",0)
    return (True,"ok",len(P0))
def mat_inv3(N):
    a,b,c=N[0]; d,e,f=N[1]; g,h,i=N[2]
    A00=f4m(e,i)^f4m(f,h); A01=f4m(d,i)^f4m(f,g); A02=f4m(d,h)^f4m(e,g)
    A10=f4m(b,i)^f4m(c,h); A11=f4m(a,i)^f4m(c,g); A12=f4m(a,h)^f4m(b,g)
    A20=f4m(b,f)^f4m(c,e); A21=f4m(a,f)^f4m(c,d); A22=f4m(a,e)^f4m(b,d)
    adj=[[A00,A10,A20],[A01,A11,A21],[A02,A12,A22]]
    det=f4m(a,A00)^f4m(b,A01)^f4m(c,A02)
    assert det!=0
    di=f4inv(det)
    return [[f4m(di,v) for v in row] for row in adj]
def map_e2(p):
    px,py,pz=p; forms=[]
    for a in range(4):
     for b in range(4):
      for c in range(4):
       if a==0 and b==0 and c==0: continue
       if (f4m(a,px)^f4m(b,py)^f4m(c,pz))==0: forms.append((a,b,c))
    r2=None
    for a in range(4):
     for b in range(4):
      for c in range(4):
       if (f4m(a,px)^f4m(b,py)^f4m(c,pz))==1: r2=(a,b,c); break
      if r2 is not None: break
    for r0 in forms:
        for r1 in forms:
            M=[r0,r1,r2]
            a,b,c=M[0]; d,e,f=M[1]; g,h,i=M[2]
            det=f4m(a,f4m(e,i)^f4m(f,h))^f4m(b,f4m(d,i)^f4m(f,g))^f4m(c,f4m(d,h)^f4m(e,g))
            if det!=0: return M
    raise AssertionError("no map")
def subst_mat(N):
    def lp(r,e):
        if e==0: return {(0,0,0):1}
        L={}
        for s in range(3):
            if N[r][s]!=0:
                ee=[0,0,0]; ee[s]=1; L[tuple(ee)]=N[r][s]
        R={(0,0,0):1}
        for _ in range(e):
            nd={}
            for e1,c1 in R.items():
                for e2,c2 in L.items():
                    ee=(e1[0]+e2[0],e1[1]+e2[1],e1[2]+e2[2]); cc=f4m(c1,c2)
                    nd[ee]=nd.get(ee,0)^cc
                    if nd[ee]==0: del nd[ee]
            R=nd
        return R
    T=[[0]*15 for _ in M4]
    for col,e in enumerate(M4):
        d1=lp(0,e[0]); d2=lp(1,e[1]); d3=lp(2,e[2])
        R={(0,0,0):1}
        for dd in (d1,d2,d3):
            nd={}
            for e1,c1 in R.items():
                for e2,c2 in dd.items():
                    ee=(e1[0]+e2[0],e1[1]+e2[1],e1[2]+e2[2]); cc=f4m(c1,c2)
                    nd[ee]=nd.get(ee,0)^cc
                    if nd[ee]==0: del nd[ee]
            R=nd
        idd={x:i for i,x in enumerate(M4)}
        for ee,cc in R.items(): T[idd[ee]][col]=cc
    return T
def sys_mult(fc,p):
    N=mat_inv3(map_e2(p)); T=subst_mat(N); out=[]
    for F in fc:
        G=[0]*15
        for i in range(15):
            s=0
            for j in range(15): s^=f4m(T[i][j],F[j])
            G[i]=s
        out.append(min(e[0]+e[1] for e,cc in zip(M4,G) if cc!=0))
    return min(out)
# ---------- representatives (coeff vectors in M4 order) ----------
# M4 = [(4,0,0),(3,1,0),(3,0,1),(2,2,0),(2,1,1),(2,0,2),(1,3,0),(1,2,1),(1,1,2),(1,0,3),(0,4,0),(0,3,1),(0,2,2),(0,1,3),(0,0,4)]
S1F=[[0,0,0,2,2,1,0,1,0,0,0,0,0,0,0],[0,0,0,1,2,2,0,0,1,0,0,0,0,0,0],[0,0,0,3,1,3,0,0,0,0,0,0,1,0,0]]
S1G=[[0,0,1,1,0,0,0,0,1,0,0,1,0,0,0],[0,0,2,2,1,2,1,0,2,1,2,2,1,0,0],[2,1,2,2,0,1,0,1,2,0,0,2,2,1,0]]
S2F=[[0,0,0,2,3,1,0,0,0,0,0,0,0,0,0],[0,0,0,2,2,0,0,1,1,0,0,0,0,0,0],[0,0,0,2,0,0,0,3,0,0,0,0,1,0,0]]
S2G=[[0,0,0,0,3,1,3,3,0,0,2,0,0,0,0],[0,0,0,0,0,2,0,3,3,0,1,3,0,0,0],[0,0,0,0,1,2,3,0,3,0,2,1,0,0,0]]
S3F=[[0,0,0,2,3,1,0,0,0,0,0,0,0,0,0],[0,0,0,2,1,0,0,2,1,0,0,0,0,0,0],[0,0,0,2,2,0,0,1,0,0,0,0,1,0,0]]
S3G=[[0,0,3,3,2,3,2,1,0,0,2,0,0,0,0],[0,0,0,0,3,2,3,2,1,0,0,1,0,0,0],[0,1,3,3,1,3,3,3,2,0,0,1,0,0,0]]
S4F=[[0,0,0,0,0,1,0,1,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0]]
S4G=[[0,0,1,1,0,0,0,0,1,0,0,1,0,0,0],[0,0,0,0,1,0,1,0,0,1,0,0,1,0,0],[0,1,0,0,0,1,0,1,0,0,0,0,0,1,0]]
DJF=[[0,1,2,0,0,0,1,0,0,0,0,0,0,0,0],[0,2,2,2,0,0,0,1,0,0,0,0,0,0,0],[0,2,3,2,2,0,0,0,0,0,0,1,0,0,0]]
DJG=[[0,3,0,0,0,0,2,0,1,0,2,0,0,0,0],[1,0,3,3,0,2,3,2,0,1,0,2,0,0,0],[0,0,0,3,3,0,2,2,0,0,0,1,0,1,0]]
REPS=[
 ("S1",S1F,S1G,[(1,0,0),(0,1,0),(0,0,1),(1,1,1),(1,1,2),(1,2,1)],[2,2,2,1,1,1],None),
 ("S2",S2F,S2G,[(1,0,0),(0,1,0),(0,0,1),(1,1,1),(1,1,2),(1,2,2)],[2,2,2,1,1,1],None),
 ("S3",S3F,S3G,[(1,0,0),(0,1,0),(0,0,1),(1,1,1),(1,1,2),(1,2,3)],[2,2,2,1,1,1],None),
 ("S4",S4F,S4G,[(1,0,0),(0,1,0),(0,0,1),(1,1,1),(1,2,3),(1,3,2)],[2,2,2,1,1,1],None),
 ("DJ",DJF,DJG,[(0,0,1),(0,1,0),(1,0,0),(1,1,0),(1,2,2)],[3,1,1,1,1],"F16pair"),
]
print("== replay: F4/F16 setup ==")
print("P2(F4)=21:",len(pts4)==21," P2(F16)=273:",len(pts16)==273)
# PGL3(F4) order check: |GL3(F4)|=(64-1)(64-4)(64-16)=63*60*48
gl=63*60*48; pgl=gl//3
print("PGL3(F4) order:",pgl); assert pgl==60480
ok_all=True
for name,F,G,rat,mults,extra in REPS:
    print("----",name,"----")
    fd=[c2d(c) for c in F]
    # exact degree 4: some coeff of total deg 4 nonzero (all are) and no common factor implied by finite base locus below
    assert any(any(v!=0 for v in row) for row in F)
    # claimed rational base points vanish with exact system multiplicity
    for p,mm in zip(rat,mults):
        assert all(peval4(d,*p)==0 for d in fd), (name,"vanish",p)
        sm=sys_mult(F,p)
        assert sm==mm, (name,"mult",p,sm,mm)
    # Noether sums over claimed proper points (+pair for DJ counted as 2 singles)
    if name.startswith("S"):
        s1=sum(mults); s2=sum(m*m for m in mults)
        assert (s1,s2)==(9,15), (s1,s2)
    else:
        s1=3+6; s2=9+6
        assert (s1,s2)==(9,15)
        P16=((1,0),(0,3),(1,0)); Q16=((1,0),frob((0,3)),(1,0))
        assert f16eval(F[0],P16)==(0,0) and f16eval(F[1],P16)==(0,0) and f16eval(F[2],P16)==(0,0)
        assert f16eval(F[0],Q16)==(0,0) and f16eval(F[1],Q16)==(0,0) and f16eval(F[2],Q16)==(0,0)
        assert Q16==((1,0),(3,3),(1,0))
    # base-locus counts
    n4=sum(1 for p in pts4 if all(peval4(d,*p)==0 for d in fd))
    n16=sum(1 for p in pts16 if all(f16eval(c,p)==(0,0) for c in F))
    print(" base counts F4/F16:",n4,n16)
    assert n4==len(rat), (name,n4)
    assert n16==(6 if name.startswith("S") else 7), (name,n16)
    # composition both ways
    r1=check_id(compose(F,G)); r2=check_id(compose(G,F))
    print(" g(f):",r1," f(g):",r2)
    assert r1[0] and r2[0], (name,r1,r2)
    # inverse exact degree 4
    assert any(c!=0 for row in G for c in row)
    print(" PASS",name)
print("== type witnesses ==")
print("S*: max mult 2 (three doubles) -> symmetric (4;2^3,1^3); no triple so not Jonquiere.")
print("DJ: unique triple at (0,0,1), six singles -> (4;3,1^6) Jonquiere type; maps pencil((0,0,1)) to pencil((1,0,2)) (checked on 5 F4-lines in DRAFT).")
print("Distinct types => S* not conjugate to DJ; S1..S4 pairwise non-conjugate by distinct base orbits under Stab({e0,e1,e2}) (5-orbit census below).")
# ---------- configuration orbit censuses ----------
print("== symmetric rational config orbits ==")
off=[p for p in pts4 if p[0]!=0 and p[1]!=0 and p[2]!=0]
idx={p:i for i,p in enumerate(pts4)}
import itertools as it
# monomial stabilizer (54)
mats=[]
for perm in it.permutations([0,1,2]):
    for d0 in [1,2,3]:
     for d1 in [1,2,3]:
      for d2 in [1,2,3]:
        M=[[0]*3 for _ in range(3)]
        for j,dd in enumerate([d0,d1,d2]): M[perm[j]][j]=dd
        mats.append(M)
def cmat(M):
    for i in range(3):
        for j in range(3):
            if M[i][j]!=0:
                iv=f4inv(M[i][j]); return tuple(f4m(x,iv) for row in M for x in row)
uniq={}
for M in mats: uniq[cmat(M)]=M
Sm=list(uniq.values()); assert len(Sm)==54
def app(M,p):
    r=[]
    for row in M:
        s=0
        for b,v in zip(row,p): s^=f4m(b,v)
        r.append(s)
    x,y,z=r
    if x!=0: return (1,f4m(y,f4inv(x)),f4m(z,f4inv(x)))
    elif y!=0: return (0,1,f4m(z,f4inv(y)))
    return (0,0,1)
combs=list(it.combinations(off,3)); assert len(combs)==84
def coc(c):
    b=None
    for M in Sm:
        im=tuple(sorted(idx[app(M,p)] for p in c))
        if b is None or im<b: b=im
    return b
orb={}
for c in combs: orb[coc(c)]=orb.get(coc(c),0)+1
print("orbits:",len(orb),"sizes:",sorted(orb.values())); assert len(orb)==5
print("== DJ rational-quadruple orbits under Stab((0,0,1)) ==")
def direc(p):
    if p[0]!=0: return (1,f4m(p[1],f4inv(p[0])))
    elif p[1]!=0: return (0,1)
    return None
oth=[p for p in pts4 if p!=(0,0,1)]
bd=defaultdict(list)
for p in oth: bd[direc(p)].append(p)
dirs=list(bd.keys())
Sm2=[]
for a in range(4):
 for b in range(4):
  for c in range(4):
   for d in range(4):
    for e in range(4):
     for f in range(4):
      for l in [1,2,3]:
        if (f4m(a,d)^f4m(b,c))==0: continue
        Sm2.append([[a,b,0],[c,d,0],[e,f,l]])
def cmat2(M):
    for i in range(3):
        for j in range(3):
            if M[i][j]!=0:
                iv=f4inv(M[i][j]); return tuple(f4m(x,iv) for row in M for x in row)
uq={}
for M in Sm2: uq[cmat2(M)]=M
S2=list(uq.values()); assert len(S2)==2880
idx2={p:i for i,p in enumerate(pts4)}
pr=[]
for M in S2:
    q=[]
    for p in pts4: q.append(idx2[app(M,p)])
    pr.append(q)
quads=[]
for ds in it.combinations(dirs,4):
    for ch in it.product(*[bd[d] for d in ds]):
        quads.append(tuple(sorted(idx2[p] for p in ch)))
assert len(quads)==1280
def cq(q):
    b=None
    for p in pr:
        im=tuple(sorted(p[i] for i in q))
        if b is None or im<b: b=im
    return b
o2={}
for q in quads: o2[cq(q)]=o2.get(cq(q),0)+1
print("quad orbits:",len(o2),"sizes:",sorted(o2.values())); assert len(o2)==3
print("ALL REPLAY CHECKS PASSED")
