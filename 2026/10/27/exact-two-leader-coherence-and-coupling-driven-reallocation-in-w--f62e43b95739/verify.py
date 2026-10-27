"""Exact rational verification of two-leader weighted complete-split formulas.

Run: python verify.py (requires SymPy). The symbolic theorem is independently
proved in RESULT.md; finite matrix checks here are corroboration only.
"""
from fractions import Fraction
import sympy as s

p, q, t = s.symbols('p q t', positive=True)
B = p*t + q
Cxx = (p-3)/B + (q-1)/p + (p+2*t+q)/(2*B)
Cxy = (p-2)/B + (q-2)/p + (p+t+q)/(p*t+p+q-1)
Cyy = (p-1)/B + (q-3)/p + (p+q)/(2*p)

checks = {
    'xx_minus_yy': s.factor(Cxx-Cyy + (p*p*t-p*p+p*q*t-6*p*t+4*p+q*q-4*q)/(2*p*B)),
    'xx_minus_xy_q3': s.factor((Cxx-Cxy).subs(q,3) - (2*p*p*t*t-(p**3+p*p-8*p)*t+p**3-3*p*p-10*p+12)/(2*p*(p*t+3)*(p*t+p+2))),
    'xx_minus_yy_q3': s.factor((Cxx-Cyy).subs(q,3) + (p-3)*(p*t-p+1)/(2*p*(p*t+3))),
    'yy_minus_xy_q3': s.factor((Cyy-Cxy).subs(q,3) - (p-1)*(p*p*t*t-p*p*t+p*t-p-6)/(2*p*(p*t+3)*(p*t+p+2))),
}
assert all(v==0 for v in checks.values()), checks

# Exact pairwise grounded inverse comparison for independent finite instances.
trial_count=0
for P in range(2,9):
    for Q in range(2,7):
        for T in (s.Rational(1,7), s.Rational(3,4), s.Integer(1), s.Rational(5,2)):
            n=P+Q
            L=s.zeros(n)
            for i in range(n):
                for j in range(i+1,n):
                    conductance = T if j<P else (1 if i<P else 0)
                    if not conductance:
                        continue
                    L[i,i] += conductance
                    L[j,j] += conductance
                    L[i,j] -= conductance
                    L[j,i] -= conductance
            for label,roots,C in [('XX',(0,1),Cxx),('XY',(0,P),Cxy),('YY',(P,P+1),Cyy)]:
                ff=[i for i in range(n) if i not in roots]
                direct=s.trace(L.extract(ff,ff).inv())
                candidate=C.subs({p:P,q:Q,t:T})
                assert s.cancel(direct-candidate)==0,(P,Q,T,label,direct,candidate)
                trial_count+=1

# Verify the exact phase regime for q=3 using rational probes;
# boundary reasoning is proved algebraically in RESULT.md.
for P in range(4,21):
    cut=s.Rational(P-1,P)
    f=2*P**2*t**2-(P**3+P**2-8*P)*t+(P**3-3*P**2-10*P+12)
    assert s.factor(f.subs(t,cut))<0
    assert s.factor((Cyy-Cxy).subs({p:P,q:3,t:cut}))<0
    assert s.factor((Cyy-Cxy).subs({p:P,q:3,t:0}))<0

assert s.factor((Cxx-Cyy).subs({p:3,q:3}))==0
assert s.factor((Cxx-Cxy).subs({p:2,q:3})-(t-1)/(2*(t+2)))==0
assert s.factor((Cxx-Cyy).subs({p:2,q:3})-(2*t-1)/(4*(2*t+3)))==0
assert s.factor((Cyy-Cxy).subs({p:2,q:3})-(2*t*t-t-4)/(4*(t+2)*(2*t+3)))==0

print('VERIFY_OK',len(checks),'symbolic comparison identities;',trial_count,
      'exact direct grounded inverse comparisons; 17 exact threshold checks')
