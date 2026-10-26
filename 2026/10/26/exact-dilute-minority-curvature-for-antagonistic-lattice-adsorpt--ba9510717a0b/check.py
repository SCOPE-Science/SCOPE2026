from fractions import Fraction as F
from collections import Counter
from itertools import product
# Local neighborhoods of square lattice sites, with center included.
def cross(a):
 x,y=a;return {(x,y),(x+1,y),(x-1,y),(x,y+1),(x,y-1)}
root=cross((0,0))
counts=Counter()
for x,y in product(range(-2,3),repeat=2):
 if x==y==0:continue
 m=len(root & cross((x,y)))
 if m:counts[m]+=1
assert counts=={2:8,1:4},counts
coop=sum((F(c*m,5*(5-m)*(10-m)) for m,c in counts.items()),F(0))
assert coop==F(7,45)
coeff_eps=coop-F(1,25)
assert coeff_eps==F(26,225)
coeff_p=F(1,5)+coeff_eps
assert coeff_p==F(71,225)
old=F(493,1800)
assert coeff_p-old==F(1,24)
# Ordered Poisson attempts for a pair at separation with intersection m:
# earlier B at time u, later B at s, A clocks on first cross >u,
# on second cross outside first cross >s;
# integration of exp[-5u-(5-m)s] over 0<u<s.
for offset,target in [((1,0),F(1,12)),((1,1),F(1,12)),((2,0),F(1,18)),((3,0),F(1,25))]:
 m=len(root&cross(offset))
 prob=F(2,(5-m)*(10-m))
 assert prob==target,(offset,prob,target)
# One B preemption gives excess probability of the later B relative to absent first B.
for m in [1,2]:
 positive=F(1,(5-m)*(10-m))
 reference=F(1,5*(10-m))
 assert positive-reference==F(m,5*(5-m)*(10-m))
print('All exact local combinatorial and rational-integral identities verified.')
print('overlap multiplicities:',dict(counts))
print('quadratic coefficient:',coeff_p,'=',float(coeff_p))
print('difference from 493/1800:',coeff_p-old)
