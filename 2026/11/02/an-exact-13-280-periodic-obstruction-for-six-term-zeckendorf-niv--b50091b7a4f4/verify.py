"""Exact periodic obstruction for six-term Zeckendorf-Niven progressions."""
from math import lcm
P=1680
primes=(2,3,5,7)
periods={2:3,3:8,5:20,7:16}
assert lcm(*(lcm(2*p,periods[p]) for p in primes))==P

def fibmod(k,mod):
    a,b=0,1
    for _ in range(k):a,b=b,(a+b)%mod
    return a

fib={p:[fibmod(k,p) for k in range(P*3+1)] for p in primes}
for p in primes:
    for k in range(P):assert fib[p][k+P]==fib[p][k]

def fits(k,a,prime_max):
    if a==5 and k%2==0:return False
    # Every surviving shape has even shifts of digit weight two.
    if k%3==0:return False
    if a==3:
        if fib[3][k]!=2:return False
        denoms=[(k-1)//2,(k-1)//2+1];targets=[3,1]
    else:
        denoms=[(k-3)//2,(k-3)//2+1,(k-3)//2+2];targets=[5,3,1]
    return all(d%p != 0 or fib[p][k] == t%p
               for p in primes if p<=prime_max
               for d,t in zip(denoms,targets))

C={}
for cutoff in (3,5,7):
    left={a:tuple(k%P for k in range(P,P*2) if fits(k,a,cutoff)) for a in (3,5)}
    for a in (3,5):
        assert all(fits(k,a,cutoff)==fits(k+P,a,cutoff) for k in range(P,P*2))
    C[cutoff]=left
    print('cutoff',cutoff,'a3',len(left[3]),'a5',len(left[5]),'union',len(set(left[3])|set(left[5])))
assert [(len(set(C[b][3])|set(C[b][5]))) for b in (3,5,7)]==[210,112,78]
assert len(C[7][3])==33 and len(C[7][5])==45
assert not(set(C[7][3]) & set(C[7][5]))
print('VERIFY_OK period=1680 counts=210,112,78 final_density=13/280 local_sieve_only=YES')
