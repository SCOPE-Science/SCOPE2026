import math
import sympy as sp
from scipy.integrate import quad
from scipy.special import ndtr

# Exact first-integral check for
# u' = w,  w' = (alpha*u-beta) w^2 + beta*w.
u, w, alpha, beta = sp.symbols('u w alpha beta', positive=True)
phi_u = alpha*u - beta
# H_u and H_w for H=e^{-Phi(u)}w-beta*int_0^u e^{-Phi(s)}ds.
H_u = sp.exp(-(alpha*u**2/2-beta*u))*(-phi_u*w-beta)
H_w = sp.exp(-(alpha*u**2/2-beta*u))
dHdt = sp.simplify(H_u*w + H_w*(phi_u*w**2+beta*w))
assert dHdt == 0
print('symbolic_dHdt =', dHdt)


def branch(alpha, beta, u0, v0):
    w0 = 1.0/(1.0-v0)
    m = beta/alpha
    pref = math.exp(beta*beta/(2*alpha))*math.sqrt(2*math.pi/alpha)

    def Phi(x):
        return 0.5*alpha*x*x-beta*x

    def int_exp_minus_phi(a, b):
        za = math.sqrt(alpha)*(a-m)
        zb = math.sqrt(alpha)*(b-m)
        return pref*(ndtr(zb)-ndtr(za))

    def Q(x):
        return w0*math.exp(-Phi(u0)) + beta*int_exp_minus_phi(u0, x)

    def invw(x):
        return math.exp(-Phi(x))/Q(x)

    sigma = 1 if w0 > 0 else -1
    if sigma > 0:
        L = w0*math.exp(-Phi(u0)) + beta*int_exp_minus_phi(u0, math.inf)
        def tail_time(x):
            return quad(invw, x, math.inf, epsabs=1e-15, epsrel=1e-12, limit=200)[0]
    else:
        L = -(w0*math.exp(-Phi(u0)) + beta*int_exp_minus_phi(u0, -math.inf))
        def tail_time(x):
            return quad(lambda z: -invw(z), -math.inf, x,
                        epsabs=1e-15, epsrel=1e-12, limit=200)[0]

    return sigma, L, Q, invw, tail_time

# Two constant-history examples for alpha=beta=1.
# phi(s)=c gives u(0)=c and v(0)=c.
for c, target in [(0.5, 10.0), (2.0, -10.0)]:
    sigma, L, Q, invw, tail_time = branch(1.0, 1.0, c, c)
    tau = tail_time(target)
    S = math.log(1.0/tau)
    ww = 1.0/invw(target)
    shifted_u_ratio = (target-1.0)/(sigma*math.sqrt(2.0*S))
    derivative_ratio = ww*tau*math.sqrt(2.0*S)/sigma
    memory_ratio = invw(target)/(sigma*tau*math.sqrt(2.0*S))
    print(f'c={c:g} sigma={sigma:+d} L={L:.12g} tau={tau:.12g}')
    print(f'  shifted_u_ratio={shifted_u_ratio:.12g}')
    print(f'  derivative_ratio={derivative_ratio:.12g}')
    print(f'  memory_ratio={memory_ratio:.12g}')
