"""Independent exact-integer checks for the binomial-convolution parity theorem.

The published normalization has a theorem-based proof; these finite checks are
illustrative only, not a proof of the infinite result.
"""
from math import comb


def pop(x):
    return x.bit_count()


def nu2(x):
    assert x > 0
    return (x & -x).bit_length() - 1


def F(k):
    return comb(6*k, 3*k)*comb(3*k,k)


def exact(n):
    z=[F(k) for k in range(n+1)]
    num=sum(z[k]*z[n-k] for k in range(n+1))
    den=(2*n-1)*comb(3*n,n)
    q,r=divmod(num,den)
    assert r==0, (n,r)
    return q


def main():
    for n in range(1,513):
        t=pop(3*n)
        s=pop(n)
        an=exact(n)
        assert nu2(an)>=t+1,('bound',n)
        if s==1:
            assert nu2(an)==3,('power2',n,an)
            assert an%16==8
        else:
            assert nu2(an)>=t+2,('nonpower',n,an)
            assert an%16==0
        for k in range(n+1):
            c=pop(k)+pop(n-k)-s
            assert c>=0
            expected=t+2*c
            # independent direct factorial-valuation computation
            def vfact(m):
                v=0
                while m:
                    m//=2
                    v+=m
                return v
            def vchoose(a,b):
                return vfact(a)-vfact(b)-vfact(a-b)
            actual=(vchoose(6*k,3*k)+vchoose(3*k,k)
                    +vchoose(6*(n-k),3*(n-k))+vchoose(3*(n-k),n-k)
                    -vchoose(3*n,n))
            assert actual==expected,('valuation',n,k)
        assert (an//(2**(t+1)))%2 == (2**(s-1))%2
    print('VERIFY_OK: n=1..512; exact integer normalizations, valuation formulas, mod-16 dichotomy, and parity counts')


if __name__=='__main__':
    main()
