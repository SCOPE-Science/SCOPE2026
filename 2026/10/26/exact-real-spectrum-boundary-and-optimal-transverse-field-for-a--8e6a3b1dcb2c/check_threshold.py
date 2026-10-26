"""Independent exact-matrix and algebraic checks for a three-spin central-defect spectrum.

Requires Python 3 with SymPy; NumPy is used only for optional numerical checks.
"""
import sympy as S

h, g, e, z, u, y = S.symbols('h g e z u y', real=True)
I2 = S.eye(2)
X = S.Matrix([[0, 1], [1, 0]])
Z = S.diag(1, -1)
P = S.Matrix([[0, 1], [0, 0]])

def one_site(op, i):
    out = S.ones(1, 1)
    for k in range(3):
        out = S.kronecker_product(out, op if i == k else I2)
    return out

Xs = [one_site(X, i) for i in range(3)]
Zs = [one_site(Z, i) for i in range(3)]
H = -(Xs[0]*Xs[1] + Xs[1]*Xs[2])/4 - h*(Zs[0] + Zs[1] + Zs[2])/2 + g*one_site(P, 1)
F = (64*y**3-(32+176*z)*y**2+(4+48*z+76*z**2-16*u)*y
     -z*(1-3*z)**2-12*u*z)
D = (16*u**3-(8+208*z+944*z**2)*u**2
     +(1+20*z+224*z**2+800*z**3-2048*z**4)*u
     +16*z**3+208*z**4+2048*z**5)

print('Checking the eight-dimensional characteristic determinant...')
cp = H.charpoly(); charpoly = cp.as_expr().subs(cp.gen, e)
assert S.simplify(charpoly-(e**2-h**2/4)*F.subs({y:e**2,z:h**2,u:g**2})/64)==0
print('Checking the cubic discriminant and threshold brackets...')
assert S.simplify(S.discriminant(F,y)-S.Rational(65536,1)*D)==0
assert S.factor(D.subs(u,z)) == z*(4*z+1)**3
assert S.factor(D.subs(u,z+S.Rational(1,4))) == -z*(448*z**3+224*z**2+83*z+8)
assert S.factor(D.subs(u,0)) == 16*z**3*(128*z**2+13*z+1)
print('Checking the global-minimum resultant...')
R = S.factor(S.resultant(D,S.diff(D,z),u))
R_target = -32768*z**2*(4*z+1)**3*(176*z**2+25*z+2)**3*(3072*z**3+876*z**2+52*z-3)
assert S.simplify(R-R_target)==0
print('Checking the low-field Puiseux expansion...')
t = S.symbols('t',real=True)
u_series=S.Rational(1,4)-S.sqrt(2)*t+S.Rational(13,2)*t**2
assert S.expand(D.subs({z:t**2,u:u_series})).coeff(t,2)==0
assert S.expand(D.subs({z:t**2,u:u_series})).coeff(t,3)==0
print('Checking the large-field expansion...')
assert S.expand(D.subs(u,z+S.Rational(1,32))).coeff(z,4)==0
print('Checking the zero-field threshold...')
assert S.simplify(F.subs(z,0) - 4*y*((4*y-1)**2-4*u))==0

from mpmath import mp
mp.dps = 50
root_z=mp.findroot(lambda a:3072*a**3+876*a*a+52*a-3,(mp.mpf('.03'),mp.mpf('.04')))
root_u=mp.findroot(lambda a:mp.mpf(16)*a**3-(8+208*root_z+944*root_z**2)*a*a+(1+20*root_z+224*root_z**2+800*root_z**3-2048*root_z**4)*a+16*root_z**3+208*root_z**4+2048*root_z**5,(mp.mpf('.13'),mp.mpf('.15')))
assert mp.mpf('0.03480049') < root_z < mp.mpf('0.03480051')
assert mp.mpf('0.14217254') < root_u < mp.mpf('0.14217257')
print('Minimum: h/J=',mp.nstr(mp.sqrt(root_z),25),'gamma/J=',mp.nstr(mp.sqrt(root_u),25))
print('All exact identities and numerical brackets verified.')
