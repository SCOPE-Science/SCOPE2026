#!/usr/bin/env python3
def T(a):
    return a*(a+1)//2

for u in range(-100, 101):
    assert T(1+3*u) == 1 + 9*T(u)

for k in range(1, 9):
    m=2**k
    vals={T(a)%m for a in range(m)}
    assert len(vals)==m

for k in range(1, 6):
    m=3**k
    tri={T(a)%m for a in range(2*m)}
    prod={x*y % m for x in tri for y in tri}
    sq={c*c % m for c in range(m)}
    good=set()
    for n in range(m):
        if any((z+n)%m in sq for z in prod):
            good.add(n)
    bad=[n for n in range(m) if n not in good]
    if k==1:
        assert bad==[]
    else:
        assert bad==[n for n in range(m) if n%9 in (2,5)]

for p in (5,7,11,13,17,19):
    for n in range(p):
        found=False
        for t in range(p):
            if t in (0,p-1):
                continue
            d=t*(t+1)%p
            if d==(16*n)%p:
                continue
            r=(16*n-d)%p
            for x in range(p):
                for y in range(p):
                    if (x*x-d*y*y-r)%p==0 and (x%p or y%p):
                        assert (2*x)%p or (-2*d*y)%p
                        found=True
                        break
                if found:
                    break
            if found:
                break
        assert found, (p,n)

print("VERIFY_OK 2adic_complete=1..8 3adic_patterns=1..5 odd_seed_primes=5,7,11,13,17,19 identity=exact")
