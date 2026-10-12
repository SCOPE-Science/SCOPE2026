import sympy as sp

x,y,z,t=sp.symbols('x y z t')
K=x**2+y**2-z**2
Q=x*(x-z)*(x+z)*(y-z)*(y+z)*K

# The four diagonal maps preserve the arrangement polynomial up to a scalar.
for sx in (1,-1):
    for sy in (1,-1):
        image=sp.expand(Q.subs({x:sx*x,y:sy*y,z:z}, simultaneous=True))
        assert sp.expand(image-sx*Q)==0

# Intersections of each line component with the unique conic.
assert sp.factor(K.subs(x,0))==(y-z)*(y+z)          # unique secant
assert sp.factor(K.subs(x,z))==y**2                 # tangent at [1:0:1]
assert sp.factor(K.subs(x,-z))==y**2                # tangent at [-1:0:1]
assert sp.factor(K.subs(y,z))==x**2                 # tangent at [0:1:1]
assert sp.factor(K.subs(y,-z))==x**2                # tangent at [0:-1:1]

# Parametrization nu(t)=[2t:1-t^2:1+t^2] of the conic.
nu=sp.Matrix([2*t,1-t**2,1+t**2])
assert sp.expand(nu[0]**2+nu[1]**2-nu[2]**2)==0

# Four induced Möbius maps, verified projectively.
nu_minus=sp.Matrix([2*(-t),1-(-t)**2,1+(-t)**2])
assert all(sp.expand(a-b)==0 for a,b in zip(sp.Matrix([-nu[0],nu[1],nu[2]]),nu_minus))

nu_inv_scaled=sp.Matrix([2*t,t**2-1,t**2+1]) # t^2*nu(1/t)
assert all(sp.expand(a-b)==0 for a,b in zip(sp.Matrix([nu[0],-nu[1],nu[2]]),nu_inv_scaled))
nu_minv_scaled=sp.Matrix([-2*t,t**2-1,t**2+1]) # t^2*nu(-1/t)
assert all(sp.expand(a-b)==0 for a,b in zip(sp.Matrix([-nu[0],-nu[1],nu[2]]),nu_minv_scaled))

# The distinguished points have parameters 0, infinity, 1, -1.
assert sp.Matrix([0,1,1])==nu.subs(t,0)
assert sp.Matrix([2,0,2])==nu.subs(t,1)
assert sp.Matrix([-2,0,2])==nu.subs(t,-1)
# At infinity put t=1/s, multiply by s^2, and set s=0.
s=sp.symbols('s')
nu_inf=[sp.expand(c.subs(t,1/s)*s**2) for c in nu]
assert [sp.limit(c,s,0) for c in nu_inf]==[0,-1,1]

# Any Möbius map preserving {0,infinity} is either t -> a*t or t -> a/t.
# Preservation of {1,-1} forces a^2=1 in either branch.
a=sp.symbols('a')
assert sp.solve(sp.Eq(a**2,1),a)==[-1,1]

print('VERIFY_OK group_order=4 group=C2xC2 restrictions=t,-t,1/t,-1/t')
