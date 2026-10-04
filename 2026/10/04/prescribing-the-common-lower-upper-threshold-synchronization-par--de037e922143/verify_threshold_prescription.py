import itertools, math

def eps(t):
    return sum(1.0-math.cos(x) for x in t)

a=2.0*math.pi/3.0
ks=list(itertools.product((a,-a), repeat=3))
pts=[]
for i in range(1,10):
    pts.append((0.173*i-1.1, 0.271*i-1.7, -0.193*i+0.8))

max_err=0.0
for k in ks:
    for t in pts:
        lhs=9.0-eps(tuple(k[j]+t[j] for j in range(3)))-eps(t)
        rhs=eps(tuple(t[j]-k[j] for j in range(3)))
        max_err=max(max_err,abs(lhs-rhs))
assert max_err < 1e-12

# Coordinate-even test form factor: sign changes leave it invariant.
def v(t):
    return math.exp(0.4*sum(math.cos(x) for x in t)) + 0.2*math.exp(-0.7*sum((math.cos(x)+0.5)**2 for x in t))
for signs in itertools.product((1,-1), repeat=3):
    for t in pts:
        u=tuple(signs[j]*t[j] for j in range(3))
        assert abs(v(u)-v(t)) < 1e-12

# Algebraic inversion of the target quotient.
for gamma in (0.25,1.0,3.0,6.0,8.75):
    r=(9.0-gamma)/(2.0*gamma)
    recovered=9.0/(1.0+2.0*r)
    assert abs(recovered-gamma) < 1e-12

print(f"VERIFY_OK identities={len(ks)*len(pts)} gamma_cases=5 max_err={max_err:.3e}")
