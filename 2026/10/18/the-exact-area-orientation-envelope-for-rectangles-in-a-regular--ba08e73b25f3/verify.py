"""Independent numerical/algebraic diagnostics for rectangles in a regular pentagon.

The theorem is proved analytically in RESULT.md. These finite checks are not
substitutes for its universal support-line and trigonometric arguments.
Uses Python 3 standard library only.
"""
from decimal import Decimal, localcontext
from math import sin, cos, pi
from random import Random

with localcontext() as ctx:
    ctx.prec = 85
    D = Decimal
    one = D(1)
    five = D(5)
    root5 = five.sqrt()
    p = (one + root5) / D(4)
    r = (root5 - one) / D(4)
    q = (D(10) - D(2)*root5).sqrt() / D(4)
    s = (D(10) + D(2)*root5).sqrt() / D(4)
    k = root5 / D(4)
    rho = (D(3) - root5) / D(2)
    T = r / s
    tol = D('2e-73')
    close = lambda a, b: abs(a-b) < tol
    assert close(q/s, one-rho)
    assert close(p*(one+rho), D(2)*k)
    assert close(q*s, k)
    assert close(k/p, (D(5)-root5)/D(4))
    # The four contact equations' weighted sum has zero centroid coefficient.
    normals = ((p,q),(-r,s),(-one,D(0)),(-r,-s),(p,-q))
    weights = (D('0.5'),rho/D(2),rho/D(2),D('0.5'))
    assert close(sum(weights[j]*normals[j][0] for j in range(4)),D(0))
    assert close(sum(weights[j]*normals[j][1] for j in range(4)),D(0))
    checks = 0
    for i in range(1001):
        t = T*D(i)/D(1000)
        # Coefficients of A and B in the four support inequalities.
        aco = (p+q*t,r-s*t,one,r+s*t)
        bco = (q-p*t,s+r*t,t,s-r*t)
        assert min(aco) >= -tol and min(bco) >= -tol
        assert close(sum(weights[j]*aco[j] for j in range(4)),p+q*t)
        assert close(sum(weights[j]*bco[j] for j in range(4)),s-r*t)
        A = k/(p+q*t)
        B = k/(s-r*t)
        cx = A+t*B-p
        cy = t*A-(r/s)*t*B
        vals = [normals[j][0]*cx+normals[j][1]*cy+
                aco[j]*A+bco[j]*B for j in range(4)]
        for val in vals:
            assert close(val,p)
        fifth = p*cx-q*cy+(p-q*t)*A+(q+p*t)*B
        residual = p-fifth
        factor = (D(5)-root5)/D(8)*t*(one-t/T)/((p+q*t)*(s-r*t))
        assert residual >= -tol
        assert close(residual,factor)
        area = D(4)*A*B*(one+t*t)
        envelope = D(5)*(one+t*t)/(D(4)*(p+q*t)*(s-r*t))
        assert close(area,envelope)
        assert area <= D(5)/(D(4)*p*s)+tol
        checks += 12
    assert close(D(4)*(k/p)*(k/s), (D(5)-root5)*q)
    assert close(D(4)*(k/p)*(k/s), D(5)/(D(4)*p*s))
    print('DECIMAL_SUPPORT_CHECKS',checks,'MAX_AREA',round(float(D(5)/(D(4)*p*s)),15))

# Independent geometric random-point containment diagnostics, including rotations.
rng = Random(5102014)
N = [(cos((2*j+1)*pi/5),sin((2*j+1)*pi/5)) for j in range(5)]
h = cos(pi/5)
Amax = (5-5**0.5)*sin(pi/5)
feasible=0
for i in range(50000):
    angle = rng.random()*pi/2
    ux,uy=cos(angle),sin(angle)
    vx,vy=-uy,ux
    a = rng.random()*0.8
    b = rng.random()*0.8
    cx = rng.uniform(-0.28,0.28)
    cy = rng.uniform(-0.28,0.28)
    fits=True
    for nx,ny in N:
        if nx*cx+ny*cy+a*abs(nx*ux+ny*uy)+b*abs(nx*vx+ny*vy)>h+1e-12:
            fits=False
            break
    if fits:
        feasible+=1
        assert 4*a*b<=Amax+1e-10
assert feasible>1000
print('VERIFY_OK','sampled_rectangles=50000','feasible=',feasible)
