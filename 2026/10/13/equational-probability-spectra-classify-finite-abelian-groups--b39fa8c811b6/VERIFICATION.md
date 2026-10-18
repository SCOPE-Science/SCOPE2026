---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

In an abelian group G of exponent m, a term equation is a linear word with integer coefficients c_i. Its image G^k->G is dG for d=gcd(m,c_1,...,c_k) by Bezout, so its satisfaction probability is 1/|dG|=|G[d]|/|G|; every divisor d|m occurs as dx=0, and multiplication-only terms realize the same equation spectrum. Under primary cyclic decomposition, |G[p^j]|=p^{f_p(j)} with increments f_p(j)-f_p(j-1)=number of elementary cyclic factors of length >=j, a positive weakly decreasing sequence. The normalized spectrum separates prime-power exponents and the independent CRT combinations, so differences reconstruct each conjugate partition and conversely characterize realizable rational sets. The identity group N=1 is handled separately. Independent exact test reconstructed sample distinct abelian groups and subgroup-kernel sizes, not relied on as unrestricted proof.

## originality

PASS

Cardó arXiv:2603.19487 introduces equational probability spectra, proves general direct-product INCLUSION, cyclic prime-power examples, and classifies minimal-spectrum semigroups; arXiv:2604.08446 studies general product/primality questions. Neither article supplies full inverse realizability of all finite abelian spectra or group isomorphism rigidity. A primary-profile inverse theorem may be implicitly classical under torsion-size distribution; this is retained as residual risk. Resultary semantic searches returned unrelated Fourier spectra and finite-group probabilistic work.

## value

PASS

An exact realizability criterion and inverse isomorphism classification for a natural newly studied probability spectrum is a complete theorem across all finite abelian groups, substantially stronger than a few numerical examples or cyclic cases. It explains why product-spectrum inclusions cannot simply be reversed for common-prime factors.

The dated certificate retains the supplied scientific assessment, sources and limitations.
