from collections import defaultdict
N=10000
sig=[0]*(N+2);div=[0]*(N+2)
for d in range(1,N+2):
 for m in range(d,N+2,d):sig[m]+=d;div[m]+=1
maxx=max(sig)
sp=list(range(maxx+1))
for i in range(2,int(maxx**0.5)+1):
 if sp[i]==i:
  for j in range(i*i,maxx+1,i):
   if sp[j]==j:sp[j]=i

def factors(z):
 out={}
 while z>1:
  p=sp[z];out[p]=out.get(p,0)+1;z//=p
 return out
hits=[]
for n in range(1,N):
 a=n-div[n];b=n+1-div[n+1]
 L=factors(sig[n]);R=factors(sig[n+1])
 if all(a*L.get(p,0)==b*R.get(p,0) for p in (L.keys()|R.keys())):hits.append(n)
print('VALUATION_VERIFIED',hits,'range',N-1)
assert hits==[1]
