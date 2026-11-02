"""Exact independent checks for a directed three-state generator splitting theorem.

Requires Python 3.10+ and SymPy 1.12+.
Run: python verify.py
"""
import sympy as sp
from fractions import Fraction

q = sp.symbols('q', positive=True)

def edge(i, j, survival):
    M = sp.eye(3)
    M[i, i] = survival
    M[i, j] = 1-survival
    return M

def simp_vector(A):
    return [sp.factor(z) for z in A]

# Symbolic exact steady-state identities, independent of numerical sampling.
L = edge(0, 1, q**2) * edge(1, 2, q**4) * edge(2, 0, q**4)
S = (edge(0, 1, q) * edge(1, 2, q**2) * edge(2, 0, q**4)
     * edge(1, 2, q**2) * edge(0, 1, q))
pL = sp.Matrix([[1+q**2,q**4,q**4]])/(1+q**2+2*q**4)
pS = sp.Matrix([[q/(1+q**2),
    (q**4-q**3+q**2-q+1)/(1+q**2)**2,
    q**2/(1+q**2)**2]])
pi = sp.Matrix([[sp.Rational(1,2), sp.Rational(1,4), sp.Rational(1,4)]])
assert simp_vector(pL*L-pL) == [0]*3
assert simp_vector(pS*S-pS) == [0]*3
assert sp.simplify(sum(pL)-1)==0
assert sp.simplify(sum(pS)-1)==0


dL = (1-q**2)*(1+2*q**2)/(2*(1+q**2+2*q**4))
dS = (1-q)**2*(3*q**2+2*q+3)/(4*(1+q**2)**2)
assert sp.factor(pL[0]-sp.Rational(1,2)-dL) == 0
assert sp.factor(pS[1]-sp.Rational(1,4)-dS) == 0
assert sp.factor(pS[0]-sp.Rational(1,2)+(q-1)**2/(2*(q**2+1))) == 0
assert sp.factor(pS[2]-sp.Rational(1,4)+(q-1)**2*(q+1)**2/(4*(q**2+1)**2)) == 0
assert sp.factor(pL[1]-sp.Rational(1,4)+dL/2) == 0
assert sp.factor(pL[2]-sp.Rational(1,4)+dL/2) == 0

P = 10*q**7+2*q**6+15*q**5+3*q**4+12*q**3+4*q**2+3*q-1
assert sp.factor(dS-dL-(q-1)*P/(4*(q*q+1)**2*(1+q*q+2*q**4))) == 0
assert sp.Poly(sp.diff(P,q),q).all_coeffs()[-1] == 3
assert all(c>0 for c in sp.Poly(sp.diff(P,q),q).all_coeffs())
assert P.subs(q,0)==-1 and P.subs(q,1)>0
assert sp.limit(dL/(-2*sp.log(q)),q,1,dir='-') == sp.Rational(3,8)
assert sp.limit(dS/(-2*sp.log(q))**2,q,1,dir='-') == sp.Rational(1,8)
assert sp.limit(dL,q,0) == sp.Rational(1,2)
assert sp.limit(dS,q,0) == sp.Rational(3,4)

# Recompute invariant distributions via the matrix-tree cofactor formula,
# rather than relying only on the candidate expressions above.
def cof_stationary(M):
    R=sp.eye(3)-M
    weights=[sp.factor(R.minor_submatrix(i,i).det()) for i in range(3)]
    den=sp.factor(sum(weights))
    return sp.Matrix([[sp.factor(w/den) for w in weights]])
for M,p in [(L,pL),(S,pS)]:
    obtained=cof_stationary(M)
    assert simp_vector(obtained-p)==[0]*3

# General-rate exact Lie formula over a separate symbolic alphabet.
u,v,w=sp.symbols('u v w', positive=True)
Lg = edge(0,1,u)*edge(1,2,v)*edge(2,0,w)
wg=sp.Matrix([[1/(1-u),v/(1-v),w/(1-w)]])
assert simp_vector(wg*Lg-wg)==[0]*3

# 300 exact-rational test cases, including invariant relations, positive
# row-stochastic factors and sign of the crossover inequality.
count=0
for numer in range(1,61):
    qq=sp.Rational(numer,61)
    for M,dist in [(L,pL),(S,pS)]:
        X=M.subs(q,qq)
        D=dist.subs(q,qq)
        assert all(x>=0 for x in X)
        assert all(sum(X[i,j] for j in range(3))==1 for i in range(3))
        assert all(x>0 for x in D)
        assert sum(D)==1
        assert D*X==D
        count+=1
    # compute total variation from definition without sign assumptions
    for D,formula in [(pL,dL),(pS,dS)]:
        actual=sum(abs(D[0,i].subs(q,qq)-pi[0,i]) for i in range(3))/2
        assert actual==formula.subs(q,qq)
        count+=1
    assert sp.sign((dS-dL).subs(q,qq)) == sp.sign(((qq-1)*P.subs(q,qq)))
    count+=1
root=sp.nsolve(P,sp.Rational(1,5),tol=sp.Float('1e-50'),prec=70)
hstar=-2*sp.log(root)
assert sp.Rational(22049,100000)<root<sp.Rational(22050,100000)
print('PASS: exact symbolic identities, cofactor checks, polynomial factorization, boundaries,',count,'rational checks')
print('q* =',root.evalf(20))
print('h* =',hstar.evalf(20))
