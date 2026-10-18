"""Exact checks for the three-oscillator heat-conductance optimization.
Requires Python 3 and SymPy. Run: python verify.py
"""
from fractions import Fraction
import sympy as s

b, g, m = s.symbols('b g m', positive=True)
B = b + 1
Acoef = b*b + 3*b + 1
D = 1 + g*g*(B**3*m*m-(2*b**3+8*b*b+7*b+1)*m+b**3+5*b*b+7*b+2) +g**4*Acoef*m
conductance = g*(1 + g*g*B*m)/(2*D)
mstar = 1+b/B**2
opt_conductance = g*B/(2*(B+g*g*Acoef))
assert s.factor(1/conductance - 1/opt_conductance - 2*g*B**3*(m-mstar)**2/(1+g*g*B*m)) == 0
assert s.factor(s.diff(conductance,m) + g**3*B**2*(m-mstar)*( (B**2*g*g*m)+(b*b*g*g+3*b*g*g+g*g+2*b+2)) /(2*D**2))==0
# Derive conductance without importing its proposed value, from independent
# 2-by-4 stationary cross-covariances in symmetric/antisymmetric normal modes.
A_minus=s.Matrix([[0,1],[-B,-g]])
A_plus=s.Matrix([[0,0,1,0],[0,0,0,1/m],[-B,2,-g,0],[1,-(b+2),0,0]])
Q=s.zeros(2,4);Q[1,2]=2*g # temperature difference fixed at 1
W=s.Matrix(2,4,lambda i,j:s.Symbol(f'W{i}{j}'))
E=A_minus*W+W*A_plus.T+Q
variables=list(W)
L=s.zeros(8);rhs=s.zeros(8,1)
for r,(i,j) in enumerate((i,j) for i in range(2) for j in range(4)):
    expr=E[i,j]
    rhs[r]=-expr.subs({v:0 for v in variables})
    for k,v in enumerate(variables):L[r,k]=expr.coeff(v)
assert s.factor(L.det(method='domain-ge')-4*D/m**2)==0
w=L.inv()*rhs
# W[1,2] = E[(p1-p3)(p1+p3)] = E[p1^2-p3^2]
derived=s.factor(g*(1-w[6])/2)
assert s.factor(derived-conductance)==0
assert s.factor(conductance.subs({b:1,g:1,m:s.Rational(5,4)})-s.Rational(1,7))==0
assert s.factor(conductance.subs({b:1,g:1,m:1})-s.Rational(3,22))==0
# Check the full, unreduced six-dimensional Lyapunov system at rational choices.
def full_flux(beta,gamma,mu,TL,TR):
    K=s.Matrix([[beta+1,-1,0],[-1,beta+2,-1],[0,-1,beta+1]])
    invM=s.diag(1,1/mu,1)
    F=s.zeros(6,6);F[:3,3:]=invM;F[3:,:3]=-K
    F[3:,3:]=-s.diag(gamma,0,gamma)*invM
    Q=s.zeros(6,6);Q[3,3]=2*gamma*TL;Q[5,5]=2*gamma*TR
    ids=[(i,j) for i in range(6) for j in range(i,6)]
    V=s.Matrix(6,6,lambda i,j:s.Symbol('v'+str(min(i,j))+'_'+str(max(i,j))))
    unknown=[V[i,j] for i,j in ids]
    R=F*V+V*F.T+Q
    mat=s.zeros(21);rr=s.zeros(21,1)
    zero={u:0 for u in unknown}
    for k,(i,j) in enumerate(ids):
        expr=R[i,j];rr[k]=-expr.subs(zero)
        for h,u in enumerate(unknown):mat[k,h]=expr.coeff(u)
    vec=mat.inv()*rr
    solution=dict(zip(unknown,vec))
    cov=V.subs(solution)
    assert cov==cov.T and F*cov+cov*F.T+Q==s.zeros(6)
    return s.factor(gamma*(TL-cov[3,3]))

cases=[(s.Rational(1,2),s.Rational(1,3),s.Rational(5,2)),
       (s.Rational(1),s.Rational(1),s.Rational(5,4)),
       (s.Rational(2),s.Rational(3,2),s.Rational(3,4)),
       (s.Rational(3,2),s.Rational(2),s.Rational(7,3)),
       (s.Rational(4),s.Rational(1,2),s.Rational(9,5)),
       (s.Rational(1,4),s.Rational(3),s.Rational(2,3)),
       (s.Rational(3),s.Rational(3),s.Rational(3,2)),
       (s.Rational(1,3),s.Rational(7,4),s.Rational(1,5))]
for beta,gamma,mu in cases:
    current=full_flux(beta,gamma,mu,s.Rational(7,3),s.Rational(2,3))
    expect=s.factor(s.Rational(5,3)*conductance.subs({b:beta,g:gamma,m:mu}))
    assert s.factor(current-expect)==0,(beta,gamma,mu,current,expect)
print('PASS: symbolic 8-equation cross-covariance elimination; determinant; exact conductance; quadratic resistance identity; derivative; 8 independent rational 21-equation full-Lyapunov solves; matched/optimal benchmark')
