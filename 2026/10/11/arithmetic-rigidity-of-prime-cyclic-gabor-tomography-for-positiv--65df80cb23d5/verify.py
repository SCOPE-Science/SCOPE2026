"""Reproducible small-instance checks for prime cyclic Gabor operator spans.
Public-domain numerical check; proof is algebraic and does not depend on it.
"""
import itertools
import numpy as np


def autocorr(g, p):
    z = np.exp(2j * np.pi / p)
    return np.array([[sum(g[x] * g[(x-a) % p] * z ** (b*x) for x in range(p))
                      for b in range(p)] for a in range(p)], complex)


def measurement(g, p):
    z = np.exp(2j * np.pi / p)
    rows = []
    for a in range(p):
        for b in range(p):
            v = np.array([g[(x-a) % p] * z ** (b*x) for x in range(p)], complex)
            rows.append(np.outer(v, v.conjugate()).reshape(-1))
    return np.array(rows)


def predicted(g, p):
    S = {i for i, v in enumerate(g) if v}
    if len(S) < p:
        D = {(x-y) % p for x in S for y in S}
        return p * len(D), {(a,b) for a in range(p) for b in range(p) if a not in D}
    if len(set(g)) == 1:
        return p, {(a,b) for a in range(p) for b in range(1,p)}
    return p*p, set()


def check(g):
    p = len(g)
    target, zeros = predicted(g,p)
    A = autocorr(g,p)
    seen = {(a,b) for a in range(p) for b in range(p) if abs(A[a,b]) < 1.e-7}
    assert zeros == seen, (p,g,'zeros',zeros ^ seen)
    M = measurement(g,p)
    sv = np.linalg.svd(M, compute_uv=False)
    rank = int(np.sum(sv > 1.e-7))
    assert rank == target, (p,g,'rank',rank,target,sv)
    # Weyl-covariant intensity analysis singular values equal sqrt(p)*|ambiguity|.
    pred_sv = np.sort((np.sqrt(p)*np.abs(A).flatten()))
    assert np.allclose(np.sort(sv), pred_sv, atol=2.e-7,rtol=2.e-7), (p,g,'singular values')
    return 1


def main():
    total = 0
    for p in (3,5,7):
        for mask in range(1, 1<<p):
            S = [x for x in range(p) if (mask>>x)&1]
            g = [((x*3+5)%4+1) if x in S else 0 for x in range(p)]
            total += check(g)
            if len(S) != p: # additionally check genuinely nonconstant positive rational weights
                g = [((x*5+3)%6+1)/((x%3)+1) if x in S else 0 for x in range(p)]
                total += check(g)
        total += check([1]*p)
    rng = np.random.default_rng(1203)
    for p in (11,):
        for _ in range(18):
            g = [int(rng.integers(1,8)) if rng.random() < .65 else 0 for _ in range(p)]
            if not any(g):g[0]=1
            total += check(g)
    print('VERIFY_OK exact_support_prediction_and_independent_lifting_SVD_cases='+str(total),'fields=[3,5,7,11]','zeros=PASS','rank=PASS','singular_values=PASS')

if __name__=='__main__': main()
