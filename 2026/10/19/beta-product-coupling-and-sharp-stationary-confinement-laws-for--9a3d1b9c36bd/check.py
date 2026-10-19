"""Independent exact-moment and special-density tests for a trapped run--stop--run process.

Pure Python standard library; execute with: python check.py
The infinite-dimensional distributional claims require the mathematical proof.
"""
from fractions import Fraction as Q
from math import gamma, log, isclose

checks=0

def check(cond, detail):
    global checks
    assert cond, detail
    checks+=1

def beta(a,b):
    return gamma(a)*gamma(b)/gamma(a+b)

def beta_moment(n,a,b):
    prod=Q(1)
    for k in range(n):
        prod*= (a+k)/(a+b+k)
    return prod

rates=[Q(a,b) for a in (1,2,3,5,7,11) for b in (1,2,3,5)]
for r in rates:
    for t in rates:
        # State-resolved invariant-measure generator equations.
        running= t/(r+t)
        stopped= r/(r+t)
        qprev=Q(0)   # Q_0: E[1_{+} - 1_{-}]
        rprev=running # R_0: E[1_{+} + 1_{-}]
        rcur=running
        qcur=Q(0)
        for n in range(1,17):
            # From stationarity, Q_n=n R_(n-1)/(n+r),
            # R_n=(n+t)Q_(n-1)/(n+r+t), T_n=r R_n/(n+t).
            qcur=Q(n)*rprev/(Q(n)+r)
            rcur=(Q(n)+t)*qprev/(Q(n)+r+t)
            tcur=r*rcur/(Q(n)+t)
            check((Q(n)+r)*qcur == Q(n)*rprev,(r,t,n,'odd state equation'))
            check((Q(n)+r)*rcur == Q(n)*qprev+t*tcur,(r,t,n,'run state equation'))
            check((Q(n)+t)*tcur == r*rcur,(r,t,n,'tumble state equation'))
            fullmoment=rcur+tcur
            if n%2 == 0:
                predicted=beta_moment(n//2,Q(1,2),r/2)*beta_moment(n//2,t/2,r/2)
                check(fullmoment == predicted,(r,t,n,fullmoment,predicted))
            else:
                check(fullmoment == 0,(r,t,n,'odd symmetry'))
            rprev,qprev=rcur,qcur

# The exactly elementary family r=2 has density
# f(x)=t/[2(t-1)]*(1-|x|^(t-1)) for t != 1,
# and f(x)=log(1/|x|)/2 for t=1, |x|<1.
for t in rates:
    for n in range(9):
        if t == 1:
            integralmoment=Q(1,(2*n+1)**2)
        else:
            integralmoment=t/((2*n+1)*(2*n+t))
        predicted=beta_moment(n,Q(1,2),Q(1))*beta_moment(n,t/2,Q(1))
        check(integralmoment==predicted,('elementary density moment',t,n))

# Compare exact general asymptotic coefficients to closed-form r=2 laws.
for t in (0.25,0.5,0.75,1.0,1.5,2.0,4.0,7.0):
    c=1.0; a=t/2
    if t < 1:
        coeff=beta((1-t)/2,c)/(beta(0.5,c)*beta(a,c))
        check(isclose(coeff,t/(2*(1-t)),rel_tol=1e-12),('power coefficient',t,coeff))
    elif t == 1:
        coeff=2/beta(0.5,c)**2
        check(isclose(coeff,0.5,rel_tol=1e-12),('log coefficient',t,coeff))
    else:
        coeff=beta((t-1)/2,c)/(beta(a,c)*beta(0.5,c))
        check(isclose(coeff,t/(2*(t-1)),rel_tol=1e-12),('finite center',t,coeff))
    edge_coeff=(2**(2*c-1))*beta(c,c)/(beta(0.5,c)*beta(a,c))
    check(isclose(edge_coeff,t/2,rel_tol=1e-12),('boundary coefficient',t,edge_coeff))

print(f'PASS: {checks} exact-rational and analytic-coefficient checks')
