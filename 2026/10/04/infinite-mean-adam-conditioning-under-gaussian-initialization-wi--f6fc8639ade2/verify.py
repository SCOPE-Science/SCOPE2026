import math
import random

def eigvals_sym2(a, b, c):
    tr = a + c
    disc = math.sqrt((a-c)*(a-c) + 4.0*b*b)
    return (0.5*(tr-disc), 0.5*(tr+disc))

def cond2_2x2(A):
    a,b = A[0]
    c,d = A[1]
    # eigenvalues of A^T A
    q11 = a*a + c*c
    q12 = a*b + c*d
    q22 = b*b + d*d
    lo,hi = eigvals_sym2(q11,q12,q22)
    assert lo > 0.0
    return math.sqrt(hi/lo)

def mat_cond_spd(H):
    a,c = H[0]
    _,b = H[1]
    lo,hi = eigvals_sym2(a,c,b)
    assert lo > 0.0
    return hi/lo

def scaled(H,t):
    return [[H[0][0],H[0][1]],[t*H[1][0],t*H[1][1]]]

def floor_formula(H):
    a,c = H[0]
    _,b = H[1]
    r1 = math.hypot(a,c)
    r2 = math.hypot(b,c)
    rho = abs(c)*(a+b)/(r1*r2)
    return math.sqrt((1.0+rho)/(1.0-rho)), r1/r2, rho

random.seed(173)

# Random SPD matrices: predicted row-equilibrating scaling attains the formula.
for _ in range(1000):
    a = 10.0**random.uniform(-1.0,1.0)
    b = 10.0**random.uniform(-1.0,1.0)
    lim = math.sqrt(a*b)
    c = random.uniform(-0.95,0.95)*lim
    H = [[a,c],[c,b]]
    kstar,tstar,rho = floor_formula(H)
    direct = cond2_2x2(scaled(H,tstar))
    assert abs(direct-kstar) <= 2e-10*max(1.0,kstar)

    # Perturb the unique positive optimum on both sides.
    for factor in (0.2,0.5,0.9,1.1,2.0,5.0):
        kval = cond2_2x2(scaled(H,tstar*factor))
        assert kval >= kstar*(1.0-2e-10)

# Axis-aligned matrices have floor one.
for kappa in (1.0,2.0,10.0,1000.0):
    H = [[1.0,0.0],[0.0,kappa]]
    kstar,tstar,rho = floor_formula(H)
    assert abs(kstar-1.0) < 1e-14
    assert abs(rho) < 1e-14
    assert abs(cond2_2x2(scaled(H,tstar))-1.0) < 1e-12

# 45-degree rotation: the best possible scaled condition number equals kappa.
for kappa in (1.0,1.5,2.0,5.0,10.0,100.0):
    a = 0.5*(kappa+1.0)
    c = 0.5*(kappa-1.0)
    H = [[a,c],[c,a]]
    assert abs(mat_cond_spd(H)-kappa) <= 2e-12*max(1.0,kappa)
    kstar,tstar,rho = floor_formula(H)
    assert abs(tstar-1.0) < 1e-14
    assert abs(kstar-kappa) <= 2e-11*max(1.0,kappa)
    for t in (1e-4,0.01,0.2,0.5,1.0,2.0,5.0,100.0,1e4):
        assert cond2_2x2(scaled(H,t)) >= kappa*(1.0-2e-10)

# Exact orientation formula.
for kappa in (2.0,5.0,20.0):
    for theta in (0.0,0.1,0.3,math.pi/8,math.pi/4):
        co = math.cos(theta)
        si = math.sin(theta)
        a = co*co + kappa*si*si
        b = si*si + kappa*co*co
        c = (1.0-kappa)*si*co
        H = [[a,c],[c,b]]
        _,_,rho = floor_formula(H)
        s2 = math.sin(2.0*theta)
        rho2 = ((kappa*kappa-1.0)**2*s2*s2) / (
            4.0*kappa*kappa + (kappa*kappa-1.0)**2*s2*s2
        )
        assert abs(rho*rho-rho2) < 3e-13

# Reciprocal singular tail in two dimensions.
H = [[2.0,0.7],[0.7,1.3]]
a,c = H[0]
_,b = H[1]
Delta = a*b-c*c
r1 = math.hypot(a,c)
prev = None
for eps in (1e-1,1e-2,1e-3,1e-4,1e-5):
    # g=(eps,1) induces D=diag(1/eps,1).
    K = cond2_2x2([[a/eps,c/eps],[c,b]])
    lower = (r1*r1)/(2.0*Delta*eps)
    assert K >= lower*(1.0-2e-10)
    if prev is not None:
        assert K > 8.0*prev
    prev = K

print("verification passed")
