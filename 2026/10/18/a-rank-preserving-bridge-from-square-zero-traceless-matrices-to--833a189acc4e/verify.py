"""Direct finite checks of a rank-preserving correspondence over chain rings.

Run: python3 verify.py
No external libraries are required.
"""
from collections import Counter
from itertools import product


def expected(q, m):
    out = {0: 1}
    for r in range(1, m + 1):
        count = (q*q-1) * q**(2*r-2)
        if r % 2 == 0:
            count += (q-1) * q**(3*r//2-1)
        for ell in range(r//2 + 1, r):
            count += (q*q-1)*(q-1)*q**(ell+r-3)
        out[r] = count
    return out


def count_residue_integers(p, m):
    n = p**m
    out = Counter()
    for a, b, c in product(range(n), repeat=3):
        if (a*a+b*c) % n:
            continue
        values = {( (a*u+b*v)%n, (c*u-a*v)%n)
                  for u in range(n) for v in range(n)}
        sz = len(values)
        r = 0
        while sz > 1:
            assert sz % p == 0
            sz //= p
            r += 1
        out[r] += 1
    return dict(out)


def gf_mult(a,b):
    s=0
    for i in range(2):
        if (b>>i)&1:s ^= a<<i
    if s&8:s ^= 0b1011
    if s&4:s ^= 0b111
    return s&3


def gf_add(a,b):return a^b


def count_equal_char(q,m,add,mul):
    els=list(product(range(q),repeat=m))
    def plus(a,b):return tuple(add(x,y) for x,y in zip(a,b))
    def neg(a):
        return next(b for b in els if plus(a,b)==(0,)*m)
    def times(a,b):
        return tuple(fold([mul(a[i],b[k-i]) for i in range(k+1)]) for k in range(m))
    def fold(items):
        x=0
        for z in items:x=add(x,z)
        return x
    zero=(0,)*m
    out=Counter()
    for a,b,c in product(els,repeat=3):
        if plus(times(a,a),times(b,c))!=zero:continue
        minus_a=neg(a)
        values={
            (plus(times(a,u),times(b,v)),plus(times(c,u),times(minus_a,v)))
            for u,v in product(els,repeat=2)
        }
        sz=len(values);r=0
        while sz>1:
            assert sz%q==0
            sz//=q;r+=1
        out[r]+=1
    return dict(out)


def check():
    for p,m in [(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3)]:
        got=count_residue_integers(p,m)
        want=expected(p,m)
        assert got==want,(p,m,got,want)
        print('Zmod',p**m,'rank multiplicities',got)
    for p,m in [(2,1),(2,2),(2,3),(3,1),(3,2)]:
        got=count_equal_char(p,m,lambda a,b:(a+b)%p,lambda a,b:(a*b)%p)
        want=expected(p,m)
        assert got==want,(p,m,got,want)
        print('poly',p,m,'rank multiplicities',got)
    got=count_equal_char(4,2,gf_add,gf_mult)
    want=expected(4,2)
    assert got==want,(4,2,got,want)
    print('GF4 polynomial length2',got)
    # Rational image-zeta coefficients obey the same initial terms and recurrence.
    for q in (2,3,4,5,7):
        coeff=expected(q,9)
        for r in range(1,10):
            lhs=coeff[r]-(q*q*coeff[r-1] if r>=1 else 0)
            if r>=2:lhs-=q**3*coeff[r-2]
            if r>=3:lhs+=q**5*coeff[r-3]
            rhs={0:1,1:-1,2:-q*q,3:q*q}.get(r,0)
            assert lhs==rhs,(q,r,lhs,rhs)
    print('VERIFY_OK_TRACEZERO_SQUAREZERO_ZETA_BRIDGE')

if __name__=='__main__':check()
