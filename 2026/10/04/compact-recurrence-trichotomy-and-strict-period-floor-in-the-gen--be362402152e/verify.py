import sympy as sp

x,y,z,a,b = sp.symbols("x y z a b", nonzero=True)
fx, fy, fz = a*z, -b*y+z, -x+y+y**2

def L(f):
    return sp.expand(sp.diff(f,x)*fx + sp.diff(f,y)*fy + sp.diff(f,z)*fz)

F = y*z - (z**2+2*x*y)/(2*b) + (a-b**2+1)*y**2/(2*b) + y**3/(3*b)
G = (z**2-y**2)/(2*b) - y**3/(3*b) + x**2/(2*a*b)

assert sp.simplify(L(F) - ((z-b*y)**2-a*y**2)) == 0
assert sp.simplify(L(G) - y**2*(y+1)) == 0
assert sp.simplify(L(x*z) - (a*z**2-x**2+x*y+x*y**2)) == 0

Y,Y1,Y2,Y3 = sp.symbols("Y Y1 Y2 Y3")
jerk = Y3 + b*Y2 + (a-1)*Y1 + a*b*Y - 2*Y*Y1
reduced = sp.expand(jerk.subs({Y2:-a*Y, Y3:-a*Y1}))
assert sp.simplify(reduced + Y1*(2*Y+1)) == 0

print("VERIFY_OK")
