"""Fast stdlib-only TARGET audit replay (exact QQ + F_p checks, no sympy).
Checks: Hilbert (1,4,9,4,1)/dim19; claimed [5,3,3,3,1,1] sums to 16 -> impossible;
general-ell Jordan = [5,3,3,3,1,1,1,1,1]; WLP+SLP ranks at ell=(1,1,1,1);
Hessian det polys nonzero with recorded evaluations; Ann_2 = span(x0^2)."""
from itertools import combinations_with_replacement
from fractions import Fraction
Nvars,D=4,4
def mons(k): return list(combinations_with_replacement(range(Nvars),k))
def tup2exp(t):
    e=[0]*Nvars
    for i in t: e[i]+=1
    return tuple(e)
F={(1,1,1,1):1,(0,4,0,0):1,(0,0,4,0):1,(0,0,0,4):1}
def diff_once(poly,i):
    out={}
    for e,c in poly.items():
        if e[i]>0:
            ne=list(e); ne[i]-=1; ne=tuple(ne)
            out[ne]=out.get(ne,0)+c*e[i]
    return out
def apply_op(t,poly):
    for i in t: poly=diff_once(poly,i)
    return poly
def rank_qq(M):
    A=[[Fraction(x) for x in row] for row in M]; m=len(A); n=len(A[0]) if m else 0; r=0
    for c in range(n):
        q=next((i for i in range(r,m) if A[i][c]!=0),None)
        if q is None: continue
        A[r],A[q]=A[q],A[r]; inv=1/A[r][c]; A[r]=[x*inv for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]!=0:
                f=A[i][c]; A[i]=[a-f*b for a,b in zip(A[i],A[r])]
        r+=1
    return r
def rref_piv(M):
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
# 1. Hilbert
Ck,Piv,H={},{},{}
for k in range(D+1):
    rows=mons(D-k); cols=mons(k); ridx={tup2exp(t):j for j,t in enumerate(rows)}
    M=[[0]*len(cols) for _ in rows]
    for j,t in enumerate(cols):
        for mon,c in apply_op(t,dict(F)).items():
            if sum(mon)==D-k and mon in ridx: M[ridx[mon]][j]=c
    Ck[k]=M; Piv[k]=rref_piv(M); H[k]=len(Piv[k])
hf=[H[k] for k in range(5)]
print("Hilbert:",hf,"dim:",sum(hf))
assert hf==[1,4,9,4,1],hf
assert sum(hf)==19
# 2. Target arithmetic impossibility
claim=[5,3,3,3,1,1]
print("claimed:",claim,"sum:",sum(claim))
assert sum(claim)==16
assert sum(claim)!=sum(hf)
print("TARGET-PARTITION-IMPOSSIBLE: 16 != 19")
# 3. Ann_2 kernel is span(x0^2)
M2=Ck[2]
# nullspace dim = 10-9 = 1; check x0^2 dies, others don't span
print("x0^2 acts:",apply_op((0,0),dict(F)))
assert apply_op((0,0),dict(F))=={}
assert H[2]==9
# 4. Multiplication + Jordan at ell=(1,1,1,1)
def solve_proj(C,piv,rhs):
    m=len(C); h=len(piv)
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
def mult_mat(k,ell):
    ck=mons(k); ck1=mons(k+1); idx1={t:j for j,t in enumerate(ck1)}
    Mk=[[Fraction(0)]*H[k] for _ in range(H[k+1])]
    for j,t in enumerate(ck):
        if j not in Piv[k]: continue
        pj=Piv[k].index(j)
        for i,c in enumerate(ell):
            if c==0: continue
            nt=tuple(sorted(t+(i,)))
            v=[0]*len(ck1); v[idx1[nt]]=c
            C=Ck[k+1]; rhs=[sum(C[r][s]*v[s] for s in range(len(v))) for r in range(len(C))]
            cc=solve_proj(C,Piv[k+1],rhs)
            for r_ in range(H[k+1]): Mk[r_][pj]+=cc[r_]
    return Mk
