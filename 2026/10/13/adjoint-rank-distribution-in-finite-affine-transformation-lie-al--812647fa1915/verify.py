"""Independent finite-field checks of affine Lie adjoint-centralizer laws.
Run: python verify.py
This program is finite evidence, not a proof for unbounded dimensions.
"""
from itertools import product
from collections import Counter
import random


def ops(q):
    if q == 4:
        def mul(a,b):
            r=0
            for i in range(2):
                if (b>>i)&1:r^=a<<i
            if r&8:r^=0b1100
            if r&4:r^=0b111
            return r
        return (lambda a,b:a^b), (lambda a:-a if False else a),mul
    return (lambda a,b:(a+b)%q), (lambda a:(-a)%q), (lambda a,b:(a*b)%q)


def rank(M,q):
    if not M:return 0
    add,neg,mul=ops(q)
    a=[list(r) for r in M]; m=len(a); n=len(a[0]); pos=0
    for j in range(n):
        pivot=next((k for k in range(pos,m) if a[k][j]),None)
        if pivot is None:continue
        a[pos],a[pivot]=a[pivot],a[pos]
        inv=next(k for k in range(1,q) if mul(k,a[pos][j])==1)
        a[pos]=[mul(inv,t) for t in a[pos]]
        for h in range(m):
            if h==pos or not a[h][j]:continue
            b=a[h][j]
            a[h]=[add(x,neg(mul(b,y))) for x,y in zip(a[h],a[pos])]
        pos+=1
        if pos==m:break
    return pos


def matmul(A,B,q):
    add,_,mul=ops(q)
    n=len(A);m=len(B[0]);k=len(B)
    return [[sum((mul(A[i][h],B[h][j]) for h in range(k)),0)%q if q!=4 else fold([mul(A[i][h],B[h][j]) for h in range(k)],add) for j in range(m)] for i in range(n)]


def fold(vals,op):
    a=0
    for b in vals:a=op(a,b)
    return a


def formula(A,u,q):
    n=len(A);add,neg,mul=ops(q)
    flat=[]
    for i in range(n):
        for j in range(n):
            B=[[int((a,b)==(i,j)) for b in range(n)] for a in range(n)]
            AB=matmul(A,B,q);BA=matmul(B,A,q)
            flat.append([add(AB[x][y],neg(BA[x][y])) for x in range(n) for y in range(n)])
    c=n*n-rank(list(zip(*flat)),q)
    rk=rank(A,q);k=n-rk
    M=[list(A[i]) for i in range(n)]
    L=0
    def aug_rank(N,vec):
        return rank([row+[v] for row,v in zip(N,vec)],q)
    if aug_rank(A,u)>rk:
        # Since ker A^L added to im A, enumerate kernel basis by Gaussian rank via augmented image A with ker(A^L).
        # Instead use rank([A, u, A^L]) criterion via invariant kernel basis.
        P=[row[:] for row in A]
        for ll in range(1,n+1):
            kernel=kernel_basis(P,q)
            N=[A[i]+[v[i] for v in kernel] for i in range(n)]
            if aug_rank(N,u)==rank(N,q):
                L=ll
                break
            P=matmul(P,A,q)
        assert L>0
    if L==0:t=0
    else:
        P=[row[:] for row in A]
        for _ in range(L-1):P=matmul(P,A,q)
        kernel=kernel_basis(P,q)
        N=[A[i]+[v[i] for v in kernel] for i in range(n)]
        t=rank(N,q)-rk
    return n*n+n-c-k+t,c,k,L,t


def kernel_basis(A,q):
    add,neg,mul=ops(q)
    a=[list(x) for x in A];m=len(a); n=len(a[0]);piv=[];p=0
    for j in range(n):
        pos=next((i for i in range(p,m) if a[i][j]),None)
        if pos is None:continue
        a[pos],a[p]=a[p],a[pos]
        inv=next(k for k in range(1,q) if mul(k,a[p][j])==1)
        a[p]=[mul(inv,x) for x in a[p]]
        for i in range(m):
            if i==p or not a[i][j]:continue
            b=a[i][j];a[i]=[add(x,neg(mul(b,y))) for x,y in zip(a[i],a[p])]
        piv.append(j);p+=1
    free=[j for j in range(n) if j not in piv]
    out=[]
    for f in free:
        v=[0]*n;v[f]=1
        for h,j in enumerate(piv):v[j]=neg(a[h][f])
        out.append(v)
    return out


def direct(A,u,q):
    add,neg,mul=ops(q);n=len(A);d=n*n+n
    cols=[]
    for j in range(d):
        B=[[0]*n for _ in range(n)];v=[0]*n
        if j<n*n:B[j//n][j%n]=1
        else:v[j-n*n]=1
        AB=matmul(A,B,q);BA=matmul(B,A,q)
        Bu=[fold([mul(B[i][h],u[h]) for h in range(n)],add) for i in range(n)]
        Av=[fold([mul(A[i][h],v[h]) for h in range(n)],add) for i in range(n)]
        cols.append([add(AB[i][h],neg(BA[i][h])) for i in range(n) for h in range(n)]+[add(Av[i],neg(Bu[i])) for i in range(n)])
    return rank(list(zip(*cols)),q)


def test(q,n,full=False,samples=220):
    rng=random.Random(1629+q*14+n)
    domain=q**(n*n+n)
    if full: cases=product(product(range(q),repeat=n*n),product(range(q),repeat=n))
    else:cases=((tuple(rng.randrange(q) for _ in range(n*n)),tuple(rng.randrange(q) for _ in range(n))) for _ in range(samples))
    cnt=Counter(); entries=0; sumcentral=0
    for aa,u in cases:
        A=[list(aa[i*n:(i+1)*n]) for i in range(n)]
        got=direct(A,u,q);expected,*rest=formula(A,u,q)
        assert got==expected,(q,n,A,u,got,expected,rest)
        cnt[got]+=1; entries+=1;sumcentral+=q**(n*n+n-got)
    if full:assert entries==domain
    print('CHECK',q,n,'full' if full else 'sample','count',entries,'rank_counts',sorted(cnt.items()),'commuting_pairs' if full else 'sample_centralizer_sum',sumcentral)

if __name__=='__main__':
    test(2,2,True)
    test(3,2,True)
    test(2,3,True)
    test(3,3,False,200)
    test(4,3,False,160)
    print('VERIFY_OK')
