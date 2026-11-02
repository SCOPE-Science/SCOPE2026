"""Exact finite-state identities for a geometric-emigration branching chain.

Run with Python 3.10 or newer; no third-party packages are needed.
These checks are finite algebraic tests, not proofs of the infinite-state theorem.
"""
from fractions import Fraction as Q

N = 0

def check(a, b, label):
    global N
    N += 1
    if a != b:
        raise AssertionError(f'{label}: {a!r} != {b!r}')

def conditional_moment(p, x, order):
    q = 1-p
    total = Q(0)
    for k in range(x+1):
        l = x+1-k
        values = (Q(1), 1+l, 1+4*l+l*l,
                  1+15*l+9*l*l+l*l*l)
        total += q*p**k*values[order]
    return total

def conditional_pgf(p, x, t):
    q = 1-p
    f = 1/(2-t)
    return p**(x+1)+t*q*sum(p**k * f**(x+1-k) for k in range(x+1))

for p in [Q(7,10), Q(3,4), Q(4,5), Q(17,20), Q(9,10), Q(19,20)]:
    q=1-p
    a=p/q
    theta=2-a
    for x in range(21):
        y1=conditional_moment(p,x,1)
        check(y1-x,theta+(a-1)*p**(x+1),'linear drift')
        c1=6-2*a
        c0=6-6*a+a*a+p/q**2
        tail=-1+4*a-p*(1+p)/q**2
        y2=conditional_moment(p,x,2)
        check(y2-x*x,c1*x+c0+tail*p**(x+1),'quadratic drift')
        c2=3*(4-a)
        c1_3=3*(21*p*p-31*p+12)/q**2
        c0_3=-(3*p-2)*(25*p*p-32*p+13)/q**3
        tail3=(2*p-1)*(13*p*p-8*p+1)/q**3
        y3=conditional_moment(p,x,3)
        check(y3-x**3,c2*x*x+c1_3*x+c0_3+tail3*p**(x+1),
              'cubic drift')
        for t in (Q(1,5), Q(2,5), Q(3,5)):
            f=1/(2-t)
            lhs=conditional_pgf(p,x,t)
            rhs=p**(x+1)+t*q*f/(f-p)*(f**(x+1)-p**(x+1))
            check(lhs,rhs,'conditional generating function')
    if p>Q(3,4):
        m=2*q/(4*p-3)
        B=(3*p-2)/(2*p-1)
        check((a-3)*m, Q(2), 'stationary mean identity')
        check((a-1)*B, a-2, 'stationary transform identity')
    if p>Q(4,5):
        e=(4+10*m)/(a-4)
        second=m+e
        check((a-4)*e, 4+10*m, 'factorial second moment')
        check(second, 6*p*q/((4*p-3)*(5*p-4)),
              'second moment formula')
        var=second-m*m
        check(var,2*q*(2*p-1)*(11*p-8)/((4*p-3)**2*(5*p-4)),
              'variance formula')

print(f'PASS: {N} exact rational conditional-moment, generating-function, and stationary-identity assertions.')
print('The recurrence, moment threshold, and stationary identities require the accompanying analytic proof.')
