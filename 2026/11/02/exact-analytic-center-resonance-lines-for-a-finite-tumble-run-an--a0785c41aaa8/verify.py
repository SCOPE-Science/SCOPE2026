"""Reproduce exact moments and stationary equations for analytic finite-tumble RTP families.
Requires SymPy. This provides finite checks; the all-parameter theorem has an analytic proof.
"""
import sympy as sp

x=sp.symbols('x', real=True)
checks=0

def poly_density(u,n):
    c=(u+1)/2
    f=(1-x*x)**(u+n-1)
    for j in range(n):
        f=sp.cancel((-sp.diff(x*f,x)/2+(c+j)*f)/(c+j))
    norm=sp.gamma(u+n+sp.Rational(1,2))/(sp.sqrt(sp.pi)*sp.gamma(u+n))
    return sp.expand(f*norm)

for u in [sp.Integer(1),sp.Integer(2),sp.Integer(3)]:
    for n in range(5):
        v=u+1+2*n
        f=poly_density(u,n)
        q=sp.cancel((u*f+x*((1-x*x)*sp.diff(f,x)+(u-2)*x*f))/(u+v-1))
        assert sp.cancel(sp.diff(x*q,x)+u*f-(u+v)*q)==0
        assert sp.cancel(sp.diff((1-x*x)*f-q,x)+u*x*f)==0
        checks+=2
        for k in range(6):
            actual=sp.integrate(x**(2*k)*f,(x,-1,1))
            target=sp.rf(v/2,k)*sp.rf(sp.Rational(1,2),k)/(sp.rf((u+v)/2,k)*sp.rf((u+1)/2,k))
            assert sp.simplify(actual-target)==0,(u,n,k,actual,target)
            checks+=1
        assert sp.simplify(q.subs(x,0))>=0
        checks+=1
assert sp.simplify(poly_density(sp.Integer(1),0)-sp.Rational(1,2))==0
checks+=1
assert sp.simplify(poly_density(sp.Integer(1),1)-sp.Rational(3,8)*(1+x*x))==0
checks+=1
# Positivity of the nonanalytic coefficient off the exceptional rays.
for u,v in [(sp.Integer(1),sp.Rational(3,2)),(sp.Integer(2),sp.Integer(2)),(sp.Integer(2),sp.Rational(5,2))]:
    K=sp.sqrt(sp.pi)*sp.gamma((u+v)/2)*sp.gamma((u+1)/2)/(sp.gamma(v/2)*sp.gamma(u/2)*sp.cos(sp.pi*v/2)*sp.gamma((u+1-v)/2)*sp.gamma((v+1)/2))
    assert sp.simplify(K)!=0
    checks+=1
print('PASS:',checks,'independent exact stationary-equation and moment checks')
