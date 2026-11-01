"""Exact symbolic checks for sign fluctuations of a paired tent map.

Run with: python verify_paired.py (requires SymPy).
The main theorem also uses finite-state Markov-chain limit theory.
"""
import sympy as sp

rt = sp.sqrt(3)
q = (rt-1)/2
s = 2*(1+q)
edges = [-1, -sp.Rational(1,2), -q, 0, q, sp.Rational(1,2), 1]
lengths = [sp.simplify(edges[j+1]-edges[j]) for j in range(6)]
image_cells = [tuple(range(4)), (3,), tuple(range(3)), (3,4,5), (2,), (2,3,4,5)]
P = sp.Matrix([[sp.simplify(lengths[j]/(s*lengths[i])) if j in image_cells[i] else 0
                for j in range(6)] for i in range(6)])
pi = sp.Matrix([[sp.simplify(lengths[j]*(rt if j in (2,3) else 1)/(2*(3-rt)))
                 for j in range(6)]])
f = sp.Matrix([-1,-1,-1,1,1,1])

def eq(a,b):
    assert sp.simplify(a-b)==0, (a,b)

assert all(x==1 for x in P*sp.ones(6,1))
assert all(sp.simplify(v)==0 for v in (pi*P-pi))
assert all(sp.simplify(x)>0 for x in pi)
assert sp.simplify(sum(pi))==1
assert sp.simplify((pi*f)[0])==0
assert all(x>0 for x in list(P**5))  # finite-state primitivity
J = sp.Matrix([[0,0,1],[0,1,0],[1,0,0]])
R = sp.simplify(P[:3,:3]-P[:3,3:]*J)
t = sp.Symbol('t')
qchar = sp.factor(R.charpoly(t).as_expr(), extension=rt)
eq(qchar,t*(t*t-2*q*t+2*q*q))
C = [sp.simplify((pi*sp.diag(*f)*P**n*f)[0]) for n in range(11)]
for n,c in enumerate(C):
    # Closed form free from trigonometric simplification.
    z=(1+sp.I)**n
    formula=sp.expand_complex(q**n*(sp.re(z)+sp.im(z)/rt))
    eq(c,formula)
    if n>=2: eq(c,2*q*C[n-1]-2*q*q*C[n-2])
z = sp.Symbol('z')
G = sp.factor((2*pi[:,:3]*(sp.eye(3)-z*R).inv()*sp.ones(3,1))[0],extension=rt)
closed = (1+(1/rt-2*q)*z)/(1-2*q*z+2*q*q*z*z)
eq(G,closed)
eq(G.subs(z,1),1+1/rt)
eq(2*G.subs(z,1)-1,1+2/rt)
eq(-2*sp.diff(G,z).subs(z,1),-1/rt)
eq(C[2],2/rt-1)
assert sp.simplify(C[2]-C[1]**2)!=0
v_true=sp.simplify(2*G.subs(z,1)-1)
v_surrogate=sp.simplify((1+C[1])/(1-C[1]))
eq(v_surrogate,2+rt)
eq(v_surrogate/v_true,rt)
print('PASS: primitive Markov chain, invariant weights, signed spectrum,')
print('      covariance recurrence and explicit coefficients (0..10),')
print('      correlation generating function, CLT variance, finite-time offset.')
print('Two-state Markov variance ratio =',sp.simplify(v_surrogate/v_true))
print('C_1 =',C[1],'; C_2 =',C[2],'; V =',sp.simplify(2*G.subs(z,1)-1))
