import time
pmod={11:{1:[0,1],2:[1,0,1],3:[4,1,0,1],4:[2,1,0,0,1]},13:{1:[0,1],2:[2,0,1],3:[2,0,0,1],4:[2,0,0,0,1]}}


def irreducible_small(coeff,p):
    """For degree <=4, irreducibility equals absence of linear/quadratic monic divisors."""
    n=len(coeff)-1
    for d in range(1,min(2,n//2)+1):
        for c in __import__('itertools').product(range(p),repeat=d):
            divisor=list(c)+[1]
            r=[v%p for v in coeff]
            for k in range(len(r)-1,d-1,-1):
                t=r[k]
                if t:
                    for j in range(d+1):r[k-d+j]=(r[k-d+j]-t*divisor[j])%p
            if all(v==0 for v in r[:d]):return False
    return True

class FF:
 def __init__(self,p,n):
  self.p,self.n,self.q=p,n,p**n
  self.mod=pmod[p][n]
  self.digits=[tuple((a//p**i)%p for i in range(n)) for a in range(self.q)]
  self.rev={a:i for i,a in enumerate(self.digits)}
 def add(self,a,b):
  p=self.p
  return self.rev[tuple((x+y)%p for x,y in zip(self.digits[a],self.digits[b]))]
 def mul(self,a,b):
  p,n=self.p,self.n
  ca,cb=self.digits[a],self.digits[b]
  z=[0]*(2*n-1)
  for i in range(n):
   if ca[i]:
    for j in range(n):
     z[i+j]+=ca[i]*cb[j]
  for k in range(2*n-2,n-1,-1):
   c=z[k]%p
   if c:
    for j in range(n): z[k-n+j]-=c*self.mod[j]
  return self.rev[tuple(z[i]%p for i in range(n))]
 def pow(self,a,e):
  v=1
  while e:
   if e&1:v=self.mul(v,a)
   a=self.mul(a,a);e//=2
  return v
 def scalar(self,a,k):
  return self.rev[tuple((k*x)%self.p for x in self.digits[a])]

def run(p):
 fields={}; sigmas={}
 for n in range(1,5):
  f=FF(p,n);t=time.time()
  sqset=set(f.mul(x,x) for x in range(1,f.q))
  chi=[(-1 if x not in sqset else 1) for x in range(f.q)];chi[0]=0
  powers=[(f.pow(x,9),f.pow(x,5)) for x in range(f.q)]
  print('prepare',p,n, f.q,round(time.time()-t,2),flush=True)
  sigmas[n]={}
  for a in range(p):
   if a*a%p==4:continue
   count=1
   for x,(x9,x5) in enumerate(powers):
    t=f.add(x9,f.scalar(x5,a));t=f.add(t,x)
    count+=1+chi[t]
   sigmas[n][a]=count
 for a in sigmas[1]:
  N=[sigmas[n][a] for n in range(1,5)]
  S=[p**(i+1)+1 - N[i] for i in range(4)]
  c=[1]
  for k in range(1,5):
   z=-sum(c[k-j]*S[j-1] for j in range(1,k+1))
   assert z%k==0
   c.append(z//k)
  c += [p*c[3],p*p*c[2],p**3*c[1],p**4]
  b=(N[1]-p*p-1)//4
  table={11:{0:0,1:6,3:10,4:-2,5:16,6:-16,7:2,8:-10,10:-6},13:{0:0,1:6,3:-10,4:-16,5:-10,6:14,7:-14,8:10,9:16,10:10,12:-6}}
  assert c==[1,0,2*b,0,b*b+2*p*p,0,2*b*p*p,0,p**4],(p,a,c,b)
  assert b==table[p][a],(p,a,b)
  assert N[0]==p+1 and N[2]==p**3+1
  print('a',p,a,'N',N,'poly',c,flush=True)

if __name__=='__main__':
 for p in [11,13]:
  for n, poly in pmod[p].items():
   if n>1:assert irreducible_small(poly,p),(p,n,poly)
  run(p)
 print('DIRECT_REPLAY_OK')
