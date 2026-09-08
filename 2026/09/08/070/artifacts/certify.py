import math
def mr_transcript(n, bases=(2,7,61)):
    assert n>2 and n%2==1
    d=n-1; r=0
    while d%2==0: d//=2; r+=1
    out={"n":n,"d":d,"r":r,"bases":{}}
    for a in bases:
        a=a % n
        x=pow(a,d,n)
        seq=[x]
        if x in (1,n-1):
            out["bases"][str(a)]={"pass":True,"x0":x,"squarings":[]}
            continue
        ok=False; sq=[]
        for j in range(r-1):
            x=(x*x)%n; sq.append(x)
            if x==n-1: ok=True; break
        # full check: if loop ended without n-1 -> composite
        if not ok:
            # last value check
            pass
        out["bases"][str(a)]={"pass":ok,"x0":seq[0],"squarings":sq}
    return out
def mr_prime(n,bases=(2,7,61)):
    if n<2: return False
    for p in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n==p: return True
        if n%p==0: return False
    t=mr_transcript(n,bases)
    return all(v["pass"] for v in t["bases"].values())
KEY=[1001755423,1001755619,1000025261,1000025263,1000025267,1000025269,1000000007,1001999989]
certs={n:mr_transcript(n) for n in KEY}
# also certify compositeness of interior of max gap: every odd in between composite with a small factor
A,B=1001755423,1001755619
def small_factor(m):
    lim=int(math.isqrt(m))+1
    f=None
    d=2
    while d*d<=m and d<=1000:
        if m%d==0: return d
        d+=1 if d==2 else 2
    # full trial to be safe (gap width 196, m~1e9, sqrt~31623, cheap)
    d=1001
    while d*d<=m:
        if m%d==0: return d
        d+=2
    return None
comp={}
for m in range(A+1,B):
    if m%2==0: comp[str(m)]="2"
    else:
        f=small_factor(m)
        assert f is not None, m
        comp[str(m)]=str(f)
import json as J
# avoid name clash tricks; plain import
J.dump({"certs":certs,"gap_interior_factors":comp},open("gap_certs.json","w"))
print("KEY prime check:",{n:mr_prime(n) for n in KEY})
print("interior composites:",len(comp))
# primality double-check of endpoints via trial division to sqrt (independent method)
def is_prime_trial(n):
    if n<2: return False
    if n%2==0: return n==2
    i=3
    while i*i<=n:
        if n%i==0: return False
        i+=2
    return True
print("trial:",{n:is_prime_trial(n) for n in [1001755423,1001755619]})
