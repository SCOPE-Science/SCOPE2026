import math

def hazard(x, alpha, beta, rho):
    t = -math.log(x)
    a = alpha*t**beta
    G = math.exp(-a)
    S0 = -math.expm1(-a)
    g = alpha*beta*t**(beta-1.0)*G/x
    return g/(S0*(1.0-rho+rho*G))

params = [
    (0.2, 0.4, 0.1),
    (1.0, 1.0, 0.5),
    (3.0, 2.0, 0.9),
    (7.0, 0.7, 0.3),
]
for alpha,beta,rho in params:
    vals=[]
    for k in (4,6,8,10):
        x=1.0-10.0**(-k)
        vals.append((1.0-x)*hazard(x,alpha,beta,rho))
    assert abs(vals[-1]-beta) < 3e-4*max(1.0,beta), (alpha,beta,rho,vals)

v1 = hazard(math.exp(-80.0), 2.0, 0.5, 0.4)
v2 = hazard(math.exp(-160.0), 2.0, 0.5, 0.4)
assert v2 > v1

u1 = hazard(math.exp(-8.0), 0.5, 2.0, 0.4)
u2 = hazard(math.exp(-12.0), 0.5, 2.0, 0.4)
assert u2 < u1

rho=0.3
for alpha in (0.7, 1.0, 1.4):
    x=1e-9
    h=hazard(x,alpha,1.0,rho)
    if alpha < 1:
        assert h > 1e2
    elif alpha == 1:
        assert abs(h-1/(1-rho)) < 1e-6
    else:
        assert h < 1e-3

print("VERIFY_OK")
