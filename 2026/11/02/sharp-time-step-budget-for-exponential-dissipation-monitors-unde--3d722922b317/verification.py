"""Reproducibility checks for the exact exponential-monitor mesh threshold.

The proof is analytic. Tests independently compare cumulative-integral meshes,
step-ratio ordering, threshold decisions, asymptotic scaling, and boundary cases.
Requires mpmath; prints deterministic counts; no network access.
"""
import random
import mpmath as mp

mp.mp.dps = 65
rng = random.Random(271828182)
R0 = 1 + mp.sqrt(2)

def H(x):
    return mp.log1p(1 / x)

def ratio(x):
    return H(x) / H(x + 1)

def root(R):
    a = mp.mpf('0.000000000001')
    b = mp.mpf(1)
    while ratio(b) > R:
        b *= 2
    for _ in range(210):
        m = (a + b) / 2
        if ratio(m) > R:
            a = m
        else:
            b = m
    return (a + b) / 2

def nodes_from_integral(lam, p, T, N):
    z = 1 - mp.exp(-p * lam * T)
    return [-mp.log1p(-mp.mpf(j) * z / N) / (p * lam)
            for j in range(N+1)]

def nodes_from_formula(lam, p, T, N):
    Dpminus = mp.expm1(p * lam * T)
    u = mp.mpf(N) / Dpminus
    h = [H(u + N - j - 1) / (lam * p) for j in range(N)]
    nodes = [mp.mpf(0)]
    for v in h:
        nodes.append(nodes[-1]+v)
    return nodes, h, u

def close(a,b,tol=mp.mpf('1e-48')):
    return abs(a-b) < tol * (1+abs(a)+abs(b))

count = 0
u = root(R0)
assert close(ratio(u),R0)
assert abs(u-mp.mpf('0.3588231634265831584937248220685824')) < mp.mpf('1e-30')
count += 2

for _ in range(130):
    lam=mp.mpf(str(rng.uniform(.1,4)))
    p=mp.mpf(str(rng.uniform(.08,1)))
    T=mp.mpf(str(rng.uniform(.05,12)))
    N=rng.randrange(2,43)
    a=nodes_from_integral(lam,p,T,N)
    b,h,U=nodes_from_formula(lam,p,T,N)
    assert all(close(x,y) for x,y in zip(a,b))
    assert close(b[-1],T)
    r=[h[j]/h[j-1] for j in range(1,N)]
    assert all(r[j+1]>r[j] for j in range(N-2))
    assert close(r[-1],ratio(U))
    # Compare the derived sharp integer cutoff to direct construction.
    Dpminus=mp.expm1(p*lam*T)
    exact_min=max(2,int(mp.floor(u*Dpminus))+1)
    for size in set((2,N,max(2,exact_min-1),exact_min,exact_min+1)):
        rr=ratio(mp.mpf(size)/Dpminus)
        assert (rr<R0)==(size>=exact_min)
        count+=1
    count+=4

for _ in range(50):
    R=mp.mpf(str(rng.uniform(1.05,10)))
    U=root(R)
    assert close(ratio(U),R)
    assert ratio(U/2)>R and ratio(2*U)<R
    count+=3

for D in (10,100,1000,1000000):
    for p in (mp.mpf(1),mp.mpf('0.5')):
        N=max(2,int(mp.floor(u*(mp.mpf(D)**p-1)))+1)
        prev=N-1
        assert N>=2
        assert ratio(mp.mpf(N)/(mp.mpf(D)**p-1))<R0
        if prev>=2:
            assert ratio(mp.mpf(prev)/(mp.mpf(D)**p-1))>=R0
        count+=2

# Direct integral equidistribution for randomly chosen intervals.
for _ in range(40):
    lam=mp.mpf(str(rng.uniform(.3,3)))
    p=mp.mpf(str(rng.uniform(.1,1)))
    T=mp.mpf(str(rng.uniform(.3,7)))
    N=rng.randint(2,20)
    a=nodes_from_integral(lam,p,T,N)
    masses=[(mp.exp(-lam*p*a[j])-mp.exp(-lam*p*a[j+1]))/(lam*p) for j in range(N)]
    assert all(close(masses[0],z) for z in masses)
    count+=1

print('PASS:',count,'independent high-precision comparisons')
print('u_(1+sqrt(2)) =',mp.nstr(u,55))
for D in [100,1000000]:
    for p in [mp.mpf(1),mp.mpf('0.5')]:
        print('D =',D,'p =',p,'minimum N =', max(2,int(mp.floor(u*(mp.mpf(D)**p-1)))+1))
