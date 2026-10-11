"""Exact algebraic consistency checks for the octagonal Wigner-area theorem.
Requires SymPy. Analytic proof of the global optimization is in RESULT.md.
"""
import sympy as S

s, a, b = S.symbols('s a b', real=True)
r = S.sqrt(2)
D = [-(a-b)/r, a, -(a+b)/r, b]
U = [(1,0), (r/2,r/2), (0,1), (-r/2,r/2),
     (-1,0), (-r/2,-r/2), (0,-1), (r/2,-r/2)]
lengths = [s+t for t in D] + [s-t for t in D]
E = [S.Matrix([S.expand(lengths[i]*z) for z in U[i]]) for i in range(8)]
P = [S.Matrix([0,0])]
for e in E:
    P.append(S.simplify(P[-1]+e))
assert all(S.simplify(z)==0 for z in P[-1]), 'closure'
P=P[:8]
W = [S.simplify((P[i]+P[i+4])/2) for i in range(4)]
Q = [S.simplify((P[i]-P[(i+4)%8])/2) for i in range(8)]
def det(x,y): return S.expand(x[0]*y[1]-x[1]*y[0])
def area(V):
    return S.simplify(sum(det(V[i],V[(i+1)%len(V)]) for i in range(len(V)))/2)
A, AW, AQ = map(area,[P,W,Q])
assert S.simplify(AW+(a*a+b*b)/4)==0, AW
assert S.simplify(AQ-2*(1+r)*s*s)==0, AQ
assert S.simplify(A-(2*(1+r)*s*s-(a*a+b*b)/2))==0, A
assert S.simplify(AQ-A+2*AW)==0, 'central symmetral area identity'
vertices = [(su*u,sv*v) for u,v in [(1,r-1),(r-1,1)]
            for su in [-1,1] for sv in [-1,1]]
for u0,v0 in vertices:
    assert S.simplify(u0*u0+v0*v0-(4-2*r))==0
    # Each signed vertex saturates one square and one diagonal constraint.
    assert abs(float(u0))<=1+1e-12 and abs(float(v0))<=1+1e-12
    assert float(S.Abs(u0)+S.Abs(v0))<=float(r)+1e-12
R = S.simplify(((4-2*r)/4)/(2*(1+r)-(4-2*r)/2))
assert S.simplify(R-(r-1)/6)==0, R
print('OCTAGON_WIGNER_EXACT_SYMBOLIC_CHECKS_OK')
