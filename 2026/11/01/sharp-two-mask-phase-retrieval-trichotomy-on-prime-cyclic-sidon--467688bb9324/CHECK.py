"""Exact finite checks for quadratic-mask sparse Fourier phase retrieval.

Run: python3 CHECK.py. Python standard library only. This is supplementary
finite testing; the all-prime theorem rests on the algebraic proof.
"""
from itertools import combinations
from random import Random


def sidon_pairs(S, p):
    pairs = {}
    for a in S:
        for b in S:
            if a != b:
                d = (a-b) % p
                if d in pairs:
                    return None
                pairs[d] = (a, b)
    return pairs


def mul(z, w):
    return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])


def conj(z):
    return (z[0], -z[1])


def autocorr(symbols, p, power):
    """Return exact cyclic autocorrelation in basis of roots of unity.

    A nonzero term at index d is represented as (a,b, exponent)
    for Gaussian-integer coefficient a+ib times omega^exponent.
    The Sidon support guarantees at most one such term per d.
    """
    S = tuple(symbols)
    out = {0: [(sum(a*a+b*b for a,b in symbols.values()), 0, 0)]}
    for a in S:
        for b in S:
            if a == b:
                continue
            d = (a-b) % p
            z = mul(symbols[a], conj(symbols[b]))
            phase = (power*(a*a-b*b)) % p
            out.setdefault(d, []).append((*z, phase))
    return out


def check_case(S,p,z,r1=0,r2=1):
    pairs = sidon_pairs(S,p)
    assert pairs is not None
    assert (r2-r1) % p != 0
    A = autocorr(z,p,r1)
    B = autocorr(z,p,r2)
    assert set(A) == set(B) == set(pairs) | {0}
    recovered_pairs = {}
    for d,(j,k) in pairs.items():
        assert len(A[d]) == len(B[d]) == 1
        a0,b0,e0 = A[d][0]
        a1,b1,e1 = B[d][0]
        assert (a0,b0) == (a1,b1)
        assert a0*a0+b0*b0 > 0
        s = ((e1-e0)*pow((r2-r1)*d % p,-1,p)) % p
        assert e0 == r1*(j*j-k*k) % p
        rec_j = ((s+d)*pow(2,-1,p)) % p
        rec_k = ((s-d)*pow(2,-1,p)) % p
        assert (rec_j,rec_k) == (j,k)
        recovered_pairs[d] = (rec_j,rec_k)
    assert {n for e in recovered_pairs.values() for n in e} == set(S)
    if len(S) >=3:
        j,i,k = S[:3]
        ji = mul(z[j],conj(z[i]))
        ik = mul(z[i],conj(z[k]))
        jk = mul(z[j],conj(z[k]))
        lhs = mul(ji,ik)
        mag2 = sum(t*t for t in z[i])
        assert lhs == (mag2*jk[0], mag2*jk[1])
    if len(S)==2:
        j,k=S
        aj2=sum(t*t for t in z[j]); bk2=sum(t*t for t in z[k])
        assert A[0][0][0] == aj2+bk2
        swapped={j:(z[j][0]*bk2, z[j][1]*bk2), k:(z[k][0]*aj2,z[k][1]*aj2)}
        # After common positive rescaling 1/sqrt(aj2*bk2), the
        # exchanged array has same pair product and total energy.
        lhs = mul(swapped[j], conj(swapped[k]))
        rhs = mul(z[j],conj(z[k]))
        assert lhs == (rhs[0]*aj2*bk2,rhs[1]*aj2*bk2)
        assert sum(sum(t*t for t in swapped[q]) for q in S) == (aj2+bk2)*aj2*bk2


def run():
    rng=Random(260428)
    checks=0
    counts={}
    for p in (3,5,7,11,13,17,19):
        ncase=0
        for k in range(2,min(6,p)):
            for S in combinations(range(p),k):
                if sidon_pairs(S,p) is None:
                    continue
                z={a:(rng.randrange(-7,8),rng.randrange(-7,8)) for a in S}
                for a in S:
                    while z[a]==(0,0):z[a]=(rng.randrange(-7,8),rng.randrange(-7,8))
                check_case(S,p,z)
                checks+=1
                if p<=13:
                    for r1,r2 in ((1,2),(2,5)):
                        if (r2-r1)%p:
                            check_case(S,p,z,r1,r2)
                            checks+=1
                ncase+=1
        counts[p]=ncase
    assert all(counts[p]>0 for p in counts)
    print('CHECK_OK', 'configurations='+str(checks),'per_prime='+str(counts))

if __name__=='__main__':run()
