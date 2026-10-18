"""Reproduce symbolic identities and exact witness calculations for the risk-cost convergence theorem.

Requires sympy; no network access.
"""
import sympy as s
x,r,c=s.symbols('x r c',real=True)
mu1,mu2,th1,th2,th3,th4,alpha,beta,b=s.symbols('mu1 mu2 th1 th2 th3 th4 alpha beta b',positive=True)
mu=mu1+mu2
h=(th1-th4)-(th1+th2)*x+(th3+th4)*r
Rstar=s.factor(((th1+th2)*mu1/mu-th1+th4)/(th3+th4))
k=(alpha-beta)*(th1+th2)/mu
Zdot=s.expand((alpha-beta)*h-k*(mu1-mu*x))
assert s.simplify(Zdot-(alpha-beta)*(th3+th4)*(r-Rstar))==0
# Mode and maximum of the general binomial pivotal curve.
N,M=8,5
K=s.binomial(N-1,M-1)*x**(M-1)*(1-x)**(N-M)
mode=s.Rational(M-1,N-1)
assert s.diff(K,x).subs(x,mode)==0
assert s.diff(K,x,2).subs(x,mode)<0
# First witness: two positive low-cost equilibria coexist with full interior collapse conditions.
case1={b:s.Rational(3,5),alpha:s.Rational(2,5),beta:s.Rational(1,5),mu1:1,mu2:2,th1:4,th2:1,th3:1,th4:1}
rv=s.simplify(Rstar.subs(case1))
assert rv==-s.Rational(2,3)
K3=2*x*(1-x)
km=s.Rational(1,2)
assert case1[beta]<case1[b]*km<case1[alpha]
roots=s.solve(case1[b]*K3-case1[beta],x)
assert roots==[(1-s.sqrt(3)/3)/2,(1+s.sqrt(3)/3)/2]
for xx in roots:
 assert s.simplify(case1[b]*K3.subs(x,xx)-case1[beta])==0
# Second witness: high-cost upper branch is a strict hyperbolic attractor with the same sign of risk-cost imbalance.
case2={b:1,alpha:s.Rational(2,5),beta:s.Rational(1,5),mu1:4,mu2:1,th1:12,th2:1,th3:1,th4:1}
assert s.simplify(Rstar.subs(case2))==-s.Rational(3,10)
xx=(1+1/s.sqrt(5))/2
assert s.simplify(K3.subs(x,xx)-case2[alpha])==0
fx=s.factor((x*(1-x)*case2[b]*s.diff(K3,x)).subs(x,xx))
fr=s.factor(-(case2[mu1]-(case2[mu1]+case2[mu2])*xx))
fc=s.factor(-(case2[alpha]-case2[beta])*(case2[th1]*(1-xx)-case2[th2]*xx+case2[th3]))
assert all(float(v)<0 for v in [fx,fr,fc]),[fx,fr,fc]
print('PASS: exact logit-odds identity')
print('PASS: interior-collapse and coexistence witnesses', roots)
print('PASS: sharpness witness with negative eigenvalues', fx,fr,fc)
