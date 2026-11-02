"""Reproducible exact and high-precision checks for Poisson-thinning rates.

Python >=3.11; only the standard library is required. This checker verifies
finite identities and numerical convergence, not the infinite theorem.
"""
import math
import json
from fractions import Fraction
from decimal import Decimal, localcontext

checks = 0

def check(assertion, label):
    global checks
    if not assertion:
        raise AssertionError(label)
    checks += 1

def polynomial_mul(a,b,max_degree=None):
    c=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if max_degree is None or i+j<=max_degree:
                c[i+j]+=x*y
    return c[:max_degree+1] if max_degree is not None else c

def truncated_poisson_masses(m):
    return [sum((Fraction((-1)**h,math.factorial(k)*math.factorial(h))
                 for h in range(m-k+1)),Fraction()) for k in range(m+1)]

def formal_exp_minus(max_degree):
    return [Fraction((-1)**j, math.factorial(j)) for j in range(max_degree+1)]

for m in range(2,11):
    p=truncated_poisson_masses(m)
    check(all(x>=0 for x in p),f'positivity m={m}')
    check(sum(p)==1,f'probability m={m}')
    for j in range(m+1):
        moment=sum((p[k]*Fraction(math.factorial(k),math.factorial(k-j))
                    for k in range(j,m+1)), Fraction())
        check(moment==1,f'factorial moment m={m} j={j}')
    r=m+1
    for n in range(1,21):
        block=[Fraction(1,math.factorial(j)*n**j) for j in range(m+1)]
        product=[Fraction(1)]
        for _ in range(n):
            product=polynomial_mul(product,block,r)
        h=polynomial_mul(formal_exp_minus(r),product,r)
        for j in range(1,r):
            check(h[j]==0,f'lower Charlier m={m} n={n} j={j}')
        check(h[r]==-Fraction(1,math.factorial(r)*n**m),f'leading Charlier m={m} n={n}')

numeric=[]
with localcontext() as ctx:
    ctx.prec=85
    for m in (2,3,4):
        target=Decimal(1)/(2*Decimal(math.factorial(m+1)))
        for n in (20,40,80):
            local=[]
            for k in range(m+1):
                val=sum((Decimal((-1)**h)/(Decimal(math.factorial(k))
                    *Decimal(math.factorial(h))*Decimal(n)**(k+h))
                    for h in range(m-k+1)),Decimal(0))
                local.append(val)
            check(abs(sum(local)-1)<Decimal('1e-75'),f'block normalization m={m} n={n}')
            probs=[Decimal(1)]
            for _ in range(n):
                updated=[Decimal(0)]*(len(probs)+m)
                for k,p in enumerate(probs):
                    for j,v in enumerate(local):
                        updated[k+j]+=p*v
                probs=updated
            KL=Decimal(0)
            chi=Decimal(0)
            q=Decimal(-1).exp()
            for k,p in enumerate(probs):
                if p:
                    KL+=p*(p/q).ln()
                chi+=(p-q)**2/q
                q=q/Decimal(k+1)
            # Summing Poisson outside finite support adds its exact tail to chi^2.
            chi+=Decimal(1)-sum((Decimal(-1).exp()/Decimal(math.factorial(k))
                                 for k in range(len(probs))),Decimal(0))
            kls=Decimal(n)**(2*m)*KL
            chis=Decimal(n)**(2*m)*chi
            check(abs(kls/target-1)<Decimal('0.025'), f'KL asymptotic m={m} n={n}')
            check(abs(chis/(2*target)-1)<Decimal('0.025'),f'chi2 asymptotic m={m} n={n}')
            numeric.append({'m':m,'n':n,'scaled_KL':format(kls,'.14f'),
                'scaled_chi2':format(chis,'.14f'),'limiting_KL':format(target,'.14f')})
print(json.dumps({'exact_and_numerical_checks_passed':checks,'numerical_samples':numeric},indent=2))
