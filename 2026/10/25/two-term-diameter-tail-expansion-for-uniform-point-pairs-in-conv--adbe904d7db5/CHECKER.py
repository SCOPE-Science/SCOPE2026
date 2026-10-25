"""Independent numerical/analytic checks for polytope diameter-tail expansion.

Dependencies: Python 3, mpmath (for 2D exact integral).  No randomness.
"""
import math
import mpmath as mp

mp.mp.dps = 65

def box_coeffs(lengths):
    d = len(lengths)
    v = math.prod(lengths)
    D = math.sqrt(sum(a * a for a in lengths))
    lead = 2**d * D**(2*d) / (math.factorial(2*d)*v**4)
    relative = 3*D*sum(1/(a*a) for a in lengths)/(2*d+1) - d/D
    return lead, relative


def rectangle_integral(a, b, eps):
    """Exact pair-distance tail as a single quadrature, independent of cone formula."""
    a, b, eps = (mp.mpf(x) for x in (a,b,eps))
    D = mp.sqrt(a*a+b*b)
    R = D-eps
    bound = a-mp.sqrt(R*R-b*b)
    def integrand(s):
        t = b-mp.sqrt(R*R-(a-s)**2)
        return 2*s*t*t/(a*a*b*b)
    return mp.quad(integrand, [mp.mpf('0'),bound])


for a,b in [(1,1),(2,1),(1.5,.7),(3,.45)]:
    D=mp.sqrt(mp.mpf(str(a))**2+mp.mpf(str(b))**2)
    v=mp.mpf(str(a))*mp.mpf(str(b))
    L=4*D**4/(mp.factorial(4)*v**4)
    rel=3*D*(1/mp.mpf(str(a))**2+1/mp.mpf(str(b))**2)/5-2/D
    errors=[]
    eps_grid = ['0.00005','0.000025','0.0000125'] if a/b>5 else ['0.001','0.0005','0.00025']
    for eps in eps_grid:
        h=mp.mpf(eps)
        val=rectangle_integral(str(a),str(b),eps)
        second=(val/(L*h**4)-1)/h
        errors.append(float(abs(second-rel)))
    assert errors[-1] < errors[0]/2, (a,b,errors)
    assert errors[-1] < .003, (a,b,errors)
    print('rectangle',a,b,'second-coefficient',mp.nstr(rel,15),'errors',errors)

# Independent moment derivation for a box: given 2d shape-two gamma/Dirichlet
# parameters, E(z_i^2)=6/[2d(2d+1)]. This reproduces the analytic second term.
for lengths in [(1,1,1),(1,2,3),(.7,1.3,3.2),(1,1,1,1)]:
    d=len(lengths)
    D=math.sqrt(sum(a*a for a in lengths))
    _,coef=box_coeffs(lengths)
    alt= 3*D/(2*d+1)*sum(a**-2 for a in lengths)-d/D
    assert abs(coef-alt)<1e-13
    assert coef>0
    print('box',lengths,'leading-and-relative',box_coeffs(lengths))

# Sharp box rigidity at fixed volume, strict away from equal lengths.
for lengths in [(1,1),(2,.5),(1,1,1),(1,2,.5),(1,2,3)]:
    d=len(lengths)
    v=math.prod(lengths)
    lead,_=box_coeffs(lengths)
    lower=2**d * d**d/(math.factorial(2*d)*v*v)
    assert lead>=lower*(1-1e-12)
    print('rigidity',lengths,'ratio',lead/lower)

print('DIAMETER_TAIL_CHECK_OK')
