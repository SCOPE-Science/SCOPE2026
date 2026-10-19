"""Exact finite-space and polynomial-identity verification of the footrule/comparison theorem.
No external packages or data are needed. Run: python verify_footrule_projection.py
"""
from fractions import Fraction as Q
from itertools import permutations
from math import factorial

def expected_cov(n, a, b):
    return Q(sum(t*(n-t) for t in range(a,b)),n*(n-1))

def r_squared(n):
    return Q(3*(17*n**4+31*n*n+24),28*(n*n-1)*(2*n*n+7))

def verify_enumerations():
    tested=0
    for n in range(2,8):
        edges=[(a,b) for a in range(1,n+1) for b in range(a+1,n+1)]
        N=factorial(n)
        counts=[0]*len(edges)
        fxs=[0]*len(edges)
        cxx=[[0]*len(edges) for _ in edges]
        total_f=total_f2=0
        for p in permutations(range(1,n+1)):
            f=sum(abs(i+1-x) for i,x in enumerate(p))
            total_f+=f;total_f2+=f*f
            x=[int(p[a-1]>p[b-1]) for a,b in edges]
            for i,xi in enumerate(x):
                counts[i]+=xi;fxs[i]+=f*xi
                if xi:
                    row=cxx[i]
                    for j,xj in enumerate(x): row[j]+=xj
        Ef=Q(total_f,N)
        Vf=Q(total_f2,N)-Ef*Ef
        assert Ef==Q(n*n-1,3);tested+=1
        assert Vf==Q((n+1)*(2*n*n+7),45);tested+=1
        v=[]
        for i,(a,b) in enumerate(edges):
            assert Q(counts[i],N)==Q(1,2);tested+=1
            vi=Q(fxs[i],N)-Ef*Q(1,2)
            assert vi==expected_cov(n,a,b),(n,a,b,vi,expected_cov(n,a,b))
            tested+=1;v.append(vi)
        # Check full correlation structure and normal equations for the unique L2 projection.
        for i,(a,b) in enumerate(edges):
            normal=Q(0)
            for j,(c,d) in enumerate(edges):
                obs=Q(cxx[i][j],N)-Q(1,4)
                incidence=(int(a==c)-int(a==d)-int(b==c)+int(b==d))
                predicted=Q((int(i==j)+incidence),12)
                assert obs==predicted,(n,i,j,obs,predicted)
                tested+=1
                normal+=obs*Q(12,n+1)*v[j]
            assert normal==v[i],(n,i,normal,v[i]);tested+=1
        explained=sum((Q(12,n+1)*q*q for q in v),Q(0))
        assert explained/Vf==r_squared(n);tested+=1
        assert Vf-explained==Q((n-2)*(n+2)*(5*n*n+67),1260*(n-1));tested+=1
    return tested

def verify_polynomial_sums():
    tested=0
    for n in range(2,101):
        s=sum((expected_cov(n,a,b)**2 for a in range(1,n+1) for b in range(a+1,n+1)),Q(0))
        assert s==Q((n+1)*(17*n**4+31*n*n+24),5040*(n-1));tested+=1
        V=Q((n+1)*(2*n*n+7),45)
        E=Q(12,n+1)*s
        assert E/V==r_squared(n);tested+=1
        assert V-E==Q((n-2)*(n+2)*(5*n*n+67),1260*(n-1));tested+=1
        assert (Q(0)<r_squared(n)<=Q(1));tested+=1
    return tested

if __name__=='__main__':
    print('enumeration_assertions',verify_enumerations())
    print('polynomial_assertions',verify_polynomial_sums())
    print('status PASS (analytic proof in RESULT.md)')
