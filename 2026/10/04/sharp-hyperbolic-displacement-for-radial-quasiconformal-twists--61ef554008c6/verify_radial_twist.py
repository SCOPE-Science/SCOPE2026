import math

def K_of_S(S):
    return ((math.sqrt(S*S+4.0)+S)/2.0)**2

def dlog_spiral(c,r):
    x=2*r*abs(math.sin(0.5*c*math.log(r)))/(1-r*r)
    return 2*math.asinh(x)

# Algebraic identity log K = 2 asinh(S/2), and elementary envelope samples.
for S in [0.0,0.1,0.5,1.0,2.0,5.0,20.0]:
    assert abs(math.log(K_of_S(S))-2*math.asinh(S/2.0)) < 2e-14
for j in range(1,10000):
    r=j/10000.0
    assert 2*r*math.log(1/r) <= 1-r*r + 2e-15
# Equality family approaches the bound at the boundary from below.
for c in [0.1,0.5,1.0,2.0,5.0]:
    target=math.log(K_of_S(c))
    vals=[dlog_spiral(c,1-10**(-k)) for k in range(2,8)]
    assert max(vals) <= target + 1e-10
    assert abs(vals[-1]-target) < 5e-7
print('VERIFY_OK identity_cases=7 envelope_points=9999 equality_families=5')
