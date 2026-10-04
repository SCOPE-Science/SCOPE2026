from math import gcd

OEIS_PREFIX = [500,864,1944,2000,2592,3456,5000,10125,10368,12348,12500,16875,19652,19773,30375,31104,32000,33275,37044,40500,49392,50000,52488,55296,61731,64827,67500,69984,78608,80000,81000,83349,84375,93312,108000,111132,124416,128000,135000]

def factor(n):
    out=[]
    d=2
    while d*d<=n:
        if n%d==0:
            e=0
            while n%d==0:
                n//=d;e+=1
            out.append((d,e))
        d=3 if d==2 else d+2
    if n>1: out.append((n,1))
    return out

def is_prime(n):
    if n<2:return False
    if n%2==0:return n==2
    d=3
    while d*d<=n:
        if n%d==0:return False
        d+=2
    return True

def phi(n):
    z=n
    for p,_ in factor(n): z=z//p*(p-1)
    return z

def achilles(n):
    fs=factor(n)
    if not fs:return False
    exps=[e for _,e in fs]
    g=0
    for e in exps:g=gcd(g,e)
    return min(exps)>=2 and g==1

def strong(n):
    return achilles(n) and achilles(phi(n))

def theorem(p,a,b):
    if not is_prime(p) or p==2:return False
    if a<2 or b<3 or gcd(a,b)!=1:return False
    u=p-1;t=0
    while u%2==0:
        u//=2;t+=1
    cs=[]
    for q,e in factor(u):
        if e<2:return False
        cs.append(e)
    exps=[a+t-1,b-1]+cs
    g=0
    for e in exps:g=gcd(g,e)
    return g==1

pair_checks=0
for p in range(3,200,2):
    if not is_prime(p):continue
    for a in range(2,19):
        for b in range(2,19):
            n=(2**a)*(p**b)
            got=strong(n)
            want=theorem(p,a,b)
            pair_checks+=1
            assert got==want,(p,a,b,n,got,want,factor(phi(n)))

# Every two-prime-support term in the displayed OEIS prefix must satisfy the theorem.
oeis_support_terms=0
for n in OEIS_PREFIX:
    fs=factor(n)
    if len(fs)==2 and fs[0][0]==2:
        p,a,b=None,None,None
        (q1,e1),(q2,e2)=fs
        if q1==2:
            a=e1;p=q2;b=e2
        else:
            a=e2;p=q1;b=e1
        assert theorem(p,a,b), (n,fs)
        assert strong(n)
        oeis_support_terms+=1

# Conversely, compare all theorem-positive support terms <=135000 to direct definition.
generated=[]
for p in range(3,200,2):
    if not is_prime(p):continue
    for a in range(2,30):
        for b in range(3,20):
            n=(2**a)*(p**b)
            if n>135000:continue
            if theorem(p,a,b):
                assert strong(n)
                generated.append(n)
generated=sorted(set(generated))
# They must be included in the displayed strong-Achilles prefix.
assert set(generated).issubset(set(OEIS_PREFIX)), (set(generated)-set(OEIS_PREFIX))

# Approximate C_*=product over primes (1-2/l^2), via primes <= 100000.
prod=1.0
for ell in range(2,100001):
    if is_prime(ell):prod*=1.0-2.0/(ell*ell)
assert 0.322 < prod < 0.324,prod

print(f'VERIFY_OK pair_checks={pair_checks} oeis_support_terms={oeis_support_terms} generated_le_135000={len(generated)} universal_product_approx={prod:.12f}')
