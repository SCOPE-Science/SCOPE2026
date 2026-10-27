"""Optional independent unsymmetrized linear programs; requires SciPy and NumPy."""
import itertools,math
from scipy.optimize import linprog
from scipy.sparse import lil_matrix

def dist(n,k):
 S=list(itertools.combinations(range(n),k)); m=len(S); points=[('v',i) for i in range(n)]+[('c',s) for s in S]
 def d(i,j):
  x,y=points[i],points[j]
  if x[0]=='v' and y[0]=='v':return 1
  if x[0]=='c' and y[0]=='c':return math.sqrt(k-len(set(x[1])&set(y[1])))/k
  if x[0]=='v':x,y=y,x
  return math.sqrt((k-1 if y[1] in x[1] else k+1)/(2*k))
 return S,points,d

def predicted(n,k):
 p=math.sqrt((k-1)/(2*k));q=math.sqrt((k+1)/(2*k));r=min(k,n-k)
 if r==1:
  b=(k*p-(k-1)*q)/((n-k)*q+k*p)
  L=(n-1)/((n-k)*q+k*p)
 else:
  z=math.sqrt(r)
  b=(k*p*z-(k-1))/(n-k+n*k*p*z)
  L=k*z*(n-1)/(n-k+n*k*p*z)
 return L,b

def check(n,k):
 S,points,d=dist(n,k);L,b=predicted(n,k);a=(1-(n-k)*b)/k; m=len(points)
 rows=[[float(i==j) for j in range(n)] for i in range(n)]
 rows += [[a if j in s else b for j in range(n)] for s in S]
 mx=(0,0,0,0)
 for i in range(m):
  for j in range(i+1,m):
   v=sum(abs(rows[i][h]-rows[j][h]) for h in range(n))/2/d(i,j)
   if v>mx[0]:mx=(v,i,j,d(i,j))
 assert abs(mx[0]-L)<1e-9,(n,k,mx,L)
 print('sym',n,k,'norm',round(mx[0],12),'b',round(b,10),'pairs',m*(m-1)//2,flush=True)
 return L

def lp(n,k):
 S,points,d=dist(n,k);m=len(S);P=n+m;num=n*m+1; rows=[]; upper=[]
 # pair residual coefficient for rows; fixed vertex-vertex pairs skip
 # each input f is subset indicator, extremes of unit Lip equilateral. signs included via complements
 for i in range(P):
  for j in range(i+1,P):
   if i<n and j<n:continue
   dij=d(i,j)
   for mask in range(1,(1<<n)-1):
    row={num-1:-dij};fixed=0
    for vertex,sgn in ((i,1),(j,-1)):
     if vertex<n:
      fixed+=sgn*((mask>>vertex)&1)
     else:
      r=vertex-n
      for a in range(n):
       if ((mask>>a)&1):row[r*n+a]=row.get(r*n+a,0)+sgn
    rows.append(row);upper.append(-fixed)
 # equality sums each barycenter 1
 Aeq=lil_matrix((m,num));beq=[1]*m
 for idx in range(m):
  for j in range(n):Aeq[idx,idx*n+j]=1
 Aub=lil_matrix((len(rows),num));
 for j,r in enumerate(rows):
  for col,val in r.items():Aub[j,col]=val
 res=linprog([0]*(num-1)+[1],A_ub=Aub.tocsr(),b_ub=upper,A_eq=Aeq.tocsr(),b_eq=beq,bounds=[(None,None)]*(num-1)+[(0,None)],method='highs',options={'time_limit':40})
 print('LP',n,k,'success',res.success,'norm',res.fun,'pred',predicted(n,k)[0], 'nconstraints',len(rows),flush=True)
 assert res.success and abs(res.fun-predicted(n,k)[0])<1e-7
if __name__=='__main__':
 for n,k in [(4,3),(5,3),(5,4),(6,3)]:lp(n,k)
