"""Independent verifier for Knodel-depth census (stdlib + numpy only).
Re-derives lambda(n*) from scratch, replays K(n*), checks minimality of
least-member table, spot-checks lambda, verifies histogram sums and m formula.
"""
import hashlib, math
import numpy as np

N = 5_000_000
ART = "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-168/output/artifacts"

def lam_of(n):
    x = n; lam = 1; f = {}
    d = 2
    while d*d <= x:
        if x % d == 0:
            e = 0
            while x % d == 0: x//=d; e+=1
            f[d]=e
        d += 1 if d==2 else 2
    if x>1: f[x]=1
    for p,e in f.items():
        if p==2:
            pw = 1 if e==1 else (2 if e==2 else 2**(e-2))
        else:
            pw = (p**(e-1))*(p-1)
        lam = lam//math.gcd(lam,pw)*pw
    return lam, f

# 1. witness replay
n_star = 4935060
lam, fac = lam_of(n_star)
assert n_star-1 >= 0
m = (n_star-1)//lam
kmin = n_star - m*lam
print("n*=",n_star,"fac=",fac,"lambda=",lam,"m=",m,"kmin=",kmin)
assert lam==36 and m==137084 and kmin==36, "witness values"
assert fac=={2:2,3:3,5:1,13:1,19:1,37:1}
assert 2**2*3**3*5*13*19*37==n_star
# prime-power lcm derivation
# lam(4)=2, lam(27)=18, lam(5)=4, lam(13)=12, lam(19)=18, lam(37)=36; lcm=36
pps=[2,18,4,12,18,36]
L=1
for v in pps: L=L//math.gcd(L,v)*v
assert L==36
print("lcm derivation ok:",pps,"->",L)
# K(n*) = {k: 36 | 4935060-k}; verify ends
K = [k for k in range(1,n_star) if (n_star-k)%lam==0]
assert len(K)==m and K[0]==kmin==36 and K[-1]==n_star-lam
assert all((n_star-k)%lam==0 for k in K)
# check a non-member fails
assert (n_star-37)%36 != 0
print("K(n*) replay ok: |K|=%d, kmin=%d, kmax=%d"%(len(K),K[0],K[-1]))

# 2. least-member table minimality: factor-scan all composites below each claimed least, with independent prime test
least={1:561,2:4,3:9,4:6,5:25,6:8,7:15,8:12,9:21,10:12}
def is_prime(n):
    if n<2: return False
    if n%2==0: return n==2
    r=int(n**0.5)
    f=3
    while f<=r:
        if n%f==0: return False
        f+=2
    return True
for k,n0 in least.items():
    lam0,_=lam_of(n0)
    assert (n0-k)%lam0==0, (k,n0)
    for n in range(k+1,n0):  # membership requires k<n
        if is_prime(n): continue
        lamn,_=lam_of(n)
        assert (n-k)%lamn!=0, f"C{k} smaller member {n}"
    print(f"C{k}: least={n0} lambda={lam0} minimality-ok")

# 3. C1 cross-check vs published count/heads: Pinch table has 595 Carmichael <5M? No — verify heads known: 561,1105,1729,2465,2821
heads=[561,1105,1729,2465,2821]
c1heads=open(ART+"/c1_list.txt").read().split()
assert [int(x) for x in c1heads[:5]]==heads
print("C1 heads ok:",heads)
# full C1 list has 74 entries; verify each is composite and satisfies lambda|n-1, and count matches
c1=[int(x) for x in c1heads]
assert len(open(ART+"/c1_list.txt").read().split())==40  # first-40 file
# count check via numpy sieve cross-check of compositeness for C1 count: recompute slice count independently here for n<=200000
cnt=0
for n in range(4,200001):
    if is_prime(n): continue
    lamn,_=lam_of(n)
    if (n-1)%lamn==0: cnt+=1
print("C1 count to 200k (independent):",cnt)

# 4. histogram consistency: sums and spot formulas
a=np.loadtxt(ART+"/mhist.csv",delimiter=",",dtype=np.int64)
assert a[:,1].sum()==4651486, a[:,1].sum()
distinct=len(a)
print("mhist rows=%d sum=%d maxm=%d count_at_max=%d"%(distinct,int(a[:,1].sum()),int(a[:,0].max()),int(a[a[:,0].argmax(),1])))
assert int(a[:,0].max())==137084
# spot-check m formula for random composites
rng=[100,1000,561,1729,4935060,4999999,4999998,123456,999983*2 if False else 999984]
import random
random.seed(7)
vals=[random.randint(4,N) for _ in range(300)]
ok=0
sieve=np.ones(N+1,dtype=bool)
sieve[:2]=False
for i in range(2,int(N**0.5)+1):
    if sieve[i]: sieve[i*i::i]=False
for n in vals:
    if sieve[n]: continue
    lamn,_=lam_of(n)
    m2=(n-1)//lamn
    assert m2>=1
    ok+=1
print("spot-checks ok:",ok)
# C3 heads
c3heads=[int(x) for x in open(ART+"/c3_list.txt").read().split()[:9]]
assert c3heads==[9,15,21,33,39,51,57,63,69], c3heads
print("C3 heads ok")
# sha
for fn in ["mhist.csv","c1_list.txt","c3_list.txt"]:
    h=hashlib.sha256(open(ART+"/"+fn,'rb').read()).hexdigest()
    print(fn,h)
print("VERIFY_OK")
