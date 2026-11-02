"""Exact independent cycle check for a binary finite-field trinomial family.
Run with Python 3; no third-party packages are required.
"""
from collections import Counter


def polygcd(a,b):
    while b:
        r=a
        while r and r.bit_length()>=b.bit_length():
            r^=b << (r.bit_length()-b.bit_length())
        a,b=b,r
    return a


def polyrem(a,f):
    d=f.bit_length()-1
    while a.bit_length()>d:
        a^=f<<(a.bit_length()-d-1)
    return a


def irreducible(f,d):
    x=2
    u=x
    for j in range(1,d+1):
        u=polyrem(poly_mul(u,u),f)
        if j<=d//2 and d%j==0 and polygcd(u^x,f)!=1:
            return False
    return u==x


def poly_mul(a,b):
    z=0
    while b:
        if b&1:z^=a
        a<<=1;b>>=1
    return z


def field(n):
    f=next(f for f in range((1<<n)+1,1<<(n+1),2) if irreducible(f,n))
    top=1<<n
    def mul(a,b):
        r=0
        while b:
            if b&1:r^=a
            b>>=1;a<<=1
            if a&top:a^=f
        return r
    def power(a,j):
        r=1
        while j:
            if j&1:r=mul(r,a)
            a=mul(a,a);j>>=1
        return r
    return f,mul,power


def cycle_counts(mapping):
    seen=bytearray(len(mapping)); out=Counter()
    for seed in range(len(mapping)):
        if seen[seed]:continue
        z=seed; k=0
        while not seen[z]:
            seen[z]=1; k+=1;z=mapping[z]
        assert z==seed, 'not a permutation'
        out[k]+=1
    return out


def verify():
    total_maps=total_points=total_t=0
    for m in (2,3,4,5,6):
        q=1<<m;n=2*m; size=q*q
        irr,mul,power=field(n)
        sub=[z for z in range(size) if power(z,q)==z]
        assert len(sub)==q
        def trace(a):
            z=0
            for j in range(m):z^=power(a,1<<j)
            assert z in (0,1)
            return z
        def inv(a):
            assert a!=0
            return power(a,size-2)
        def order(a):
            assert a in sub and a!=0
            x=1
            for k in range(1,q):
                x=mul(x,a)
                if x==1:return k
            raise AssertionError('missing order')
        zset=[z for z in sub if z and trace(inv(z))==1]
        assert len(zset)==q//2
        kloosterman=sum(1 if trace(w^inv(w))==0 else -1 for w in sub if w)
        admitted=[t for t in sub if t and trace(inv(t))==0]
        assert len(admitted)==q//2-1
        predicted_two=(q-1-kloosterman)//4
        assert 4*predicted_two==q-1-kloosterman
        observed_two=0
        for t in admitted:
            fvalues=[0]*size
            for x in range(1,size):
                fvalues[x]=x ^ mul(t,power(x,q)) ^ power(x,2*q-1)
            actual=cycle_counts(fvalues)
            predicted=Counter({1:1})
            predicted[order(t)]+=(q-1)//order(t)
            for z in zset:
                s=t^z
                assert s!=0
                L=2*order(s)
                predicted[L]+=(q-1)//order(s)
            assert actual==predicted,(q,hex(t),actual,predicted)
            if actual.get(2,0):
                assert actual[2]==q-1
                observed_two+=1
            total_maps+=1;total_points+=size
        assert observed_two==predicted_two,(q,observed_two,predicted_two,kloosterman)
        total_t+=len(admitted)
        print(f'PASS q={q} modulus={hex(irr)} admissible={len(admitted)} two_cycle_t={observed_two} K={kloosterman}')
    print(f'VERIFY_OK field_orders=5 coefficients={total_t} full_maps={total_maps} states={total_points}')

if __name__=='__main__':verify()
