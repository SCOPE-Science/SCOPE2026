"""Exact independent checks for a one-defect common-factor pivoting theorem.

Run: python3 verify.py.  Uses only the Python standard library.
The checks are finite diagnostics, not substitutes for the analytic proof.
"""
from fractions import Fraction as F
from itertools import combinations
from math import sqrt

checks = 0

def ok(condition, label=''):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(f'check {checks}: {label}')

def matrix(n,a,b):
    return [[F(b)+(F(a) if i==j==0 else F(1) if i==j else F(0)) for j in range(n)] for i in range(n)]

def residual(A,S):
    B=[row[:] for row in A]
    for i in S:
        p=B[i][i]
        ok(p>0,'positive pivot')
        v=[B[j][i] for j in range(len(A))]
        B=[[B[j][h]-v[j]*v[h]/p for h in range(len(A))] for j in range(len(A))]
    return B

def trace(B):
    return sum((B[i][i] for i in range(len(B))),F(0))

def theory(n,a,b,k):
    bm=1/(1/b+F(k))
    bh=1/(1/b+F(k-1)+1/a)
    t0=a+F(n-k-1)+F(n-k)*bm
    t1=F(n-k)*(1+bh)
    p0=F(1)
    for j in range(k):
        bj=1/(1/b+F(j))
        rem=n-1-j
        p0*=F(rem)*(1+bj)/(F(rem)*(1+bj)+a+bj)
    x=1/b+F(k-1)
    delta=(a-1)*(1-F(n-k)/((a*x+1)*(x+1)))
    return t0,t1,p0,delta

for n in range(3,8):
 for a in (F(3,2), F(2), F(5)):
  for b in (F(1,3),F(1),F(4)):
   A=matrix(n,a,b)
   for k in range(1,n):
    t0,t1,p0,delta=theory(n,a,b,k)
    ok(t0-t1==delta,'sharp frontier identity')
    ok(F(0)<p0<F(1),'nondegenerate Bernoulli support')
    for S in combinations(range(n),k):
        measured=trace(residual(A,S))
        ok(measured==(t1 if 0 in S else t0),'subset Schur-complement trace')

# Direct dynamic probability enumeration uses full Schur updates and not the
# sequential survival-product derivation, for a second independent check.
def enumerate_paths(B,alive,k,weight,out):
    if k==0:
        out.append((weight,0 in alive,trace(B)))
        return
    total=sum((B[i][i] for i in alive),F(0))
    for i in alive:
        p=B[i][i]/total
        v=[B[j][i] for j in range(len(B))]
        C=[[B[j][h]-v[j]*v[h]/B[i][i] for h in range(len(B))] for j in range(len(B))]
        enumerate_paths(C, tuple(x for x in alive if x!=i),k-1,weight*p,out)

for n in range(3,7):
 for a,b in ((F(3,2),F(1,2)), (F(2),F(3)),(F(5),F(1,3))):
  A=matrix(n,a,b)
  for k in range(1,n):
   paths=[]
   enumerate_paths(A,tuple(range(n)),k,F(1),paths)
   t0,t1,p0,delta=theory(n,a,b,k)
   ok(sum((p for p,_,_ in paths),F(0))==1,'path probabilities sum one')
   ok(sum((p for p,no_spike,_ in paths if no_spike),F(0))==p0,'survival product')
   ok(all(v==(t0 if no_spike else t1) for _,no_spike,v in paths),'two-atom law')
   expected=sum((p*v for p,_,v in paths),F(0))
   ok(expected==p0*t0+(1-p0)*t1,'exact expectation')

# Asymptotic scaling and near-equality of all normalized correlations.
# These are convergence diagnostics at finite t; the proof handles infinity.
for t in (10,30,100,300):
    t=F(t); n=int(t**3); a=t; b=t*t
    t0,t1,p0,delta=theory(n,a,b,1)
    e=p0*t0+(1-p0)*t1
    ratio=t1/e
    ok(delta<0,'greedy worse for the constructed family')
    ok(abs(float(ratio/(t/2))-1)<(4/float(t)),'ratio t/2')
    ok(abs(float(t0/(2*t**3))-1)<(4/float(t)),'miss trace 2t^3')
    ok(abs(float(t1/(t**4))-1)<(4/float(t)),'greedy trace t^4')
    ok(abs(float((b+a)/(b+1))-1)<(2/float(t)),'nearly identical diagonals')
    ok(abs(float(b)/sqrt(float((b+a)*(b+1)))-1)<(3/float(t)),'all correlations near one')

print(f'PASS {checks} checks (exact-rational equalities and finite asymptotic diagnostics)')
