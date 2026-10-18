"""Independent finite checks for sharp coordinatewise stability of epigraph projections.
Python >=3.10, standard library only. Numerical checks do not prove infinite claims.
"""
from itertools import combinations, product
from fractions import Fraction
from math import isclose, sqrt
from random import Random


def norm_candidates(a):
    n=len(a)
    def r(ss):
        return (1+sum(a[j] for j in ss))/(1+sum(a[j]*a[j] for j in ss))
    direct=Fraction(1)
    for mask in range(1<<n):
        ss=[j for j in range(n) if mask>>j & 1]
        cur=r(ss)
        direct=max(direct,cur)
        for j in ss:
            direct=max(direct,a[j]*cur)
    efficient=Fraction(1)
    idx=sorted(range(n),key=lambda j:a[j])
    for k in range(n+1):
        efficient=max(efficient,r(idx[:k]))
    for j in range(n):
        other=[i for i in idx if i!=j]
        for k in range(n):
            efficient=max(efficient,a[j]*r([j]+other[:k]))
    return direct,efficient


def project_max_epi(v,a):
    b,y=v[0],v[1:]
    # Exact first-order stationarity via scalar minimization, bisection.
    def d(t):
        return t-b-sum(aa*max(abs(yy)-aa*t,0) for yy,aa in zip(y,a))
    if d(0)>=0: return [0.0]+[0.0]*len(a)
    hi=max(1.,b+sum(abs(x) for x in y))
    while d(hi)<0: hi*=2
    lo=0.
    for _ in range(74):
        mid=(lo+hi)*.5
        if d(mid)>=0:hi=mid
        else:lo=mid
    t=(lo+hi)*.5
    return [t]+[max(-aa*t,min(aa*t,yy)) for yy,aa in zip(y,a)]


def project_l1_epi(v):
    b,y=v[0],v[1:]
    if sum(map(abs,y))<=b:return list(v)
    if b+max(map(abs,y))<=0:return [0.]*len(v)
    vals=sorted((abs(z) for z in y),reverse=True)
    lam=0
    for k in range(1,len(y)+1):
        trial=(sum(vals[:k])-b)/(k+1)
        if trial>=0 and vals[k-1]>trial and (k==len(y) or vals[k]<=trial):
            lam=trial
            break
    return [b+lam]+[max(abs(z)-lam,0)*(1 if z>=0 else -1) for z in y]


def rowmax(matrix):
    return max(sum(abs(z) for z in row) for row in matrix)


def chart_matrix_max(a,ss):
    n=len(a); S=set(ss); D=1+sum(a[j]**2 for j in S)
    B=[[0]*(n+1) for _ in range(n+1)]
    B[0][0]=1/D
    for j in S:B[0][j+1]=a[j]/D
    for i in range(n):
        if i in S:
            for j in range(n+1): B[i+1][j]=a[i]*B[0][j]
        else:B[i+1][i+1]=1
    return B


def chart_matrix_l1(n,ss):
    S=set(ss); k=len(S)
    if k==0:return [[int(i==j) for j in range(n+1)] for i in range(n+1)]
    B=[[0.]*(n+1) for _ in range(n+1)]
    B[0][0]=k/(k+1)
    for j in S:B[0][j+1]=1/(k+1)
    for i in S:
        B[i+1][0]=1/(k+1)
        for j in S:B[i+1][j+1]=(int(i==j)-1/(k+1))
    return B


def sample_base_max(a,ss):
    n=len(a); S=set(ss)
    # Output scalar t=1, active output y_j=a_j, inactive 0;
    # input shifts are strict outward normal with coefficient 1.
    b=1-len(S)
    v=[float(b)]+[float(a[i]+1/a[i]) if i in S else 0. for i in range(n)]
    return v


def verify():
    check=0
    vals=[Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1),Fraction(3,2),Fraction(2),Fraction(4)]
    for n in range(1,5):
        for a in product(vals,repeat=n):
            b,c=norm_candidates(a)
            assert b==c,(a,b,c)
            check+=1
    rng=Random(241017)
    for n in range(1,8):
        for _ in range(100):
            a=[Fraction(rng.randint(1,30),rng.randint(1,30)) for _ in range(n)]
            x,y=norm_candidates(a)
            assert x==y,(a,x,y)
            check+=1
            for mask in range(1<<n):
                S=[i for i in range(n) if mask>>i & 1]
                if not S:continue
                af=[float(z) for z in a]
                mat=chart_matrix_max(af,S)
                base=sample_base_max(af,S)
                pb=project_max_epi(base,af)
                assert max(abs(x-z) for x,z in zip(pb,[1.]+[af[i] if i in S else 0 for i in range(n)]))<1e-8
                e=1e-5
                for j in range(n+1):
                    vec=base[:];vec[j]+=e
                    diff=[(x-y)/e for x,y in zip(project_max_epi(vec,af),pb)]
                    assert max(abs(x-y) for x,y in zip(diff,[row[j] for row in mat]))<1e-7,(a,S,j,diff,mat)
                    check+=1
    for n in range(1,14):
        for k in range(1,n+1):
            S=list(range(k))
            M=chart_matrix_l1(n,S)
            assert abs(rowmax(M)-max(1,2*k/(k+1)))<1e-12
            b=k-1.;v=[b]+[2. if i in S else 0. for i in range(n)]
            p=project_l1_epi(v)
            assert max(abs(z-z0) for z,z0 in zip(p,[float(k)]+[1. if i in S else 0. for i in range(n)]))<1e-8,(n,k,p)
            # k=n open chart; k<n zero entries at transition, use -0.1 for inactive
            if k==n:
                for j in range(n+1):
                    dv=v[:];dv[j]+=1e-5
                    d=[(z-w)/1e-5 for z,w in zip(project_l1_epi(dv),p)]
                    assert max(abs(z-w) for z,w in zip(d,[row[j] for row in M]))<1e-6
                    check+=1
    # Moreau polar decomposition: max epigraph + negative l1 epigraph projection is identity
    for n in range(1,13):
        for rep in range(150):
            v=[rng.uniform(-7,7) for i in range(n+1)]
            p=project_max_epi(v,[1.]*n)
            q=project_l1_epi([-z for z in v])
            assert max(abs(x-(y-z)) for x,y,z in zip(v,p,q))<1e-8,(v,p,q)
            assert abs(sum(x*y for x,y in zip(p,q)))<1e-8
            check+=1

    # Universal weight-design extremizers, including the dual nonidentical families.
    for n in range(1,61):
        s=sqrt(n+1)
        lam=(1+s)/2
        low=[1/(1+s)]*n
        high=[1.]*(n-1)+[1+s]
        def spatial_and_height(a):
            R=(1+sum(a))/(1+sum(z*z for z in a))
            return max(R,R*max(a))
        assert abs(spatial_and_height(low)-lam)<1e-11
        assert abs(spatial_and_height(high)-lam)<1e-11
        if n<=11:
            assert abs(float(norm_candidates(tuple(Fraction(z).limit_denominator(10000000) for z in low))[0])-lam)<1e-8
            assert abs(float(norm_candidates(tuple(Fraction(z).limit_denominator(10000000) for z in high))[0])-lam)<1e-8
        check+=2
    print('VERIFY_OK checks='+str(check)+' exhaustive_prefix_n<=4 exact_rationals_and_random_n<=7; numerical_chart_and_polar_tests')

if __name__=='__main__':verify()
