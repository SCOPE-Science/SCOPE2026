"""Standalone arithmetic checks for Kneser pair-metric exponential-kernel formulas.
Run with Python 3. No third-party dependencies are required.
Finite checks do not replace the uniform-in-n analytic proof.
"""
from fractions import Fraction
from itertools import combinations
from math import exp, expm1, log, sqrt


def mat_vec(A, v):
    return [sum(row[j] * v[j] for j in range(len(v))) for row in A]


def kernel_scalar(n, t, x):
    m = n - 4
    # Cancellation-resistant for very small t.
    return -expm1(-t) - m * exp(-t) * (-expm1(-(x-1)*t))


def threshold(n, x):
    assert n >= 5 and x > (n - 3)/(n - 4)
    lo = 1e-10
    hi = log(n-3)
    assert kernel_scalar(n,lo,x) < 0
    assert kernel_scalar(n,hi,x) > 0
    for _ in range(150):
        mid = (lo + hi)/2
        if kernel_scalar(n,mid,x) > 0:
            hi = mid
        else:
            lo = mid
    return (lo+hi)/2


def checked_case(n):
    pairs=list(combinations(range(n),2))
    N=len(pairs)
    B=[[int(i in e) for e in pairs] for i in range(n)]
    A=[[int(i != j and not set(e).intersection(f)) for j,f in enumerate(pairs)]
       for i,e in enumerate(pairs)]
    for i in range(n):
        for j in range(n):
            assert sum(B[i][u]*B[j][u] for u in range(N)) == (n-2)*(i==j)+1
    for i in range(N):
        for j in range(N):
            assert A[i][j] == 1+(i==j)-sum(B[v][i]*B[v][j] for v in range(n))
    # First harmonic: edge values a_i+a_j for sum a=0.
    for z in range(n-1):
        a=[0]*n;a[z]=1;a[-1]=-1
        u=[a[i]+a[j] for i,j in pairs]
        assert mat_vec(A,u)==[-(n-3)*v for v in u]
        for x in [Fraction(1),Fraction(4,3),Fraction(2),Fraction(5,2)]:
            D=[[0 if i==j else (1 if A[i][j] else x) for j in range(N)] for i in range(N)]
            assert mat_vec(D,u)==[((n-4)*x-(n-3))*v for v in u]
    # Second harmonic: edge weights whose n incidence sums vanish.
    for i,j,k,l in combinations(range(n),4):
        w=[0]*N
        w[pairs.index((i,j))]+=1
        w[pairs.index((k,l))]+=1
        w[pairs.index((i,k))]-=1
        w[pairs.index((j,l))]-=1
        assert mat_vec(B,w)==[0]*n
        assert mat_vec(A,w)==w
    # Independent full-matrix exponential-kernel multiplication.
    u=[(int(0 in e)-int((n-1) in e)) for e in pairs]
    w=[0]*N
    a,b,c,d=0,1,2,3
    for e,sgn in [((a,b),1),((c,d),1),((a,c),-1),((b,d),-1)]:
        w[pairs.index(e)]+=sgn
    for x in [1.01,1.2,1.6,2.,3.]:
        for t in [0.01,0.13,0.8,2.]:
            a0,b0=exp(-t),exp(-x*t)
            K=[[1.0 if i==j else (a0 if A[i][j] else b0) for j in range(N)] for i in range(N)]
            eig_u=1-(n-3)*a0+(n-4)*b0
            eig_w=1+a0-2*b0
            for vec,eig in [(u,eig_u),(w,eig_w)]:
                lhs=mat_vec(K,vec)
                assert max(abs(lhs[i]-eig*vec[i]) for i in range(N))<3e-12
    return N


def main():
    cases=0
    for n in range(5,12):
        N=checked_case(n)
        cases+=1
        print('EXACT_GRAPH_SPECTRA',n,N,'first_harmonic',n-1,'second_harmonic',N-n)
    roots=[]
    for n in range(5,17):
        m=n-4
        x=1+2/m
        T=threshold(n,x)
        roots.append(T)
        assert 0 < T < log(n-3)
        assert kernel_scalar(n,T/2,x) < 0
        assert kernel_scalar(n,(T+log(n-3))/2,x) > 0
    assert all(a<b for a,b in zip(roots, roots[1:]))
    phi=(1+sqrt(5))/2
    assert abs(roots[0]-log(phi)) < 1e-12
    assert abs(roots[1]-log(2)) < 1e-12
    print('ROOT_EXACT_SPECIAL_CASES',repr(roots[0]),repr(roots[1]))
    # Critical-window limit and its first finite-size correction.
    lo,hi=1e-9,3.
    for _ in range(120):
        mid=(lo+hi)/2
        if exp(mid)>1+2*mid:hi=mid
        else:lo=mid
    Tinf=(lo+hi)/2
    assert abs(Tinf-1.2564312086261693)<1e-12
    for n in [20,50,200,1000]:
        Tn=threshold(n,1+2/(n-4))
        correction=4*Tinf*Tinf/(2*(n-4)*(1+2*Tinf-2))
        assert abs((Tinf-Tn)-correction)<10/(n-4)**2
    print('ASYMPTOTIC_WINDOW_OK','limit',repr(Tinf))
    print('ALL_PAIR_KERNEL_CHECKS_OK',cases,'graph_cases; 12 finite-size roots')

if __name__=='__main__':main()
