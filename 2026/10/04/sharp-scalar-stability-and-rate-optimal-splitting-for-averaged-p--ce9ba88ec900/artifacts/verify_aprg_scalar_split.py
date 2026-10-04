from fractions import Fraction as Q
import math

def coeff(g,t):
    d = 1 + g*t
    A = (2 + (g-2)*t)/(2*d)
    B = t/(2*d)
    return A,B

def roots(g,t):
    A,B = coeff(float(g),float(t))
    s = math.sqrt(A*A + 4*B)
    return (A+s)/2, (A-s)/2

def qfac(g,t):
    r1,r2 = roots(g,t)
    return max(abs(r1),abs(r2))

# Exact Jury identities and selected finite boundaries.
for g in [Q(1,4),Q(1,2),Q(3,4)]:
    ts = Q(4,1)/(3*(1-g))
    A,B = coeff(g,ts)
    assert 1 + A - B == 0
    assert 1 - A - B > 0
    assert B == Q(2,1)/(g+3)

# The no-finite-ceiling regime has positive Jury margins at arbitrary samples.
for g in [Q(1),Q(3,2),Q(2),Q(3)]:
    for t in [Q(1,10),Q(1),Q(7),Q(100)]:
        A,B = coeff(g,t)
        assert 1-A-B > 0
        assert 1+A-B > 0
        assert 1+B > 0

# Exact optimal points for 0 < gamma < 2.
for g in [Q(1,4),Q(1,2),Q(1),Q(3,2)]:
    tstar = Q(2,1)/(2-g)
    A,B = coeff(g,tstar)
    assert A == 0
    assert B == Q(1,1)/(g+2)
    qstar = math.sqrt(float(B))
    assert qfac(g, float(tstar)*0.9) > qstar
    assert qfac(g, float(tstar)*1.1) > qstar

# Strong-proximal-curvature regime decreases toward 1/2.
for g in [Q(2),Q(3),Q(5)]:
    vals = [qfac(g,t) for t in [1,2,5,20,1000]]
    assert all(vals[i+1] < vals[i] for i in range(len(vals)-1))
    assert abs(vals[-1]-0.5) < 0.001

# Direct recurrence coefficient check from the proximal update for rational data.
a = Q(3,2)
mu = Q(3,4)
tau = Q(2,5)
g = mu/a
t = a*tau
A,B = coeff(g,t)
xprev = Q(7,5)
x = Q(-4,3)
v = x - tau*a*(2*x-xprev)
prox = v/(1+tau*mu)
xnext_direct = (x+prox)/2
xnext_recurrence = A*x+B*xprev
assert xnext_direct == xnext_recurrence

print("VERIFY_OK")
