"""Characteristic-sensitivity probe of the TARGET object (stdlib only, exact integer/F_p linear algebra).
Proves: char 0 Hilbert is (1,4,9,4,1) [dim 19]; in char 2,3 it drops to (1,4,6,4,1) [dim 16]
because the Fermat-tail 2nd-derivative coefficients 12 vanish mod 2,3.
Exhaustive {0,1,2}^4 ell-scan: target partition [5,3,3,3,1,1] NEVER occurs (char 0 or 3)."""
from itertools import combinations_with_replacement, product
from collections import Counter
from fractions import Fraction

Nvars, D = 4, 4
def mons(k): return list(combinations_with_replacement(range(Nvars), k))
def tup2exp(t):
    e = [0]*Nvars
    for i in t: e[i] += 1
    return tuple(e)
F = {(1,1,1,1):1,(0,4,0,0):1,(0,0,4,0):1,(0,0,0,4):1}
def diff_once(poly,i):
    out = {}
    for e,c in poly.items():
        if e[i]>0:
            ne=list(e); ne[i]-=1; ne=tuple(ne)
            out[ne]=out.get(ne,0)+c*e[i]
    return out
def apply_op(t,poly):
    for i in t: poly=diff_once(poly,i)
    return poly
def rref_piv(M,p):
    if p==0:
        A=[[Fraction(x) for x in row] for row in M]; m=len(A); n=len(A[0])
        piv=[]; r=0
        for c in range(n):
            q=next((i for i in range(r,m) if A[i][c]!=0),None)
            if q is None: continue
            A[r],A[q]=A[q],A[r]; inv=1/A[r][c]; A[r]=[x*inv for x in A[r]]
            for i in range(m):
                if i!=r and A[i][c]!=0:
                    f=A[i][c]; A[i]=[a-f*b for a,b in zip(A[i],A[r])]
            piv.append(c); r+=1
        return piv
    A=[[x%p for x in row] for row in M]; m=len(A); n=len(A[0])
    piv=[]; r=0
    for c in range(n):
        q=next((i for i in range(r,m) if A[i][c]%p!=0),None)
        if q is None: continue
        A[r],A[q]=A[q],A[r]; inv=pow(A[r][c],-1,p); A[r]=[(x*inv)%p for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]%p!=0:
                f=A[i][c]; A[i]=[(a-f*b)%p for a,b in zip(A[i],A[r])]
        piv.append(c); r+=1
    return piv
def build(p):
    Ck,Piv,H={},{},{}
    for k in range(D+1):
        rows=mons(D-k); cols=mons(k)
        ridx={tup2exp(t):j for j,t in enumerate(rows)}
        M=[[0]*len(cols) for _ in rows]
        for j,t in enumerate(cols):
            g=apply_op(t,dict(F))
            for mon,c in g.items():
                if sum(mon)==D-k and mon in ridx: M[ridx[mon]][j]=c
        Ck[k]=M; Piv[k]=rref_piv(M,p); H[k]=len(Piv[k])
    return Ck,Piv,H
def solve_proj(C,piv,rhs,p):
    m=len(C); h=len(piv)
    if p==0:
        CP=[[Fraction(C[i][j]) for j in piv] for i in range(m)]; rhs=[Fraction(x) for x in rhs]
        G=[[sum(CP[i][a]*CP[i][b] for i in range(m)) for b in range(h)] for a in range(h)]
        bvec=[sum(CP[i][a]*rhs[i] for i in range(m)) for a in range(h)]
        A=[row[:]+[bv] for row,bv in zip(G,bvec)]
        for c_ in range(h):
            q=next(i for i in range(c_,h) if A[i][c_]!=0)
            A[c_],A[q]=A[q],A[c_]; inv=1/A[c_][c_]; A[c_]=[x*inv for x in A[c_]]
            for i in range(h):
                if i!=c_ and A[i][c_]!=0:
                    f=A[i][c_]; A[i]=[a-f*bb for a,bb in zip(A[i],A[c_])]
        return [A[i][h] for i in range(h)]
    CP=[[C[i][j]%p for j in piv] for i in range(m)]; rhs=[x%p for x in rhs]
    G=[[sum(CP[i][a]*CP[i][b] for i in range(m))%p for b in range(h)] for a in range(h)]
    bvec=[sum(CP[i][a]*rhs[i] for i in range(m))%p for a in range(h)]
    A=[row[:]+[bv] for row,bv in zip(G,bvec)]
    for c_ in range(h):
        q=next((i for i in range(c_,h) if A[i][c_]%p!=0),None)
        if q is None: raise Exception("singular G")
        A[c_],A[q]=A[q],A[c_]; inv=pow(A[c_][c_],-1,p); A[c_]=[(x*inv)%p for x in A[c_]]
        for i in range(h):
            if i!=c_ and A[i][c_]%p!=0:
                f=A[i][c_]; A[i]=[(a-f*bb)%p for a,bb in zip(A[i],A[c_])]
    return [A[i][h]%p for i in range(h)]
