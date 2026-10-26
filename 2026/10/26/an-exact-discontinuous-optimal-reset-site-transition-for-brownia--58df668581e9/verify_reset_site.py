#!/usr/bin/env python3
"""Deterministic consistency checks for optimal restart location in Brownian cover time.
Uses only the Python standard library. Numerical tests support, not replace, proof.
"""
import math

CHECKS = 0
def close(x, y, tol=3e-10):
    global CHECKS
    assert math.isfinite(x) and math.isfinite(y), (x,y)
    assert abs(x-y) < tol * (1+abs(x)+abs(y)), (x,y)
    CHECKS += 1

def check(flag, info=""):
    global CHECKS
    assert flag, info
    CHECKS += 1

def mean_scaled(k, a):
    """Dimensionless r E[T], interval [0,1], r/D = k^2."""
    return (math.cosh(k)/math.cosh(k*a) +
            math.cosh(k)/math.cosh(k*(1-a)) -
            math.cosh(k/2)/math.cosh(k*(a-.5)) - 1)

def mean_linn_scaled(k, a):
    """Independent asymmetric reflected-interval expression, Linn--Lawley (38)."""
    b=1-a
    sa, sb = math.sinh(k*a), math.sinh(k*b)
    den=sa+sb
    xa=sb/den
    xb=sa/den
    edge=math.sinh(k)/den-1
    term_a=(math.expm1(k)**2)/(math.exp(k*b)*(math.exp(2*k*a)+1))
    term_b=(math.expm1(k)**2)/(math.exp(k*a)*(math.exp(2*k*b)+1))
    return edge+xa*term_a+xb*term_b

def rational(k,a):
    c=math.cosh(k/2)
    t=math.cosh(k*(a-.5))
    b=c*c-1
    C=2*c*c-1
    return 2*c*C*t/(t*t+b)-c/t-1

def polynomial(c,w):
    b=c*c-1
    return (3-4*c*c)*w*w+4*c*c*b*w+b*b

def positive_root(c):
    b=c*c-1
    A=4*c*c-3
    return b*(2*c*c+math.sqrt((2*c*c-1)*(2*c*c+3)))/A

c_star=(1+math.sqrt(17))/4
k_star=2*math.acosh(c_star)
c_spin=math.sqrt(1+1/math.sqrt(5))
k_spin=2*math.acosh(c_spin)

for k in [.07,.17,.27,.5,.75,1,1.15,k_spin,1.28,k_star,1.6,1.8,2.2,3.0,4.0,5.5]:
    c=math.cosh(k/2)
    for j in range(101):
        a=j/100
        exact=mean_scaled(k,a)
        close(exact,mean_linn_scaled(k,a))
        close(exact,rational(k,a))
        close(exact,mean_scaled(k,1-a))
        is_best=min(mean_scaled(k,0),mean_scaled(k,.5))
        check(exact >= is_best-1e-11, ("global",k,a,exact,is_best))
    # exactly one positive root in the derivative numerator
    wpos=positive_root(c)
    check(wpos>0)
    close(polynomial(c,wpos),0)
    check(polynomial(c,0)>0)
    check(polynomial(c,1e6)<0)
    close(polynomial(c,c*c),1-2*c*c,2e-10)
    close(mean_scaled(k,.5),3*c-2/c-1)
    close(mean_scaled(k,0),2*c*c-2)
    close(mean_scaled(k,0)-mean_scaled(k,.5),
          (c-1)*(2*c*c-c-2)/c)
    if k > k_spin+1e-9:
        check(1<wpos<c*c)
        alpha=math.acosh(math.sqrt(wpos))/k
        for delta in [.001,.005]:
            xm=.5-alpha
            check(0<xm<.5)
            if delta<min(xm,.5-xm):
                check(mean_scaled(k,xm)>mean_scaled(k,xm-delta))
                check(mean_scaled(k,xm)>mean_scaled(k,xm+delta))
    elif k < k_spin-1e-9:
        check(wpos<1)
close(mean_scaled(k_star,.5),mean_scaled(k_star,0))
close(polynomial(c_spin,1),0)
check(k_spin<k_star)

for k in [.0005,.001,.002]:
    for a in [0,.1,.3,.5,.7,.9,1]:
        actual=mean_scaled(k,a)/k**2
        no_reset=(1+a-a*a)/2
        close(actual,no_reset,4e-6)

# Independent finite-difference derivative check, away from symmetry points.
for k in [.4,1,1.4,2,4]:
    c=math.cosh(k/2)
    b=c*c-1
    C=2*c*c-1
    for j in range(1,99):
        a=j/100
        t=math.cosh(k*(a-.5))
        dp=c*polynomial(c,t*t)/(t*t*(t*t+b)**2)
        num=(rational(k,a+1e-5)-rational(k,a-1e-5))/(2e-5)
        close(num,dp*k*math.sinh(k*(a-.5)),2e-6)

print("PASS:",CHECKS,"independent deterministic comparisons")
print("critical k =",format(k_star,'.15g'),"critical rho =",format(k_star**2/4,'.15g'))
print("local shape threshold k =",format(k_spin,'.15g'))
