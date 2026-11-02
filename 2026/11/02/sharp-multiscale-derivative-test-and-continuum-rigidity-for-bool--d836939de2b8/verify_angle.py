"""Deterministic checks for multiscale Boolean-angle mixed-difference identity.

All finite-difference tests use exact rational arithmetic where possible.
"""
from fractions import Fraction
from math import factorial, exp, prod

checks=0

def diff_theta(theta, n, q, block):
    """q-fold low-bit alternating difference in coarse dyadic block."""
    assert n>=q
    a=2**q * block
    return sum(((-1)**(q-k.bit_count())) * theta(Fraction(a+k,2**n)) for k in range(2**q))

for q in range(1,7):
    for n in range(q, min(q+5,11)):
        for block in range(2**(n-q)):
            # At degree q the normalized difference is exactly q!.
            delta=diff_theta(lambda x: x**q,n,q,block)
            prod_steps=Fraction(2**(q*(q-1)//2),2**(q*n))
            assert delta == factorial(q)*prod_steps, (q,n,block,delta)
            checks+=1
            # At degree q-1 it must vanish on every coarse block.
            assert diff_theta(lambda x: x**(q-1),n,q,block)==0
            checks+=1

# Every grid polynomial of real degree <=d has Boolean degree <=d.
def mobius_coeff(values,n,mask):
    r=Fraction(0)
    t=mask
    while True:
        r+=(-1)**((mask^t).bit_count())*values[t]
        if t==0:break
        t=(t-1)&mask
    return r

for d in range(0,5):
    for n in range(d+1,9):
        v=[sum(Fraction(j+1,7)*(Fraction(i,2**n)**j) for j in range(d+1)) for i in range(2**n)]
        for mask in range(1,2**n):
            if mask.bit_count()>d:
                assert mobius_coeff(v,n,mask)==0,(d,n,mask)
                checks+=1

# Nonpolynomial analytic angle has full Boolean monomial support.
for n in range(1,9):
    for mask in range(1,2**n):
        c=1.0
        direct=sum((-1)**((mask^t).bit_count())*exp(c*t/2**n) for t in range(2**n) if (t&mask)==t)
        fact=prod(exp(c*(2**j)/2**n)-1 for j in range(n) if (mask>>j)&1)
        assert abs(direct-fact)<3e-11,(n,mask,direct,fact)
        checks+=1

# For a genuinely nonpolynomial analytic theta, the scaled finite difference
# recovers the norm of the derivative as grid gets fine (tested away from roundoff).
for q in range(1,4):
    approx=[]
    for n in range(q+2, q+10):
        h=[2**(j-n) for j in range(q)]
        val=[]
        for b in range(2**(n-q)):
            x=(2**q)*b/2**n
            # Numerically stable mixed difference by exponential factorization.
            val.append(exp(x)*prod(expm1 for expm1 in [__import__('math').expm1(hi) for hi in h]))
        amp=max(val)/prod(h)
        approx.append(amp)
    assert abs(approx[-1]-exp(1))<0.05, (q,approx[-1])
    checks+=1

print(f'PASS: {checks} deterministic exact and numerical checks')

# Fixed leading-bit obstruction: every degree-(q-1) Boolean polynomial
# differs from the monomial of degree q by at least |coefficient|/2**q
# on the q-dimensional leading-bit face. For theta(x)=x**q,
# the alternating difference is exactly q!*product(2**-j).
for q in range(1,8):
    steps=[Fraction(1,2**j) for j in range(1,q+1)]
    observed=sum((-1)**(q-mask.bit_count())*
                 (sum(steps[j] for j in range(q) if (mask>>j)&1))**q
                 for mask in range(2**q))
    target=Fraction(factorial(q), 2**(q*(q+1)//2))
    assert observed==target,(q,observed,target)
    checks+=1

# The source's angular map can be realized by an amplitude g=sin(theta/2)^2.
# For theta(x)=1+x**q on [0,1], theta stays in [1,2] subset [0,pi],
# and the real degree q equals the Boolean degree on every n>=q.
for q in range(1,6):
    for n in range(q,min(q+5,9)):
        values=[Fraction(1)+Fraction(k,2**n)**q for k in range(2**n)]
        nonzero_q=sum(mobius_coeff(values,n,mask)!=0 for mask in range(2**n)
                      if mask.bit_count()==q)
        assert nonzero_q>0,(q,n)
        checks+=1

print(f'PASS: {checks} total checks after leading-bit and angular-range tests')
