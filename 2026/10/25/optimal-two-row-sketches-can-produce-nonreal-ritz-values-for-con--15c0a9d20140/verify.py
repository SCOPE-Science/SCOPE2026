"""Reproduce exact two-step sketched Rayleigh--Ritz spectral calculations.

Uses SymPy symbolic and rational arithmetic; finite samples complement proof.
Run: python verify.py
"""
from itertools import combinations
from fractions import Fraction
from random import Random
import sympy as sp

p,h,t,d=sp.symbols('p h t d',positive=True,real=True)
c=1/sp.sqrt(1+p**2)
U=sp.Matrix([[c,0,-p*c],[0,1,0],[p*c,0,c]])
V=U[:,:2]
H=sp.Matrix([[d,h,0],[h,d,t],[0,t,d]])
A=U*H*U.T
S=sp.Matrix([[1,0,0],[0,1,0]])
M=(S*V).inv()*(S*A*V)
RR=V.T*A*V
assert sp.simplify(U.T*U-sp.eye(3))==sp.zeros(3)
assert sp.simplify(U.T*A*U-H)==sp.zeros(3)
assert sp.simplify(M-sp.Matrix([[d,h-p*t],[h,d]]))==sp.zeros(2)
assert sp.simplify(RR-sp.Matrix([[d,h],[h,d]]))==sp.zeros(2)
assert sp.factor(M.charpoly().as_expr())==sp.factor((sp.Symbol('lambda')-d)**2-h*(h-p*t))
assert sp.simplify(A*V[:,0]-d*V[:,0]-h*V[:,1])==sp.zeros(3,1)
assert sp.simplify((S*V).T*(S*V)-sp.diag(1/(1+p*p),1))==sp.zeros(2)

# Rational exact instance has rational orthogonal change of basis and entries.
pv,hv,tv,dv=sp.Rational(3,4),sp.Rational(3,8),sp.Integer(1),sp.Integer(3)
subs={p:pv,h:hv,t:tv,d:dv}
Au=sp.simplify(A.subs(subs)); Vu=sp.simplify(V.subs(subs))
Mu=sp.simplify(M.subs(subs))
assert Mu==sp.Matrix([[3,-sp.Rational(3,8)],[sp.Rational(3,8),3]])
assert Mu.eigenvals()=={3+sp.Rational(3,8)*sp.I:1,3-sp.Rational(3,8)*sp.I:1}
assert Au==Au.T
assert all(ev.is_positive for ev in Au.eigenvals())
# Exhaustive three possible two-row coordinate samplers: E-optimal set is (0,1).
rowmat=Vu
sigmins={}
for I in combinations(range(3),2):
    Ri=rowmat[list(I),:]
    sigmins[I]=min(sp.sqrt(z) for z in (Ri.T*Ri).eigenvals())
assert sigmins[(0,1)]==sp.Rational(4,5)
assert sigmins[(1,2)]==sp.Rational(3,5)
assert sigmins[(0,2)]==0
# DEIM picks row 0 from q1, row 1 from the unchanged q2.
assert abs(Vu[0,0])>abs(Vu[2,0])
assert Vu[0,1]==0 and Vu[1,1]==1
# Q-DEIM (QR pivoting) initially picks row 1 of length 1, then row 0 over row 2.
assert (Vu[1,:].norm())>(Vu[0,:].norm())>(Vu[2,:].norm())
# Cases: the threshold is h=pt and the imaginary part is maximized at h=pt/2.
assert sp.factor((h*(p*t-h)).subs(h,p*t/2))==p*p*t*t/4
assert sp.simplify((h*(p*t-h)-p*p*t*t/4).subs(h,p*t/2))==0

rng=Random(17329)
for _ in range(100):
    P=sp.Rational(rng.randint(1,99),100)
    T=sp.Rational(rng.randint(1,20),5)
    r=sp.Rational(rng.randint(1,19),10)
    HH=P*T*r
    # choose d bigger than sqrt(h^2+t^2) without decimals
    D=HH+T+1
    mv=M.subs({p:P,h:HH,t:T,d:D})
    discr=sp.factor((mv.trace())**2-4*mv.det())
    assert sp.sign(discr)==sp.sign(HH-P*T)
    assert HH>0 and D*D>HH*HH+T*T
    assert sp.simplify((mv-sp.eye(2)*D)**2-sp.eye(2)*(HH*(HH-P*T)))==sp.zeros(2)
print('PASS: 11 symbolic/rational certificates plus 100 reproducible phase checks')
# Sharp imaginary pollution envelope at fixed SPD spectral half-width
k=sp.symbols('k',real=True, positive=True)
g=k*(p-k)/(1+k*k)
kstar=p/(1+sp.sqrt(1+p*p))
gstar=(sp.sqrt(1+p*p)-1)/2
assert sp.simplify(g.subs(k,kstar)-gstar)==0
assert sp.factor(sp.diff(g,k)*(1+k*k)**2)==p-2*k-p*k*k
# Algebraic nonnegative gap for every k: completion of a square using kstar.
assert sp.simplify((gstar-g)*(1+k*k) - (1+gstar)*(k-kstar)**2)==0
print('PASS: sharp fixed-spectral-width imaginary envelope certificate')
# Rational SPD witness with exactly condition number 2, not merely bounded.
ww={p:sp.Rational(3,4),h:sp.Rational(5,13),t:sp.Rational(12,13),d:sp.Integer(3)}
Aww=sp.simplify(A.subs(ww)); Mww=sp.simplify(M.subs(ww))
assert Aww==sp.Matrix([[3,-sp.Rational(16,65),0],[-sp.Rational(16,65),3,sp.Rational(63,65)],[0,sp.Rational(63,65),3]])
assert set(Aww.eigenvals())=={sp.Integer(2),sp.Integer(3),sp.Integer(4)}
assert Mww==sp.Matrix([[3,-sp.Rational(4,13)],[sp.Rational(5,13),3]])
assert set(Mww.eigenvals())=={3+2*sp.sqrt(5)*sp.I/13,3-2*sp.sqrt(5)*sp.I/13}
assert sp.simplify(2*sp.sqrt(5)/13)>0
print('PASS: rational 3-by-3 SPD witness with spectrum {2,3,4} and nonreal optimized sketch')
