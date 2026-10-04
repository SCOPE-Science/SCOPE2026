from fractions import Fraction as F
import math

def coeff(alpha, theta, beta, lam):
    m = alpha - theta*lam
    s = beta*lam
    A = 1 + m - s
    return m, s, A

def roots(m,s):
    A = float(1+m-s)
    disc = A*A - 4*float(m)
    if disc >= 0:
        d = math.sqrt(disc)
        return (A+d)/2, (A-d)/2
    d = math.sqrt(-disc)
    z1 = complex(A/2,d/2)
    z2 = complex(A/2,-d/2)
    return z1,z2

def qfac(m,s):
    r1,r2 = roots(m,s)
    return max(abs(r1),abs(r2))

# Modal Jury identities.
for m,s in [(F(1,4),F(1,2)), (F(-1,3),F(1,2)), (F(0),F(1))]:
    assert -1 < m < 1
    assert 0 < s < 2*(1+m)
    A = 1+m-s
    assert 1-A+m == s
    assert 1+A+m == 2+2*m-s
    assert 1-m > 0
    assert qfac(m,s) < 1

# Uniform SPD stability budget: test rational spectra and both sides of the boundary.
alpha = F(3,5)
theta = F(1,10)
L = F(4)
beta_good = F(1,2)  # L(beta+2theta)=14/5 < 16/5
assert L*(beta_good+2*theta) < 2*(1+alpha)
for lam in [F(1),F(2),F(4)]:
    m,s,_=coeff(alpha,theta,beta_good,lam)
    assert -1 < m < 1
    assert 0 < s < 2*(1+m)

beta_boundary = 2*(1+alpha)/L - 2*theta
m,s,_=coeff(alpha,theta,beta_boundary,L)
assert s == 2*(1+m)
r=roots(m,s)
assert min(abs(complex(x)+1) for x in r) < 1e-12

# Positive effective momentum: a whole interval has factor sqrt(m).
for m in [F(1,9),F(1,4),F(4,9)]:
    rt=math.sqrt(float(m))
    lo=(1-rt)**2
    hi=(1+rt)**2
    for s in [lo,(lo+hi)/2,hi]:
        assert abs(qfac(m,s)-rt) < 1e-10
    assert qfac(m,lo*0.9) > rt

# Negative effective momentum: unique balance point s=1+m.
for m in [F(-1,4),F(-1,2),F(-3,4)]:
    s=1+m
    qstar=math.sqrt(float(-m))
    assert abs(qfac(m,s)-qstar) < 1e-12
    assert qfac(m,float(s)*0.9) > qstar
    assert qfac(m,float(s)*1.1) > qstar

# Matched curvature cancellation.
alpha=F(2,3)
lam=F(5,2)
theta=alpha/lam
beta=1/lam
m,s,A=coeff(alpha,theta,beta,lam)
assert m == 0 and s == 1 and A == 0
for uk,uprev in [(F(3),F(-2)),(F(7,5),F(11,3))]:
    unext=A*uk-m*uprev
    assert unext == 0

print("VERIFY_OK")
