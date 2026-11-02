"""Reproduce the six-season two-capacity constant-quota ordering identities.
Run: python verify6harvest.py (requires SymPy)."""
import sympy as sp
m,L,H,h=sp.symbols('m L H h',positive=True)

def B(k):
    return sp.Matrix([[k,m-1],[-h*k,m*k-h*(m-1)]])

def trace(d):
    M=sp.eye(2)
    for j in range(6):
        M=B(H if j in (0,d) else L)*M
    return sp.trace(M)
T={d:trace(d) for d in (1,2,3)}
pref=h**2*m*(H-L)**2*(m-1)**2
t=L*(m+1)-h*(m-1)
assert sp.factor(T[2]-T[1]-pref*(t*t-m*L*L))==0
assert sp.factor(T[3]-T[2]-pref*m*L*L)==0
assert sp.factor(B(L).det()-m*L*L)==0
assert sp.factor(T[1].subs(h,0)-(1+m**6)*H**2*L**4)==0
h0=L*(m+1-sp.sqrt(m))/(m-1)
F=lambda x:m*L*x/(L+(m-1)*x)-h
limit=m*L/(m-1)-h
assert sp.simplify(F(limit).subs(h,h0)+L/(m-1))==0
for d,lo,hi in [(1,sp.Rational(413372280,10**9),sp.Rational(413372282,10**9)),
                 (2,sp.Rational(424771624,10**9),sp.Rational(424771627,10**9)),
                 (3,sp.Rational(429903690,10**9),sp.Rational(429903692,10**9))]:
    q=sp.factor((T[d]-2*m**3*H**2*L**4).subs({m:4,L:1,H:4}))
    assert q.subs(h,lo)>0 and q.subs(h,hi)<0,(d,q)
    print('d=',d,'polynomial=',q,'bracket=',lo,hi)
print('All symbolic matrix identities, exact two-low-block bound, and rational root brackets passed.')
