"""Reproducible finite sanity checks for the exact containment-frontier theorem.

Only finite algebra and illustrative trajectories are checked here;
the universal scheduling statement follows from the proof, not sampling.
"""
from fractions import Fraction as F
from math import exp, log, isclose


def flow(y, a, b, beta, u, duration):
    rate = beta * (a - u)
    if abs(rate) < 1e-13:
        return y - beta*b*duration
    equilibr = b/(a-u)
    return equilibr + (y - equilibr)*exp(rate*duration)


def threshold_time(a, b, beta, y0, cap):
    yc = b/a
    initial_growth = a - b/y0
    if cap <= initial_growth:
        return None
    d = a - cap
    if abs(d) < 1e-13:
        return (y0-yc)/(beta*b)
    q = b/d
    return log((yc-q)/(y0-q))/(beta*d)


# Exact derivative transformation at time zero for many rational tuples.
checks = 0
for beta in [F(1), F(2), F(3, 2)]:
    for a in [F(1), F(3, 2), F(2)]:
        for b in [F(1), F(2), F(5, 2)]:
            for y in [F(3), F(5)]:
                for u in [F(0), F(1, 2), F(2)]:
                    nlog_derivative = a - b/y - u
                    power_derivative = beta * y * nlog_derivative
                    assert power_derivative == beta*(a-u)*y-beta*b
                    checks += 1

# Exact elementary example corresponds to p_ref=0, N_ref=1,
# kappa=2, mu=1, tau=1 and beta=1.
a, b, beta, y0 = 1.0, 2.0, 1.0, 4.0
assert threshold_time(a,b,beta,y0,0.5) is None
assert isclose(threshold_time(a,b,beta,y0,1),1,abs_tol=1e-12)
two_cap_t = threshold_time(a,b,beta,y0,2)
assert isclose(two_cap_t,log(1.5),rel_tol=1e-13)
assert isclose(flow(y0,a,b,beta,2,two_cap_t),2,abs_tol=1e-12)
assert isclose(flow(y0,a,b,beta,1,1),2,abs_tol=1e-12)

# All listed admissible rate caps have strictly decreasing minimum budgets.
caps = [0.51, 0.6, 1, 2, 5, 20, 100]
budgets = [c*threshold_time(a,b,beta,y0,c) for c in caps]
assert all(budgets[i] > budgets[i+1] for i in range(len(budgets)-1))
assert budgets[-1] > log(2)

# Equal total effort over a finite horizon: exact piecewise flow evaluations.
T, B, cap = .7, .6, 2.0
front = flow(flow(y0,a,b,beta,cap,B/cap),a,b,beta,0,T-B/cap)
back = flow(flow(y0,a,b,beta,0,T-B/cap),a,b,beta,cap,B/cap)
uniform = flow(y0,a,b,beta,B/T,T)
assert front < uniform < back

# Check exact nonnegative terminal scheduling gap identity via quadrature
# in a single two-block schedule; integration is used only as a finite check.
def integrate(f, left, right, n=10000):
    h=(right-left)/n
    return h*(.5*f(left)+sum(f(left+j*h) for j in range(1,n))+.5*f(right))

# Front-load H_F=min(cap*t,B), uniform H_U=B*t/T.
def diff_integrand(t):
    hf=min(cap*t,B)
    hu=B*t/T
    return exp(-beta*a*t)*(exp(beta*hf)-exp(beta*hu))

gap = beta*b*exp(beta*(a*T-B))*integrate(diff_integrand,0,T)
assert isclose(uniform-front,gap,rel_tol=2e-8)

# Check the nontrivial logarithmic-cap singularity away from g0=a-g0.
a2, b2, beta2, y02 = 2.0, 1.0, 1.5, 3.0
g02 = a2 - b2/y02
r2 = b2/y02
yc2 = b2/a2
asymptotic_errors=[]
for eps in [1e-3,1e-5,1e-7]:
    cap2 = g02+eps
    tc = threshold_time(a2,b2,beta2,y02,cap2)
    exact = cap2*tc
    ratio = yc2*(g02+eps)/(y02*eps)
    closed = cap2/(beta2*(r2-eps))*log(ratio)
    leading = g02/(beta2*r2)*log(yc2*g02/(y02*eps))
    assert isclose(exact,closed,rel_tol=1e-9)
    asymptotic_errors.append(abs(exact-leading))
assert all(asymptotic_errors[i]>asymptotic_errors[i+1] for i in range(2))
assert asymptotic_errors[-1] < 0.00005

print(f'VERIFY_OK: {checks} exact rational transformed-derivative checks; exact cap-1 and cap-2 threshold witnesses; 7 cap-cost monotonicity points; general-parameter logarithmic asymptotic; terminal-control gap {gap:.12f}')
