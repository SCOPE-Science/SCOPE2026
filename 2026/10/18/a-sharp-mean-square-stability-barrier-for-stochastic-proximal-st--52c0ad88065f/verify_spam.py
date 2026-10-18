"""Exact symbolic and rational verification for the two-client SPAM stability theorem.
Requires Python 3 and SymPy; no external files or network.
"""
import sympy as S

t = S.symbols('t', positive=True)
L = S.symbols('L')
q=S.Rational(1,2)
I=S.eye(3)
def step_matrix(a,T=t):
    T=S.sympify(T); a=S.sympify(a)
    z=1+T*a
    return S.Matrix([[1/z,T*q*a/z,-T*q/z],[1,0,0],[a,-q*a,q]])
M0,M2=step_matrix(0),step_matrix(2)
coords=[(i,j) for i in range(3) for j in range(i,3)]
def sym_to_vec(X): return S.Matrix([X[i,j] for i,j in coords])
def lift(M):
    C=S.zeros(6)
    for col,(i,j) in enumerate(coords):
        E=S.zeros(3);E[i,j]=E[j,i]=1
        C[:,col]=sym_to_vec(M*E*M.T)
    return C
C=S.simplify((lift(M0)+lift(M2))/2)
f=3*t**5+19*t**4+5*t**3-54*t**2-54*t-12
assert S.factor((S.eye(6)-C).det()+t*f/(16*(2*t+1)**3))==0
assert S.sign(f.subs(t,S.Rational(1797,1000)))==-1
assert S.sign(f.subs(t,S.Rational(1798,1000)))==1
# Descartes: f has exactly one positive real root (counting multiplicity).
assert [S.sign(c) for c in S.Poly(f,t).all_coeffs()]==[1,1,1,-1,-1,-1]
# Exact Lyapunov witness: P - E(M^T P M) = I at t=1/2.
P=S.Matrix([[14776,-1960,-1227],[-1960,4005,-1193],[-1227,-1193,3235]])/1619
op=lambda X:S.simplify((M0.T*X*M0+M2.T*X*M2)/2)
assert S.simplify(P-op(P).subs(t,S.Rational(1,2)))==S.eye(3)
assert all(P[:k,:k].det()>0 for k in [1,2,3])
# From z0=(1,1,0), two independent samples give a strictly PD covariance.
z=S.Matrix([1,1,0]);Q=z*z.T
for j in range(2):
    Q=S.simplify((M0*Q*M0.T+M2*Q*M2.T)/2)
assert S.factor(Q.det()-t**4*(10*t**2+14*t+7)/(128*(2*t+1)**4))==0
# Observability: after two steps every nonzero state influences squared x.
O=S.diag(1,0,0)
for j in range(2):O=op(O)
assert S.factor(O.det()-9*t**6*(2*t+3)**2*(2*t**2+2*t+1)/(1024*(2*t+1)**6))==0
# At t=2 signed first moment contracts, but the second-moment operator is unstable.
B=S.simplify((M0+M2)/2)
assert S.factor(B.subs(t,2).charpoly(L).as_expr()-(2*L-1)*(5*L**2-3*L+2)/10)==0
assert S.factor(C.subs(t,2).charpoly(L).as_expr()-L*(1000*L**5-1070*L**4-119*L**3+225*L**2-168*L+28)/1000)==0
assert S.factor((S.eye(6)-C.subs(t,2)).det())==-S.Rational(13,125)
# Direct re-evaluation of the full proximal subproblem after the gradient estimator.
for T in [S.Rational(1,10),S.Rational(1,2),S.Integer(1),S.Integer(2),S.Integer(5)]:
    for a in [0,2]:
        R=step_matrix(a,T)
        for x,xold,gold in [(1,1,0),(2,3,1),(-2,1,S.Rational(7,5)),(0,-1,4)]:
            x,xold,gold=map(S.Rational,(x,xold,gold))
            z=S.Matrix([x,xold,gold])
            g=a*x+q*(gold-a*xold)
            xnew=(x+T*(a*x-g))/(1+T*a)
            assert R*z==S.Matrix([xnew,x,g])
# Independent enumeration of both clients at two steps versus exact covariance evolution.
for T in [S.Rational(1,3),S.Rational(2),S.Rational(5,2)]:
    Q0=z*z.T
    exact=S.zeros(3)
    for a in [0,2]:
        for b in [0,2]:
            w=step_matrix(b,T)*step_matrix(a,T)*z
            exact+=w*w.T/4
    proc=Q0
    for j in range(2):
        proc=(step_matrix(0,T)*proc*step_matrix(0,T).T+step_matrix(2,T)*proc*step_matrix(2,T).T)/2
    assert S.simplify(exact-proc)==S.zeros(3)
print('PASS: exact determinant, one positive threshold, Lyapunov certificate, two-step covariance/observability, first moment and 40 direct updates.')
print('threshold',S.nroots(f)[-1])
