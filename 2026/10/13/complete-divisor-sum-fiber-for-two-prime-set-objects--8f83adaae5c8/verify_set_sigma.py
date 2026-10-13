from math import isqrt

def is_prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    d = 3
    while d*d <= n:
        if n % d == 0: return False
        d += 2
    return True

def sigma_prime_power(p,e):
    return (p**(e+1)-1)//(p-1)

def in_Set_N(x,A,p):
    if x <= 0: return False
    a=b=0
    while x%2==0:
        x//=2; a+=1
    while x%p==0:
        x//=p; b+=1
    return x==1 and 1<=a<=A and 1<=b<=A

def actual_fiber(A,p):
    out=[]
    for a in range(1,A+1):
        for b in range(1,A+1):
            m=(2**a)*(p**b)
            sm=(2**(a+1)-1)*sigma_prime_power(p,b)
            if in_Set_N(sm,A,p): out.append((a,b,m,sm))
    return out

def predicted_fiber(A,p):
    out=[]
    for s in range(2,A+1):
        if p==2**s-1 and is_prime(p):
            m=2**(s-1)*p
            out.append((s-1,1,m,2**s*p))
    return out

primes=[p for p in range(3,2001,2) if is_prime(p)]
cases=0
for A in range(1,13):
    for p in primes:
        cases += 1
        got=actual_fiber(A,p)
        exp=predicted_fiber(A,p)
        if got != exp:
            raise SystemExit(f'FAIL A={A} p={p} got={got} exp={exp}')
print(f'VERIFY_OK cases={cases} A_max=12 p_max=2000 primes={len(primes)}')
print('sample_nonempty=',[(A,p,actual_fiber(A,p)) for A in range(1,8) for p in primes if actual_fiber(A,p)][:8])
