"""Exact rational checks for periodic orbits in a best-response public-goods opinion map.
The mathematical proof is in RESULT.md; these finite checks are independent consistency tests.
Requires Python 3 and SymPy for the non-permutation examples.
"""
from fractions import Fraction as Q
from itertools import product
from math import gcd

ALPHA=Q(1,20)
BETA=LAMBDA=Q(19,40)
A=BETA/(BETA+LAMBDA)
B=LAMBDA/(BETA+LAMBDA)
THETA=Q(21,38)

def shift(v):
    return (v[-1],)+tuple(v[:-1])

def primitive_length(word):
    current=tuple(word)
    for m in range(1,len(word)+1):
        current=shift(current)
        if current==tuple(word):return m
    raise AssertionError('impossible')

def mul(M, y):
    return tuple(sum((M[i][j]*y[j] for j in range(len(y))),Q(0)) for i in range(len(y)))

def step(M,y):
    u=mul(M,y)
    x=tuple(int(v>THETA) for v in u)
    return x,tuple(A*v+B*t for v,t in zip(u,x))

def perm_matrix(n):
    return tuple(tuple(Q(int(j==(i-1)%n)) for j in range(n)) for i in range(n))

assert ALPHA+BETA+LAMBDA==1
assert BETA*LAMBDA/(BETA+LAMBDA)==Q(19,80)
assert Q(1,2)+ALPHA*Q(1,4)/(BETA*LAMBDA/(BETA+LAMBDA))==THETA

cases=0
for n in range(2,9):
    P=perm_matrix(n)
    assert 1<Q(3*n,4)<n
    for sigma in product((0,1),repeat=n):
        # Initial opinions include a threshold tie (assigned action zero).
        y0=tuple(Q(0) if t==0 else Q(1) for t in sigma)
        for t in range(2*n+1):
            expected_word=tuple(sigma)
            for _ in range(t): expected_word=shift(expected_word)
            # Starting from binary y0=sigma, this is an exact periodic orbit.
            action,y1=step(P,y0)
            assert action==shift(expected_word)
            assert y1==tuple(Q(k) for k in action)
            y0=y1
            cases+=1
    for word in product((0,1),repeat=n):
        p=primitive_length(word)
        assert n%p==0

# Exact rational test of the globally attracting formula for nonbinary initial states.
for n in range(2,9):
    P=perm_matrix(n)
    y0=tuple((THETA if i%4==0 else Q(i%3,3)) for i in range(n))
    sigma=tuple(int(v>THETA) for v in y0)
    y=y0
    for t in range(2*n+3):
        sig=tuple(sigma)
        for _ in range(t):sig=shift(sig)
        initial=tuple((THETA if i%4==0 else Q(i%3,3)) for i in range(n))
        initial_rot=initial
        for _ in range(t): initial_rot=shift(initial_rot)
        expected=tuple(Q(s)+A**t*(v-Q(s)) for s,v in zip(sig,initial_rot))
        assert y==expected, (n,t)
        x,y=step(P,y)
        assert x==shift(sig)
        cases+=1

# Strictly positive off-diagonal influence matrices, exact unique m-cycles.
try:
    import sympy as sp
except ImportError:
    print('PASS permutation checks:',cases,'(SymPy unavailable, mixed-network checks skipped)')
else:
    mixed=0
    for n in range(3,7):
        PP=sp.Matrix(perm_matrix(n)); I=sp.eye(n)
        Qmat=(sp.ones(n,n)-I)/sp.Integer(n-1)
        W=sp.Rational(19,20)*PP+sp.Rational(1,20)*Qmat
        assert all(W[i,j]>0 for i in range(n) for j in range(n) if i!=j)
        assert all(W[i,i]==0 for i in range(n))
        eps=max(sum(abs(W[i,j]-PP[i,j]) for j in range(n)) for i in range(n))
        assert eps<sp.Rational(17,76)
        for ones in (1, 2, n-1):
            word=tuple(1 if i<ones else 0 for i in range(n))
            m=primitive_length(word)
            sigs=[]
            sig=word
            for t in range(m):
                sigs.append(sp.Matrix(sig))
                sig=shift(sig)
            # y_m = (aW)^m y_0 + sum_{k=1}^m (aW)^(m-k) b sigma_k.
            M=sp.Rational(1,2)*W
            forcing=sp.zeros(n,1)
            for k in range(1,m+1):
                forcing+=M**(m-k)*sp.Rational(1,2)*sigs[k%m]
            y=(I-M**m).inv()*forcing
            ys=[]
            for t in range(m):
                ys.append(y)
                u=W*y
                decision=sp.Matrix([int(bool(z>sp.Rational(21,38))) for z in u])
                assert decision==sigs[(t+1)%m], (n,m,t)
                y=M*y+sp.Rational(1,2)*decision
            assert y==ys[0]
            assert all(max(abs(v-Q(s)) for v,s in zip(yt,sigs[t]))<=sp.Rational(1,2)*eps/(1-sp.Rational(1,2)) for t,yt in enumerate(ys))
            mixed+=1
    print('PASS exact permutation checks:',cases,'PASS fully connected directed network cycles:',mixed)
