"""Exact and numerical checks for Gaussian invariance of coordinate Langevin updates.

This is a finite verification companion to the mathematical proof, not a substitute
for the universal Gaussian-mixture/graph argument.
"""
from fractions import Fraction
import sympy as s

Q=s.Rational

def post_cov(H, Sigma, h, probs, i):
    d=H.rows
    e=s.zeros(d,1); e[i]=1
    a=h/probs[i]
    A=s.eye(d)-a*e*e.T*H
    return s.simplify(A*Sigma*A.T+2*a*e*e.T)

def diagnostics(H,h,probs,Sigma):
    d=H.rows
    comps=[post_cov(H,Sigma,h,probs,i) for i in range(d)]
    avg=s.zeros(d)
    for p,C in zip(probs,comps):avg+=p*C
    return s.simplify(avg-Sigma),comps

def stationary_cov(H,h,probs):
    d=H.rows
    ss=s.symbols('s:'+str(d*d))
    S=s.Matrix(d,d,ss)
    K=s.zeros(d)
    for i,p in enumerate(probs):
        K+=p*post_cov(H,S,h,probs,i)
    eq=list(K-S)
    sol=s.solve(eq, ss, dict=True)
    assert len(sol)==1
    return s.simplify(S.subs(sol[0]))

cases=[
    (s.Matrix([[1,Q(1,2)],[Q(1,2),2]]),Q(1,4),[Q(1,3),Q(2,3)]),
    (s.Matrix([[4,1,0],[1,3,Q(1,2)],[0,Q(1,2),2]]),Q(1,10),[Q(4,9),Q(3,9),Q(2,9)]),
    (s.Matrix([[1,Q(1,3),0],[Q(1,3),2,0],[0,0,3]]),Q(1,6),[Q(2,9),Q(4,9),Q(1,3)]),
    (s.diag(1,2,3),Q(1,20),[Q(1,2),Q(1,3),Q(1,6)]),
]

count=0
for H,h,probs in cases:
    comps=[]
    visited=set()
    for i in range(H.rows):
        if i in visited:continue
        stack=[i]; grp=set()
        while stack:
            j=stack.pop()
            if j in grp:continue
            grp.add(j)
            stack.extend(k for k in range(H.rows) if k not in grp and H[j,k]!=0)
        visited.update(grp);comps.append(sorted(grp))
    S=s.zeros(H.rows)
    for cc in comps:
        T=sum(H[i,i] for i in cc)
        P=sum(probs[i] for i in cc)
        assert all(s.simplify(probs[i]/H[i,i]-P/T)==0 for i in cc)
        gamma=1/(1-h*T/(2*P))
        assert gamma>0
        inv=H.extract(cc,cc).inv()
        for j,i in enumerate(cc):
            for l,k in enumerate(cc):S[i,k]=gamma*inv[j,l]
    _,covs=diagnostics(H,h,probs,S)
    assert all(C==S for C in covs)
    count+=H.rows*H.rows*len(covs)
    assert stationary_cov(H,h,probs)==S
    count+=H.rows*H.rows

# A coupled target with unequal diagonal and uniform probabilities admits a
# stationary covariance, but not a stationary Gaussian distribution.
H=s.Matrix([[1,Q(1,2)],[Q(1,2),2]])
h=Q(1,4)
probs=[Q(1,2),Q(1,2)]
S=stationary_cov(H,h,probs)
assert S.is_symmetric() and S.det()>0 and S[0,0]>0
res,covs=diagnostics(H,h,probs,S)
assert res==s.zeros(2)
assert any(C!=S for C in covs)
v=s.Matrix([1,1]); vv=[(v.T*C*v)[0] for C in covs]; vm=(v.T*S*v)[0]
assert sum(p*z for p,z in zip(probs,vv))==vm
excess=s.factor(3*(sum(p*z*z for p,z in zip(probs,vv))-vm*vm))
assert excess>0
print('exact tests',count,'unbalanced stationary covariance',S,'Gaussian 4th-moment closure excess',excess)

# Randomized multiple-step covariance transport of balanced and unbalanced schemes.
for H,h,probs in cases[:2]:
    s0=s.zeros(H.rows)
    S=stationary_cov(H,h,probs)
    for j in range(12):
        err,covs=diagnostics(H,h,probs,s0)
        s0=s0+err
        assert all(z.is_finite for z in s0)
        assert (S-s0).is_positive_semidefinite
        count+=1
print('PASS',count,'symbolic stationarity, covariance, and monotonicity checks')
