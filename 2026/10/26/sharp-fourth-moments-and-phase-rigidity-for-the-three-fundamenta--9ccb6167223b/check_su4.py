from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import factorial
zero=(0,0,0)
v=[(1,0,0),(0,1,0),(0,0,1),(-1,-1,-1)]
def add(*dics):
 q=defaultdict(int)
 for d in dics:
  for x,c in d.items():q[x]+=c
 return {k:v for k,v in q.items() if v}
def mon(k,c=1):return {k:c}
def conj(p):return {tuple(-x for x in e):c for e,c in p.items()}
def mul(p,q):
 r=defaultdict(int)
 for x,c in p.items():
  for y,d in q.items():r[tuple(a+b for a,b in zip(x,y))]+=c*d
 return {k:v for k,v in r.items() if v}
def neg(p):return {k:-v for k,v in p.items()}
def scale(p,c):return {k:c*v for k,v in p.items()}
V=add(*[mon(x) for x in v])
Vb=conj(V)
W=add(*[mon(tuple(x+y for x,y in zip(v[i],v[j]))) for i,j in combinations(range(4),2)])
assert W==conj(W)
D=mon(zero)
for i,j in combinations(range(4),2):
 delta=tuple(x-y for x,y in zip(v[i],v[j]))
 D=mul(D,add(mon(zero,2),neg(mon(delta)),neg(mon(tuple(-e for e in delta)))))
assert len(D)<500
A=[mul(V,V),mul(Vb,Vb),mul(W,W),scale(mul(V,Vb),2),scale(mul(V,W),2),scale(mul(Vb,W),2)]
G=[]
for i in range(6):
 line=[]
 for j in range(6):
  t=mul(A[i],conj(A[j])); z=sum(v*D.get(tuple(-a for a in k),0) for k,v in t.items())
  assert z%24==0
  line.append(z//24)
 G.append(line)
print('Weyl Haar exact Gram of [V²,Vbar²,W²,2VVbar,2VW,2VbarW]')
for line in G:print(line)
print('D length',len(D))
# Predicted using irreducible tensor products:
# V²: (10)+W
# Vbar²: (10bar)+W
# W²: 1+Adj+20prime
# 2VVbar:2(1+Adj)
# 2VW:2(20+Vbar)
# 2VbarW:2(20bar+V)
expected=[[2,1,0,0,0,0],[1,2,0,0,0,0],[0,0,3,4,0,0],[0,0,4,8,0,0],[0,0,0,0,8,0],[0,0,0,0,0,8]]
assert G==expected,(G,expected)
print('PASS exact Haar Gram matches six character product decompositions')
# Coefficient identities checked by exact Gaussian-integer arithmetic.
from itertools import product
cs=[0,1,-1,1j,-1j,1+1j,-1+1j,2-1j]
test_count=0
for a,b,c in product(cs[:6],repeat=3):
 coeff=[a*a,b*b,c*c,a*b,a*c,b*c]
 mg=sum((coeff[i]*coeff[j].conjugate()*G[i][j] for i in range(6) for j in range(6)),0)
 assert mg.imag==0
 x2=a.real**2+a.imag**2;y2=b.real**2+b.imag**2;z2=c.real**2+c.imag**2
 E=2*x2*x2+2*y2*y2+3*z2*z2+8*x2*y2+8*z2*(x2+y2)+2*(a*a*b.conjugate()**2).real+8*(c*c*(a*b).conjugate()).real
 assert mg.real==E,(a,b,c,mg,E)
 N=x2+y2+z2
 assert 51*N*N-11*E>=0,(a,b,c)
 test_count+=1
from fractions import Fraction as Q
X=Q(3);Y=Q(3);Z=Q(5)
N=X+Y+Z
M=2*X**2+2*Y**2+3*Z**2+8*X*Y+8*Z*(X+Y)+2*X*Y+8*Z*X
assert N==11 and M==561 and Q(51,11)*N*N==M
print(f'PASS {test_count} exact Gaussian-integer moment and inequality tests plus rational sharpness test')
