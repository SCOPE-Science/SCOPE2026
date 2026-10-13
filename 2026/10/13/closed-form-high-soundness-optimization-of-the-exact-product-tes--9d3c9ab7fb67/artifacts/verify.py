import math

def sfun(w):
    if w <= 0.0:
        return 0.0
    m = int(math.floor(1.0/w + 1e-12))
    r = 1.0 - m*w
    return m*w*w + r*r

def R(e):
    return (1.0 - sfun(1.0-e))/2.0

def objective(e1,e2,sigma):
    return 0.5*(1.0-(R(e1)+R(e2))/2.0+
                min(1.0, sigma+(math.sqrt(e1)+math.sqrt(e2))/2.0))

def closed(sigma):
    a = 1.0-sigma
    return 1.0-(a*a-a**4)/2.0

# Exact scalar identities represented numerically.
for a in [1/(2*math.sqrt(2)), 0.3, 0.2, 0.1, 0.03]:
    assert a <= 1/(2*math.sqrt(2)) + 1e-15
    # The claimed optimizer.
    e=a*a
    assert abs(objective(e,e,1-a)-closed(1-a)) < 2e-14
    # Strict improvement over Proposition 7.1.
    old=1-a*a/4
    assert closed(1-a) < old

# Deterministic grid corroboration of the full piecewise source objective.
for sigma in [1-1/(2*math.sqrt(2)), 0.7, 0.8, 0.9, 0.97]:
    a=1-sigma
    best=-1.0
    # Fine grid in sqrt(epsilon), where the optimizer is known to be near a.
    # Include a exactly.
    xs=[i/800 for i in range(801)]
    xs.append(a)
    for x in xs:
        for y in xs:
            v=objective(x*x,y*y,sigma)
            if v>best:
                best=v
    assert best <= closed(sigma) + 2e-6
    assert best >= closed(sigma) - 2e-12

# Boundary defect is nonnegative on the theorem domain.
for a in [1/(2*math.sqrt(2)),0.3,0.2,0.1]:
    for j in range(101):
        z=-a+2*a*j/100
        defect=2*z*z*(1-6*a*a-z*z)
        assert defect >= -1e-14

print("VERIFY_OK")
