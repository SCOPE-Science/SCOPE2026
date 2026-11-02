"""Finite checks for sharp powered-distance thresholds on projective incidence graphs.
Requires Python 3 only. The infinite classification is proved separately.
"""
from itertools import product
from math import sqrt, log, exp, isclose
from collections import deque


def representatives(n, q):
    result = []
    for x in product(range(q), repeat=n):
        if not any(x):
            continue
        j = next(i for i,a in enumerate(x) if a)
        if x[j] != 1:
            continue
        result.append(x)
    return result


def incidence(d, q):
    pts = representatives(d+1, q)
    assert len(pts) == (q**(d+1)-1)//(q-1)
    A = [[int(sum(xi*yi for xi,yi in zip(x,y))%q==0) for y in pts] for x in pts]
    return A


def check_design(A, v,k,lam):
    assert len(A)==v
    assert all(len(row)==v and sum(row)==k for row in A)
    assert all(sum(A[i][j] for i in range(v))==k for j in range(v))
    for i in range(v):
        for j in range(v):
            overlap = sum(A[i][s]*A[j][s] for s in range(v))
            assert overlap == (k if i==j else lam)


def shortest_path_checks(A):
    v = len(A)
    graph = [set() for _ in range(2*v)]
    for i in range(v):
        for j in range(v):
            if A[i][j]:
                graph[i].add(v+j)
                graph[v+j].add(i)
    for i in range(2*v):
        dist = [-1]*(2*v); dist[i]=0
        queue=deque([i])
        while queue:
            x=queue.popleft()
            for y in graph[x]:
                if dist[y] < 0:
                    dist[y]=dist[x]+1; queue.append(y)
        assert all(d>=0 for d in dist)
        for j in range(2*v):
            if i==j: ideal=0
            elif (i<v)==(j<v): ideal=2
            else:
                a,b=(i,j-v) if i<v else (j,i-v)
                ideal=1 if A[a][b] else 3
            assert dist[j]==ideal


def bisection(f,lo,hi):
    assert f(lo)<0 < f(hi)
    for _ in range(75):
        mid=(lo+hi)/2
        if f(mid)>0: hi=mid
        else: lo=mid
    return (lo+hi)/2


def checks(d,q):
    A=incidence(d,q)
    v=(q**(d+1)-1)//(q-1)
    k=(q**d-1)//(q-1)
    lam=(q**(d-1)-1)//(q-1)
    assert k-lam==q**(d-1)
    check_design(A,v,k,lam)
    shortest_path_checks(A)
    t=sqrt(k-lam)
    g=lambda p:t*(3**p-1)-2**p
    h=lambda p:(v-1)*2**p-(v-k)*3**p-k
    ps=bisection(g,0,3)
    expected='contrast' if q==2 and d>=5 else 'nonconstant'
    if expected=='contrast':
        assert h(ps)>1e-3
        critical=bisection(h,0,ps)
        nullity=1
    else:
        assert h(ps)<-1e-3
        critical=ps
        nullity=v-1
    assert max(g(critical),h(critical))<1e-9
    assert max(g(critical*.95),h(critical*.95)) < -1e-5
    assert max(g(critical*1.05),h(critical*1.05)) > 1e-5
    # Invariant eigenvectors, with a genuinely nonconstant singular pair.
    u=[int(i==0)-int(i==1) for i in range(v)]
    z=[sum(A[i][j]*u[i] for i in range(v))/t for j in range(v)]
    assert abs(sum(z))<1e-9
    for p in [0,.1,.5,1,critical]:
        xp=2**p;yp=3**p
        # Matrix-vector product directly using the four distance categories.
        def mult(x,y):
            sx=sum(x); sy=sum(y)
            return [xp*(sx-x[i]) + yp*sy-(yp-1)*sum(A[i][j]*y[j] for j in range(v)) for i in range(v)], [xp*(sy-y[j])+yp*sx-(yp-1)*sum(A[i][j]*x[i] for i in range(v)) for j in range(v)]
        b,c=mult(u,[-w for w in z])
        eig=g(p)
        assert max(abs(b[i]-eig*u[i]) for i in range(v))<1e-8
        assert max(abs(c[j]+eig*z[j]) for j in range(v))<1e-8
        b,c=mult([1]*v,[-1]*v)
        eig=h(p)
        assert max(abs(a-eig) for a in b)<1e-8
        assert max(abs(a+eig) for a in c)<1e-8
    print(f'PG({d},{q}): v={v},k={k},lambda={lam}, threshold={critical:.12f}, mode={expected}, endpoint_nullity={nullity}; PASS')


if __name__=='__main__':
    for d,q in [(2,2),(3,2),(4,2),(5,2),(6,2),(2,3),(3,3),(2,5)]:
        checks(d,q)
    # Integer inequalities used to prove the two endpoint exponent bounds.
    assert 2**3 < 3**2 and 2**11 < 3**7 and 3**5 < 2**8
    assert 7**8*24**5 < 31**5*6**8
    print('PROJECTIVE_INCIDENCE_NEGATIVE_TYPE_PHASE_OK')
