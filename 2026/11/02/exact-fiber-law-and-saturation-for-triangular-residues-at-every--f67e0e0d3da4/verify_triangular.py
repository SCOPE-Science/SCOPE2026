"""Independent finite checks for the triangular-residue fiber theorem."""
from collections import Counter
from math import isqrt

def odd_part(m):
    while m % 2 == 0 and m > 0:
        m //= 2
    return m

def odd_factor(n):
    d = 3
    while d * d <= n:
        if n % d == 0:
            k=0
            while n % d == 0:
                n//=d;k+=1
            yield d,k
        d += 2
    if n > 1:yield n,1

def local_square_roots(p,e,D):
    pe=p**e
    z=D%pe
    if z==0:return p**(e//2)
    v=0
    while z%p==0:
        z//=p;v+=1
    if v&1:return 0
    if pow(z%p,(p-1)//2,p)!=1:return 0
    return 2*p**(v//2)

def predicted(m,t):
    n=1
    for p,e in odd_factor(odd_part(m)):
        n*=local_square_roots(p,e,1+8*t)
    return n

for m in range(1,751):
    f=Counter((n*(n+1)//2)%m for n in range(m))
    for t in range(m):
        expect=predicted(m,t)
        assert f[t]==expect,(m,t,f[t],expect)

for p in (3,5,7,11,13,17):
    for e in range(1,6):
        pe=p**e
        if pe>3000:continue
        f=Counter((n*(n+1)//2)%pe for n in range(pe))
        for t in range(pe):
            assert f[t]==local_square_roots(p,e,1+8*t),(p,e,t)

for q in (1,3,5,7,9,15,21,25,45):
    for a in range(1,8):
        m=(2**a)*q
        if m>3500:continue
        f=Counter((n*(n+1)//2)%m for n in range(m))
        fq=Counter((n*(n+1)//2)%q for n in range(q))
        assert all(f[t]==fq[t%q] for t in range(m)), (q,a)
print('VERIFY_OK moduli=750 all_fibers=exact primepowers=checked doubling_lift=checked')
