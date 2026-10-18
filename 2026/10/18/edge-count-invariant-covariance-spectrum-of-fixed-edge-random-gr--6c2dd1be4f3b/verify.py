from itertools import combinations
from fractions import Fraction as F
from math import comb

def fall(a,j):
 out=1
 for i in range(j):out*=a-i
 return out

def calc(n,m,enumerate_graphs=True):
 M=n*(n-1)//2;s=n-1;t=M-s
 lo=max(0,m-t);hi=min(s,m);sup=list(range(lo,hi+1));r=len(sup)-1
 pi=[F(comb(s,k)*comb(t,m-k),comb(M,m)) for k in sup]
 # Polynomial Gram-Schmidt on hypergeometric support
 basis=[];norms=[]
 for j in range(r+1):
  vec=[F(k)**j for k in sup]
  for b,nb in zip(basis,norms):
   alpha=sum((pi[z]*F(k)**j*b[z] for z,k in enumerate(sup)),F(0))/nb
   vec=[v-alpha*w for v,w in zip(vec,b)]
  nb=sum((pi[z]*vec[z]**2 for z in range(r+1)),F(0))
  assert nb>0
  basis.append(vec);norms.append(nb)
 if enumerate_graphs:
  edges=list(combinations(range(n),2));L=comb(M,m)
  count=[0]*(r+1);second=[[0]*(r+1) for _ in sup]
  for choice in combinations(range(M),m):
   degrees=[0]*n
   for ei in choice:
    a,b=edges[ei];degrees[a]+=1;degrees[b]+=1
   hist=[0]*(r+1)
   for d in degrees:hist[d-lo]+=1
   for i in range(r+1):
    count[i]+=hist[i]
    for h in range(r+1):second[i][h]+=hist[i]*hist[h]
  covariance=[[F(second[i][h],L)-F(count[i]*count[h],L*L) for h in range(r+1)] for i in range(r+1)]
  for i in range(r+1):assert F(count[i],L)==n*pi[i]
 else:
  # exact pair joint from shared edge and hypergeom exterior
  def hyper_joint(k,h):
   base=F(0)
   for z in range(2):
    if k-z<0 or h-z<0:continue
    a=s-1;outside=M-2*s+1
    left=m-z-(k-z)-(h-z)
    if not (0<=left<=outside):continue
    base+=F(comb(a,k-z)*comb(a,h-z)*comb(outside,left),comb(M,m))
   return base
  covariance=[[n*pi[i]*(int(i==h)-pi[h])+n*(n-1)*(hyper_joint(k,l)-pi[i]*pi[h]) for h,l in enumerate(sup)] for i,k in enumerate(sup)]
 for j in range(r+1):
  if j>=1:
   rho=F((-1)**j*fall(s-1,j),fall(t,j))+F((-1)**(j-1)*j*fall(s-1,j-1),s*fall(t,j-1))
  else:rho=F(1)
  eigen=F(0) if j in [0,1] else n*(1+(n-1)*rho)
  for l in range(r+1):
   lhs=sum((basis[j][i]*covariance[i][h]*basis[l][h] for i in range(r+1) for h in range(r+1)),F(0))
   expected=eigen*norms[j] if j==l else F(0)
   assert lhs==expected, (n,m,j,l,lhs,expected)
 return (r, [str(n*(1+(n-1)*(F((-1)**j*fall(s-1,j),fall(t,j))+F((-1)**(j-1)*j*fall(s-1,j-1),s*fall(t,j-1))))) for j in range(2,r+1)])

if __name__=='__main__':
 tests=0
 for n in range(4,7):
  M=n*(n-1)//2
  for m in range(1,M):
   calc(n,m,True)
   calc(n,m,False)
   tests+=2
 print('VERIFY_OK',tests,'independent graph-enumeration and hypergeometric-pair cases')
