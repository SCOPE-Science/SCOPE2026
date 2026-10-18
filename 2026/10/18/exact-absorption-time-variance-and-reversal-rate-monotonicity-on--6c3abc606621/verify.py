import numpy as np

def formulas(n,i,L,K):
 b=i*(n-i)
 mean=n/K+(2*L*b+n)/(2*(L+1)) if i else n/K
 var0=n*n/K**2+(n*(n*n-1)*L/3+n*(n-1))/(K*(L+1))
 if i==0:return mean,var0
 vh=(4*L**2*n*n*b-8*L**2*b*b+4*L**2*b+2*L*n**3-2*L*n+12*L*b+3*n*n+6*n-12*b)/(12*(1+L)**2)
 return mean,var0+vh

count=0
for n in range(3,41):
 for L in (0.,0.23,1.,7.):
  K=1.7
  M=np.zeros((2*n,2*n))
  for j in range(n):
   for a,v in enumerate((1,-1)):
    q=2*j+a
    M[q,q]+=1+L+(K if j==0 else 0)
    M[q,2*((j+v)%n)+a]-=1
    M[q,2*j+1-a]-=L
  f=np.linalg.solve(M,np.ones(2*n));g=np.linalg.solve(M,2*f)
  for j in range(n):
   mean=(f[2*j]+f[2*j+1])/2
   var=(g[2*j]+g[2*j+1])/2-mean**2
   fm,fv=formulas(n,j,L,K)
   assert abs(mean-fm)<1e-7,(n,j,L,'mean',mean,fm)
   assert abs(var-fv)<1e-5,(n,j,L,'var',var,fv)
   count+=1
print('CHECKED',count,'pairs','PASS')
