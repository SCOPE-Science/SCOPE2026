"""Finite exact-arithmetic cross-check of a ternary g-adic two-summand census.
Run: python3 verify.py (Python standard library only).
This is a finite cross-check; the all-k theorem is proved in RESULT.md.
"""

def digits(n, base=9):
    if n == 0:
        return [0]
    ds=[]
    while n:
        ds.append(n % base)
        n //= base
    return ds


def C(n):
    if n <= 0:
        return 0
    ds=digits(n)
    if any(d>4 for d in ds):
        return 0
    factors=(1,2,3,2,1)
    product=1
    for d in ds:
        product*=factors[d]
    in_same=all(d<=2 for d in ds)
    diagonal=all(d%2==0 for d in ds)
    v=product-2*int(in_same)+int(diagonal)
    assert v>=0 and v%2==0
    return v//2


def R(n):
    ds=digits(n)
    mixed=any(d%3 for d in ds) and any(d//3 for d in ds)
    return C(n)+(C(n//3) if n%3==0 else 0)+int(mixed)


def is_member(n):
    if n<=0:
        return False
    mask=0
    while n:
        if n%3:
            mask |= 1
        n//=3
        if n%3:
            mask |= 2
        n//=3
    return mask in (1,2)


def enumerated(maximum):
    a=[n for n in range(1,maximum) if is_member(n)]
    rr=[0]*maximum
    for i,x in enumerate(a):
        for y in a[i:]:
            z=x+y
            if z>=maximum: break
            rr[z]+=1
    return rr


def formula(k):
    return 8*5**(k-1) - 2**(2*k-1) - 5*k

for k in range(1,5):
    bound=9**k
    exhaustive=enumerated(bound)
    for n,expected in enumerate(exhaustive):
        assert R(n)==expected,(k,n,expected,R(n))
    count=sum(r>1 for r in exhaustive)
    assert count==formula(k),(k,count,formula(k))
    assert [i for i,r in enumerate(exhaustive) if r==0]==[0,1]
    print(f'EXHAUSTIVE k={k} range={bound} ambiguous={count} verified')
for k in (5,6):
    bound=9**k
    count=sum(R(n)>1 for n in range(bound))
    assert count==formula(k),(k,count,formula(k))
    print(f'DIGIT_FORMULA k={k} range={bound} ambiguous={count} verified')
print('CERTIFICATE_OK')
