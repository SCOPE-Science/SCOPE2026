from itertools import product

OEIS=[2,4,8,16,32,58,108,190,336,560,948,1574,2568,4116]
SYM=[2,4,8,16,32,52,100,160,260,424,684,1036,1640,2552]

def symmetric(z):
    return z[::-1] in z+z

def has_period(w,m):
    return all(w[i]==w[i-m] for i in range(m,len(w)))

def pal_periodicity(w):
    return any(has_period(w,m) and symmetric(w[:m]) for m in range(1,len(w)+1))

def census(n):
    pp=sym=0
    for b in product('01', repeat=n):
        w=''.join(b)
        s=symmetric(w)
        p=pal_periodicity(w)
        if s:
            sym+=1
            assert p
        if p:
            pp+=1
    return pp,sym

for n in range(1,15):
    pp,sym=census(n)
    assert pp==OEIS[n-1], (n,pp,OEIS[n-1])
    assert sym==SYM[n-1], (n,sym,SYM[n-1])
    # Direct reflection union equals reversal-as-rotation.
    for b in product('01', repeat=n):
        w=''.join(b)
        refl=any(all(w[i]==w[(h-i)%n] for i in range(n)) for h in range(n))
        assert refl==symmetric(w)
print('VERIFY_OK')
