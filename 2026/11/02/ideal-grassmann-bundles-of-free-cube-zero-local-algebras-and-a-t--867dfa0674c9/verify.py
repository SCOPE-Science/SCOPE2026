"""Independent arithmetic tests for two-sided ideals in length-three free local algebras."""
import itertools
from collections import Counter
from math import prod


def rref(rows, q):
    A = [list(map(lambda t: t % q, row)) for row in rows if any(v % q for v in row)]
    if not A:
        return ()
    n = len(A[0]); lead=0; rank=0
    for j in range(n):
        p = next((i for i in range(rank, len(A)) if A[i][j]), None)
        if p is None: continue
        A[rank], A[p] = A[p], A[rank]
        inv = pow(A[rank][j], -1, q)
        A[rank] = [(v*inv)%q for v in A[rank]]
        for i in range(len(A)):
            if i != rank and A[i][j]:
                mul=A[i][j]
                A[i] = [(x-mul*y)%q for x,y in zip(A[i],A[rank])]
        rank += 1
        if rank==len(A):break
    return tuple(tuple(x) for x in A[:rank])


def in_span(v, basis, q):
    x = list(v)
    for row in basis:
        p=next(j for j,t in enumerate(row) if t)
        a=x[p]
        if a: x=[(xi-a*ri)%q for xi,ri in zip(x,row)]
    return not any(x)


def subspaces(n,q):
    for d in range(n+1):
        for piv in itertools.combinations(range(n),d):
            free=[(i,j) for i,p in enumerate(piv) for j in range(p+1,n) if j not in piv]
            for vals in itertools.product(range(q),repeat=len(free)):
                B=[[0]*n for _ in range(d)]
                for i,p in enumerate(piv):B[i][p]=1
                for (i,j),x in zip(free,vals):B[i][j]=x
                yield tuple(map(tuple,B))


def is_ideal(B,n,q):
    # J = V + V tensor V, with basis (x_i, x_i*x_j).
    for r in B:
        for j in range(n):
            L=[0]*(n+n*n); R=L.copy()
            for i in range(n):
                L[n+j*n+i]=r[i] # x_j * x_i
                R[n+i*n+j]=r[i] # x_i * x_j
            if not in_span(L,B,q) or not in_span(R,B,q):return False
    return True


def gaussian(n,r,q):
    if not 0 <= r <= n:return 0
    num=prod(q**(n-i)-1 for i in range(r))
    den=prod(q**(r-i)-1 for i in range(r))
    assert num%den==0
    return num//den


def predicted(n,q):
    h=Counter()
    for u in range(n+1):
        m=n-u
        for w in range(m*m+1):
            d=n*n-m*m+u+w
            h[d]+=gaussian(n,u,q)*gaussian(m*m,w,q)*q**(u*(m*m-w))
    h[n+n*n+1]+=1
    return h


def null_basis(B, q):
    n=len(B[0]); piv=[next(i for i,v in enumerate(row) if v) for row in B]
    free=[j for j in range(n) if j not in piv]
    ker=[]
    for j in free:
        x=[0]*n; x[j]=1
        for row,p in zip(B,piv): x[p]=(-row[j])%q
        ker.append(x)
    return ker


def verify_twisted_cubic_cone(B,q):
    assert len(B)==4 and len(B[0])==6
    h,j=null_basis(B,q)
    p={(a,b):(h[a]*j[b]-h[b]*j[a])%q for a in range(6) for b in range(a+1,6)}
    C0=(-p[1,5])%q;C1=p[0,5];C2=(-p[0,3])%q;C3=p[0,2]
    allowed={(0,1),(0,2),(0,3),(0,4),(0,5),(1,2),(1,3),(1,4),(1,5)}
    assert all(v==0 for ab,v in p.items() if ab not in allowed)
    assert (p[1,3]-C1)%q==0 and (p[1,4]-C1)%q==0
    assert (p[0,4]+C2)%q==0 and (p[1,2]+C2)%q==0
    assert (C0*C2-C1*C1)%q==0
    assert (C0*C3-C1*C2)%q==0
    assert (C1*C3-C2*C2)%q==0
    assert any(p.values())


def test(n,q):
    h=Counter(); cnt=0; geometry=set()
    for B in subspaces(n+n*n,q):
        if is_ideal(B,n,q):
            h[len(B)]+=1;cnt+=1
            if n==2 and len(B)==4:
                verify_twisted_cubic_cone(B,q)
                geometry.add(B)
    h[n+n*n+1]+=1;cnt+=1  # the full algebra is the sole ideal outside J
    exp=predicted(n,q)
    assert h==exp,(n,q,h,exp)
    if n==2:
        images=set()
        # projective parameters: [a:b], t in field, plus vertex.
        for a,b in [(1,z) for z in range(q)]+[(0,1)]:
            u=[a,b]
            T=[]
            for i in range(2):
                row=[0]*6
                for j in range(2):row[2+j*2+i]=u[j]
                T.append(row)
                row=[0]*6
                for j in range(2):row[2+i*2+j]=u[j]
                T.append(row)
            H=rref(T,q);assert len(H)==3
            for ell in range(2,6):
                e=[0]*6;e[ell]=1
                if not in_span(e,H,q):break
            for t in range(q):
                lift=[a,b]+[0]*4
                lift[ell]=t
                images.add(rref(tuple(T)+(tuple(lift),),q))
        images.add(rref(tuple(tuple(int(i==j) for i in range(6)) for j in range(2,6)),q))
        assert images==geometry,(n,q,len(images),len(geometry))
    print('PASS',n,q,'full_subspaces','ideal_total',cnt,'dimension_counts',sorted(h.items()))


if __name__=='__main__':
    for n,q in [(1,2),(1,3),(1,5),(2,2),(2,3)]:test(n,q)
    print('FREE_CUBE_ZERO_IDEAL_CENSUS_OK 5 EXHAUSTIVE_CASES')