def mult_mat(Ck,Piv,H,k,ell,p):
    ck=mons(k); ck1=mons(k+1); idx1={t:j for j,t in enumerate(ck1)}
    Mk=[[0]*H[k] for _ in range(H[k+1])]
    for j,t in enumerate(ck):
        if j not in Piv[k]: continue
        pj=Piv[k].index(j)
        for i,c in enumerate(ell):
            if (c%p if p else c)==0: continue
            nt=tuple(sorted(t+(i,)))
            v=[0]*len(ck1); v[idx1[nt]]=c
            C=Ck[k+1]; rhs=[sum(C[r][s]*v[s] for s in range(len(v))) for r in range(len(C))]
            if p: rhs=[x%p for x in rhs]
            cc=solve_proj(C,Piv[k+1],rhs,p)
            for r_ in range(H[k+1]):
                Mk[r_][pj]+=cc[r_]
                if p: Mk[r_][pj]%=p
    return Mk
def rank_p(M,p):
    if p==0:
        A=[[Fraction(x) for x in row] for row in M]; m=len(A); n=len(A[0]); r=0
        for c in range(n):
            q=next((i for i in range(r,m) if A[i][c]!=0),None)
            if q is None: continue
            A[r],A[q]=A[q],A[r]; inv=1/A[r][c]; A[r]=[x*inv for x in A[r]]
            for i in range(m):
                if i!=r and A[i][c]!=0:
                    f=A[i][c]; A[i]=[a-f*b for a,b in zip(A[i],A[r])]
            r+=1
        return r
    A=[[x%p for x in row] for row in M]; m=len(A); n=len(A[0]); r=0
    for c in range(n):
        q=next((i for i in range(r,m) if A[i][c]%p!=0),None)
        if q is None: continue
        A[r],A[q]=A[q],A[r]; inv=pow(A[r][c],-1,p); A[r]=[(x*inv)%p for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]%p!=0:
                f=A[i][c]; A[i]=[(a-f*b)%p for a,b in zip(A[i],A[r])]
        r+=1
    return r
def matmul_p(A,B,p):
    m=len(A); k=len(B); n=len(B[0])
    C=[[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            s=0
            for t in range(k): s+=A[i][t]*B[t][j]
            C[i][j]=s%p if p else s
    return C
def jordan_p(p,ell,Ck,Piv,H):
    Ms={k:mult_mat(Ck,Piv,H,k,ell,p) for k in range(D)}
    offs=[0]
    for k in range(5): offs.append(offs[-1]+H[k])
    n=offs[-1]
    N=[[0]*n for _ in range(n)]
    for k in range(D):
        for a in range(H[k]):
            for b in range(H[k+1]):
                N[offs[k+1]+b][offs[k]+a]=Ms[k][b][a]
    nulls=[0]; P=[row[:] for row in N]
    for j in range(1,8):
        if j>1: P=matmul_p(P,N,p)
        nulls.append(n-rank_p(P,p))
    d=[nulls[j]-nulls[j-1] for j in range(1,len(nulls))]
    blocks=[]; rem=list(d)
    while any(x>0 for x in rem):
        blocks.append(sum(1 for x in rem if x>0)); rem=[x-1 for x in rem]
    return tuple(blocks)
target=(5,3,3,3,1,1)
ok=True
for p in [0,2,3,5]:
    Ck,Piv,H=build(p)
    hf=[H[k] for k in range(5)]
    print(f"char {p}: Hilbert {hf} dim {sum(hf)}")
    if p==0: assert hf==[1,4,9,4,1],hf
    if p in (2,3): assert hf==[1,4,6,4,1],hf
    cnt=Counter(); hits=[]
    for ell in product(range(3),repeat=4):
        if all(v==0 for v in ell): continue
        ellp=[v%p for v in ell] if p else list(ell)
        b=jordan_p(p,ellp,Ck,Piv,H)
        assert sum(b)==sum(hf)
        cnt[b]+=1
        if b==target: hits.append(ellp)
    print(f"  Jordan census ({sum(cnt.values())} ells): {dict(cnt)}")
    print(f"  target {target} hits: {hits if hits else 'NONE'}")
    ok = ok and (not hits)
print("TARGET-NEVER-OCCURS:",ok)
print("VERIFY_OK")
