"""Independent finite checks of a unitary proper-divisor classification.

Usage: python3 verify.py
Uses only the standard library. The theorem itself requires a symbolic proof.
"""
from itertools import product

EXCEPTIONAL = {60, 84, 90, 120, 168, 240}


def prime_list(bound):
    out = []
    for p in range(2, bound + 1):
        if all(p % d for d in range(2, int(p ** 0.5) + 1)):
            out.append(p)
    return out


def actual_half(a, b, c, q):
    A, B, C = 2 ** a, 3 ** b, q ** c
    # Exactly the proper unitary divisors; the identity holds for distinct primes.
    D = [1, A, B, A * B, C, A * C, B * C]
    h, r = divmod(sum(D), 2)
    if r:
        return False
    # Exhaustive subset-sum search, independent of the symbolic coefficient bound.
    return any(sum(D[i] for i in range(7) if mask >> i & 1) == h
               for mask in range(1, (1 << 7) - 1))


def predicted(a, b, c, q):
    if a == b == 1:
        return True
    return 2 ** a * 3 ** b * q ** c in EXCEPTIONAL


def sign_half(a, b, c, q):
    A, B, C = 2 ** a, 3 ** b, q ** c
    U = [1, A, B, A * B]
    V = [1, A, B]
    return any(sum(s * x for s, x in zip(ss, U)) + C *
               sum(s * x for s, x in zip(tt, V)) == 0
               for ss in product((-1, 1), repeat=4)
               for tt in product((-1, 1), repeat=3))


def coefficient_candidates(A, B, least=5):
    U = [1, A, B, A * B]
    V = [1, A, B]
    NN = {sum(s*x for s,x in zip(ss,U)) for ss in product((-1,1), repeat=4)}
    DD = {sum(s*x for s,x in zip(tt,V)) for tt in product((-1,1), repeat=3)}
    infinite = (0 in NN and 0 in DD)
    out = {-n//d for n in NN for d in DD if d != 0 and (-n) % d == 0 and -n//d >= least}
    return infinite, sorted(out)


if __name__ == '__main__':
    primes = [p for p in prime_list(150) if p > 3]
    total = 0
    for a in range(1, 13):
        for b in range(1, 13):
            if min(a, b) != 1:
                continue
            for q in primes:
                for c in range(1, 4):
                    assert actual_half(a,b,c,q) == predicted(a,b,c,q), (a,b,c,q)
                    assert sign_half(a,b,c,q) == actual_half(a,b,c,q), (a,b,c,q)
                    total += 1
    print('finite_boundary_cases_checked=', total, 'PASS')
    for a in range(1,6):
        inf, cs = coefficient_candidates(2**a, 3)
        print('a=',a,'b=1','unbounded=',inf,'admissible_C_ge_5=',cs)
    for b in range(1,5):
        inf, cs = coefficient_candidates(2,3**b)
        print('a=1','b=',b,'unbounded=',inf,'admissible_C_ge_5=',cs)
    for n in sorted(EXCEPTIONAL):
        ok = False
        for a in range(1,10):
            for b in range(1,10):
                for q in primes:
                    for c in range(1,4):
                        if 2**a * 3**b * q**c == n and min(a,b)==1:
                            assert actual_half(a,b,c,q)
                            ok=True
        assert ok, n
    print('exceptional_membership=6_PASS')
    for n in [84,120,168,240]:
        t=n; ex=[]
        for p in prime_list(100):
            if t % p==0:
                power=1
                while t%p==0:
                    power*=p; t//=p
                ex.append(power)
        assert t==1 and len(ex)==3
        sigstar=1
        for pp in ex: sigstar*=pp+1
        assert sigstar<2*n
    print('four_half_only_not_unitary_full=PASS')
    print('VERIFY_OK; finite checks supplement the unrestricted coefficient proof')
