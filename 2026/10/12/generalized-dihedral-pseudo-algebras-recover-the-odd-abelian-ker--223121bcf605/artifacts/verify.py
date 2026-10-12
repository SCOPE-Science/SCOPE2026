from itertools import product
from collections import Counter
from math import gcd, lcm, prod

def element_order(x,mods):
    out=1
    for a,n in zip(x,mods):
        if a:
            out=lcm(out,n//gcd(a,n))
    return out

def order_spectrum(mods):
    C=Counter()
    for x in product(*[range(n) for n in mods]):
        C[element_order(x,mods)]+=1
    return C

def pseudo_algebra(mods):
    assert all(n%2==1 for n in mods)
    spectrum=order_spectrum(mods)
    P={1:1,2:1}
    for d,N in spectrum.items():
        if d==1:
            continue
        assert d%2==1
        assert N%2==0
        P[d]=N//2
    return P,spectrum

def prime_factors(n):
    out=[]
    p=2
    while p*p<=n:
        if n%p==0:
            out.append(p)
            while n%p==0:
                n//=p
        p+=1
    if n>1:
        out.append(n)
    return out

def reconstruct_p(P,p):
    e=0
    while p**(e+1) in P:
        e+=1
    if e==0:
        return []
    s=[0]
    for k in range(1,e+1):
        M=1+2*sum(P[p**j] for j in range(1,k+1))
        z=M
        log=0
        while z>1 and z%p==0:
            z//=p
            log+=1
        assert z==1
        s.append(log)
    r=[0]+[s[k]-s[k-1] for k in range(1,e+1)]
    factors=[]
    for k in range(1,e+1):
        next_r=r[k+1] if k<e else 0
        factors += [p**k]*(r[k]-next_r)
    return factors

def reconstruct(P):
    primes=set()
    for d in P:
        if d%2==1:
            primes.update(prime_factors(d))
    factors=[]
    for p in sorted(primes):
        factors += reconstruct_p(P,p)
    return sorted(factors)

examples=[
    [9],
    [3,3],
    [9,5],
    [3,9],
    [5,5],
    [3,3,5],
    [9,25],
    [3,9,5],
]

pseudos={}
for mods in examples:
    P,S=pseudo_algebra(mods)
    size=prod(mods)

    assert P[1]==1 and P[2]==1
    for d,N in S.items():
        if d>1:
            assert P[d]==N//2

    nonlinear=sum(v for d,v in P.items() if d not in (1,2))
    assert nonlinear==(size-1)//2
    assert 2 + 4*nonlinear == 2*size

    rec=reconstruct(P)
    assert rec==sorted(mods),(mods,rec,P)

    pseudos[tuple(mods)]=P
    print({
        "kernel":mods,
        "order":size,
        "order_spectrum":dict(sorted(S.items())),
        "pseudo_algebra":dict(sorted(P.items())),
        "reconstructed":rec,
    })

assert prod([9,5])==prod([3,3,5])==45
assert pseudos[(9,5)] != pseudos[(3,3,5)]

print("VERIFY_OK")
