import math
A=10**9; B=A+2_000_000
N=B-A+1
is_prime=bytearray(b'\x01')*N
lim=int(math.isqrt(B))+1
small=bytearray(b'\x01')*(lim+1)
small[0]=0
if lim>=1: small[1]=0
for i in range(2,int(math.isqrt(lim))+1):
    if small[i]:
        for j in range(i*i, lim+1, i):
            small[j]=0
base=[i for i in range(2,lim+1) if small[i]]
for p in base:
    start=max(p*p, ((A+p-1)//p)*p)
    for j in range(start, B+1, p):
        is_prime[j-A]=0
primes=[A+i for i in range(N) if is_prime[i]]
print("count",len(primes))
gaps=[(primes[i+1]-primes[i],primes[i],primes[i+1]) for i in range(len(primes)-1)]
gmax=max(g for g,_,_ in gaps)
cands=[t for t in gaps if t[0]==gmax]
print("maxgap",gmax,"occ",len(cands))
for t in cands: print(t)
from collections import Counter
c=Counter(g for g,_,_ in gaps)
print("nspec",len(c))
print("spectrum:",sorted(c.items()))
S=set(primes)
quad=[p for p in primes if p+8<=B and (p+2 in S) and (p+6 in S) and (p+8 in S)]
print("quads",len(quad),quad[:8])
def find(offsets):
    res=[]
    for p in primes:
        if p+offsets[-1]>B: break
        ok=True
        for o in offsets:
            if (p+o) not in S: ok=False; break
        if ok: res.append(p)
    return res
sex1=find([0,4,6,10,12,16])
print("sex1",len(sex1),sex1[:8])
sex2=find([0,2,6,8,12,18])
print("sex2",len(sex2),sex2[:8])
# largest gaps list
big=sorted(c.items(),key=lambda x:-x[0])[:12]
print("biggest:",big)
# first few primes and last few
print("first",primes[:5],"last",primes[-5:])
