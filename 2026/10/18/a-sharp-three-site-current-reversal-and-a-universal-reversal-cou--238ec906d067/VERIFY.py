"""Exact algebraic checks for rate-dependent circulation in reversible switching cycles."""
from fractions import Fraction
import random
import sympy as sp

K = sp.symbols('kappa', positive=True)

def make_generator(weights, conductances, rate):
    n = len(weights[0]); size = 2*n
    A = sp.zeros(size)
    for e in (0, 1):
        for i in range(n):
            s = e*n + i
            for delta in (-1, 1):
                j = (i+delta) % n
                edge = i if delta == 1 else j
                q = sp.Rational(conductances[e][edge], weights[e][i])
                A[s,e*n+j] += q
                A[s,s] -= q
            A[s,(1-e)*n+i] += rate
            A[s,s] -= rate
    return A

def stationary_edge_flux(A, weights, conductances):
    n = len(weights[0]); M = A.T.copy()
    for j in range(2*n): M[2*n-1,j] = 1
    b = sp.zeros(2*n, 1); b[2*n-1] = 1
    p = M.inv() * b
    f = sum(p[e*n]*sp.Rational(conductances[e][0],weights[e][0])
            - p[e*n+1]*sp.Rational(conductances[e][0],weights[e][1])
            for e in (0,1))
    return sp.factor(f), p

def reduced_flux(weights, conductances, rate):
    n = len(weights[0]); R = []; g=[]; pi=[]
    for e in (0, 1):
        A = sp.zeros(n)
        for i in range(n):
            for d in (-1, 1):
                j=(i+d)%n
                edge = i if d==1 else j
                q=sp.Rational(conductances[e][edge],weights[e][i])
                A[i,j]+=q; A[i,i]-=q
        B=sp.zeros(n-1,n)
        for i in range(n-1):B[i,i]=1;B[i,n-1]=-1
        # The coordinate for each row v in the zero-sum basis is v[:n-1].
        S=(B*A)[:,:n-1]
        R.append(S.inv())
        f=sp.zeros(n,1)
        f[0]=sp.Rational(conductances[e][0], weights[e][0])
        f[1]=-sp.Rational(conductances[e][0], weights[e][1])
        g.append(B*f)
        z=sum(weights[e]);pi.append(sp.Matrix([[sp.Rational(weights[e][i],z) for i in range(n-1)]]))
    d=pi[0]-pi[1]
    T=sp.eye(n-1)-rate*(R[0]+R[1])
    expression=(rate*sp.Rational(1,2)*d*T.inv()*(R[0]*g[0]-R[1]*g[1]))[0]
    return sp.factor(expression),sp.factor(T.det())

w=[[2,3,1],[1,1,2]]
c=[[1,2,3],[1,1,1]]
Q=make_generator(w,c,K)
current,probs=stationary_edge_flux(Q,w,c)
assert sp.simplify(current - K*(5*K-2)/(2*(469*K**2+1236*K+792)))==0
assert sp.simplify(sum(probs)-1)==0
assert sp.simplify(sum(probs[:3])-sp.Rational(1,2))==0
assert sp.simplify(sum(probs[3:])-sp.Rational(1,2))==0
assert reduced_flux(w,c,K)[0] == current
assert sp.simplify(current.subs(K,sp.Rational(1,5))) <0
assert sp.simplify(current.subs(K,sp.Rational(2,5))) ==0
assert sp.simplify(current.subs(K,sp.Integer(1))) >0
checks=7
random.seed(42042)
for n in range(3,7):
    for example in range(3):
        W=[[random.randint(1,5) for _ in range(n)] for e in (0,1)]
        C=[[random.randint(1,5) for _ in range(n)] for e in (0,1)]
        for e in (0,1):
            for i in range(n):
                j=(i+1)%n
                assert sp.Rational(W[e][i],sum(W[e]))*sp.Rational(C[e][i],W[e][i]) == sp.Rational(W[e][j],sum(W[e]))*sp.Rational(C[e][i],W[e][j])
                checks+=1
        for rate in (sp.Rational(1,7),sp.Rational(4,3)):
            q=make_generator(W,C,rate)
            brute,p=stationary_edge_flux(q,W,C)
            reduced,D=reduced_flux(W,C,rate)
            assert D>0 and sp.simplify(brute-reduced)==0
            assert sp.simplify(sum(p)-1)==0
            checks+=3
print('PASS:',checks,'exact rational and symbolic checks including closed six-state current and all-n reduction samples')
