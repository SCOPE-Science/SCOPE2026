"""Reproducibility checks for two-generation Poisson outbreak-size comparisons.

Only numerical corroboration of the stated analytical formulas is claimed.
Run: python3 verify_poisson.py
Python >=3.9, standard library only.
"""
from decimal import Decimal, localcontext
from math import factorial


def coefficients_recurrence(c, d, nmax):
    """PGF logarithmic-derivative recursion for Poi(c) clusters of 1+Poi(d)."""
    c, d = Decimal(str(c)), Decimal(str(d))
    p = [(-c).exp()]
    v = c * (-d).exp()
    for n in range(1, nmax+1):
        s = sum(Decimal(j) * d**(j-1) / Decimal(factorial(j-1)) * p[n-j]
                for j in range(1, n+1))
        p.append(v*s/Decimal(n))
    return p


def coefficients_condition(c, d, nmax):
    """Direct summation over first-generation cases, not the PGF recursion."""
    c, d = Decimal(str(c)), Decimal(str(d))
    p = []
    for n in range(nmax+1):
        s = Decimal(0)
        for k in range(n+1):
            if not k and n:
                continue
            j = n-k
            term = (-(c+d*k)).exp() * c**k / Decimal(factorial(k))
            if j:
                term *= (d*Decimal(k))**j / Decimal(factorial(j))
            s += term
        p.append(s)
    return p


def pgf(c, d, z):
    c, d, z = (Decimal(str(v)) for v in (c, d, z))
    return (c*(z*(d*(z-Decimal(1))).exp()-Decimal(1))).exp()


def tail(p, k):
    return Decimal(1)-sum(p[:k], Decimal(0))


def run():
    tests = 0
    with localcontext() as ctx:
        ctx.prec = 67
        for a,b in [('0.5','2'),('0.2','5'),('1','3'),('0.8','1.4')]:
            pe = coefficients_recurrence(a,b,32)
            pl = coefficients_recurrence(b,a,32)
            qe = coefficients_condition(a,b,32)
            ql = coefficients_condition(b,a,32)
            for p,q in ((pe,qe),(pl,ql)):
                for i in range(len(p)):
                    assert abs(p[i]-q[i]) < Decimal('1e-48'), (a,b,i,p[i],q[i])
                    assert p[i]>=0
                    tests+=2
            assert pe[0] > pl[0]
            tests+=1
            for ii in range(20):
                z=Decimal(ii)/Decimal(20)
                assert pgf(a,b,z)>pgf(b,a,z)
                tests+=1
            # Early strong suppression has smaller expected outbreak size.
            assert Decimal(a)*(1+Decimal(b)) < Decimal(b)*(1+Decimal(a))
            tests+=1
        pe=coefficients_recurrence('0.5','2',32)
        pl=coefficients_recurrence('2','0.5',32)
        for k in range(1,12):
            assert tail(pe,k)<tail(pl,k)
            tests+=1
        for k in range(12,28):
            assert tail(pe,k)>tail(pl,k)
            tests+=1
        d11=tail(pe,11)-tail(pl,11)
        d12=tail(pe,12)-tail(pl,12)
        d13=tail(pe,13)-tail(pl,13)
        assert Decimal('-0.000537')<d11<Decimal('-0.000536')
        assert Decimal('0.0003060')<d12<Decimal('0.0003061')
        assert Decimal('0.0005024')<d13<Decimal('0.0005026')
        tests+=3
        print('All',tests,'checks passed')
        print('P(C_0.5,2 >= 12) - P(C_2,0.5 >= 12) =',d12)
        print('P(C_0.5,2 >= 13) - P(C_2,0.5 >= 13) =',d13)
        print('Numerical checks are not proofs of asymptotic conclusions.')

if __name__=='__main__':
    run()
