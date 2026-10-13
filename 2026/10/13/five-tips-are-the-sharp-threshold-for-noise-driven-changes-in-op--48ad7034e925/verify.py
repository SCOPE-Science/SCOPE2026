"""Exact symbolic checks for a five-tip Brownian-phylogeny subset-switch theorem.

Run with Python 3 and SymPy: python verify.py
"""
from itertools import combinations
import sympy as S

x=S.symbols('x', nonnegative=True)
K=S.Matrix([
    [55,25,0,0,35],
    [25,55,0,0,25],
    [0,0,55,50,0],
    [0,0,50,55,0],
    [35,25,0,0,55],
])

def info(indices):
    Q=K.extract(indices,indices)+x*S.eye(len(indices))
    return S.factor((S.ones(1,len(indices))*Q.inv()*S.ones(len(indices),1))[0])

infos={omit: info([j for j in range(5) if j!=omit]) for omit in range(5)}
L=S.factor(2*(2*x**2+205*x+4600)/((x+55)*(x**2+145*x+3700)))
R=S.factor(2/(x+105)+2/(x+80))
D=S.factor(2/(x+105)+2/(x+90))
for omit,expected in [(0,R),(1,D),(2,L),(3,L),(4,R)]:
    assert S.simplify(infos[omit]-expected)==0, omit
assert S.simplify((L-R)+10*(2*x**3+205*x**2-1225*x-198500)/((x+55)*(x+80)*(x+105)*(x**2+145*x+3700)))==0
assert S.simplify((R-D)-20/((x+80)*(x+90)))==0
p=2*x**3+205*x**2-1225*x-198500
assert p.subs(x,29)<0<p.subs(x,30)
assert len([z for z in S.nroots(p) if abs(S.im(z))<S.Rational(1,10**9) and S.re(z)>0])==1
for v in [0,1,10,29,30,100,1000]:
    values={omit: S.factor(expr.subs(x,v)) for omit,expr in infos.items()}
    assert all(value>0 for value in values.values())
    assert values[1]<values[0]==values[4]
    assert values[2]==values[3]
    if v<=29: assert values[2]>values[0]
    if v>=30: assert values[0]>values[2]

# A three-tip root singleton plus a non-root cherry: all BLUE coefficients
# are positive for any 0 <= a <= b < D. Formulae are verified symbolically.
D_,a,b=S.symbols('D a b',positive=True)
T=S.Matrix([[D_,a,a],[a,D_,b],[a,b,D_]])
w=T.inv()*S.ones(3,1)
assert S.simplify(w[0]-(D_+b-2*a)/(D_*(D_+b)-2*a*a))==0
assert S.simplify(w[1]-(D_-a)/(D_*(D_+b)-2*a*a))==0
assert S.simplify(w[2]-w[1])==0

print('VERIFY_OK five_tip_subsets=5 exact_rational_noise_checks=35 fixed_four_tip_weight_identity=3 cubic_positive_root_interval=(29,30)')
