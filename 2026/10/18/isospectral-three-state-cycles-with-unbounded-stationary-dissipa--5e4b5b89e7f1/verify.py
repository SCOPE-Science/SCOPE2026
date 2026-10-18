"""Independent reproducibility checks for a finite-state nonequilibrium Markov example.

Run with Python 3 and SymPy: python verify.py.
This is a finite checker; the mathematical argument is in RESULT.md.
"""
import math
import sympy as S

x, a, b, c = S.symbols('x a b c', real=True)
z = S.Symbol('z')
G = S.Matrix([[-(a+c), a+x, c-x], [a-x, -(a+b), b+x], [c+x, b-x, -(b+c)]])
assert all(S.simplify(sum(G[i, j] for j in range(3))) == 0 for i in range(3))
assert all(S.simplify(sum(G[i, j] for i in range(3))) == 0 for j in range(3))
expected = z*(z*z+2*(a+b+c)*z+3*(a*b+a*c+b*c+x*x))
assert S.simplify(G.charpoly(z).as_expr()-expected) == 0

h=S.sqrt(x*x+S.Rational(2,3))
vals=[1+x/2+h/2,1+x/2-h/2,1-x]
assert S.simplify(sum(vals)-3)==0
assert S.simplify(vals[0]*vals[1]+vals[0]*vals[2]+vals[1]*vals[2]+x*x-S.Rational(17,6))==0
F=G.subs({a:vals[0], b:vals[1], c:vals[2]})
assert S.simplify(F.charpoly(z).as_expr()-z*(z*z+6*z+S.Rational(17,2)))==0
checks=6
for j in range(101):
    t=.5*j/101
    v1,v2,v3=[float(y.subs(x,t)) for y in vals]
    rates=[(v1+t,v1-t),(v2+t,v2-t),(v3+t,v3-t)]
    assert all(r>0 for p in rates for r in p)
    M=[[float(F[i,k].subs(x,t)) for k in range(3)] for i in range(3)]
    assert max(abs(sum(row)) for row in M)<1e-12
    assert max(abs(sum(M[i][k] for i in range(3))) for k in range(3))<1e-12
    assert abs(sum(-M[i][i] for i in range(3))/3-2)<1e-12
    assert max(-M[i][i] for i in range(3))<2.5+1e-12
    tr=sum(M[i][i] for i in range(3))
    sub=sum(M[i][i]*M[k][k]-M[i][k]*M[k][i] for i in range(3) for k in range(i+1,3))
    assert abs(tr+6)<1e-12 and abs(sub-8.5)<1e-12
    J=(rates[0][0]-rates[0][1])/3
    assert abs(J-2*t/3)<1e-12
    entropy=sum(J*math.log(p/q) for p,q in rates)
    assert entropy>=-1e-14
    checks+=8
for t in (0.4,0.45,0.49,0.499,0.4999):
    vv=[float(y.subs(x,t)) for y in vals]
    ep=(2*t/3)*sum(math.log((s+t)/(s-t)) for s in vv)
    assert math.isfinite(ep)
    checks+=1
print('PASS',checks,'independent algebraic and numerical assertions')
