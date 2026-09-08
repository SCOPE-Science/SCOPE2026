"""Independent replay verifier: re-sieves [1e9,1e9+2e6] by a different code path
(simple odd-only sieve), recomputes max gap / quadruplets / sextuplets,
replays MR transcripts in gap_certs.json, checks interior factors."""
import math, json, os
H=os.path.dirname(os.path.abspath(__file__))
A=10**9; B=A+2_000_000
# odd-only sieve
nodd=(B-A)//2+1
is_p=bytearray(b'\x01')*nodd  # index i -> A+2i if A even... A=1e9 even
def val(i): return A+2*i
lim=int(math.isqrt(B))
sp=[True]*(lim+1); sp[0]=sp[1]=False
for i in range(2,int(math.isqrt(lim))+1):
    if sp[i]:
        for j in range(i*i,lim+1,i): sp[j]=False
for p in [i for i,v in enumerate(sp) if v]:
    if p==2: continue
    start=((A+p-1)//p)*p
    if start%2==0: start+=p if p%2==1 else 0
    # mark odd multiples
    for m in range(start,B+1,2*p):
        is_p[(m-A)//2]=0
primes=[m for m in range(A,B+1) if m%2==1 and is_p[(m-A)//2]]
# A itself even, fine
print("count",len(primes))
assert len(primes)==96417, len(primes)
gaps=[primes[i+1]-primes[i] for i in range(len(primes)-1)]
assert max(gaps)==196
idx=gaps.index(196)
assert (primes[idx],primes[idx+1])==(1001755423,1001755619)
print("maxgap OK",primes[idx],primes[idx+1])
S=set(primes)
quad=[p for p in primes if p+8<=B and p+2 in S and p+6 in S and p+8 in S]
assert len(quad)==33 and quad[0]==1000025261
print("quad OK",len(quad),quad[0])
for off in ([0,4,6,10,12,16],[0,2,6,8,12,18]):
    r=[p for p in primes if p+off[-1]<=B and all(p+o in S for o in off)]
    assert r==[], (off,r[:3])
print("sextuplet-zero OK")
# replay MR certs
D=json.load(open(os.path.join(H,"gap_certs.json")))
for nstr,cert in D["certs"].items():
    n=int(nstr); d=cert["d"]; r=cert["r"]
    assert d*(2**r)==n-1
    for astr,t in cert["bases"].items():
        a=int(astr); x=pow(a,d,n)
        assert x==t["x0"]
        y=x
        for k,v in enumerate(t["squarings"]):
            y=(y*y)%n; assert y==v
        if t["pass"]:
            assert (t["x0"] in (1,n-1)) or ((t["squarings"] and t["squarings"][-1]==n-1))
        else: raise SystemExit("cert fail")
print("MR replay OK",len(D["certs"]),"keys")
# interior factors
for mstr,f in D["gap_interior_factors"].items():
    m=int(mstr); f=int(f)
    assert A < m < 1001755619 and m%f==0 and 1<f<m
assert len(D["gap_interior_factors"])==195
print("interior OK")
print("VERIFY_OK")
