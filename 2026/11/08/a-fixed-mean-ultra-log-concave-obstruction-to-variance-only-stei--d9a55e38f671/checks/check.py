"""Reproduce finite diagnostics for a Bernoulli--Poisson Stein obstruction.

The rigorous infinite-support argument is in RESULT.md. This program checks
specified rational ratio identities exactly and assesses finite sums at
80-decimal-digit precision. Truncations are explicitly controlled, not proofs.
"""
from decimal import Decimal, localcontext
from fractions import Fraction
from math import factorial


def ratio(n, e):
    b = 1 - e
    return e * (e*e + n*b) / (n * (e*e + (n-1)*b))


def unnormalized(n, e):
    return e ** (n-1) * (e*e + n*(1-e)) / factorial(n)


checks = 0
for denominator in [2,3,4,5,7,10,20,50,100,1000]:
    e = Fraction(1, denominator)
    assert ratio(2,e) < e
    assert ratio(3,e) <= e/2
    checks += 2
    for n in range(1,80):
        assert ratio(n,e) > ratio(n+1,e), (denominator,n)
        checks += 1
    for n in range(1,30):
        a = unnormalized(n,e)*factorial(n)
        b = unnormalized(n-1,e)*factorial(n-1)
        c = unnormalized(n+1,e)*factorial(n+1)
        assert a*a > b*c, (denominator,n)
        checks += 1

with localcontext() as context:
    context.prec = 80
    for denominator in [2,3,4,5,7,10,20,50,100,1000]:
        e = Decimal(1) / Decimal(denominator)
        b = Decimal(1)-e
        pmf = [e*(-e).exp()]
        for n in range(1,101):
            r = e * (e*e + Decimal(n)*b) / (Decimal(n)*(e*e + Decimal(n-1)*b))
            pmf.append(pmf[-1]*r)
        assert abs(sum(pmf)-Decimal(1)) < Decimal('1e-60')
        checks += 1
        mean=sum(Decimal(n)*p for n,p in enumerate(pmf))
        var=sum((Decimal(n)-mean)**2*p for n,p in enumerate(pmf))
        assert abs(mean-Decimal(1)) < Decimal('1e-58')
        assert abs(var-(2*e-e*e)) < Decimal('1e-57')
        checks+=2
        F=Decimal(0)
        gammas=[]
        for j in range(1,81):
            F+=pmf[j-1]
            G=sum(pmf[j:])
            gammas.append(F*G/pmf[j-1])
        g1=Decimal(1)-e*(-e).exp()
        assert abs(gammas[0]-g1) < Decimal('1e-58')
        assert gammas[0]>max(gammas[1:])
        checks+=2
        print('eps=1/%-5d mean=%s variance=%s wGamma=%s ratio=%s' %
            (denominator,format(mean,'.12g'),format(var,'.12g'),
             format(g1,'.12g'),format(g1/var.sqrt(),'.12g')))
        assert (Decimal(1)-e*(-e).exp())>Decimal(2)/3
        assert e/(1-e/2)<=Decimal(2)/3
        checks+=2

print('PASS: %d diagnostic assertions. Infinite claims proved separately.' % checks)
