import math
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

r, K, a = 0.85, 100.0, 4.0
p0, a0, b0, h0 = 0.26, 1.0, 2.0, 5.0
s, b1, c1, a1 = 0.25, 1.0, 4.0, 1.0
h1, h2 = 30.0, 65.0
p1, p2 = 0.45, 0.4
tau1, tau2 = 2.0, 5.0

def field(t, z):
    x, y = z
    q = p0 + a0*y/(1.0+b0*y)
    P = r*x*(1.0-x/K)*(x/K+a/K) - q*x*y/(1.0+h0*q*x)
    Q = s*y*(y/(y+b1) - a1*y/(x+c1))
    return (P, Q)

def Pval(x, y):
    return field(0.0, (x, y))[0]

def divergence(x, y):
    q = p0 + a0*y/(1.0+b0*y)
    dgdx = r/(K*K)*((K-x)*(x+a) - x*(x+a) + x*(K-x))
    dpred_dx = -q*y/(1.0+h0*q*x)**2
    dQdy = s*(y*(y+2.0*b1)/(y+b1)**2 - 2.0*a1*y/(x+c1))
    return dgdx + dpred_dx + dQdy

def event_hi(t, z): return z[0]-h2
event_hi.terminal = True
event_hi.direction = 1

def event_lo(t, z): return z[0]-h1
event_lo.terminal = True
event_lo.direction = -1

def one_return(yA, details=False):
    A = ((1.0+p1)*h1, yA)
    sol1 = solve_ivp(field, (0.0, 100.0), A, events=event_hi,
                     rtol=2e-10, atol=1e-12, max_step=0.2)
    assert len(sol1.t_events[0]) == 1
    B = tuple(sol1.y_events[0][0])
    C = ((1.0-p2)*h2, B[1]+tau2)
    sol2 = solve_ivp(field, (0.0, 100.0), C, events=event_lo,
                     rtol=2e-10, atol=1e-12, max_step=0.2)
    assert len(sol2.t_events[0]) == 1
    D = tuple(sol2.y_events[0][0])
    Anew = ((1.0+p1)*h1, D[1]-tau1)
    if details: return A, B, C, D, Anew
    return Anew[1]-yA

yA = brentq(one_return, 46.0, 48.0, xtol=1e-13)
A, B, C, D, Anew = one_return(yA, details=True)
assert abs(Anew[1]-A[1]) < 1e-8

def aug(t, z):
    P, Q = field(t, z[:2])
    return (P, Q, divergence(z[0], z[1]))

sol1 = solve_ivp(aug, (0.0, 100.0), (A[0], A[1], 0.0),
                 events=event_hi, rtol=2e-11, atol=1e-13, max_step=0.1)
Baug = tuple(sol1.y_events[0][0])
sol2 = solve_ivp(aug, (0.0, 100.0),
                 ((1.0-p2)*h2, Baug[1]+tau2, Baug[2]),
                 events=event_lo, rtol=2e-11, atol=1e-13, max_step=0.1)
Daug = tuple(sol2.y_events[0][0])
int_div = Daug[2]

delta1 = Pval(C[0], C[1]) / Pval(B[0], B[1])
delta2 = Pval(A[0], A[1]) / Pval(D[0], D[1])
mu = delta1 * delta2 * math.exp(int_div)

eps = 1e-5
mu_fd = 1.0 + (one_return(yA+eps)-one_return(yA-eps))/(2.0*eps)

PA_wrong = Pval((1.0+p1)*h1, D[1]-tau2)
delta2_wrong = PA_wrong / Pval(D[0], D[1])
mu_wrong = delta1 * delta2_wrong * math.exp(int_div)

assert abs(mu-0.19233304) < 2e-6
assert abs(mu_fd-mu) < 2e-6
assert abs(mu_wrong-0.40351843) < 2e-6
assert abs(mu_wrong/mu) > 2.0

print("VERIFY_OK")
print("A4", A)
print("B4", B)
print("C4", C)
print("D4", D)
print("mu_correct", mu)
print("mu_return_derivative", mu_fd)
print("mu_printed_tau2_substitution", mu_wrong)
