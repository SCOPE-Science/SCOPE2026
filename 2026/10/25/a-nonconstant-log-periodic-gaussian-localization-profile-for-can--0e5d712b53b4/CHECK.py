"""Reproducibility checks for the exact mid-third Cantor vacuum asymptotics.
The infinite-product assertion is proved analytically in RESULT.md; this program
checks its critical nonconstancy certificate and finite-product identities.
"""
from fractions import Fraction as Q
from math import factorial
from decimal import Decimal, localcontext

checks = 0

def check(condition, explanation):
    global checks
    assert condition, explanation
    checks += 1

def exp_upper(x, N=36):
    """Rigorous rational upper bound for exp(x) when 0<=x<=6."""
    check(Q(0) <= x <= Q(6), 'x out of interval')
    s = sum((x**j)/Q(factorial(j)) for j in range(N+1))
    first = x**(N+1)/Q(factorial(N+1))
    return s + first/(1-x/Q(N+2))

xs = [Q(2,3**(-k)) if k < 0 else Q(2*3**k) for k in range(-6,2)]
lower_sum = sum(x/(1+exp_upper(x)) for x in xs)
check(lower_sum > Q(631,1000), 'strict lower derivative bound failed')
check(2**1000 < 3**631, 'log_3 2 upper bound failed')

with localcontext() as ctx:
    ctx.prec = 60
    one, two, three = Decimal(1), Decimal(2), Decimal(3)
    delta = two.ln()/three.ln()
    def prod_H(t, NK=22, NR=52):
        p = one
        for k in range(NK):
            p *= (one+(-two*t*three**k).exp())
        for r in range(1,NR+1):
            p *= (one+(-two*t/three**r).exp())/two
        return (t.ln()*delta).exp()*p
    for t in (one,Decimal('1.2'),Decimal('1.5'),Decimal('2'),Decimal('2.8')):
        check(abs(prod_H(t)-prod_H(three*t)) < Decimal('1e-23'), 'periodicity approximation')
    check(prod_H(one) > prod_H(Decimal('1.5'))+Decimal('0.0003'), 'numeric nonconstancy diagnostic')
    # Exact finite identity by independent endpoint-integration and digit factorization.
    for n in range(1,8):
        for A in (Decimal('0.3'),one,three,Decimal('11.5')):
            width = A/(three**n)
            brute = Decimal(0)
            for mask in range(2**n):
                left = sum(two*A*Decimal((mask>>j)&1)/(three**(j+1)) for j in range(n))
                brute += (-left).exp()-(-(left+width)).exp()
            factor = (one-(-width).exp())
            for j in range(1,n+1):
                factor *= one+(-two*A/(three**j)).exp()
            check(abs(brute-factor) < Decimal('1e-52'), 'digit-product identity')
    # Check the explicit finite-size relative-error enclosure, with H truncated very accurately.
    for n in (8,10,12):
        for A in (Decimal('5'),Decimal('11'),three**(n//2)):
            check(A < three**n, 'scale assumption')
            m=0
            while three**(m+1)<=A: m+=1
            t=A/(three**m)
            h=A/(three**n)
            lam=one-(-h).exp()
            for j in range(1,n+1):
                lam*=one+(-two*A/(three**j)).exp()
            approximation=(two/three)**n*(A.ln()*(one-delta)).exp()*prod_H(t)
            ratio=lam/approximation
            epsilon=Decimal('1.5')*h+(-two*A).exp()/(one-(-Decimal(4)*A).exp())
            check(((-epsilon).exp() <= ratio <= epsilon.exp()), 'quantitative remainder')

print('PASS:',checks,'assertions; strict rational derivative certificate and finite identities')
print('lower_dlog_H_test_sum>',str(Q(631,1000)),'(exact rational comparison)')
print('H(1) / H(3/2) is nontrivially larger than 1 (independent numerical diagnostic)')
