from math import isqrt

def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))

def unitary(n):
    factors = []
    x=n
    for p in range(2, isqrt(x)+1):
        if x%p==0:
            e=0
            while x%p==0: x//=p; e+=1
            factors.append((p,e))
    if x>1: factors.append((x,1))
    ans=1
    for p,e in factors: ans*=1+p**e
    return ans

def exponential(n):
    factors = []
    x=n
    for p in range(2, isqrt(x)+1):
        if x%p==0:
            e=0
            while x%p==0: x//=p; e+=1
            factors.append((p,e))
    if x>1: factors.append((x,1))
    ans=1
    for p,e in factors: ans*=sum(p**d for d in range(1,e+1) if e%d==0)
    return ans

expected={2:-1116,5:2601,7:7889,11:25209,13:37241}
for q,delta in expected.items():
    assert 281*q*q-728*q-784==delta
    if q!=5: assert delta<0 or isqrt(delta)**2!=delta
assert 9*7*7-75*7+84==0
n=27*7*7*5
assert n==6615 and unitary(n)==exponential(n)==8400
solutions=[]
for r in range(2,100001):
    if not is_prime(r) or r==3:continue
    d=r*r+15*r-14
    x=14*(r*r+1)
    if x%d==0:
        q=x//d
        if q!=3 and q!=r and is_prime(q):solutions.append((r,q))
assert solutions==[(7,5)],solutions
print('PASS: exact discriminants, factorization identity, equality and finite cross-check')
