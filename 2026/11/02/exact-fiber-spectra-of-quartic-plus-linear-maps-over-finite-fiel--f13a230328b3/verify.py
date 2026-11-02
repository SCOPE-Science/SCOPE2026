"""Independent finite-field fiber enumeration for quartic-plus-linear maps."""
from collections import Counter
from math import gcd


def predicted(q):
    assert q % 2 and q % 3 == 2
    return {5: ((3*q-7)//8, (q+4)//3, (q-1)//4, 0, (q-5)//24),
            11:((3*q-1)//8, (q+1)//3, (q-3)//4, 1, (q-11)//24),
            17:((3*q-3)//8, (q+1)//3, (q-1)//4, 1, (q-17)//24),
            23:((3*q-5)//8, (q+4)//3, (q-3)//4, 0, (q+1)//24)}[q % 24]


def sample_prime(p):
    for a in range(1,p):
        sizes = Counter((pow(x,4,p) + a*x)%p for x in range(p))
        got = tuple(sum(n==k for n in sizes.values()) if k else p-len(sizes) for k in range(5))
        assert got==predicted(p),(p,a,got,predicted(p))


def irreducible_cubic(p):
    # Pick x^3 + c*x + d with no root; over a field this is irreducible.
    for c in range(p):
        for d in range(1,p):
            if all((x*x*x+c*x+d)%p for x in range(p)):
                return c,d
    raise AssertionError(p)


def sample_cubic(p, exhaustive_coefficients=True):
    c,d=irreducible_cubic(p)
    q=p**3
    def mul(u,v):
        a,b,e=(u%p,(u//p)%p,u//(p*p))
        f,g,h=(v%p,(v//p)%p,v//(p*p))
        w0=a*f; w1=a*g+b*f; w2=a*h+b*g+e*f
        w3=b*h+e*g; w4=e*h
        # X^3=-cX-d, X^4=-cX^2-dX
        w0=(w0-d*w3)%p
        w1=(w1-c*w3-d*w4)%p
        w2=(w2-c*w4)%p
        return w0+p*w1+p*p*w2
    fourth=[mul(mul(x,x),mul(x,x)) for x in range(q)]
    aa=range(1,q) if exhaustive_coefficients else [1,2,p+1,p*p+p+2]
    for a in aa:
        sizes=Counter()
        for x in range(q):
            # Field addition is componentwise, not encoded integer addition.
            ax=mul(a,x); w=fourth[x]
            z=(w%p+ax%p)%p + p*((w//p%p+ax//p%p)%p)+p*p*((w//(p*p)+ax//(p*p))%p)
            sizes[z]+=1
        got=tuple(sum(n==k for n in sizes.values()) if k else q-len(sizes) for k in range(5))
        assert got==predicted(q),(p,q,a,got,predicted(q))
    return (p,q,c,d,len(list(aa)))

if __name__ == '__main__':
    primes=[5,11,17,23,29,41,47,53,59,71,83,89,101,113,137]
    for p in primes:sample_prime(p)
    ext=[sample_cubic(5,True),sample_cubic(11,False)]
    print('VERIFY_OK primes=',len(primes),'cubic_extensions=',ext,'histogram=PASS')
