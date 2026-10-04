import sympy as sp

a,b,c,d,e,f,g,h = sp.symbols('a b c d e f g h')
y,z,w,t,u,v = sp.symbols('y z w t u v')
# affine x=1 local equation at P=[1:0:0:0]
F = e*y + f*y**2 + a*y*z + b*y*w + c*z*w + d*y*z*w + g*z**2*w + h*z*w**2
# P is singular iff e=0: gradient at origin
G = [sp.diff(F,q).subs({y:0,z:0,w:0}) for q in (y,z,w)]
assert G == [e,0,0]
F0 = sp.expand(F.subs(e,0))
H = sp.hessian(F0,(y,z,w)).subs({y:0,z:0,w:0})
assert sp.factor(H.det()) == 2*c*(a*b-c*f)
# Corank-one locus D=ab-cf=0, so f=ab/c (c != 0)
Fc = sp.expand(F0.subs(f,a*b/c))
k = sp.Matrix([-c,b,a])
assert sp.simplify((H.subs(f,a*b/c))*k) == sp.zeros(3,1)
T = a*h+b*g-c*d
# cubic restriction along kernel
kernel_restriction = sp.factor(Fc.subs({y:-c*t,z:b*t,w:a*t}))
assert kernel_restriction == a*b*T*t**3
# Coordinates adapted to kernel: w=t, y=u-c*t/a, z=v+b*t/a.
Fuvt = sp.factor(Fc.subs({y:u-c*t/a,z:v+b*t/a,w:t}))
# At t=0, transverse Hessian in (u,v) is nondegenerate.
Huv = sp.hessian(Fuvt,(u,v)).subs({u:0,v:0,t:0})
assert sp.factor(Huv.det()) == -a**2
# Critical graph u(t),v(t) begins in order t^2; solve those coefficients.
U2,V2 = sp.symbols('U2 V2')
Fu,Fv = sp.diff(Fuvt,u), sp.diff(Fuvt,v)
cu = sp.expand(Fu.subs({u:U2*t**2,v:V2*t**2})).coeff(t,2)
cv = sp.expand(Fv.subs({u:U2*t**2,v:V2*t**2})).coeff(t,2)
sol = sp.solve([cu,cv],[U2,V2], dict=True, simplify=True)[0]
red = sp.expand(Fuvt.subs({u:sol[U2]*t**2,v:sol[V2]*t**2}))
c3 = sp.factor(red.coeff(t,3))
c4 = sp.factor(red.coeff(t,4))
assert c3 == b*T/a**2
# On T=0, d=(ah+bg)/c and quartic coefficient is nonzero if a,b,c,g,h are nonzero.
c4_T = sp.factor(c4.subs(d,(a*h+b*g)/c))
assert c4_T == -b**2*g*h/(a**2*c)
# Sample points for all three strata, all with a*b*c*g*h != 0.
def vals(A,B,C,D,E,F,G,Hh):
    return {a:A,b:B,c:C,d:D,e:E,f:F,g:G,h:Hh}
assert H.det().subs(vals(1,1,1,0,0,0,1,1)) != 0 # A1
assert (a*b-c*f).subs(vals(1,1,1,0,0,1,1,1)) == 0 and T.subs(vals(1,1,1,0,0,1,1,1)) != 0 # A2
assert (a*b-c*f).subs(vals(1,1,1,2,0,1,1,1)) == 0 and T.subs(vals(1,1,1,2,0,1,1,1)) == 0 and c4_T.subs(vals(1,1,1,2,0,1,1,1)) != 0 # A3
print('gradient_at_P =', G)
print('hessian_det =', sp.factor(H.det()))
print('kernel_on_D0 =', list(k))
print('kernel_cubic =', kernel_restriction)
print('transverse_hessian_det =', sp.factor(Huv.det()))
print('reduced_t3 =', c3)
print('reduced_t4_on_T0 =', c4_T)
print('VERIFY_OK')
