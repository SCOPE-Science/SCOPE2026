import sympy as sp
from itertools import product

t = sp.symbols("t", positive=True, real=True)
vals = [sp.Integer(0), t, sp.Integer(1)]
rank = {sp.Integer(0): 0, t: 1, sp.Integer(1): 2}
EL=EU=EL2=EU2=ELU=sp.Integer(0)
for s in product(vals, repeat=3):
    L=min(s, key=lambda z: rank[z])
    U=max(s, key=lambda z: rank[z])
    EL += L; EU += U; EL2 += L**2; EU2 += U**2; ELU += L*U
EL,EU,EL2,EU2,ELU=[sp.simplify(z/27) for z in (EL,EU,EL2,EU2,ELU)]
assert EL == (7*t+1)/27
assert EU == (7*t+19)/27
assert EL2 == (7*t**2+1)/27
assert EU2 == (7*t**2+19)/27
assert ELU == (t**2+6*t+1)/27
cov=sp.factor(ELU-EL*EU)
vL=sp.factor(EL2-EL**2)
vU=sp.factor(EU2-EU**2)
assert sp.simplify(cov - (-2*(11*t**2-11*t-4)/729)) == 0
assert sp.simplify(vL - 2*(70*t**2-7*t+13)/729) == 0
assert sp.simplify(vU - 2*(70*t**2-133*t+76)/729) == 0
R=sp.factor(cov**2/(vL*vU))
expected=(11*t**2-11*t-4)**2/((70*t**2-133*t+76)*(70*t**2-7*t+13))
assert sp.simplify(R-expected)==0
D=sp.factor(sp.diff(R,t))
expectedD=81*(2*t-1)*(11*t**2-11*t-4)*(791*t**2-791*t+380)/((70*t**2-133*t+76)**2*(70*t**2-7*t+13)**2)
assert sp.simplify(D-expectedD)==0
assert sp.simplify(R.subs(t,sp.Rational(1,2))-sp.Rational(1,16))==0
print("VERIFY_OK")
