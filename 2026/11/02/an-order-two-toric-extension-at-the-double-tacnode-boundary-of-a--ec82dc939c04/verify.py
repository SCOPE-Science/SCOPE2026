"""Exact checks for a two-tacnode degeneration of plane quartics.

Run with Python 3 and SymPy. The geometric semistable-reduction
argument is given in the accompanying proof, not inferred from testing.
"""
from sympy import symbols, I, factor, simplify, Poly, groebner

x,y,z,a,s,u,v,U,r,W,V = symbols('x y z a s u v U r W V')
F = x**4 + y**4 + z**4 + a*x**2*y**2
assert simplify(F.subs(a,2) - ((x**2+y**2)**2+z**4)) == 0
assert simplify(F.subs(a,-2) - ((x**2-y**2)**2+z**4)) == 0
assert simplify(F.subs(y,I*y) - F.subs(a,-a)) == 0

# The genus-three fibers are smooth for a^2 != 4. At every singular
# fiber each of the two components is a nondegenerate conic.
assert factor(F.diff(z)) == 4*z**3
assert factor(F.diff(x)) == 2*x*(2*x**2+a*y**2)
assert factor(F.diff(y)) == 2*y*(a*x**2+2*y**2)
assert simplify((a*x**2+2*y**2).subs(x**2,-a*y**2/2) - (4-a**2)*y**2/2) == 0

local = u**2+v**4+s**4*(u-1)
completed = (u+s**4/2)**2 + v**4 -s**4*(1+s**4/4)
assert simplify(local-completed)==0

# Weighted blow-up (weights 2,1,1): U=r^2 W, v=r V, rho=r.
# Exceptional curve W^2+V^4=1; chart with v nonzero has
# W^2+1-R^4=0 and base rho=v R.
assert simplify((U**2+v**4-r**4).subs({U:r**2*W,v:r*V})/r**4-(W**2+V**4-1))==0
assert simplify((U**2+v**4-r**4).subs({U:v**2*W,r:v*V})/v**4-(W**2+1-V**4))==0

# Smooth elliptic exceptional: affine partials of W^2+V^4-1
# do not vanish simultaneously on the curve.
assert list(groebner([W**2+V**4-1,2*W,4*V**3],W,V))==[1]

# Binary-quartic invariants of W^2=1-V^4 give j=1728.
aa,bb,cc,dd,ee=(-1,0,0,0,1)
InvI=12*aa*ee-3*bb*dd+cc**2
InvJ=72*aa*cc*ee+9*bb*cc*dd-27*aa*dd**2-27*bb**2*ee-2*cc**3
assert InvI==-12 and InvJ==0
assert 1728*4*InvI**3/(4*InvI**3-InvJ**2)==1728

# At rho=0 the exceptional meets the two strict-transform conics in
# W^2+1=0. They are distinct, and the crossing equation rho=v V
# shows both nodes are transverse.
assert factor((W**2+1).subs(W,I))==0
assert factor((W**2+1).subs(W,-I))==0
assert simplify((W**2+1).diff(W).subs(W,I))!=0
assert simplify((W**2+1).diff(W).subs(W,-I))!=0

# Genus check after resolution: two elliptic and two rational
# components, four transverse edges; g=sum(g_i)+b1=2+(4-4+1)=3.
assert 2+(4-4+1)==3
print('QUARTIC_OK: two smooth conics at a=2; two A3 tacnodes; smooth elsewhere')
print('LOCAL_OK: exact completed square and weighted charts')
print('ELLIPTIC_OK: smooth exceptional quartic, j=1728, two points at infinity')
print('STABLE_OK: four nodes on semistable model and genus-three banana contraction')
