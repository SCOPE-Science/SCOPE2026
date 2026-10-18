from math import comb

def coefficients(p,a,b):
  return [sum(comb(a,i)*comb(b,j-i)*(-b)**i*a**(j-i) for i in range(max(0,j-b),min(a,j)+1))%p for j in range(a+b+1)]

def check(p,a,b):
  assert p%2 and b>a>0 and (b-a)%p==0 and a%p
  e=0; t=b-a
  while t%p==0:e+=1;t//=p
  ell=p**e; d=a+b
  c=coefficients(p,a,b)
  assert c[0]==1 and c[1]==0,(p,a,b,'linear',c[1])
  assert c[2]==(-a*b*d*pow(2,-1,p))%p,(p,a,b,'quadratic',c[2])
  assert c[ell]==(a*t)%p,(p,a,b,'ell',c[ell],a*t%p)
  S={2*i+ell*j for i in range(d+1) for j in range(d+1)}
  assert all(c[j]==0 or j in S for j in range(2,d+1)),(p,a,b,'gap')
  assert all(c[j]==0 for j in range(3,ell,2)),(p,a,b,'odds')
  return ell
import itertools
ps=[3,5,7,11,13,17]
cnt=0; maxl=0
for p in ps:
  for a in range(1,12):
    if a%p==0: continue
    for t in range(1,8):
      b=a+p*t
      ell=check(p,a,b)
      cnt+=1;maxl=max(ell,maxl)
for x in [(3,2,5),(5,2,7),(5,2,27),(3,2,11),(7,3,10),(7,2,51)]:
  ell=check(*x); print('example',x,'ell',ell,'delta',(ell-1)//2)
print('PASS exact modular coefficient tests',cnt,'maximum ell',maxl)
