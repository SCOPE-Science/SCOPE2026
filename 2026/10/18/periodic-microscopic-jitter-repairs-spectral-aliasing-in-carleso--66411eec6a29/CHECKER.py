"""Finite-fiber diagnostics for periodic-jitter Carleson orbit sampling.

The infinite-dimensional Carleson interpolation step is analytic and is not
verified by this finite checker. Python standard library only.
"""
import cmath
import math


def ppower(z, t):
    return cmath.exp(t * (math.log(abs(z)) + 1j * cmath.phase(z)))


def close(a, b, tol=1e-10):
    assert abs(a-b) <= tol * max(1.0, abs(a), abs(b)), (a,b)


def vandermonde(z, r, eps, p):
    return [[ppower(q, (r+eps)*a) for q in z] for a in range(p)]


def det2(m):
    return m[0][0]*m[1][1]-m[0][1]*m[1][0]


def det3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
            -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
            +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))


rho = 0.7
z2 = [1j*rho, -1j*rho]
r, p = 2, 2
close(ppower(z2[0], r), ppower(z2[1], r))
close(ppower(z2[0], r*p), ppower(z2[1], r*p))

# The underlying coefficients of the infinite frame agree exactly with
# the residue-wise kernel factorization for each finite coordinate input.
x = [complex(0.4, -0.3), complex(-0.6, 0.2)]
eps = 0.017
for a in range(p):
    for k in range(18):
        t = r*(p*k+a)+a*eps
        direct = sum(x[j]*(1-abs(z2[j])**2)**0.5*ppower(z2[j], t)
                     for j in range(2))
        xi = ppower(z2[0], r*p)
        norm_factor = ((1-rho*rho)/(1-abs(xi)**2))**0.5
        grouped = xi**k*(1-abs(xi)**2)**0.5*norm_factor * sum(
                    x[j]*ppower(z2[j], (r+eps)*a) for j in range(2))
        close(direct, grouped)

# Analytic two-column singular-value formula and sharp epsilon^2 law.
c = ((1-rho**2)/(1-rho**(2*r*p)))**0.5
limit = c*c*rho**4*math.pi**2/(2*(1+rho**4))
for eps in [0.04, 0.02, 0.01, 0.005, 0.002]:
    v = vandermonde(z2, r, eps, p)
    delta2 = c**4*abs(det2(v))**2
    tr = 2*c**2*(1+rho**(4+2*eps))
    low = 2*delta2/(tr+math.sqrt(tr*tr-4*delta2))
    assert low > 0
    assert abs(low/eps**2-limit)/limit < 0.15
    close(abs(det2(v))**2,
          4*rho**(4+2*eps)*math.sin(math.pi*eps/2)**2)

# Three aliased rth powers: the 3x3 determinant is of cubic order, while
# the second finite difference is of quadratic order in epsilon.
z3 = [rho*cmath.exp(1j*theta) for theta in [-math.pi/2, 0, math.pi/2]]
r3,p3=4,3
for j in range(1,3):
    close(ppower(z3[0],r3), ppower(z3[j],r3))
    close(ppower(z3[0],r3*p3), ppower(z3[j],r3*p3))
for eps in [.03,.02,.01,.005]:
    v=vandermonde(z3,r3,eps,p3)
    determinant=abs(det3(v))
    assert determinant>0
    # Vandermonde determinant equals the product of all node differences.
    w=[ppower(q,r3+eps) for q in z3]
    product=abs((w[1]-w[0])*(w[2]-w[0])*(w[2]-w[1]))
    close(determinant,product)
    assert 0.0001 < determinant/eps**3 < 1000
    cancellation=[sum(v[a][j]*coef for j,coef in enumerate((1,-2,1)))
                  for a in range(p3)]
    assert max(abs(q) for q in cancellation) < 5*eps**2
print('PASS: 36 residue identities, two-point determinant and quadratic loss,')
print('      three-point Vandermonde and second-order cancellation.')
