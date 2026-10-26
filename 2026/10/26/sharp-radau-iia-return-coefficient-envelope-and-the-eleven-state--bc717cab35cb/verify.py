"""Exact rational replay of the Radau IIA return-coefficient theorem.

Usage: python verify.py
Dependency: sympy (for symbolic identities and rational matrix arithmetic).
The universal statement is proved analytically; samples are consistency checks.
"""
import itertools
import sympy as S

x, p, n = S.symbols('x p n', real=True)
r = (6 - 2*x)/(x*x + 4*x + 6)
zstar = 3 + 3*S.sqrt(3)
rmin = (5 - 3*S.sqrt(3))/2
pcrit = (2-S.sqrt(3))/3
assert S.simplify(r.subs(x,zstar) - rmin) == 0
assert S.simplify(S.diff(r,x) - 2*(x*x-6*x-18)/(x*x+4*x+6)**2)==0
assert S.simplify(pcrit - (-rmin/(1-rmin))) == 0
assert S.simplify(1/pcrit - (6+3*S.sqrt(3))) == 0
F=S.factor((p+(1-p)*r)*(x*x+4*x+6))
assert S.expand(F-(p*x*x+(6*p-2)*x+6))==0
D=S.factor(S.discriminant(F,x))
assert S.simplify(D-4*(9*p*p-12*p+1))==0

def matrix_step(Q,h):
    m=Q.rows
    I=S.eye(m)
    numer=6*I+2*h*Q
    denom=6*I-4*h*Q+h*h*Q*Q
    return numer*denom.inv()

def reversible_generator(pi,conductances):
    m=len(pi)
    Q=S.zeros(m)
    for (i,j),c in conductances.items():
        assert 0 <= i < j < m and c>0
        Q[i,j]=c/pi[i]
        Q[j,i]=c/pi[j]
    for i in range(m):
        Q[i,i]=-sum(Q[i,j] for j in range(m) if j!=i)
    assert Q*S.ones(m,1)==S.zeros(m,1)
    assert all(S.simplify(pi[i]*Q[i,j]-pi[j]*Q[j,i])==0 for i in range(m) for j in range(m))
    return Q

# All reset chains have exactly one nonzero decay mode, regardless of pi.
for pi in [(S.Rational(1,2),S.Rational(1,2)),(S.Rational(1,5),S.Rational(1,3),S.Rational(7,15)),tuple(S.Rational(1,12) for _ in range(12))]:
    m=len(pi)
    P=S.ones(m,1)*S.Matrix([list(pi)])
    Q=P-S.eye(m)  # unit-rate complete reset
    assert Q*Q==-Q
    for h in (S.Rational(1,10), S.Rational(3,4), S.Rational(3,1)):
        T=matrix_step(Q,h)
        scalar=r.subs(x,h)
        assert T==(P+scalar*(S.eye(m)-P))
        for i in range(m):
            assert S.simplify(T[i,i]-(pi[i]+(1-pi[i])*scalar))==0

# Sharp universal 12-state witness: same result on a unit-weight star
# even after connecting arbitrary pairs of leaves among themselves.
for extra in [[],[(1,2)],[(1,2),(3,4),(5,6)],[(i,j) for i in range(1,12) for j in range(i+1,12)]]:
    pi=[S.Rational(1,12)]*12
    edges={(0,i):S.Rational(1,12) for i in range(1,12)}
    edges.update({(i,j):S.Rational(1,12) for i,j in extra})
    Q=reversible_generator(pi,edges)
    assert Q*S.Matrix([11]+[-1]*11)==-12*S.Matrix([11]+[-1]*11)
    T=matrix_step(Q,S.Rational(3,4))
    assert T[0,0]==-S.Rational(1,164)
    assert all(sum(T[i,j] for j in range(12))==1 for i in range(12))

# Nontrivial reversible networks and exact Padé row sums / detailed balance.
checks=0
for m in range(2,8):
    weights=[S.Rational(i+1, m*(m+1)//2) for i in range(m)]
    edge_set={(i,j):S.Rational((i+j)%3+1,m+2) for i in range(m) for j in range(i+1,m) if (j==i+1 or (i+j)%3==0)}
    Q=reversible_generator(weights,edge_set)
    for h in (S.Rational(1,7),S.Rational(3,4),S.Rational(7,3)):
        T=matrix_step(Q,h)
        for i in range(m):
            assert sum(T[i,j] for j in range(m))==1
            for j in range(m):
                assert S.simplify(weights[i]*T[i,j]-weights[j]*T[j,i])==0
            b=S.N(weights[i]+(1-weights[i])*rmin,60)
            assert S.N(T[i,i],60)>b-S.Float('1e-45')
            checks+=1

# Analytic cone roots and the 11-versus-12 boundary.
N,h=S.symbols('N h', positive=True)
cone_diag=S.factor((1+(N-1)*r.subs(x,N*h))/N)
assert S.simplify(cone_diag-(N*N*h*h+(6-2*N)*N*h+6*N)/(N*(N*N*h*h+4*N*h+6)))==0
root_low=N-3-S.sqrt(N*N-12*N+9)
root_high=N-3+S.sqrt(N*N-12*N+9)
assert S.factor((x-root_low)*(x-root_high) -(x*x+(6-2*N)*x+6*N))==0
assert S.simplify(1+10*rmin)>0
assert S.simplify(1+11*rmin)<0
print('VERIFY_OK: scalar extremum and stationary-mass identities; reset chains; '
      'four exact 12-state cone constructions (-1/164); '
      f'{checks} reversible-state return bounds; exact stochasticity and detailed balance; 11/12 cutoff')
