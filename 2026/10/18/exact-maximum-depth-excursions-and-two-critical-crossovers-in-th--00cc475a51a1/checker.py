from fractions import Fraction as F

def exact_tail(p,m):
 q=1-p
 if p==F(1,2): return (1-F(1,2)**(m+1))/m
 if p==F(2,3): return F(m+1,3*(2**m-1))
 if p==1: return F(1,2)**m
 r=p/q
 return ((r-1)/(2-r))*(2*q-p*(r/2)**m)/(r**m-1)

def via_dirichlet(p,m):
 # solve for probability h_j of hitting top level m before lower 0, via Gaussian elimination on m-1 states
 q=1-p
 size=m-1
 if size==0: return 1-p/2
 A=[[F(0) for j in range(size+1)] for i in range(size)]
 for i in range(size):
  j=i+1
  A[i][i]=1
  if j>1:A[i][i-1]=-p
  if j<m-1:A[i][i+1]=-q
  else:A[i][-1]=q
 for i in range(size):
  t=A[i][i]
  for j in range(i,size+1): A[i][j]/=t
  for k in range(i+1,size):
   t=A[k][i]
   for j in range(i,size+1): A[k][j]-=t*A[i][j]
 h=[F(0)]*m
 for i in range(size-1,-1,-1): h[i+1]=A[i][-1]-sum(A[i][j]*h[j+1] for j in range(i+1,size))
 return q*h[1]+p*sum(F(1,2)**(j+1)*h[j] for j in range(1,m)) +p*F(1,2)**m

if __name__=='__main__':
 count=0
 for p in [F(1,2),F(11,20),F(3,5),F(2,3),F(7,10),F(4,5),F(9,10),F(1)]:
  for m in range(1,15):
   a=exact_tail(p,m); b=via_dirichlet(p,m)
   assert a==b,(p,m,a,b)
   count+=1
 print('PASS',count,'exact rational comparisons')
 for p in (F(1,2),F(3,5),F(2,3),F(4,5)):
  print('p',p,'tails', [str(exact_tail(p,m)) for m in range(1,6)])
