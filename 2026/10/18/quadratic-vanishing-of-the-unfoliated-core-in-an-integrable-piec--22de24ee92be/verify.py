"""Standalone finite checks for the exact corner-polygon area identity.
These are reproducibility checks, not a replacement for the analytic proof.
"""
import sympy as sp
import mpmath as mp

s,t=sp.symbols('s t',real=True)
B=sp.Matrix([[t**2-(1-s)**2,(1-2*s)*t],[(2*s-1)*t,(2*t-1)*t]])/(t-s)
v=sp.Matrix([t,1-s]); Q=sp.Matrix([[t,sp.Rational(-1,2)],[sp.Rational(-1,2),t]])
poly=s*s-t+t*t

def relation_zero(x):
    v=sp.together(sp.cancel(x))
    n,_=sp.fraction(v)
    assert sp.simplify(sp.rem(sp.Poly(n,s),sp.Poly(poly,s)).as_expr())==0, n

relation_zero(B.det()-1)
for z in B.T*Q*B-Q:
    relation_zero(z)
relation_zero(sp.det(sp.Matrix.hstack(v,B*v))+t*(1-2*s))
relation_zero(sp.trace(B)-(2+(1-2*s)**2/(s-t)))
mp.mp.dps=65

def k_real(e):
    return mp.acosh(1/(1-mp.sin(2*e)))/mp.acosh(1+2*mp.sin(e)**3/(mp.cos(e)-mp.sin(e)))

for k in (3,4,8,12):
    e=mp.findroot(lambda x:k_real(x)-k,(mp.mpf('.85')/k,mp.mpf('1.1')/k))
    theta=mp.pi/4-e
    tm=mp.sin(theta)**2; sm=mp.sin(theta)*mp.cos(theta)
    bm=mp.matrix([[tm*tm-(1-sm)**2,(1-2*sm)*tm],[(2*sm-1)*tm,(2*tm-1)*tm]])/(tm-sm)
    z=mp.matrix([tm,1-sm]); vec=[]
    for _ in range(k):
        vec.append(z)
        z=bm*z
    assert mp.fabs(z[0]-sm)<mp.mpf('1e-48') and mp.fabs(z[1]-tm)<mp.mpf('1e-48')
    vertices=[]
    for i in range(4):
        for a in vec:
            x,y=a[0]-mp.mpf('.5'),a[1]-mp.mpf('.5')
            for _ in range(i):
                x,y=-y,x
            vertices.append((x,y))
    twice=mp.fsum(vertices[j][0]*vertices[(j+1)%(4*k)][1]-vertices[j][1]*vertices[(j+1)%(4*k)][0] for j in range(4*k))
    actual=mp.fabs(twice)/2
    exact=mp.sin(2*e)-2*k*(1-mp.sin(2*e))*mp.sin(e)**2
    assert mp.fabs(actual-exact)<mp.mpf('1e-45'),(k,actual,exact)
for k in (100,300,1000):
    e=mp.findroot(lambda x:k_real(x)-k,(mp.mpf('.85')/k,mp.mpf('1.1')/k))
    A=mp.sin(2*e)-2*k*(1-mp.sin(2*e))*mp.sin(e)**2
    assert mp.fabs(k*k*A-mp.mpf(10)/3)<mp.mpf('0.2')
print('VERIFY_OK')
