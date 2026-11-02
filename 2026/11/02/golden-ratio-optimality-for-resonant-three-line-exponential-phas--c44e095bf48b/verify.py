"""Supplementary finite arithmetic checks for a two-exponential phase-retrieval formula.

Only the standard Python library is required. Checks are supplementary to the
analytical proof; floating-point tests do not certify limiting statements.
"""
import cmath
import math
import random

rng = random.Random(29317)
phi_inv = (math.sqrt(5.0) - 1.0) / 2.0
checks = 0

def close(a, b, tol=2e-8):
    global checks
    checks += 1
    assert abs(a-b) <= tol * max(1.0, abs(a), abs(b)), (a,b)

# The exact coefficient identity on three lines, Gram eigenvalues, and
# invertibility of four specified phaseless evaluations.
for alpha in [phi_inv, math.sqrt(2.0)/2.0, 2.0/7.0, 0.37]:
    for k in range(1, 41):
        h = 1.3
        a = math.pi*k/(2*h)
        theta = math.pi*k*alpha
        cs, sn = math.cos(theta), math.sin(theta)
        A = ((1.0, 0.0), ((-1.0)**k,0.0), (cs,-sn))
        g11 = sum(row[0]**2 for row in A)
        g22 = sum(row[1]**2 for row in A)
        g12 = sum(row[0]*row[1] for row in A)
        close(g11+g22, 3.0)
        close(g11*g22-g12*g12, 2.0*sn*sn)
        lower = (3-math.sqrt(9-8*sn*sn))/2
        close(lower*(3-lower), 2*sn*sn)
        if abs(sn)<1e-10:
            continue
        for _ in range(12):
            c = complex(rng.uniform(-2,2),rng.uniform(-2,2))
            d = complex(rng.uniform(-2,2),rng.uniform(-2,2))
            u,v=abs(c)**2,abs(d)**2
            z=c*d.conjugate()
            U,V=z.real,z.imag
            r=0.47
            def intensity(xx,yy):
                zz=complex(xx,yy)
                return abs(c*cmath.exp(a*zz)+d*cmath.exp(-a*zz))**2
            i0=intensity(0,0)
            ip=intensity(r/a,0)
            im=intensity(-r/a,0)
            ia=intensity(0,alpha*h)
            ud=(ip-im)/(2*math.sinh(2*r))
            us=(ip+im-2*i0)/(2*(math.cosh(2*r)-1))
            uu,vv=(us+ud)/2,(us-ud)/2
            UU=(i0-us)/2
            VV=(UU*cs-(ia-us)/2)/sn
            for x,y in [(uu,u),(vv,v),(UU,U),(VV,V)]:
                close(x,y,2e-7)

# Two noncollinear phase witnesses are sharply separated at scaled real sites.
for k in range(1,56):
    a=math.pi*k/2
    r=math.log(2)/2
    f=[cmath.exp(a*x)+1j*cmath.exp(-a*x) for x in (-r/a,r/a)]
    g=[cmath.exp(a*x)-1j*cmath.exp(-a*x) for x in (-r/a,r/a)]
    phase_distance_sq=sum(abs(x)**2+abs(y)**2 for x,y in zip(f,g))-2*abs(sum(x*y.conjugate() for x,y in zip(f,g)))
    close(phase_distance_sq,2)
    for y in (0,1,phi_inv):
        diff=abs(cmath.exp(a*complex(0,y))+1j*cmath.exp(-a*complex(0,y)))**2-abs(cmath.exp(a*complex(0,y))-1j*cmath.exp(-a*complex(0,y)))**2
        close(diff,4*math.sin(math.pi*k*y))

# Fibonacci subsequence sanity check for the Hurwitz-scale asymptotic.
prev,cur=1,2
for _ in range(9):
    p, prev, cur = cur,cur,prev+cur
    k = p
    ss=abs(math.sin(math.pi*k*phi_inv))
    sens=math.sqrt((3-math.sqrt(9-8*ss*ss))/2)
    if k>=21:
        assert abs(k*sens-math.pi*math.sqrt(2/15))<0.03
        checks+=1
print('PASS',checks,'finite assertions')
