#!/usr/bin/env python3
"""Independent finite-field checks of the low-codimension ideal-orbit threshold.
Scientific inputs: free two-step Lie bracket and elementary field arithmetic.
No external packages required; run with Python 3.9+.
"""
from itertools import combinations, product
from math import comb

def gaussian(n,k,q):
    if k<0 or k>n:return 0
    numerator=1;denominator=1
    for i in range(k):
        numerator*=q**(n-i)-1
        denominator*=q**(k-i)-1
    assert numerator%denominator==0
    return numerator//denominator

def rank(rows,q,ncols=None):
    a=[list(r) for r in rows]
    if not a:return 0
    n=ncols or len(a[0]); m=len(a); r=0
    for c in range(n):
        t=next((j for j in range(r,m) if a[j][c]%q),None)
        if t is None:continue
        a[r],a[t]=a[t],a[r]
        inv=pow(a[r][c],-1,q)
        a[r]=[(v*inv)%q for v in a[r]]
        for j in range(m):
            if j!=r and a[j][c]:
                v=a[j][c]
                a[j]=[(a[j][i]-v*a[r][i])%q for i in range(n)]
        r+=1
        if r==m:break
    return r

def rref_subspaces(n,k,q):
    for piv in combinations(range(n),k):
        free=[(i,j) for i in range(k) for j in range(piv[i]+1,n) if j not in piv]
        for vals in product(range(q),repeat=len(free)):
            a=[[int(j==piv[i]) for j in range(n)] for i in range(k)]
            for (i,j),v in zip(free,vals):a[i][j]=v
            yield a

def bracket(x,y,d):
    c=comb(d,2);z=[0]*(d+c)
    for t,(i,j) in enumerate(combinations(range(d),2)):
        z[d+t]=(x[i]*y[j]-x[j]*y[i])%2
    return z

def test_ideals_d3():
    d=3; N=d+comb(d,2)
    observed={}; total=0
    for kdim in range(N+1):
        for bas in rref_subspaces(N,kdim,2):
            rr=rank(bas,2)
            if any(rank(bas+[bracket(v,[int(j==i) for j in range(N)],d)],2)>rr
                   for v in bas for i in range(d)):
                continue
            proj=rank([x[:d] for x in bas],2)
            delta=comb(d,2)-kdim+proj
            assert delta>=0
            observed[d-proj,delta]=observed.get((d-proj,delta),0)+1
            total+=1
    expected={(k,delta):gaussian(d,k,2)*gaussian(comb(k,2),delta,2)*2**((d-k)*delta)
              for k in range(d+1) for delta in range(comb(k,2)+1)}
    expected={key:v for key,v in expected.items() if v}
    assert observed==expected,(observed,expected)
    print('F2_d3_full_ideal_enumeration',total,sorted(observed.items()))

def sym_rank(entries,q):
    F=[[0]*4 for _ in range(4)]
    for z,(i,j) in zip(entries,combinations(range(4),2)):
        F[i][j]=z;F[j][i]=-z%q
    return rank(F,q)

def transform_form(a,g,q):
    F=[[0]*4 for _ in range(4)]
    for z,(i,j) in zip(a,combinations(range(4),2)):
        F[i][j]=z%q;F[j][i]=(-z)%q
    B=[[sum(F[i][j]*g[j][l] for j in range(4))%q for l in range(4)] for i in range(4)]
    C=[[sum(g[i][k]*B[i][j] for i in range(4))%q for j in range(4)] for k in range(4)]
    return tuple(C[i][j] for i,j in combinations(range(4),2))

def test_orbits_f2():
    g=[]
    for i in range(4):
        for j in range(4):
            if i==j:continue
            x=[[int(u==v) for v in range(4)] for u in range(4)]
            x[i][j]=1
            g.append(x)
    unseen={tuple(x) for x in product(range(2),repeat=6) if any(x)}
    orbits=[]
    while unseen:
        start=next(iter(unseen)); vis={start}; todo=[start]
        while todo:
            a=todo.pop()
            for h in g:
                b=transform_form(a,h,2)
                if b not in vis:vis.add(b);todo.append(b)
        unseen.difference_update(vis)
        rs={sym_rank(a,2) for a in vis}
        assert len(rs)==1
        orbits.append((len(vis),rs.pop()))
    assert sorted(orbits)==[(28,4),(35,2)],orbits
    print('F2_GL4_alternating_form_orbits',sorted(orbits))

def test_projective_forms_q3():
    q=3; counts={2:0,4:0}
    for a in product(range(q),repeat=6):
        if not any(a):continue
        if next(x for x in a if x)!=1:continue
        counts[sym_rank(a,q)]+=1
    rank2=gaussian(4,2,q)
    all_proj=gaussian(6,1,q)
    assert counts=={2:rank2,4:all_proj-rank2},(counts,rank2,all_proj)
    print('F3_projective_alternating_rank_counts',counts)

def test_codimension_polynomial():
    for q in (2,3,5):
        for d in (3,4,5,6):
            bycod={}
            for k in range(d+1):
                for delta in range(comb(k,2)+1):
                    c=k+delta
                    count=gaussian(d,k,q)*gaussian(comb(k,2),delta,q)*q**((d-k)*delta)
                    bycod[c]=bycod.get(c,0)+count
            for c in range(min(5,d+comb(d,2))+1):
                count=sum(gaussian(d,k,q)*gaussian(comb(k,2),c-k,q)*q**((d-k)*(c-k))
                       for k in range(d+1) if 0<=c-k<=comb(k,2))
                assert bycod[c]==count
            if d>=5:
                five=gaussian(d,5,q)+gaussian(d,4,q)*gaussian(6,1,q)*q**(d-4)+gaussian(d,3,q)*gaussian(3,1,q)*q**(2*(d-3))
                assert bycod[5]==five
    print('LOW_CODIMENSION_IDEAL_POLYNOMIAL_CHECKS_PASSED')

if __name__=='__main__':
    test_ideals_d3()
    test_orbits_f2()
    test_projective_forms_q3()
    test_codimension_polynomial()
    print('ALL_IDEAL_ORBIT_THRESHOLD_CHECKS_PASSED')
