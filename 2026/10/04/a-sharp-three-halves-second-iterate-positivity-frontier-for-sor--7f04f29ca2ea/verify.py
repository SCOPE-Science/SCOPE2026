from fractions import Fraction as F

def sor_step(rho, omega, g, x):
    # Normalized A = [[1,-rho],[-rho,1]], forward SOR.
    x1 = (1-omega)*x[0] + omega*(g[0] + rho*x[1])
    x2 = (1-omega)*x[1] + omega*(g[1] + rho*x1)
    return (x1, x2)

def response_formula(rho, omega):
    p1 = (
        (omega, F(0)),
        (rho*omega*omega, omega),
    )
    d = omega*(2-omega+omega*omega*rho*rho)
    p2 = (
        (d, rho*omega*omega),
        (rho*omega*omega*(3-2*omega+omega*omega*rho*rho), d),
    )
    return p1, p2

def apply(P, g):
    return tuple(sum((P[i][j]*g[j] for j in range(2)), F(0)) for i in range(2))

tests = [
    (F(0), F(1)),
    (F(1,10), F(4,3)),
    (F(1,5), F(3,2)),
    (F(1,5), F(5,3)),
    (F(1,2), F(19,10)),
    (F(3,4), F(7,4)),
]
for rho,omega in tests:
    p1,p2=response_formula(rho,omega)
    for g in [(F(1),F(0)), (F(0),F(1)), (F(2,7),F(5,11))]:
        x0=(F(0),F(0))
        x1=sor_step(rho,omega,g,x0)
        x2=sor_step(rho,omega,g,x1)
        assert x1 == apply(p1,g)
        assert x2 == apply(p2,g)

# Robust safe side: omega <= 3/2 makes the critical factor nonnegative.
for omega in [F(1,10),F(1),F(7,5),F(3,2)]:
    for rho in [F(0),F(1,100),F(1,5),F(1,2),F(9,10)]:
        critical=3-2*omega+omega*omega*rho*rho
        assert critical >= 0

# Above 3/2, weak coupling can make the critical entry negative.
for omega,rho in [(F(8,5),F(1,10)),(F(5,3),F(1,5)),(F(19,10),F(1,10))]:
    critical=3-2*omega+omega*omega*rho*rho
    assert critical < 0

# Exact strictly positive witness.
rho=F(1,5)
omega=F(5,3)
g=(F(1),F(1,10))
x0=(F(0),F(0))
x1=sor_step(rho,omega,g,x0)
x2=sor_step(rho,omega,g,x1)
assert x1 == (F(5,3),F(13,18))
assert x2 == (F(43,54),F(-4,81))
assert x1[0] > 0 and x1[1] > 0 and x2[1] < 0

# Exact solution of [[1,-rho],[-rho,1]] y=g.
det=1-rho*rho
xstar=((g[0]+rho*g[1])/det,(rho*g[0]+g[1])/det)
assert xstar == (F(17,16),F(5,16))
assert all(v>0 for v in xstar)

# One-dimensional positivity for representative rational omega and many k.
for omega in [F(1,10),F(1),F(3,2),F(19,10)]:
    for k in range(1,21):
        coeff=1-(1-omega)**k
        assert coeff > 0

print("VERIFY_OK")
