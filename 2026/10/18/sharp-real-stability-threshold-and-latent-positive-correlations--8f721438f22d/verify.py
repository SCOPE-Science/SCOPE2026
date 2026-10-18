"""Exact symbolic verification of a three-site stationary coalescing lattice.
Run: python verify.py. Requires sympy.
"""
import sympy as sp

r, x, y, z = sp.symbols('r x y z', positive=True)
u, v, w = sp.symbols('u v w', real=True)
N = 8
Q = sp.zeros(N)

def add_transition(state, dest, rate):
    if state != dest:
        Q[state, dest] += rate
        Q[state, state] -= rate

for state in range(N):
    add_transition(state, state | 1, r)
    for j in range(3):
        if state & (1 << j):
            nxt = state & ~(1 << j)
            if j < 2:
                nxt |= 1 << (j + 1)
            add_transition(state, nxt, sp.Integer(1))

numerators = [8, 2*r**3+6*r**2+8*r, 5*r**2+8*r,
              3*r**3+4*r**2, 8*r, 2*r**3+6*r**2,
              3*r**2, r**3]
p = sp.Matrix([sp.factor(a/(8*(1+r)**3)) for a in numerators])
assert sp.simplify(sum(p)-1) == 0
assert all(sp.factor(expr)==0 for expr in Q.T*p)
F = sp.expand(sum(p[state] * (x if state&1 else 1)
                          * (y if state&2 else 1)
                          * (z if state&4 else 1)
                  for state in range(8)))
assert sp.simplify(F.subs({x:1,y:1,z:1})-1)==0
common_discriminant=r**6*(r**2-16*r-16)/(256*(1+r)**10)
for a,b,rest in [(x,y,z),(x,z,y),(y,z,x)]:
    delta=sp.factor(sp.diff(F,a)*sp.diff(F,b)-F*sp.diff(F,a,b))
    polynomial=sp.Poly(delta,rest)
    assert polynomial.degree()==2
    assert sp.factor(polynomial.LC()/r**2).subs(r,1)>0
    assert sp.factor(sp.discriminant(polynomial.as_expr(),rest)-common_discriminant)==0

D13=sp.factor(sp.diff(F,x)*sp.diff(F,z)-F*sp.diff(F,x,z))
assert sp.factor(D13-r**2*(r**2*(y**2-y)+4*(r+1))/(16*(r+1)**5))==0
assert sp.factor(F.subs({x:1,z:1})-(r**2*y+r**2+2*r*y+2*r+2)/(2*(r+1)**2))==0
assert sp.factor(D13.subs({r:20,y:sp.Rational(1,2)})) < 0
assert sp.factor(D13.subs({r:20,y:1})) > 0
assert sp.factor(D13.subs({r:1,y:sp.Rational(1,2)})) > 0

# Check an independently obtained stationary law of a four-site chain
# at two rational parameter values, projected onto the first three sites.
for param in [sp.Rational(1),sp.Rational(3)]:
    S=16;G=sp.zeros(S)
    for state in range(S):
        def add(dest,rate):
            if dest!=state:
                G[state,dest]+=rate;G[state,state]-=rate
        add(state|1,param)
        for j in range(4):
            if (state>>j)&1:
                dest=state&~(1<<j)
                if j<3: dest|=1<<(j+1)
                add(dest,sp.Integer(1))
    A=G.T.copy();A[-1,:]=sp.ones(1,S)
    b=sp.zeros(S,1);b[-1]=1
    ans=A.LUsolve(b)
    for k in range(8):
        projected=sp.factor(ans[k]+ans[k+8])
        assert sp.simplify(projected-p[k].subs(r,param))==0

print('PASS: exact balance, normalization, three quadratic discriminants,')
print('      external-field correlation witness, four-site marginal check.')
