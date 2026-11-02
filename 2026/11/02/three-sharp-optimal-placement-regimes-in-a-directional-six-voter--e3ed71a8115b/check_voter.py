"""Exact certificate for the six-site directed voter model with two fixed opinions.
Requires SymPy; all computations use rational arithmetic.
"""
import sympy as sp
from itertools import product
q = sp.symbols('q',positive=True)
z = sp.symbols('z',positive=True)

def variance(L, u=q):
    if L == 1:
        return sp.Integer(0)
    return sp.factor(u/(1-u)**2 - L**2*u**L/(1-u**L)**2)

def F(a, u=q):
    return variance(a,u)+variance(6-a,u)

P = z**6+2*z**5-z**4-18*z**3-38*z**2-12*z+8
Q = 2*z**3-z**2-10*z-4
D12 = sp.factor(F(1)-F(2))
D23 = sp.factor(F(2)-F(3))
assert sp.simplify(D12 + q**7*P.subs(z,q+1/q)/((q+1)**2*(q**2+1)**2*(q**4+q**3+q**2+q+1)**2)) == 0
assert sp.simplify(D23 + 2*q**5*Q.subs(z,q+1/q)/((q+1)**2*(q**2+1)**2*(q**2+q+1)**2)) == 0
assert sp.expand(P.subs(z,z+2)) == z**6+14*z**5+79*z**4+214*z**3+230*z**2-60*z-200
assert sp.expand(Q.subs(z,z+2)) == 2*z**3+11*z**2+10*z-12
assert P.subs(z,sp.Rational(27,10))<0 and Q.subs(z,sp.Rational(27,10))>0
assert F(2).subs(q,sp.Rational(4,9)) < min(F(1).subs(q,sp.Rational(4,9)),F(3).subs(q,sp.Rational(4,9)))

def exact_chain(a, u):
    n=6
    free=tuple(i for i in range(n) if i not in (0,a))
    states=tuple(product([0,1],repeat=len(free)))
    index={s:i for i,s in enumerate(states)}
    G=sp.zeros(len(states))
    for ix,s in enumerate(states):
        bits=list(s)
        op={0:0,a:1}
        op.update(zip(free,bits))
        for pos in free:
            for neigh, rate in (((pos+1)%n,sp.Integer(1)),((pos-1)%n,u)):
                if op[pos] == op[neigh]:
                    continue
                cp=list(s)
                cp[free.index(pos)]=op[neigh]
                j=index[tuple(cp)]
                G[ix,j]+=rate
                G[ix,ix]-=rate
    M=G.T
    M[-1,:]=sp.ones(1,len(states))
    rhs=sp.zeros(len(states),1);rhs[-1,0]=1
    prob=list(M.inv()*rhs)
    assert all(p>=0 for p in prob)
    tot=[1+sum(s) for s in states]
    mean=sum(p*k for p,k in zip(prob,tot))
    var=sp.factor(sum(p*(k-mean)**2 for p,k in zip(prob,tot)))
    return var

for u in [sp.Rational(4,9),sp.Rational(1,2),sp.Rational(1,3)]:
    for a in (1,2,3):
        direct=exact_chain(a,u)
        predicted=sp.factor(F(a).subs(q,u))
        assert direct==predicted, (a,u,direct,predicted)
print('PASS: symbolic factorization, unique-root sign tests, interior witness, and 9 exact CTMC solutions')
for a in (1,2,3):
    print(a,sp.factor(F(a).subs(q,sp.Rational(4,9))))
