"""Exact rational verification for the fixed-control six-compartment SIR theorem.

Run with: python3 verify.py
Only the standard library is needed. General proofs are in RESULT.md.
"""
from fractions import Fraction as Q


def model_rhs(z, p):
    S, I, R, Ss, Is, Rs = z
    b, d, gam, beta, alpha, eta, mustar, mu, nu, xi = p
    q = mustar - mu
    ns = Ss + Is + Rs
    w = (1 - alpha) * I + Is
    return (
        (1 - xi) * b - beta * (1 - alpha) * S * w - q * S * ns + nu * Ss - d * S,
        beta * (1 - alpha) * S * w - (gam + eta + d) * I - q * I * ns + nu * Is,
        (gam + eta) * I - q * R * ns + nu * Rs - d * R,
        xi * b - beta * Ss * w + q * S * ns - nu * Ss - d * Ss,
        beta * Ss * w - (gam + nu + d) * Is + q * I * ns,
        gam * Is + q * R * ns - nu * Rs - d * Rs,
    )


def threshold(p, s, ss):
    b, d, gam, beta, alpha, eta, mustar, mu, nu, xi = p
    a = 1 - alpha
    g = gam + d
    ell = gam + eta + d
    m = (mustar - mu) * ss
    J = (ell + m) * (g + nu) - m * nu
    P = a * (a * (g + nu) + m)
    T = a * nu + ell + m
    corrected = beta * (P * s + T * ss) / J
    t = gam + eta + nu + d + m
    published = beta * (
        a*a * (1 + (alpha*mu*ss/a - eta)/t) * s
        + (1 - alpha*nu/t)*ss
    ) / (g + eta*nu/t)
    difference = beta * alpha * a * s * ss * ((mustar - mu) - mu) / J
    return corrected, published, difference, J, P, T


p = (Q(1), Q(1), Q(1), Q(3652, 925), Q(1, 2),
     Q(1), Q(2), Q(0), Q(1), Q(1, 2))
z = (Q(1900, 3901), Q(379, 85822), Q(366, 42911),
     Q(3775, 7802), Q(340, 42911), Q(353, 42911))
assert all(v > 0 for v in z)
assert sum(z) == 1
assert sum(z[:3]) == sum(z[3:]) == Q(1, 2)
assert all(v == 0 for v in model_rhs(z, p))
S, I, R, Ss, Is, Rs = z
beta, alpha = p[3], p[4]
assert beta*((1-alpha)*I + Is) == Q(1, 25)
corrected, printed, difference, J, P, T = threshold(p, Q(1, 2), Q(1, 2))
assert (corrected, printed) == (Q(1909, 1850), Q(913, 925))
assert corrected - printed == difference == Q(83, 1850)
assert J == 11 and P == Q(5,4) and T == Q(9,2)
assert printed < 1 < corrected

# At the DFE, the infected Jacobian block has negative determinant,
# hence one strictly positive and one strictly negative real eigenvalue.
a = 1-alpha
g = p[2]+p[1]
ell = p[2]+p[5]+p[1]
m = (p[6]-p[7])*Q(1,2)
B11 = beta*a*a*Q(1,2) - ell - m
B12 = beta*a*Q(1,2) + p[8]
B21 = beta*a*Q(1,2) + m
B22 = beta*Q(1,2) - g - p[8]
trace = B11+B22
det = B11*B22-B12*B21
assert trace == Q(-1677,370)
assert det == Q(-649,1850)
assert trace < 0 and det < 0

# The equilibrium behavior total solves the fixed-point equation exactly.
b, d, gam, beta, alpha, eta, mustar, mu, nu, xi = p
u = Ss+Is+Rs
assert u == Q(1,2)
assert xi*b+(mustar-mu)*(b/d-u)*u-(nu+d)*u == 0

# Scalar equilibrium quadratic: unique positive root is w=1/25.
w=Q(1,25)
A=1-alpha
L=gam+eta+d
G=gam+d
m=(mustar-mu)*u
J=(L+m)*(G+nu)-nu*m
P=A*(A*(G+nu)+m)
T=A*nu+L+m
D0=d*(d+m+nu)
D1=d+m+A*(d+nu)
E0=P*(nu+(1-xi)*d)+T*(m+xi*d)
E1=P*(1-xi)+T*xi*A
assert J*(D0 + D1*w + A*w*w) == beta*b*(E0 + E1*w)
assert J*D0 < beta*b*E0  # increasing feedback at zero
assert (J*D1-beta*b*E1)*w+J*A*w*w == beta*b*E0-J*D0
print('VERIFY_OK')
