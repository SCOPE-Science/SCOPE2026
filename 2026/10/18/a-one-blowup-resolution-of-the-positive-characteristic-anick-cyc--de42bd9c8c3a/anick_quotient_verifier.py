"""Finite arithmetic checks for the Anick cyclic quotient and blow-up charts.
These checks supplement (and do not replace) the algebraic proofs.
"""
from itertools import product
from sympy import symbols, Poly, expand
x,y,z,t,d,U,V,a,b,c = symbols('x y z t d U V a b c')
for p in (2,3,5,7):
    for xx,yy,zz,tt in product(range(p),repeat=4):
        dd=(xx*zz-yy*tt)%p
        x1=(xx+dd*tt)%p; y1=(yy+dd*zz)%p
        assert (x1*zz-y1*tt)%p==dd
        u=(pow(xx,p,p)-pow(dd*tt,p-1,p)*xx)%p
        v=(pow(yy,p,p)-pow(dd*zz,p-1,p)*yy)%p
        u1=(pow(x1,p,p)-pow(dd*tt,p-1,p)*x1)%p
        v1=(pow(y1,p,p)-pow(dd*zz,p-1,p)*y1)%p
        assert (u,v)==(u1,v1)
        assert (pow(zz,p,p)*u-pow(tt,p,p)*v-pow(dd,p,p)*(1-pow(zz*tt,p-1,p)))%p==0
    # Chart identities for strict transforms of the invariant hypersurface.
    F=z**p*U-t**p*V-d**p*(1-(z*t)**(p-1))
    for expr, scale, rhs in (
        ({t:z*b,d:z*c},z,U-b**p*V-c**p*(1-(z*z*b)**(p-1))),
        ({z:t*a,d:t*c},t,a**p*U-V-c**p*(1-(t*t*a)**(p-1))),
        ({z:d*a,t:d*b},d,a**p*U-b**p*V-1+(d*d*a*b)**(p-1)),
    ):
        remainder=Poly(expand(F.subs(expr,simultaneous=True)/scale**p-rhs),z,t,d,U,V,a,b,c)
        assert all(int(q)%p==0 for q in remainder.coeffs()),(p,expr,remainder)
    print('PASS characteristic',p,'points',p**4,'blow-up chart identities')
print('All finite checks passed; smoothness and factoriality follow from the written proofs.')
