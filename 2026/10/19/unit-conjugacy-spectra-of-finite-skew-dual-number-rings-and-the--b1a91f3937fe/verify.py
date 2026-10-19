"""Exact finite-field tests of the twisted-dual-number orbit theorem.

Run: python verify.py.  No third-party libraries or external data required.
"""
from collections import Counter
from math import gcd


def make_field(p, modulus):
    n = len(modulus) - 1
    q = p**n
    def vec(x):
        return [(x//(p**i))%p for i in range(n)]
    def pack(v):
        return sum((v[i]%p)*(p**i) for i in range(n))
    def add(x,y):
        return pack([(a+b)%p for a,b in zip(vec(x),vec(y))])
    def neg(x):
        return pack([-a for a in vec(x)])
    def mul(x,y):
        a,b=vec(x),vec(y)
        c=[0]*(2*n-1)
        for i in range(n):
            for j in range(n):
                c[i+j]=(c[i+j]+a[i]*b[j])%p
        for h in range(2*n-2,n-1,-1):
            t=c[h]
            for j in range(n):
                c[h-n+j]=(c[h-n+j]-t*modulus[j])%p
        return pack(c[:n])
    def power(a,k):
        out=1
        while k:
            if k%2:out=mul(out,a)
            a=mul(a,a)
            k//=2
        return out
    assert all(power(x,q)==x for x in range(q))
    return q,add,neg,mul,power


def test(p, polynomial, exponent):
    q,add,neg,mul,power=make_field(p,polynomial)
    f=len(polynomial)-1
    sigma=[power(a,p**exponent) for a in range(q)]
    q0=p**gcd(f,exponent)
    assert sum(sigma[a]==a for a in range(q))==q0
    def prod(x,y):
        a,b=x;c,d=y
        return (mul(a,c),add(mul(a,d),mul(b,sigma[c])))
    points=[(a,b) for a in range(q) for b in range(q)]
    inv={c:power(c,q-2) for c in range(1,q)}
    units=[(c,d) for c in range(1,q) for d in range(q)]
    size_counts=Counter()
    seen=set()
    for x in points:
        if x in seen: continue
        a,b=x
        orb=set()
        for c,d in units:
            v=mul(add(mul(c,b),mul(d,add(sigma[a],neg(a)))),inv[sigma[c]])
            orb.add((a,v))
        for y in orb:
            assert y not in seen
            seen.add(y)
        size_counts[len(orb)]+=1
    assert len(seen)==q*q
    expect=Counter({1:q0})
    expect[(q-1)//(q0-1)]+=q0*(q0-1) if q0>1 else 0
    expect[q]+=q-q0
    expect=Counter({i:v for i,v in expect.items() if v})
    assert size_counts==expect,(p,f,exponent,size_counts,expect)
    comm_pairs=sum(prod(x,y)==prod(y,x) for x in points for y in points)
    assert comm_pairs == q**3+q0*q0*q*(q-1),(p,f,exponent,comm_pairs)
    radical=[(0,b) for b in range(q)]
    assert sum(prod((a,b),(c,d))==(0,0) for a,b in radical for c,d in radical)==q*q
    assert all(prod((a,b),(c,d))[0]!=0 for a in range(1,q) for b in range(q) for c in range(1,q) for d in range(q))
    print('PASS', 'q=',q,'Frob exponent=',exponent,'fixed field=',q0,'unit-orbits=',dict(sorted(size_counts.items())),'commuting pairs=',comm_pairs)

if __name__=='__main__':
    for p,mod in [(2,[1,1,1]),(2,[1,1,0,1]),(3,[1,0,1]),(2,[1,1,0,0,1]),(5,[2,0,1])]:
        f=len(mod)-1
        for k in range(1,f):test(p,mod,k)
    print('VERIFY_OK')
