"""Exact finite certificate for symmetry of consecutive hexagonal semigroups."""
from math import gcd
from heapq import heappush, heappop

def H(n):
    return n*(2*n-1)

def factorization(target, u, v):
    for x in range(target//u + 1):
        rem = target-x*u
        if rem % v == 0:
            return (x, rem//v)
    return None

def pair_witnesses(n):
    a,b,c = H(n), H(n+1), H(n+2)
    vals=(a,b,c)
    out=[]
    for i,j,k in ((0,1,2),(0,2,1),(1,2,0)):
        g=gcd(vals[i],vals[j])
        if g>1:
            w=factorization(vals[k],vals[i]//g,vals[j]//g)
            if w is not None:
                out.append((i,j,k,g,*w))
    return out

def frobenius_genus(vals):
    a=min(vals)
    dist=[None]*a
    dist[0]=0
    pq=[(0,0)]
    for_weight=vals[1:]
    while pq:
        d,r=heappop(pq)
        if dist[r]!=d: continue
        for k in for_weight:
            nr=(r+k)%a
            nd=d+k
            if dist[nr] is None or nd<dist[nr]:
                dist[nr]=nd
                heappush(pq,(nd,nr))
    assert all(z is not None for z in dist)
    F=max(dist)-a
    twice_g=(2*sum(dist))//a-(a-1)
    assert (2*sum(dist)) % a==0
    return F,twice_g

chosen=(2,3,6,7,8,18)
assert H(3)==15 and H(5)==45
assert H(5)==3*H(3)
assert gcd(H(3),H(4))==1
pairs={}
for n in range(2,61):
    a,b,c=H(n),H(n+1),H(n+2)
    assert gcd(a,gcd(b,c))==1
    if n>=6: assert c<2*a
    if n==2:
        assert b%a != 0 and c%gcd(a,b) != 0
    if n in (4,5):
        assert b<2*a and c<3*a and c<2*b
        assert c not in (2*a,a+b)
    # The criterion below applies to minimal triples only (n=3 has a redundant generator).
    w=[] if n==3 else pair_witnesses(n)
    verdict=(n==3) or bool(w)
    assert verdict==(n in chosen), (n,verdict,w)
    if verdict: pairs[n]=w
assert set(pairs)==set(chosen)
# Independent numerical-semigroup symmetry test using exact Apéry residues.
oeis_F=[65,377,395,797,1589,6029,3347,4571,6035,10997,10979,12212,
        19409,47246,24023,29003,35357,52112,50603,50411,73049,
        158207,78155,90203,102005,144443,138467,131474,183077]
computed_F=[]
for n in range(2,61):
    vals=(H(n),H(n+1),H(n+2))
    F,two_g=frobenius_genus(vals)
    if n<=30: computed_F.append(F)
    assert (F+1==two_g)==(n in chosen),(n,F,two_g)
assert computed_F==oeis_F
# From n>=61 each potential gcd-pair membership is excluded analytically.
assert 2*61**2-121*61-30>0
assert 2*61**2-113*61-144>0
assert 2*61**2-25*61-18>0
assert 2*61**2-17*61-12>0
assert 30/(4*61+3)<.5
# These polynomials are strictly increasing at and after n=61.
for linear in (121,113,25,17):
    assert 4*61-linear>0
print('EXACT_CERTIFICATE_OK indices='+','.join(map(str,chosen))+' checked=2..60 independent_apery=59 oeis_F=29 universal_cutoff=61')
for n,w in pairs.items():print('SURVIVOR',n,(H(n),H(n+1),H(n+2)),w)
