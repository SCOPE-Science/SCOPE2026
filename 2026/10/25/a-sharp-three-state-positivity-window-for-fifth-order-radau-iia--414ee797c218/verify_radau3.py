"""Exact checks for the three-state positivity phase of fifth-order Radau IIA.

Run: python verify_radau3.py
Requires: sympy >= 1.12.  Every decisive identity uses rational arithmetic.
"""
from sympy import Matrix, eye, Rational, Symbol, factor, diff, nroots, simplify

h = Symbol('h', nonnegative=True)
z = Symbol('z')
R = (60 + 24*z + 3*z**2)/(60 - 36*z + 9*z**2 - z**3)
D = h**3 + 9*h**2 + 36*h + 60
p = h**4 - 16*h**3 - 48*h**2 + 240*h + 1200
q = h**4 + 12*h**3 + 198*h**2 + 960*h + 1800
rminus = R.subs(z, -h)
assert simplify(rminus - 3*(h**2-8*h+20)/D) == 0
assert simplify(diff(R,z).subs(z,-h) - 3*p/D**2) == 0
assert simplify(1-rminus-h*diff(R,z).subs(z,-h)-h**2*q/D**2) == 0
assert [int(p.subs(h,x)) for x in (4,5,17,18)] == [624,-175,-3679,1632]
# Two changes of sign and Descartes' rule imply exactly two positive roots.
assert len([i for i in nroots(p, maxsteps=100) if abs(float(i.as_real_imag()[1])) < 1e-12 and float(i.as_real_imag()[0]) > 0]) == 2

Q = Matrix([[-1,1,0],[0,-1,1],[0,0,0]])
def step(G,t):
    A=60*eye(G.rows)+24*t*G+3*t*t*(G**2)
    B=60*eye(G.rows)-36*t*G+9*t*t*(G**2)-t**3*(G**3)
    return A*B.inv()
T = step(Q,h)
want=Matrix([[rminus,3*h*p/D**2,h**2*q/D**2],
             [0,rminus,h*(h**2+6*h+60)/D],
             [0,0,1]])
assert all(simplify((T-want)[i,j]) == 0 for i in range(3) for j in range(3))
T5=step(Q,Rational(5))
assert T5[0,1] == Rational(-105,13924)
assert all(sum(T5[i,j] for j in range(3)) == 1 for i in range(3))

# An explicitly irreducible, reversible birth-death perturbation.
eps=Rational(1,1000)
Qr=Matrix([[-1,1,0],[eps,-1-eps,1],[0,eps,-eps]])
pi=Matrix([[eps**2,eps,1]])/(1+eps+eps**2)
assert pi*Qr == Matrix([[0,0,0]])
assert pi[0,0]*Qr[0,1] == pi[0,1]*Qr[1,0]
assert pi[0,1]*Qr[1,2] == pi[0,2]*Qr[2,1]
Tr=step(Qr,Rational(5))
assert Tr[0,1] == Rational(-4448823545303000,676819275720209897)
assert all(sum(Tr[i,j] for j in range(3)) == 1 for i in range(3))

# Every two-state generator satisfies Q^2 = -(a+b)Q.
a,b=Symbol('a',positive=True),Symbol('b',positive=True)
Q2=Matrix([[-a,a],[b,-b]])
assert all(simplify(v)==0 for v in Q2**2+(a+b)*Q2)
x=Symbol('x',positive=True)
assert factor(1-R.subs(z,-x)) == x*(x**2+6*x+60)/(x**3+9*x**2+36*x+60)
assert simplify(factor(R.subs(z,-x)) - 3*((x-4)**2+4)/(x**3+9*x**2+36*x+60)) == 0
print('VERIFY_OK: exact Radau rational identities, all three-state entries, two positive quartic roots,')
print('two-state generator reduction, irreducible reversible exact negative witness, and row-stochasticity')
print('roots approximately:',*[float(simplify(t.as_real_imag()[0])) for t in nroots(p) if abs(float(t.as_real_imag()[1])) < 1e-12 and float(t.as_real_imag()[0]) > 0])
