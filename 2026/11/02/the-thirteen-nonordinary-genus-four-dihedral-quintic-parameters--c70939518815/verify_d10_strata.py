"""Reproduce the finite-field polynomial certificates for the genus-four quintic pencil.

Pure Python 3, no third-party dependencies. The printed checks are finite
corroboration of the separately stated symbolic proof for all primes.
"""
from math import comb


def trim(a, p):
    a = [x % p for x in a]
    while len(a) > 1 and not a[-1]:
        a.pop()
    return a


def add(a, b, p):
    return trim([(a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))], p)


def mul(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return trim(out, p)


def scale(a, c, p):
    return trim([c*x for x in a], p)


def derivative(a, p):
    return trim([i*a[i] for i in range(1, len(a))] or [0], p)


def rem(a, b, p):
    a = trim(a[:], p)
    b = trim(b, p)
    assert b != [0]
    while a != [0] and len(a) >= len(b):
        shift = len(a) - len(b)
        multiplier = a[-1] * pow(b[-1], -1, p) % p
        for i, z in enumerate(b):
            a[i + shift] = (a[i + shift] - multiplier*z) % p
        a = trim(a, p)
    return a


def gcd(a, b, p):
    while b != [0]:
        a, b = b, rem(a, b, p)
    return scale(a, pow(a[-1], -1, p), p)


def P(e, d, p):
    return trim([comb(e, j)*comb(e, d-j) for j in range(d+1)], p)


def evaluate(a, x, p):
    ans = 0
    for c in a[::-1]:
        ans = (ans*x + c) % p
    return ans


def ode_residue(a, e, d, p):
    # z(1-z)y'' + (e-d+1+(e+d-1)z)y' - ed y
    deriv = derivative(a, p)
    second = derivative(deriv, p)
    return add(add(mul([0,1,-1], second, p),
                   mul([e-d+1,e+d-1], deriv, p), p),
               scale(a, -e*d, p), p)


def coefficient_from_two_factors(e, k, p):
    # Coefficient of z^k in (z-1)^e (z-lambda)^e.
    ans = [0] * (e+1)
    for i in range(max(0,k-e),min(e,k)+1):
        j = k-i
        ans[e-j] += (-1)**(2*e-k)*comb(e,i)*comb(e,j)
    return trim(ans,p)


def prime_list(limit):
    return [p for p in range(7,limit+1)
            if all(p % t for t in range(2,int(p**0.5)+1))]


def verify_general_examples():
    for p in prime_list(151):
        e = (p-1)//2
        rs = [(3*p)%5,(4*p)%5]
        ds = [p-1-(i*p-r)//5 for i,r in zip([3,4],rs)]
        assert all(0<d<=e for d in ds)
        assert sum(ds) == (3*(p-1))//5
        for d in ds:
            A = P(e,d,p)
            assert len(A)==d+1
            assert evaluate(A,0,p)!=0 and evaluate(A,1,p)!=0
            assert ode_residue(A,e,d,p)==[0]
            assert gcd(A,derivative(A,p),p)==[1]
        # All four sparse matrix entries and the reciprocity pairs.
        slots = [(i,j,(p*i-j)//5) for i in range(1,5)
                 for j in range(1,5) if (p*i-j)%5==0]
        assert len(slots)==4
        for i,j,k in slots:
            ci = coefficient_from_two_factors(e,k,p)
            partner = coefficient_from_two_factors(e,2*e-k,p)
            if k>e:
                assert ci==scale(P(e,2*e-k,p),(-1)**(2*e-(2*e-k)),p)
            # coefficient reciprocity: c_low = lambda^(e-d)c_high
            d=min(k,2*e-k)
            low=coefficient_from_two_factors(e,d,p)
            high=coefficient_from_two_factors(e,2*e-d,p)
            assert low==mul([0]*(e-d)+[1],high,p)
    print('prime examples through 151: coefficient, ODE, squarefree, reciprocity PASS')


def verify_23():
    p=23;e=11
    A=P(e,9,p)
    B=P(e,4,p)
    Fa=[[1,1],[1,3,1],[-10,4,1],[1,7,1],[-7,-5,1]]
    Fb=[[6,8,1],[4,9,1]]
    aa=[1]
    for f in Fa:
        aa=mul(aa,f,p)
    bb=[1]
    for f in Fb:
        bb=mul(bb,f,p)
    assert A==scale(aa,9,p) and B==scale(bb,8,p)
    assert gcd(A,B,p)==[1]
    for f in Fa[1:]+Fb:
        assert all(evaluate(f,z,p) != 0 for z in range(p))
    assert all(evaluate(f,0,p)!=0 and evaluate(f,1,p)!=0
               for f in Fa+Fb)
    assert len(A)-1+len(B)-1==13
    # Coarse isomorphism coordinate t=lambda+lambda^{-1}.
    # Reciprocal quadratic pairs descend via lambda^2(t^2+a t+b).
    assert mul(Fa[2],Fa[4],p)==[1,-1,9,-1,1] or mul(Fa[2],Fa[4],p)==trim([1,-1,9,-1,1],p)
    assert mul(Fb[0],Fb[1],p)==trim([1,-6,13,-6,1],p)
    # All degree-two t-factors irreducible; three linear factors distinct.
    Rt=[[2,1],[3,1],[7,1],[7,-1,1],[11,-6,1]]
    for f in Rt[3:]:
        assert all(evaluate(f,z,p)!=0 for z in range(p))
    R=[1]
    for f in Rt:
        R=mul(R,f,p)
    assert len(R)==8 and gcd(R,derivative(R,p),p)==[1]
    # All degree 9/4 roots lie in F_23^2, with one rational lambda=-1.
    assert [x for x in range(p) if evaluate(A,x,p)*evaluate(B,x,p)%p==0]==[22]
    print('characteristic 23: 13 marked strata, 7 moduli classes, six irreducible quadratics PASS')
    print('coarse moduli polynomial coefficients, constant first:',R)


if __name__=='__main__':
    verify_general_examples()
    verify_23()
    print('GENUS4_QUINTIC_D10_STRATA_PASS')
