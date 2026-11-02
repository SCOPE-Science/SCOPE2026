#!/usr/bin/env python3
"""Exact algebraic checks accompanying the three-state Gibbs-averaging theorem.

Requires sympy. Symbolic checks support the written proof but are not a
substitute for the stated universal inequality argument.
"""
import sympy as sp
from fractions import Fraction

checks = 0

def check(condition, reason):
    global checks
    checks += 1
    if condition is not True and condition != sp.true:
        raise AssertionError(reason)

def z(expr, reason):
    check(sp.simplify(expr) == 0, reason)

def same(A, B, reason):
    check(A.shape == B.shape, reason + ': shape')
    for i in range(A.rows):
        for j in range(A.cols):
            z(A[i,j]-B[i,j], reason + ' entry %d,%d' % (i,j))

s,t,d = sp.symbols('s t d', real=True)
r = 1-s
x,y = (t+d)/2,(t-d)/2
P = sp.Matrix([
    [1-s-t/2, s+d/2, y],
    [s-d/2, t/2, 1-s-y],
    [x, 1-s-x, s]])
J = sp.ones(3,3)/3
G = sp.Matrix([[sp.Rational(1,2),sp.Rational(1,2),0],
               [sp.Rational(1,2),sp.Rational(1,2),0],[0,0,1]])
H = G-J
tau = (3*s-1)/2

# Universal polynomial identities used in the proof.
same(P*sp.ones(3,1),sp.ones(3,1),'stochastic row identities')
same(sp.ones(1,3)*P,sp.ones(1,3),'stochastic column identities')
z(sp.trace(P)-1,'trace identity')
z(sp.factor(P.det())-sp.Rational(3,4)*(d*d-(t-r)**2-3*(s-sp.Rational(1,3))**2), 'determinant identity')
same(G*P*G,J+tau*H,'Gibbs compression identity')
same(H*H,H,'projection idempotence')
same(J*H,sp.zeros(3),'projection orthogonality left')
same(H*J,sp.zeros(3),'projection orthogonality right')
z(sum(v*v for v in H)-1,'Frobenius-square normalization')

lo=(2*sp.sqrt(3)-3)/3
hi=sp.sqrt(3)/3
z((3*lo-1)/2-(sp.sqrt(3)-2),'lower spectral endpoint')
z((3*hi-1)/2-(sp.sqrt(3)-1)/2,'upper spectral endpoint')
z(sp.sqrt(3)*(sp.Rational(1,3)-lo)-2*lo,'lower endpoint active constraint')
z(sp.sqrt(3)*(hi-sp.Rational(1,3))-(1-hi),'upper endpoint active constraint')

# Explicit entire interval: d = sqrt(3)(s-1/3), t = 1-s.
Pline=sp.simplify(P.subs({t:r,d:sp.sqrt(3)*(s-sp.Rational(1,3))}))
same(Pline*Pline,J,'symbolic all-parameter two-step mixing')
same(G*Pline*G,J+tau*H,'symbolic all-parameter compression')

samples = [lo,sp.Rational(1,6),sp.Rational(1,4),sp.Rational(1,3),
           sp.Rational(2,5),sp.Rational(1,2),sp.Rational(4,7),hi]
for k,ss in enumerate(samples):
    T=Pline.subs(s,ss)
    for entry in T:
        check(sp.simplify(entry).is_nonnegative is True,'nonnegative interval witness %d' % k)
    if 0<k<len(samples)-1:
        for entry in T:
            check(sp.simplify(entry).is_positive is True,'positive interior witness %d' % k)
    same(T*T,J,'endpoint/interior two-step law %d' % k)
    for m in range(1,7):
        same((G*T*G)**m,J+((3*ss-1)/2)**m*H,'compressed power %d %d' % (k,m))

# Additional independent rational, strictly-positive two-step mixers.  
# u,v lie in the zero-sum plane with v.u=0, so (u v^T)^2=0.
ones=sp.Matrix([1,1,1])
examples=0
for aa in range(-2,3):
    for bb in range(-2,3):
        if aa==0 and bb==0:
            continue
        u=sp.Matrix([aa,bb,-aa-bb])
        v=ones.cross(u)
        z(v.dot(u),'orthogonal nilpotent factors')
        mag=max(abs(q) for q in u*v.T)
        for sign in (-1,1):
            eps=sp.Rational(sign,6*mag)
            T=J+eps*u*v.T
            for entry in T:
                check(entry>0,'positive rational kernel')
            same(T*T,J,'rational exact mixing')
            ss=T[2,2]
            check(bool(sp.simplify(ss-lo)>0),'rational bound lower')
            check(bool(sp.simplify(hi-ss)>0),'rational bound upper')
            Q=G*T*G
            for m in (1,2,3,4):
                same(Q**m,J+((3*ss-1)/2)**m*H,'rational compressed power')
            examples+=1

# For a two-state bistochastic chain, squared stationarity forces one-step stationarity.
a=sp.symbols('a',real=True)
B=sp.Matrix([[a,1-a],[1-a,a]])
J2=sp.ones(2,2)/2
z((B*B-J2)[0,0]-(2*a-1)**2/2,'two-state rigidity identity')
print('PASS: %d exact symbolic/algebraic assertions; %d positive rational two-step mixers;' % (checks,examples))
print('full three-state interval, both sharp endpoints, compression powers, and dimension-two rigidity checked.')
