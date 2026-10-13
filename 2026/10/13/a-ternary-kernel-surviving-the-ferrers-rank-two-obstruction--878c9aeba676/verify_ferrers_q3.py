#!/usr/bin/env python3
from itertools import product, combinations
from collections import Counter
P=3
F=[1,0,1,1,1]  # 1 + x^2 + x^3 + x^4
U_BASIS=[[[0, 1, 1, 1], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[2, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 2, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 2, 0], [0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 1, 1, 0], [0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 1, 1], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]], [[2, 0, 2, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]], [[0, 2, 0, 2], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0]], [[0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]], [[0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0]], [[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0]], [[2, 0, 2, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]]
H=[[0, 2, 1, 0, 2, 1, 1, 2, 1, 0, 2, 2], [0, 1, 0, 0, 1, 1, 2, 1, 1, 1, 0, 1]]

def inv(a):
    a%=P
    assert a
    return 1 if a==1 else 2

def rref(A):
    A=[[x%P for x in row] for row in A]
    if not A: return A,[]
    m,n=len(A),len(A[0]); piv=[]; r=0
    for c in range(n):
        pivrow=next((i for i in range(r,m) if A[i][c]%P),None)
        if pivrow is None: continue
        A[r],A[pivrow]=A[pivrow],A[r]
        z=inv(A[r][c]); A[r]=[(z*x)%P for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]%P:
                z=A[i][c]%P; A[i]=[(A[i][j]-z*A[r][j])%P for j in range(n)]
        piv.append(c); r+=1
        if r==m: break
    return A,piv

def rank(A): return len(rref(A)[1])

def nullspace(A):
    R,piv=rref(A); n=len(R[0]); free=[j for j in range(n) if j not in piv]; out=[]
    for f in free:
        v=[0]*n; v[f]=1
        for i,c in enumerate(piv): v[c]=(-R[i][f])%P
        out.append(v)
    return out

def flat(A): return [x for row in A for x in row]
def dot(A,B): return sum(a*b for a,b in zip(flat(A),flat(B)))%P

def pmul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]=(c[i+j]+x*y)%P
    while len(c)>4:
        d=c[-1]%P; deg=len(c)-1
        if d:
            shift=deg-4
            for i in range(5): c[shift+i]=(c[shift+i]-d*F[i])%P
        c.pop()
    c += [0]*(4-len(c)); return c

def mult_matrix(a):
    cols=[]
    for j in range(4):
        b=[0]*4; b[j]=1; cols.append(pmul(a,b))
    return [[cols[j][i] for j in range(4)] for i in range(4)]

def combine(coeff,basis):
    A=[[0]*4 for _ in range(4)]
    for c,B in zip(coeff,basis):
        if c:
            for i in range(4):
                for j in range(4): A[i][j]=(A[i][j]+c*B[i][j])%P
    return A

def canon_plane_from_kernel(M):
    N=nullspace(M)
    assert len(N)==2
    R,piv=rref(N)
    return tuple(tuple(row) for row in R if any(row))

def all_planes():
    s=set()
    vecs=[v for v in product(range(P),repeat=4) if any(v)]
    for a,b in combinations(vecs,2):
        if rank([a,b])==2:
            R,_=rref([a,b]); s.add(tuple(tuple(row) for row in R if any(row)))
    return s

def irreducible_quartic():
    # A reducible quartic over F_3 has a linear factor or a monic quadratic factor.
    def evalp(a): return sum(F[i]*pow(a,i,P) for i in range(5))%P
    assert all(evalp(a)!=0 for a in range(P))
    for b,c in product(range(P),repeat=2):
        q=[c,b,1]
        # long divide F by q
        r=F[:]
        for d in range(4,1,-1):
            z=r[d]%P
            if z:
                for i in range(3): r[d-2+i]=(r[d-2+i]-z*q[i])%P
        assert any(r[:2])

def main():
    irreducible_quartic()
    S=[mult_matrix([1,0,0,0]),mult_matrix([0,1,0,0]),mult_matrix([0,0,1,0]),mult_matrix([0,0,0,1])]
    assert rank([flat(B) for B in S])==4
    assert rank([flat(B) for B in U_BASIS])==12
    assert all(dot(A,B)==0 for A in S for B in U_BASIS)
    hist=Counter()
    for c in product(range(P),repeat=12): hist[rank(combine(c,U_BASIS))]+=1
    assert hist==Counter({4:300240,3:220800,2:10400,0:1}),hist
    Kcoeff=nullspace(H)
    assert len(Kcoeff)==10
    kh=Counter()
    for a in product(range(P),repeat=10):
        c=[sum(a[i]*Kcoeff[i][j] for i in range(10))%P for j in range(12)]
        M=combine(c,U_BASIS); rr=rank(M)
        if rr==2: kh[canon_plane_from_kernel(M)]+=1
    assert sum(kh.values())==1040
    assert len(kh)==130
    assert set(kh.values())=={8}
    planes=all_planes()
    assert len(planes)==130 and set(kh)==planes
    print('U_RANK_DISTRIBUTION',dict(sorted(hist.items())))
    print('K_RANK2',sum(kh.values()),'PLANES',len(kh),'EACH',next(iter(kh.values())))
    print('VERIFY_OK')
if __name__=='__main__': main()
