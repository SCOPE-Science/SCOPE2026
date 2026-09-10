"""Replay: certify HF (1,3,5,3,1), H1 sextic factorization, Hess^2 constancy,
Ann_2 generator, and Jordan partitions of representative linear forms.
Run: python3 replay.py  -> prints VERIFY_OK with all certificates. Stdlib+sympy only."""
import sympy as sp
from sympy import Matrix
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from engine import Apolar
X,Y,Z,a,b,c = sp.symbols('X Y Z a b c')
F0 = X**4+X**3*Y+Y**3*Z+Z**4
A = Apolar(F0)
assert A.hf == [1,3,5,3,1], A.hf
assert sum(A.hf) == 13
# Ann_2: left nullspace of C_2 is span{xz}
ns = (A.C[2].T).nullspace()
assert len(ns) == 1
# H1 sextic + factorization
T1={k:A.T[(k,1)] for k in range(3)}; T2={k:A.T[(k,2)] for k in range(3)}
L1=a*T1[0]+b*T1[1]+c*T1[2]; L2=a*T2[0]+b*T2[1]+c*T2[2]
H1=sp.expand((L2*L1).det())
assert sp.Poly(H1,a,b,c).total_degree()==6
assert sp.expand(H1 + a*(2*a**3*c**2+2*a*b**4-16*a*b*c**3+b**5-8*b**2*c**3)/2)==0
fac=sp.factor_list(H1)
degs=sorted(sp.Poly(f[0],a,b,c).total_degree() for f in fac[1])
assert degs==[1,5], fac
# Hess^2 constant
G=A.R[2]*A.R[2].T
assert G.det()==15116544
# Jordan representatives
checks={(1,1,1):[5,3,3,1,1],(1,0,0):[5,3,1,1,1,1,1],(0,1,0):[4,4,2,2,1],
        (0,0,1):[5,2,2,1,1,1,1],(0,1,1):[5,3,2,2,1],(1,-1,1):[4,4,3,1,1]}
for t,want in checks.items():
    p,kd=A.jordan(t)
    assert p==want, (t,p,want)
    assert sum(p)==13
print("VERIFY_OK")
print("hf:",A.hf,"H1-degs:",degs,"Hess2:",G.det())
