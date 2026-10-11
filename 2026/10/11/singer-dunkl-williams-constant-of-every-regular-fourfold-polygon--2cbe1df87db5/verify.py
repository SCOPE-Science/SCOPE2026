import math
import sympy as s

def d_to_normals(theta, alpha):
    beta = 2*alpha
    r = (theta + alpha) % beta - alpha
    return abs(r)

def objective(theta, delta, N):
    alpha = math.pi/N
    return math.cos(d_to_normals(theta+delta, alpha)) / (
        math.cos(d_to_normals(theta, alpha))*math.cos(delta)
    )

# Symbolic identity used in the |m|>=2 case.
c=s.symbols('c', real=True)
assert s.expand((1-c)*(4*c+3)) == s.expand(3+c-4*c*c)

# Equality configuration and deterministic lower-bound sampling.
for N in (4,8,12,16,20,28,40,64):
    alpha=math.pi/N
    D0=2*math.cos(alpha)/(1+math.cos(alpha))
    theta=alpha/2
    delta=alpha/2
    eq=objective(theta,delta,N)
    assert abs(eq-D0) < 2e-12, (N,eq,D0)

    # Deterministic grid over a fundamental theta interval and all finite delta values away from ±pi/2.
    for i in range(81):
        th=-alpha + 2*alpha*i/80
        for j in range(321):
            de=(-math.pi/2+1e-5) + (math.pi-2e-5)*j/320
            val=objective(th,de,N)
            assert val >= D0-2e-10, (N,th,de,val,D0)

    DWS=2/D0
    target=1+1/math.cos(alpha)
    assert abs(DWS-target)<2e-14

print("VERIFY_OK N=4,8,12,16,20,28,40,64 formula=DWS=1+sec(pi/N)")
