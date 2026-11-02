"""Exact Fourier-cube moment identity, odd-phase quantization algebra, supplementary checks.
Python 3 standard library only. Infinite-order optimality is proved analytically in RESULT.md.
"""
from collections import defaultdict
from itertools import product
from fractions import Fraction
from math import cos,pi
import cmath

NV=4

def atom(exps=(0,0,0,0),c=1):return {tuple(exps):int(c)} if c else {}
def plus(*polys):
 d=defaultdict(int)
 for p in polys:
  for e,c in p.items():d[e]+=c
 return {e:c for e,c in d.items() if c}
def mul(p,q):
 d=defaultdict(int)
 for e,a in p.items():
  for f,b in q.items():d[tuple(x+y for x,y in zip(e,f))]+=a*b
 return {e:c for e,c in d.items() if c}
def conj(p):return {tuple(-x for x in e):c for e,c in p.items()}
def norm(p):return mul(p,conj(p))
def scale(p,s):return {e:c*s for e,c in p.items() if c*s}
O=atom();Z={}
vars=[atom(tuple(int(k==j) for k in range(NV))) for j in range(NV)]
A,B,C,D=vars
# 27-term convolution with formal Laurent variables.
coeff={(0,0,0):O,(1,0,0):O,(0,1,0):O,(0,0,1):O,(1,1,0):A,(1,0,1):B,(0,1,1):C,(1,1,1):D}
conv=defaultdict(dict)
for i,v in coeff.items():
 for j,w in coeff.items():
  k=tuple(x+y for x,y in zip(i,j))
  conv[k]=plus(conv[k],mul(v,w))
assert len(conv)==27
lhs=plus(*(norm(p) for p in conv.values()))
S0=plus(A,B,C,D)
S1=plus(O,A,B,mul(D,conj(C)))
S2=plus(O,A,C,mul(D,conj(B)))
S3=plus(O,B,C,mul(D,conj(A)))
rhs=plus(scale(O,88),*(scale(norm(s),2) for s in (S0,S1,S2,S3)))
assert lhs==rhs,(len(lhs),len(rhs),list(set(lhs)^set(rhs))[:10])
# Verify exact Hessian of 2*sum|S_i|^2 near (A,B,C,D)=(1,-1,-1,1).
base=[1,-1,-1,1]
R=[[1,-1,-1,1],[1,-1,1,-1],[1,1,-1,-1],[-1,-1,-1,1]]
G=[[2*sum(R[k][i]*R[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
assert G==[[8,0,0,-4],[0,8,0,-4],[0,0,8,-4],[ -4,-4,-4,8]]
# Laurent variable X represents exp(i*pi/q), with X^{-1} its conjugate.
def apow(n,sign=1):return { (n,0,0,0):sign }
def eval_form(p,vals):
 d=defaultdict(int)
 for e,c in p.items():
  power=sum(e[j]*vals[j][0] for j in range(4))
  sign=c
  for j in range(4):sign*=vals[j][1]**e[j]
  d[power]+=sign
 return {p:c for p,c in d.items() if c}
X2={2:1,-2:1}
# 136-64*(X+X^-1)/2+16*((X+X^-1)/2)^2
formula={0:144,1:-32,-1:-32,2:4,-2:4}
valid=[]
for v in product(range(-4,5),repeat=4):
 if v[0]%2 or v[3]%2 or not v[1]%2 or not v[2]%2:continue
 Q=sum(v[i]*G[i][j]*v[j] for i in range(4) for j in range(4))
 if Q==16:valid.append(v)
assert len(valid)==8
assert sorted(valid)==[(-2,-1,-1,-2),(0,-1,-1,-2),(0,-1,-1,0),(0,-1,1,0),(0,1,-1,0),(0,1,1,0),(0,1,1,2),(2,1,1,2)]
for v in valid:
 vals=[(v[0],1),(v[1],-1),(v[2],-1),(v[3],1)]
 assert eval_form(lhs,vals)==formula,(v,eval_form(lhs,vals))
# Every minimizer of continuous problem has one of three centers, and permuting A,B,C preserves M.
for perm in [(0,1,2),(1,0,2),(2,1,0)]:
 for v in valid:
  vals=[[(v[i],(1,-1,-1)[i]) for i in perm][i] for i in range(3)]+[(v[3],1)]
  assert eval_form(lhs,vals)==formula
# Supplementary independent complex arithmetic: directly sum 27 squared convolution values.
vertices=list(product((0,1),repeat=3))
def conv_numeric(a,b,c,d):
 cs={(0,0,0):1,(1,0,0):1,(0,1,0):1,(0,0,1):1,(1,1,0):a,(1,0,1):b,(0,1,1):c,(1,1,1):d}
 y=defaultdict(complex)
 for i,z in cs.items():
  for j,w in cs.items():
   y[tuple(i[t]+j[t] for t in range(3))]+=z*w
 return sum(abs(z)**2 for z in y.values())
for q in (3,5,7,9):
 z=[cmath.exp(2j*pi*k/q) for k in range(q)]
 best=1e100; num=0
 for i,j,k,l in product(range(q),repeat=4):
  a,b,c,d=z[i],z[j],z[k],z[l]
  val=conv_numeric(a,b,c,d)
  if val<best-1e-7:best=val;num=1
  elif abs(val-best)<1e-7:num+=1
 expected=136-64*cos(pi/q)+16*cos(pi/q)**2
 assert abs(best-expected)<1e-8,(q,best,expected)
 assert num==({3:56}.get(q,24)),(q,num)
print('CHECK_OK formal_27term_and_identity Hessian 24_candidate_laurent_cases exhaustive_q3_5_7_9')
