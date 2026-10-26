from math import gcd

def mul(x,y,p):
 a,b=x;c,d=y
 return ((a*c-b*d)%p,(a*d+b*c-3*b*d)%p)

def order(p):
 x=(0,1);a=(1,0)
 for r in range(1,2*p+4):
  a=mul(a,x,p)
  if a==(1,0):return r
 raise AssertionError(('no order',p))

def fact(n):
 p=2
 while p*p<=n:
  if n%p==0:
   e=0
   while n%p==0:n//=p;e+=1
   yield p,e
  p+=1
 if n>1:yield n,1

def formula(k):
 g=2 if k%3==0 else 1
 for p,e in fact(k):
  if p>=7 and k%order(p)==0:g*=p**e
 return g

def actual(X,k):
 a,b=X
 v=[]
 for j in range(k+7):
  v.append(a**4);a,b=b,a+b
 win=sum(v[1:k+1]);g=0
 for j in range(5):
  if j:win+=v[j+k]-v[j]
  g=gcd(g,win)
 return g

def run():
 cases=0
 for k in range(1,1200,2):
  if k%5==0:continue
  target=formula(k)
  for name,X in [('Fibonacci',(0,1)),('Lucas',(2,1))]:
   got=actual(X,k)
   assert got==target,(name,k,got,target)
   cases+=1
 print('VERIFIED',cases,'exact gcd comparisons for all odd k<1200 coprime to 5')
 for p in (7,11,13,17,19,23,29,31,37,41):
  print('order',p,order(p))
if __name__=='__main__':run()
