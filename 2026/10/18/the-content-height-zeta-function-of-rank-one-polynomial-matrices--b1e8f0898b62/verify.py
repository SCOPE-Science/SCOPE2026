from collections import defaultdict
from itertools import product

def pol_mul(a,b,q):
 la=[];lb=[]
 while a: la.append(a%q);a//=q
 while b: lb.append(b%q);b//=q
 c=[0]*(len(la)+len(lb)-1) if la and lb else []
 for i,ai in enumerate(la):
  for j,bj in enumerate(lb):c[i+j]=(c[i+j]+ai*bj)%q
 return sum(z*q**i for i,z in enumerate(c))

def deg(a,q):
 d=-1
 while a:a//=q;d+=1
 return d

def poly_gcd(a,b,q):
 def rem(a,b):
  db=deg(b,q);lb=(b//(q**db))%q
  bb=[];t=b
  while t:bb.append(t%q);t//=q
  aa=[];t=a
  while t:aa.append(t%q);t//=q
  while len(aa)>=len(bb):
   v=aa[-1]*pow(lb,-1,q)%q
   ix=len(aa)-len(bb)
   for j,c in enumerate(bb):aa[ix+j]=(aa[ix+j]-v*c)%q
   while aa and aa[-1]==0:aa.pop()
  return sum(c*q**i for i,c in enumerate(aa))
 while b:a,b=b,rem(a,b)
 return a

def run(q,m,n,dmax):
 pp=q**(dmax+1)
 res=defaultdict(int)
 for arr in product(range(pp),repeat=m*n):
  if not any(arr):continue
  if any(pol_mul(arr[i*n+j],arr[k*n+l],q)!=pol_mul(arr[i*n+l],arr[k*n+j],q) for i in range(m) for k in range(i+1,m) for j in range(n) for l in range(j+1,n)):continue
  d=max(deg(x,q) for x in arr)
  g=0
  for a in arr:g=poly_gcd(g,a,q)
  res[(d,deg(g,q))]+=1
 for d in range(dmax+1):
  for h in range(d+1):
   # primitive vector max-degree a count formula
   def P(k,a):return q**k-1 if a==0 else (q**k-1)*(q**k-q)*q**(k*(a-1))
   pred=q**h*sum(P(m,a)*P(n,d-h-a) for a in range(d-h+1))//(q-1)
   assert pred == res[(d,h)],(q,m,n,d,h,pred,res[(d,h)])
 print('PASS q,m,n,dmax',q,m,n,dmax, 'distribution',dict(res))
run(2,2,2,1)
run(2,2,3,1)
run(3,2,2,1)

def primitive_count(q, k, a):
    return q**k - 1 if a == 0 else (q**k - 1) * (q**k-q) * q**(k*(a-1))

def shell_content(q,m,n,d,h):
    if h > d: return 0
    return q**h * sum(primitive_count(q,m,a)*primitive_count(q,n,d-h-a)
                       for a in range(d-h+1)) // (q-1)

for q in (2,3,4):
    for d in range(9):
        # Independent comparison with the motivating theorem's rank <=1 count,
        # including the excluded zero matrix.
        from_formula = 1 + sum(shell_content(q,2,2,a,h)
                               for a in range(d+1) for h in range(a+1))
        known = (d+1)*q**(2*d+3)+q**(2*d+2)-(d+1)*q**(2*d+1)
        assert from_formula == known, (q,d,from_formula,known)
    for m,n in ((2,3),(3,3),(2,4)):
        for d in range(9):
            a,b=q**m,q**n
            c=(a-1)*(b-1)//(q-1)
            count = sum(shell_content(q,m,n,d,h) for h in range(d+1))
            closed = (c*((a-q)*a**d-(b-q)*b**d)//(a-b) if a!=b
                      else c*((d+1)*a**d-(q*d*a**(d-1) if d else 0)))
            assert count == closed, (q,m,n,d,count,closed)
print('PASS all q=2,3,4 height counts through degree 8 versus closed formulas and published 2x2 total')
