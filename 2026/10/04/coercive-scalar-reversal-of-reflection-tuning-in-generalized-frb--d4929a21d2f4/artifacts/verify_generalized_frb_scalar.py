from fractions import Fraction as Q
import math

def coeff(alpha,t):
    return 1-(1+alpha)*t, alpha*t

def roots(alpha,t):
    A,B=coeff(float(alpha),float(t))
    d=math.sqrt(A*A+4*B)
    return (A+d)/2,(A-d)/2

def qfac(alpha,t):
    r1,r2=roots(alpha,t)
    return max(abs(r1),abs(r2))

# Exact Jury reductions and boundary factorization.
for alpha in [Q(3,5),Q(1),Q(2),Q(7,2)]:
    tb=Q(2)/(1+2*alpha)
    A,B=coeff(alpha,tb)
    assert 1-A-B == tb
    assert 1+A-B == 0
    assert 1+B > 0
    # Boundary roots are -1 and B.
    assert Q(1)+A-B == 0
    assert B == 2*alpha/(1+2*alpha)
    # Source initialization ratio is not any characteristic root.
    rinit=1-tb
    assert rinit*rinit-A*rinit-B == -alpha*tb*tb

# Stable/boundary/unstable root checks.
for alpha in [Q(3,5),Q(1),Q(2)]:
    tb=float(Q(2)/(1+2*alpha))
    assert qfac(alpha,0.9*tb) < 1
    assert abs(qfac(alpha,tb)-1) < 1e-12
    assert qfac(alpha,1.1*tb) > 1

# Unique rate optimum checked on both sides.
for alpha in [Q(3,5),Q(1),Q(2),Q(7,2)]:
    ts=float(Q(1)/(1+alpha))
    qstar=math.sqrt(float(alpha/(1+alpha)))
    assert abs(qfac(alpha,ts)-qstar) < 1e-12
    assert qfac(alpha,0.9*ts) > qstar
    assert qfac(alpha,1.1*ts) > qstar

# Reflection preference: stability ceiling falls and best factor rises with alpha.
vals=[Q(51,100),Q(3,5),Q(1),Q(2)]
ceilings=[float(Q(2)/(1+2*x)) for x in vals]
opts=[math.sqrt(float(x/(1+x))) for x in vals]
assert all(ceilings[i+1] < ceilings[i] for i in range(len(vals)-1))
assert all(opts[i+1] > opts[i] for i in range(len(vals)-1))

print("VERIFY_OK")
