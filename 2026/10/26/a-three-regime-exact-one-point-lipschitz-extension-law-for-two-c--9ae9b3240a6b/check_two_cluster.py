from scipy.optimize import linprog
from fractions import Fraction
import random

def solve(p,q,s,t,R,U):
 n=p+q
 d=[[0 if i==j else (s if i<p and j<p else t if i>=p and j>=p else 1) for j in range(n)] for i in range(n)]
 # potential anchored f_0=0
 A=[]; b=[]
 for i in range(n):
  for j in range(i):
   v=[0.]* (n-1)
   if i:v[i-1]+=1
   if j:v[j-1]-=1
   A.extend([v,[-x for x in v]]);b.extend([d[i][j]]*2)
 bounds=[(None,None)]*(n-1)
 # master variables a_0...a_n-1, L
 rows=[[0.]*n+[-1.]];rh=[-1.]
 for it in range(160):
  c=[0.]*n+[1.]
  v=linprog(c,A_ub=rows,b_ub=rh,A_eq=[[1.]*n+[0.]],b_eq=[1.],bounds=[(None,None)]*(n+1),method='highs')
  assert v.success,(it,v.message)
  alpha=v.x[:n];L=v.x[-1]
  worse=0
  for j in range(n):
   w=[-a for a in alpha];w[j]+=1
   # objective over potentials anchored f0=0
   pot=linprog([-z for z in w[1:]],A_ub=A,b_ub=b,bounds=bounds,method='highs')
   assert pot.success
   norm=-pot.fun
   gap=norm-(R if j<p else U)*L
   if gap>1.e-8:
    worse=max(worse,gap)
    fj=[0.]+list(pot.x)
    rows.append([-float(z) for z in fj]+[-float(R if j<p else U)])
    rh.append(-fj[j])
  if worse<1.e-8: return L,it+1,alpha
 raise RuntimeError('did not converge')

rng=random.Random(228)
count=0
for trial in range(35):
 p,q=rng.randint(2,4),rng.randint(2,4)
 s,t=rng.randint(1,5)/5,rng.randint(1,5)/5
 R,U=rng.randint(3,15)/10,rng.randint(3,15)/10
 if R<s/2 or U<t/2 or R+U<1 or abs(R-U)>1:continue
 k=s*(p-1)/p;ell=t*(q-1)/q
 aa=max(0,min(1,(U-R*ell)/(U*(1-k)+R*(1-ell))))
 expect=max(1,(1-(1-k)*aa)/R,(ell+(1-ell)*aa)/U)
 got,its,alpha=solve(p,q,s,t,R,U)
 if abs(got-expect)>1e-7:raise RuntimeError((p,q,s,t,R,U,got,expect,its,alpha))
 count+=1
print('UNRESTRICTED_SIGNED_LP_OK',count,'instances')

# Exact-rational checks of one example in each support regime.
examples = [
 ((3,5,Fraction(4,5),Fraction(4,5),Fraction(1),Fraction(1,2)), Fraction(0), Fraction(32,25)),
 ((4,3,Fraction(4,5),Fraction(4,5),Fraction(1,2),Fraction(6,5)), Fraction(1), Fraction(6,5)),
 ((3,3,Fraction(4,5),Fraction(4,5),Fraction(3,5),Fraction(3,5)), Fraction(1,2), Fraction(23,18)),
]
for (p,q,s,t,R,U),expected_a,expected_L in examples:
    k=s*(p-1)/p;ell=t*(q-1)/q
    a=max(Fraction(0),min(Fraction(1),(U-R*ell)/(U*(1-k)+R*(1-ell))))
    L=max(Fraction(1),(1-(1-k)*a)/R,(ell+(1-ell)*a)/U)
    assert a==expected_a and L==expected_L,(a,L,expected_a,expected_L)
print('EXACT_RATIONAL_SUPPORT_EXAMPLES_OK',len(examples))
