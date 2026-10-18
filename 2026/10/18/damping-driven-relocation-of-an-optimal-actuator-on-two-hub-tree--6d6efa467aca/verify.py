"""Symbolic and exact-arithmetic cross-checks for the damped-tree actuator-location theorem.

Requires SymPy. Finite matrix tests corroborate, rather than prove, the all-order identities.
"""
import sympy as s

x, m = s.symbols('x m', positive=True)
a=x+1
C=x+3-1/a
H=x+m+1-m/a
D=C-2/H
Gc=1/a+1/(a*a*D)
Go=1/a+(1/H+1/(H*H*D))/a**2
Q=(m-2)*x*x+(m*m-4)*x-2
Den=(x+1)*(x*x+(m+2)*x+1)*(x**3+(m+6)*x*x+(4*m+9)*x+2*m+4)
assert s.cancel(Gc-Go-Q/Den)==0
assert s.simplify(s.diff(Q,x) - (2*x*(m-2)+m**2-4))==0
assert s.simplify(Q.subs({m:3,x:1}))==4
assert s.simplify((Gc-Go).subs({m:3,x:1}))==s.Rational(2,287)
assert s.simplify(Q.subs({m:3,x:(s.sqrt(33)-5)/2}))==0
# Riccati-like asymptotic: positive root is 2/( (m-2)*(sqrt((m+2)^2+8/(m-2))+(m+2))/2 )
# m^2*root tends to 2, checked by exact symbolic limit.
root = (s.sqrt((m+2)**2+8/(m-2))-(m+2))/2
assert s.limit(m*m*root,m,s.oo)==2

checks=6
for M in range(2,12):
  n=2*M+4
  edges=[(0,1),(0,2),(0,3)]
  edges += [(2,4+i) for i in range(M)]
  edges += [(3,4+M+i) for i in range(M)]
  L=s.zeros(n)
  for i,j in edges:
    L[i,i]+=1; L[j,j]+=1; L[i,j]-=1; L[j,i]-=1
  for z in [s.Rational(1,20),s.Rational(1,3),s.Rational(1,1),s.Rational(3,1),s.Rational(10,1)]:
    G=(L+z*s.eye(n)).inv()
    assert G[1,1]==s.factor(Gc.subs({m:M,x:z})); checks+=1
    assert G[4,4]==s.factor(Go.subs({m:M,x:z})); checks+=1
    assert G[1,1]>G[0,0]; checks+=1
    assert G[4,4]>G[2,2]; checks+=1
    assert G[4+M,4+M]>G[3,3]; checks+=1
    assert all(G[i,i]==G[4,4] for i in list(range(4,4+M))+list(range(4+M,n))); checks+=1
    S=[G[i,i] for i in range(n)]
    best=max(S)
    expected= max(G[1,1],G[4,4])
    assert best==expected; checks+=1
    sign=s.sign(Q.subs({m:M,x:z}))
    assert s.sign(G[1,1]-G[4,4])==sign; checks+=1
print('PASS',checks,'symbolic, exact-matrix and structural assertions')
