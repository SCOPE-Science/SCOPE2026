import math

def isprime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    d = 3
    while d*d <= n:
        if n % d == 0: return False
        d += 2
    return True

def Pplus(n):
    m=n; mx=1; d=2
    while d*d <= m:
        while m%d==0:
            mx=d; m//=d
        d = 3 if d==2 else d+2
    if m>1: mx=max(mx,m)
    return mx

def rho(k):
    p=2
    while True:
        if isprime(p) and k%p: return p
        p+=1

def next_prime_after_block(p,k):
    assert isprime(p) and k%2==0
    ell=0
    x=p
    while isprime(x):
        ell += 1
        x = p + ell*k
    return ell, Pplus(x), x

# Critical local lemma, on a broad finite regression range.
for k in range(2, 402, 2):
    r=rho(k)
    B=max(r, k*(r-1)/2)
    for p in range(3, 5001, 2):
        if isprime(p) and p>B:
            ell,q,c=next_prime_after_block(p,k)
            assert ell <= r-1, (k,p,r,ell)
            assert c%2==1 and not isprime(c)
            assert q <= c//3
            assert q < p, (k,p,r,ell,q)

# Special corollaries.
for k in range(2,1000,2):
    r=rho(k)
    if k%3:
        assert r==3 and max(r,k*(r-1)//2) == (3 if k==2 else k)
    if k%6==0 and k%5:
        assert r==5 and max(r,k*(r-1)//2) == 2*k

# Observed-cycle regression: starts in a large box, not used for exhaustiveness.
def phi(x,k):
    return x+k if isprime(x) else Pplus(x)

def cyc(start,k):
    seen={}; seq=[]; x=start
    for _ in range(20000):
        if x in seen: return seq[seen[x]:]
        seen[x]=len(seq); seq.append(x); x=phi(x,k)
    raise RuntimeError('orbit regression did not close')

for k in range(2,102,2):
    B=max(rho(k), k*(rho(k)-1)/2)
    cycles=set()
    for start in range(2,1001):
        c=cyc(start,k)
        rots=[tuple(c[i:]+c[:i]) for i in range(len(c))]
        cycles.add(min(rots))
    for c in cycles:
        ps=[x for x in c if isprime(x)]
        assert ps and min(ps)<=B, (k,B,c)

print('VERIFY_OK')
print('even_k_local_range=2..400')
print('prime_regression_max=5000')
print('cycle_start_box=k<=100,start<=1000')
