"""Independent finite checks of the stated semiprime classification (finite evidence only)."""
from math import isqrt

def prime(n):
    if n<2:return False
    for d in range(2,isqrt(n)+1):
        if n%d==0:return False
    return True

def direct(a):
    primes=[p for p in range(a+1,4*a-2) if prime(p)]
    return {(p,q) for p in primes for q in primes if p>q and (p*q-a)%(p-a)==0 and (p*q-a)%(q-a)==0}

def param(a):
    c=a-1
    ans=set()
    for u in range(1,2*c+2):
        for v in range(u+1,2*c+2):
            d=u*v-1
            if (v+1)*c%d or (u+1)*c%d:continue
            p=a+(v+1)*c//d
            q=a+(u+1)*c//d
            if p>q>a and prime(p) and prime(q):ans.add((p,q))
    return ans

checks=0; witnesses=0
for a in range(2,101):
    d=direct(a); t=param(a)
    assert d==t,(a,d^t)
    for p,q in d:
        assert p<= (a+5*(a-1)/7 if a%2==0 else 4*a-3)
        assert (p*q-a)%(p-a)==0 and (p*q-a)%(q-a)==0
        witnesses+=1
    checks+=1
assert (41,31) in direct(11) and 41==4*11-3
assert (13,11) in direct(8) and 7*(13-8)==5*(8-1)
assert (37,31) in direct(22) and 7*(37-22)==5*(22-1)
print(f'VERIFY_OK parameters={checks} parameterized_pairs={witnesses} sharp_odd=11 sharp_even=8 independent_enumeration=PASS finite_only=YES')
