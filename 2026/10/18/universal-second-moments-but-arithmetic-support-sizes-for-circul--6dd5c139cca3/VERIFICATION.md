---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Centering changes each score only by a deterministic term: shifting all values by c adds c times the regular lag degree times the sample sum, plus |E_d|c². The score itself is not shift-invariant, but its covariance is. For the centered sample the same-edge, incident-edge and disjoint-edge moments are respectively (Q²−R)/(n(n−1)), (2R−Q²)/(n(n−1)(n−2)), and (3Q²−6R)/(n(n−1)(n−2)(n−3)). A degree-two class has n identical and 2n distinct incident ordered comparisons with itself; two ordinary classes are disjoint and have 4n incident pairs, so diagonal minus ordinary off-diagonal is Λ. The perfect matching has half the ordinary cross-pair counts. At n=4 there is no actual ordinary off-diagonal, but its displayed algebraic expression B still satisfies V−B=Λ and D=B/2 by counting the matching. The deterministic sum gives zero rows; contrasts within ordinary lags have eigenvalue Λ, and the even contrast against the matching gives nΛ/[2(n−1)]. Four distinct positions give Λ=n/4 times the product-of-squared-differences mean. This vanishes exactly when two disjoint unequal pairs are impossible, i.e. at least n−1 observations coincide. Correlation is defined only for Λ>0 and where two ordinary lags exist. For algebraically independent data, equal values imply equal formal edge coefficients. Each marginal score fiber is a coset of the position graph automorphism group, a wreath product of g copies of the cycle dihedral group with S_g, or of g copies of the two-element group with S_g for a matching. The joint fiber is exactly a coset of the distance-one dihedral group, since it preserves all distances. These give the stated support and uniform atom masses, including 20,160 versus 280 at n=9.

## originality

PASS

Exact individual moments and cross-covariances are already accessible from general quadratic-form permutation moments by polarization. The contribution supported as distinct is the circular all-lag structural simplification combined with the exact arithmetic law of equiprobable marginal and joint score values. The latter needs identification of quadratic coefficients and the component geometry, not just moment information. The closest inspected cyclic or permutation covariance records use different statistics.

## value

PASS

The result identifies a finite-sample inferential distinction that covariance cannot reveal: with equal ordinary lag variances, the arithmetic of the lag controls exact attainable permutation significance. The n=9 example changes the attainable upper-tail resolution by a factor of 72. The joint count and uniform masses quantify the analogous simultaneous randomization support rather than only giving a collision bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
