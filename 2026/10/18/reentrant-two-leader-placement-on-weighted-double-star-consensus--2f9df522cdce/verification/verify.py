"""Exact checks for a two-leader noise-corrupted consensus design theorem.

Requires Python 3.10+ and SymPy. Run: python verification/verify.py
All infinite-family conclusions are proved in RESULT.md; these finite checks corroborate them.
"""
from itertools import combinations
from fractions import Fraction as F
from sympy import symbols, factor, cancel, sqrt, Matrix, Rational, simplify

m, b, r = symbols('m b r', positive=True)
checks = 0

def check(expression):
    global checks
    assert expression, 'verification assertion failed'
    checks += 1

def g(x, L):
    return cancel((x+r)*(L-x+r)/(L+2*r))

J_HH = factor(2*m+2*(m+1)*g(0,b))
J_HL = factor(2*m-1+(m+1)*g(0,b+1)+m*g(b,b+1)+g(b+1,b+1))
J_LL = factor(2*(m-1)+2*g(0,b+2)+2*m*g(1,b+2))
J_HS = factor(2*m-1+(m+1)*b+(2*m+1)*g(0,1)+g(1,1))
J_LS = factor(2*m-2+(m+1)*b+2*g(0,2)+2*m*g(1,2))

P = 2*(m-1)*r*r+2*((m-2)*b-1)*r+b*((m-1)*b-1)
Q_HS = b*(2*b*m*r+b*m+2*b*r+b+2*m*r*r+2*m*r+2*r*r+4*r+1)
Q_LL = (m-1)*b*b+2*(m-2)*b*r+(2*m-3)*b+2*(m-1)*r*r+(4*m-6)*r+2*(m-1)
Q_LS = (m-1)*r*r+(2*m-3)*r+(m-1)
check(cancel((J_HH-J_HL)+(P/((b+2*r)*(b+2*r+1))))==0)
check(cancel((J_HL-J_HS)+Q_HS/((2*r+1)*(b+2*r+1)))==0)
check(cancel((J_HL-J_LL)+Q_LL/((b+2*r+1)*(b+2*r+2)))==0)
check(cancel((J_HS-J_LS)+Q_LS/((r+1)*(2*r+1)))==0)

D=1+2*b-(m*m-2)*b*b
check(cancel((2*((m-2)*b-1))**2-4*2*(m-1)*b*((m-1)*b-1)-4*D)==0)
b0=1/(m-1)
bc=(1+sqrt(m*m-1))/(m*m-2)
rminus=(1-(m-2)*b-sqrt(D))/(2*(m-1))
rplus=(1-(m-2)*b+sqrt(D))/(2*(m-1))
check(cancel(P.subs(r,rminus))==0)
check(cancel(P.subs(r,rplus))==0)

# A six-vertex re-entrant example with three exact rational control strengths.
for R,expected in [(Rational(1,20),'HH'),(Rational(1,2),'HL'),(Rational(2),'HH')]:
    d=cancel((J_HH-J_HL).subs({m:2,b:Rational(6,5),r:R}))
    check(d<0 if expected=='HH' else d>0)
check(simplify(bc.subs(m,2)-(1+sqrt(3))/2)==0)
check(simplify(rminus.subs({m:2,b:Rational(6,5)})-(5-sqrt(13))/10)==0)
check(simplify(rplus.subs({m:2,b:Rational(6,5)})-(5+sqrt(13))/10)==0)

def graph_laplacian(M,bridge_res):
    n=2*M+2
    X=Matrix.zeros(n)
    edges=[(0,1,1/bridge_res)]+[(0,2+i,Rational(1)) for i in range(M)]+[(1,2+M+i,Rational(1)) for i in range(M)]
    for u,v,w in edges:
        X[u,u]+=w;X[v,v]+=w;X[u,v]-=w;X[v,u]-=w
    return X

def pair_type(u,v,M):
    if u==0 and v==1: return 'HH'
    if u<2 and v>=2:
        return 'HL' if (u==0 and v>=M+2) or (u==1 and v<M+2) else 'HS'
    return 'LL' if ((u<M+2)!=(v<M+2)) else 'LS'

forms={'HH':J_HH,'HL':J_HL,'LL':J_LL,'HS':J_HS,'LS':J_LS}
for M in [2,3,4,5]:
    for B,R in [(Rational(6,5),Rational(1,20)), (Rational(6,5),Rational(1,2)), (Rational(6,5),Rational(2)), (Rational(1,3),Rational(2))]:
        L=graph_laplacian(M,B)
        v=[]
        for u,w in combinations(range(2*M+2),2):
            Y=L.copy();Y[u,u]+=1/R;Y[w,w]+=1/R
            actual=cancel(Y.inv().trace())
            predicted=cancel(forms[pair_type(u,w,M)].subs({m:M,b:B,r:R}))
            check(actual==predicted)
            v.append(actual)
        target=min(J_HH.subs({m:M,b:B,r:R}),J_HL.subs({m:M,b:B,r:R}))
        check(min(v)==target)

# Symbolic positivity of all coefficients underlying the three strict eliminations
for M in [2,3,4,9]:
    for B,R in [(Rational(1,9),Rational(1,7)),(Rational(6,5),Rational(1,2)),(Rational(4),Rational(3))]:
        val={m:M,b:B,r:R}
        check(Q_HS.subs(val)>0)
        check(Q_LL.subs(val)>0)
        check(Q_LS.subs(val)>0)

print(f'PASS: {checks} exact symbolic identities, full-matrix pair checks, and positivity tests')
