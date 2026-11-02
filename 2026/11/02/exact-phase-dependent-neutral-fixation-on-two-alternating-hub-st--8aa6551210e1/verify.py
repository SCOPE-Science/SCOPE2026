"""Finite exact checks of two-hub alternating-star neutral fixation theorem.

Run: python verify.py
Only Python standard library and SymPy are needed; SciPy/Numpy not required.
"""
from fractions import Fraction as F
from itertools import product
from math import isclose
import sympy as sp


def coefficients(n, tau):
    assert n >= 3 and tau >= 1
    x = (F(1, 1) - F(1, n*(n-1)))**tau
    y = F(n-2, n*(n-1))**tau
    A = (n-1)-x+(n*n-3*n+3)*y-(n-1)**2*x*y
    B = (n-1)**2-(n*n-3*n+3)*x-(n-1)*x*y+y
    C = (n-1)**2*(1-x*y)-x+y
    Z = A+B+(n-2)*C
    return (A/Z, B/Z, C/Z), (A,B,C,Z,x,y)


def matrix3(n, center):
    a = F(1,n); b = F(1,n*(n-1)); k=n-2
    if center == 0: return [[a,a,k*a],[b,1-b,0],[b,0,1-b]]
    return [[1-b,b,0],[a,a,k*a],[0,b,1-b]]


def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def mpow(A,t):
    n=len(A); R=[[F(int(i==j)) for j in range(n)] for i in range(n)]
    for _ in range(t): R=matmul(A,R)
    return R


def state_transition(n,center):
    """Independent full 2^n state-space Moran birth-death transition."""
    Q=[[F(0) for _ in range(1<<n)] for _ in range(1<<n)]
    for mask in range(1<<n):
        for donor in range(n):
            neighbours = [j for j in range(n) if j != donor and (donor == center or j == center)]
            for target in neighbours:
                prob=F(1,n*len(neighbours))
                child = (mask | (1<<target)) if (mask & (1<<donor)) else (mask & ~(1<<target))
                Q[mask][child]+=prob
        assert sum(Q[mask])==1
    return Q


def absorption_exact(n,tau):
    """Solve exact finite-state absorbing chain at complete-period boundaries."""
    QA=mpow(state_transition(n,0),tau)
    QB=mpow(state_transition(n,1),tau)
    # probability row distributions evolve QA then QB
    Q=matmul(QA,QB)
    trans=[i for i in range(1, (1<<n)-1)]
    H=sp.Matrix([[int(i==j)-sp.Rational(Q[i][j].numerator,Q[i][j].denominator) for j in trans] for i in trans]);
    v=sp.Matrix([sp.Rational(Q[i][-1].numerator,Q[i][-1].denominator) for i in trans]);
    ans=H.inv()*v
    return [F(int(ans[trans.index(1<<i)].p),int(ans[trans.index(1<<i)].q)) for i in range(n)]


def run():
    counts={'matrix_stationarity':0,'strict_order':0,'full_state_exact':0,'asymptotic_numeric':0}
    for n in range(3,11):
        for tau in range(1,7):
            p,(A,B,C,Z,x,y)=coefficients(n,tau)
            assert all(v>0 for v in (A,B,C,Z))
            assert p[0]+p[1]+(n-2)*p[2]==1
            assert p[0]<p[1]<p[2]
            assert B-A==(n-1)*(n-2)*(1-x)*(1-y)
            assert C-B==(n-1)*(n-2)*x*(1-y)
            T=matmul(mpow(matrix3(n,1),tau),mpow(matrix3(n,0),tau))
            row=[p[0],p[1],(n-2)*p[2]]
            assert [sum(row[i]*T[i][j] for i in range(3)) for j in range(3)]==row
            counts['matrix_stationarity']+=1
            counts['strict_order']+=1
    for n in (3,4,5):
        for tau in (1,2,3):
            if n==5 and tau==3:continue
            expected=absorption_exact(n,tau)
            p,_=coefficients(n,tau)
            assert expected==[p[0],p[1]]+[p[2]]*(n-2), (n,tau,expected,p)
            counts['full_state_exact']+=n
    for n in [80,200,500]:
        for theta in [0.1,0.5,1,4,15]:
            tau=int(n*n*theta)
            x=(1-1/(n*(n-1)))**tau
            y=((n-2)/(n*(n-1)))**tau
            A=(n-1)-x+(n*n-3*n+3)*y-(n-1)**2*x*y
            B=(n-1)**2-(n*n-3*n+3)*x-(n-1)*x*y+y
            C=(n-1)**2*(1-x*y)-x+y
            Z=A+B+(n-2)*C
            assert abs(n*B/Z-(1-__import__('math').exp(-theta))) < 0.07
            assert abs(n*n*A/Z-1) < 0.07
            assert abs(n*C/Z-1) < 0.07
            counts['asymptotic_numeric']+=1
    # τ=1 special formula, no calculation of stationary vector involved
    for n in range(3,101):
        D=n**4-4*n**3+6*n**2-2*n-2
        p,_=coefficients(n,1)
        assert p==(F((n-1)**2,D),F(n*n-n-1,D),F((n-1)*(n*n-n-1),D))
    print('PASS',counts,'tau_one_cases=98')

if __name__=='__main__':run()
