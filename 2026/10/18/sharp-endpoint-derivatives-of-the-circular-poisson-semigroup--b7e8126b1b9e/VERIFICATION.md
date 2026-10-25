---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

The circular Poisson kernel P=sinh(t)/(cosh(t)-cos θ) and convolution norm identity reduce endpoint L1/L∞ norms to normalized absolute derivative kernel integrals. Direct differentiation yields first two sign-change roots 1/h and (-h+sqrt(h²+8))/2, with primitive identities and stated finite-time laws. Third derivative cubic endpoint signs locate two-to-one interior root transition at cosh t=2. For arbitrary j, periodization ≤ real-line derivative L1 norm, strict cancellation at each positive t and equality in the t→0 limit. Cauchy scaling and an exact total-variation primitive give trig sum; gamma asymptotics give j^-1/2 coefficient. Independently integrated j=1,...,6 Cauchy formula against exact sum (differences ≤9e-9); SymPy t²N2 expansion confirms zero t² term and relative -t⁴/135. Finite checks do not establish all-order strictness, whose analytic argument is supplied.

## originality

PASS

Best-of-knowledge PASS. Xiong–Xu–Yin 2018 arXiv full HTML §III.3 develops Poisson/heat semigroup derivatives and Besov characterizations using equivalence signs, not exact L1/L∞ jth derivative operator norm constants or cubic root-transition. Real-line Cauchy derivative homogeneity is classical, but strict periodic periodization plus explicit all-j sums and exact t^4 correction are separate results. Published Resultary searches for circular Poisson derivatives located no matching dominating formula; this absence is not exhaustive priority proof.

## value

PASS

Sharp all-order analyticity constants of a canonical semigroup, strict non-attainment, two distinct finite-size correction orders, and a nodal transition of the third derivative are natural analytic quantities that sharpen qualitative operator-semigroup estimates and test periodization cancellation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
