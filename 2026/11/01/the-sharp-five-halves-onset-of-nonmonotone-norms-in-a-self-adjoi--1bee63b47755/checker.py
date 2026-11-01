"""Finite cross-checks for a two-parameter self-adjoint matrix-norm pencil.

Requires only Python's standard library. These numerical checks do not prove
uniform asymptotics or monotonicity at all real parameter values.
"""
import math
from fractions import Fraction

count = 0


def check(condition, msg):
    global count
    count += 1
    if not condition:
        raise AssertionError(msg)


def norm(alpha, b, t):
    m = t ** alpha
    return (b * abs(1.0 - m) + math.hypot(b * (1.0 + m), 2.0 * t)) / 2.0


def critical_b(alpha):
    return 2.0 / math.sqrt(alpha * (alpha - 4.0))


def threshold_residual(alpha, b, t):
    return alpha * b * b * t ** (alpha - 2.0) * ((alpha - 2.0) * t ** alpha - 2.0) - 4.0


def peak_t(alpha, b):
    check(alpha > 4.0 and b > critical_b(alpha), 'peak domain')
    left = (2.0 / (alpha - 2.0)) ** (1.0 / alpha)
    right = 1.0
    for _ in range(95):
        mid = (left + right) / 2.0
        if threshold_residual(alpha, b, mid) > 0.0:
            right = mid
        else:
            left = mid
    return (left + right) / 2.0


# Exact algebraic factorization in the published fifth-power example.
for k in range(1, 50):
    t = Fraction(k, 51)
    eq = 5 * 4 * t**3 * (3*t**5-2)-4
    check(eq == 4*(15*t**8-10*t**3-1), 'degree-five identity')

# Direct norm formula, quadratic-root identity, and monotone/nonmonotone regimes.
for alpha in [2.5, 3.5, 4., 4.02, 4.2, 5., 6., 10.]:
    bs = ([.05, .3, 1., 2., 5.] if alpha <= 4. else
          [.3*critical_b(alpha), .9*critical_b(alpha),
           critical_b(alpha), 1.1*critical_b(alpha), 2.*critical_b(alpha)])
    for b in bs:
        R = math.hypot(b, 1.0)
        for k in range(1, 200):
            t = k / 200.0
            f = norm(alpha, b, t)
            u = f - b
            check(abs(u*(b*(1+t**alpha)+u)-t*t) < 3e-10*(1+f*f), 'quadratic equation')
            q = (t*t-t**alpha)/(1-t*t)
            if abs(q - R/b) > 1e-9 and abs(f-R) > 1e-9:
                check((f > R) == (q > R/b), 'overshoot equivalence')
        if alpha <= 4. or b <= critical_b(alpha):
            for k in range(1, 200):
                t0=(k-1)/200
                t1=k/200
                check(norm(alpha,b,t1)>=norm(alpha,b,t0)-1e-10, 'monotone branch')
        elif alpha > 4.0:
            tp = peak_t(alpha,b)
            check(0<tp<1 and abs(threshold_residual(alpha,b,tp))<1e-7,
                  'stationary equation')
            check(norm(alpha,b,tp)>R, 'positive interior overshoot')
            for k in range(1,101):
                check(norm(alpha,b,tp*k/101)<norm(alpha,b,tp), 'left of maximum')
                check(norm(alpha,b,tp+(1-tp)*k/101)<norm(alpha,b,tp), 'right of maximum')

# Critical onset: the predicted scale and optimizing parameters.
limit=1/(100*math.sqrt(5))
last=0.
for eps in [.3,.2,.1,.05,.025,.01]:
    a=4+eps
    b=math.sqrt(5)/math.sqrt(eps)
    t=1-eps/10
    val=norm(a,b,t)-norm(a,b,1.)
    ratio=val/eps**2.5
    check(val>0 and 0<ratio<limit*1.1, 'positive scaled overshoot')
    check(ratio>last, 'limiting coefficient approached from below')
    last=ratio
check(abs(last-limit)<.00008, 'approach to sharp coefficient')

# Numerical comparison against a discrete grid of scaled parameter pairs.
for eps in [.2,.1,.05]:
    a=4+eps
    candidate=norm(a,math.sqrt(5/eps),1-eps/10)-norm(a,math.sqrt(5/eps),1)
    largest=-1.0
    for k in range(19,101):
        beta=k/10.
        b=beta/math.sqrt(eps)
        for j in range(0,26):
            t=1-eps*j/100.
            delta=norm(a,b,t)-norm(a,b,1.)
            largest=max(largest,delta)
    check(largest <= candidate*1.1, 'grid consistent with critical optimizer')

print('PASS finite assertions:',count)
print('Critical coefficient:',format(limit,'.16g'))
print('Last tested scaled ratio:',format(last,'.16g'))