def rank_m(M): return rank_qq([[float(x) if False else x for x in row] for row in M])
ell=[1,1,1,1]
Ms={k:mult_mat(k,ell) for k in range(D)}
rks=tuple(rank_qq(Ms[k]) for k in range(4))
print("WLP ranks:",rks)
assert rks==(1,4,4,1),rks
# powers for SLP: x^2:A1->A3, x^4:A0->A4
def matmul(A,B):
    m=len(A); k=len(B); n=len(B[0])
    return [[sum(A[i][t]*B[t][j] for t in range(k)) for j in range(n)] for i in range(m)]
def det4(M):
    # exact 4x4 det via Fractions
    import copy
    A=[[Fraction(x) for x in row] for row in M]; n=4; d=Fraction(1)
    for c in range(n):
        q=next((i for i in range(c,n) if A[i][c]!=0),None)
        if q is None: return Fraction(0)
        if q!=c: A[c],A[q]=A[q],A[c]; d=-d
        d*=A[c][c]; inv=1/A[c][c]
        for i in range(c+1,n):
            f=A[i][c]*inv
            for j in range(c,n): A[i][j]-=f*A[c][j]
    return d
E2=matmul(Ms[2],Ms[1]); E4=matmul(matmul(matmul(Ms[3],Ms[2]),Ms[1]),Ms[0])
d2=det4(E2)
print("det x^2:A1->A3 =",d2,"(expect -5808)")
assert d2==Fraction(-5808),d2
print("x^4:A0->A4 =",E4[0][0],"(expect 96)")
assert E4[0][0]==Fraction(96),E4[0][0]
# Jordan via nullities
offs=[0]
for k in range(5): offs.append(offs[-1]+H[k])
n=offs[-1]
N=[[Fraction(0)]*n for _ in range(n)]
for k in range(D):
    for a in range(H[k]):
        for b in range(H[k+1]):
            N[offs[k+1]+b][offs[k]+a]=Ms[k][b][a]
nulls=[0]; P=[row[:] for row in N]
for j in range(1,8):
    if j>1: P=matmul(P,N)
    nulls.append(n-rank_qq(P))
dblocks=[nulls[j]-nulls[j-1] for j in range(1,len(nulls))]
blocks=[]; rem=list(dblocks)
while any(x>0 for x in rem):
    blocks.append(sum(1 for x in rem if x>0)); rem=[x-1 for x in rem]
print("nullities:",nulls,"Jordan:",blocks)
assert tuple(blocks)==(5,3,3,3,1,1,1,1,1),blocks
# conjugate check
h=hf; conj=sorted([sum(1 for x in h if x>j) for j in range(max(h))],reverse=True)
print("conjugate(HF):",conj)
assert tuple(conj)==tuple(blocks)
# 5. Hessian evaluations (integer arithmetic)
def hess_det(pt):
    X0,U,V,W=pt
    Hm=[[0,V*W,U*W,U*V],[V*W,12*U*U,W*X0,V*X0],[U*W,W*X0,12*V*V,U*X0],[U*V,V*X0,U*X0,12*W*W]]
    # det via Fractions
    A=[[Fraction(x) for x in row] for row in Hm]; n=4; d=Fraction(1)
    for c in range(n):
        q=next((i for i in range(c,n) if A[i][c]!=0),None)
        if q is None: return Fraction(0)
        if q!=c: A[c],A[q]=A[q],A[c]; d=-d
        d*=A[c][c]; inv=1/A[c][c]
        for i in range(c+1,n):
            f=A[i][c]*inv
            for j in range(c,n): A[i][j]-=f*A[c][j]
    return d
for pt,exp in [((1,1,1,1),-363),((1,2,3,5),-8399484),((0,1,1,1),-432)]:
    v=hess_det(pt); print(f"detH{pt} =",v); assert v==exp,v
print("VERIFY_OK")
