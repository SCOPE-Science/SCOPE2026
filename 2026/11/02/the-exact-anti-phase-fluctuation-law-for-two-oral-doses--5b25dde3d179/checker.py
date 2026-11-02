"""Independent numerical reproduction of periodic two-dose Bateman phase penalty.

Uses only Python standard library. Numerical quadrature is a diagnostic, not a proof.
"""
from math import exp, expm1, cosh, sinh, isclose

checks = 0

def check(condition, msg):
    global checks
    assert condition, msg
    checks += 1

def g(t, a, b, T):
    t = t % T
    if a == b:
        x = exp(-a * T)
        return a * a * exp(-a * t) * (t / (1-x) + T*x / (1-x)**2)
    return (a*b / (b-a) * (exp(-a*t) / (-expm1(-a*T)) -
                           exp(-b*t) / (-expm1(-b*T))))

def cost(delta, a, b, T, w1, w2, steps=6000):
    # Composite Simpson rule for the smooth, periodized concentration.
    dx = T / steps
    mean = (w1 + w2) / T
    def f(t):
        v = w1*g(t, a, b, T) + w2*g(t-delta, a, b, T)-mean
        return v*v
    return (dx/3) * (f(0) + f(T) +
              4*sum(f(j*dx) for j in range(1,steps,2)) +
              2*sum(f(j*dx) for j in range(2,steps,2)))

def F(rate, d, L):
    return (cosh(rate*d) - 1)/(rate*sinh(rate*L))

def penalty(delta, a, b, T, w1, w2):
    d = abs(delta-T/2)
    if a == b:
        # derivative limit in rate, from dF/drate<0; central finite difference
        e = 1.e-4*min(a,1/T)
        derivative = (F(a+e,d,T/2)-F(a-e,d,T/2))/(2*e)
        return -w1*w2*a**3/2*derivative
    return w1*w2*(a*a*b*b)/((a+b)*(b-a))*(F(a,d,T/2)-F(b,d,T/2))

for a,b,T,w1,w2 in [(0.3,0.8,2,1,1),(1,4,1,1,2),(2,20,1,2,3),
                      (0.7,0.7001,2,1.5,0.5),(0.5,0.5,3,1,2),
                      (5,2,1.25,1,0.25),(0.25,0.9,8,0.2,3)]:
    baseline=cost(T/2,a,b,T,w1,w2)
    for fraction in [0,0.125,0.25,0.375,0.5,0.625,0.75,0.875,1]:
        s=T*fraction
        direct=cost(s,a,b,T,w1,w2)-baseline
        predicted=penalty(s,a,b,T,w1,w2)
        tol=0.000025*max(1,abs(direct),abs(predicted))
        check(abs(direct-predicted)<tol,
              f'mismatch: {a=} {b=} {T=} {s=} {direct=} {predicted=} {tol=}')
        check(predicted>=-1.e-12, f'negative penalty: {a=} {b=} {s=} {predicted=}')
        if s != T/2:
            check(predicted>0, 'uniqueness fails')
        check(isclose(penalty(s,a,b,T,w1,w2),penalty(T-s,a,b,T,w1,w2),rel_tol=1.e-7,abs_tol=1.e-10), 'phase symmetry fails')

# Check T dimensional rescaling: rate -> rate/c; T -> c*T, J -> J/c.
for a,b,T,w1,w2,delta,scale in [(1,4,1,1,2,0.2,3),(.5,1,2,2,3,.4,0.5)]:
    left=penalty(scale*delta,a/scale,b/scale,T*scale,w1,w2)
    right=penalty(delta,a,b,T,w1,w2)/scale
    check(isclose(left,right,rel_tol=1.e-9,abs_tol=1.e-10),'rescale mismatch')

print(f'VERIFY_OK assertions={checks}')
