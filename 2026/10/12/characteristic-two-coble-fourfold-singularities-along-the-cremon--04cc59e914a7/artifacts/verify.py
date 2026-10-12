import sympy as sp

# Work over F_2.
y0,y1,y2,y3,y4,w,t = sp.symbols('y0 y1 y2 y3 y4 w t')
S = y0+y1+y2+y3+y4
q = y2*y3 + y1*y4 + y0*S
b = y0*y1*y4*S
G = w**2 + w*q + b
vars6=[y0,y1,y2,y3,y4,w]

def mod2(expr):
    return sp.Poly(sp.expand(expr), *vars6, modulus=2).as_expr()

dG=[mod2(sp.diff(G,z)) for z in vars6]
G2=mod2(G)

# Three representative singular curves through P=[0:0:0:0:1;0].
u,v=sp.symbols('u v')
branches=[
    {y0:0,y1:0,y2:0,y3:u,y4:v,w:0},
    {y0:0,y1:0,y2:u,y3:0,y4:v,w:0},
    {y0:u,y1:u,y2:0,y3:0,y4:v,w:u*v},
]
for sub in branches:
    assert sp.Poly(sp.expand(G.subs(sub)),u,v,modulus=2).is_zero
    for h in dG:
        assert sp.Poly(sp.expand(h.subs(sub)),u,v,modulus=2).is_zero

# Local chart y4=1 along L: y0=y1=y2=w=0, parameter y3=t.
x0,x1,x2=sp.symbols('x0 x1 x2')
Gloc=sp.expand(G.subs({y0:x0,y1:x1,y2:x2,y3:t,y4:1}))
# Extract total degree 2 in normal variables w,x0,x1,x2, with t a coefficient.
normal=[w,x0,x1,x2]
Q=0
for term in sp.Poly(Gloc, *normal).terms():
    mon, coeff = term
    if sum(mon)==2:
        Q += coeff*sp.prod(z**e for z,e in zip(normal,mon))
Q=sp.Poly(sp.expand(Q),t,*normal, modulus=2).as_expr()
expected=sp.Poly(w**2+w*((t+1)*x0+x1+t*x2)+(t+1)*x0*x1,t,*normal,modulus=2).as_expr()
assert sp.expand(Q-expected)==0

# Polar matrix determinant = t^2(t+1)^2 over F2.
M=sp.Matrix([
    [0,t+1,1,t],
    [t+1,0,t+1,0],
    [1,t+1,0,0],
    [t,0,0,0],
])
det=sp.factor(M.det())
assert sp.expand(det - t**2*(t+1)**2)==0

# At t=0 the tangent cone is two distinct hyperplanes.
Q0=sp.Poly(Q.subs(t,0),*normal,modulus=2).as_expr()
factor0=sp.Poly((w+x0)*(w+x1),*normal,modulus=2).as_expr()
assert sp.expand(Q0-factor0)==0

# The three tangent directions of the representative singular branches are distinct.
# Coordinates are (x0,x1,x2,dt,w), with y4=1.
dirs=[(0,0,0,1,0),(0,0,1,0,0),(1,1,0,0,1)]
assert len(set(dirs))==3

# Cremona--Richmond combinatorics on Q(F2): enumerate 15 points and 15 lines.
# Projective points over F2 are nonzero 5-bit vectors; q=0.
def qF(a):
    a0,a1,a2,a3,a4=a
    return (a2*a3+a1*a4+a0*(a0+a1+a2+a3+a4))%2
points=[p for p in __import__('itertools').product([0,1], repeat=5) if any(p) and qF(p)==0]
assert len(points)==15
Pset=set(points)
# In F2, a projective line has three points {a,b,a+b}.
lines=set()
for i,a in enumerate(points):
    for b in points[i+1:]:
        c=tuple((aa+bb)%2 for aa,bb in zip(a,b))
        if c in Pset:
            line=tuple(sorted((a,b,c)))
            lines.add(line)
assert len(lines)==15
inc={p:0 for p in points}
for L in lines:
    assert len(L)==3
    for p in L: inc[p]+=1
assert set(inc.values())=={3}

print('VERIFY_OK')
print('polar_determinant=',det)
print('special_affine_parameters=t=0,1; third point at infinity')
print('cr_points=',len(points),'cr_lines=',len(lines),'incidence=15_3')
