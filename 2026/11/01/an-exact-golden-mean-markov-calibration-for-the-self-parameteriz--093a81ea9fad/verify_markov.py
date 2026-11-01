"""Reproducible exact algebra and periodic symbolic census for a quadratic tent map.
Uses SymPy for exact algebraic identities and high-precision numerical crosschecks.
"""
import sympy as s
from fractions import Fraction

C = s.symbols('C', real=True)
a = s.Rational(37,25)+C/4
h = (a+s.Rational(1,8))/2
q = s.expand((a+h/4)*(1-h))
P=s.factor(q*(a+q/4)-s.Rational(1,2))
expected=(50*C+121)*(450*C-13511)*(22500*C**2+178900*C-18831)/s.Integer(1638400000000)
assert s.simplify(P-expected)==0
Cstar=(100*s.sqrt(337)-1789)/450
assert s.simplify((22500*C**2+178900*C-18831).subs(C,Cstar))==0
A=s.simplify(a.subs(C,Cstar))
H=s.simplify(h.subs(C,Cstar))
Q=s.simplify(q.subs(C,Cstar))
assert s.simplify(A-(s.Rational(35,72)+s.sqrt(337)/18))==0
assert s.simplify(H-(11+s.sqrt(337))/36)==0
assert s.simplify(Q-(s.sqrt(337)-7)/36)==0
assert s.simplify(Q*(A+Q/4)-s.Rational(1,2))==0
assert s.Rational(103902,1000000)<Cstar<s.Rational(103903,1000000)
assert 0<Q<s.Rational(1,2)<H<1
assert s.simplify(H-Q-s.Rational(1,2))==0

M=s.Matrix([[0,1],[1,1]])
L=[2,1]
for n in range(2,17):L.append(L[-1]+L[-2])
for n in range(1,16):
 assert s.trace(M**n)==L[n]

# Numerically compute each primitive period-n orbit from the contracting
# inverse-branch coding; compare the dynamically obtained unique points
# against the exact transfer-matrix periodic-word count.
import mpmath as mp
mp.mp.dps=65
c0=mp.mpf(str(s.N(Cstar,70)))
a0=mp.mpf(37)/25+c0/4
h0=(a0+mp.mpf('0.125'))/2
q0=(a0+h0/4)*(1-h0)
def f(x):
 return (a0+x/4)*(x if x<=mp.mpf('0.5') else 1-x)
def inv(branch,y):
 # f_A(x)=a x + x*x/4; f_B(x)=(a+x/4)(1-x)
 if branch==0:
  return 2*(mp.sqrt(a0*a0+y)-a0)
 # solve x*x/4 + (a-1/4)*x + (y-a)=0, root x>=.5
 return 2*(-(a0-mp.mpf('.25'))+mp.sqrt((a0-mp.mpf('.25'))**2+(a0-y)))

def coding_word(w):
 n=len(w)
 if not all(M[w[i],w[(i+1)%n]]==1 for i in range(n)):
  return None
 x=(mp.mpf('.5') if w[0]==0 else (mp.mpf('.5')+h0)/2)
 for _ in range(250):
  y=x
  for branch in reversed(w):y=inv(branch,y)
  if abs(y-x)<mp.mpf('1e-56'):
   x=y;break
  x=y
 if not (q0-mp.mpf('1e-50')<=x<=h0+mp.mpf('1e-50')):raise AssertionError((w,x))
 y=x
 for b in w:
  if b==0 and y>mp.mpf('.5')+mp.mpf('1e-48'):raise AssertionError((w,b,y))
  if b==1 and y<mp.mpf('.5')-mp.mpf('1e-48'):raise AssertionError((w,b,y))
  y=f(y)
 assert abs(y-x)<mp.mpf('1e-40')
 return x

import itertools
for n in range(1,9):
 xs=[]
 for w in itertools.product([0,1],repeat=n):
  x=coding_word(w)
  if x is not None:xs.append(x)
 assert len(xs)==L[n],(n,len(xs),L[n])
 for i in range(len(xs)):
  for j in range(i):
   if abs(xs[i]-xs[j])<mp.mpf('1e-35'):raise AssertionError(('duplicate coding',n,i,j))
 assert abs(f(mp.mpf('.5'))-h0)<mp.mpf('1e-45')
 assert abs(f(h0)-q0)<mp.mpf('1e-45')
 assert abs(f(q0)-mp.mpf('.5'))<mp.mpf('1e-45')
 print('period',n,'symbolic fixed points',len(xs),'plus external origin',1,'total',len(xs)+1)
print('C*=',mp.nstr(c0,50))
print('q, h=',mp.nstr(q0,32),mp.nstr(h0,32))
print('all exact symbolic identities and inverse-branch checks passed')
