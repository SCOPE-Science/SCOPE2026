"""Reproduce exact cost, eigenvector and PSD-factor identities for priced stars.

Uses the Python standard library only; the infinite-dimensional parameter
claims are proved analytically in RESULT.md, not by finite enumeration.
"""
from fractions import Fraction as Q
from itertools import product


def optimum(lengths):
    m = len(lengths)
    assert m >= 2 and all(d > 0 for d in lengths)
    d = tuple(Q(a) for a in lengths)
    n = m + 1
    S = sum(a*a for a in d)
    delta = max(Q(0), 2*max(d)-sum(d))
    rho = 1/(S-delta*delta/n)
    expensive = d.index(max(d))
    rates = [rho*(1+delta/(n*a)) for a in d]
    if delta:
        rates[expensive] = rho*(1-delta/(n*d[expensive]))
    return d,rho,delta,rates,expensive


def squared_norms_identity(d,lam,delta,w,j,z):
    m = len(d)
    n = m+1
    # Pinned hub is zero. This is the exact Rayleigh residual.
    residual = sum(w[i]*z[i]*z[i] for i in range(m)) - lam*(
        sum(v*v for v in z)-sum(z)**2/Q(n))
    if not delta:
        certificate = lam*sum(z)**2/Q(n)
    else:
        B = sum(d[i] for i in range(m) if i!=j)
        T = sum(z[i] for i in range(m) if i!=j)
        certificate = lam/Q(n)*(delta*(
            sum(z[i]*z[i]/d[i] for i in range(m) if i!=j)-T*T/B)
            +(B/d[j])*(z[j]+d[j]*T/B)**2)
        assert sum(z[i]*z[i]/d[i] for i in range(m) if i!=j)-T*T/B>=0
    assert residual == certificate
    assert certificate>=0


def main():
    cases=0
    quadratic_tests=0
    for m in range(2,6):
        for lengths in product(range(1,5),repeat=m):
            d,lam,delta,w,j=optimum(lengths)
            assert all(v>0 for v in w)
            assert sum(d[i]*d[i]*w[i] for i in range(m))==1
            assert lam==1/(sum(v*v for v in d)-delta*delta/(m+1))
            if delta:
                z=[-v for v in d]
                z[j]=d[j]
                mean=sum(z)/Q(m+1)
                assert mean==delta/Q(m+1)
                assert all(w[i]*z[i]==lam*(z[i]-mean) for i in range(m))
            else:
                assert all(v==lam for v in w)
            tests = [[Q(0)]*m]
            for i in range(m):
                for a in [-2,-1,1,2]:
                    z=[Q(0)]*m
                    z[i]=Q(a)
                    tests.append(z)
            for i in range(m):
                for k in range(i+1,m):
                    for a,b in ((-2,1),(-1,-1),(1,2),(2,-1)):
                        z=[Q(0)]*m
                        z[i]=Q(a);z[k]=Q(b)
                        tests.append(z)
            tests.append([Q(i-2) for i in range(m)])
            tests.append([Q(1)]*m)
            for z in tests:
                squared_norms_identity(d,lam,delta,w,j,z)
                quadratic_tests+=1
            cases+=1
    print('VERIFY_OK',cases,'exact cost/eigenvalue cases;',quadratic_tests,
          'exact PSD-factorization tests')

if __name__=='__main__':
    main()
