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

For Cr_n with chosen index sets P,Q, define d_i=1_P(i)-1_Q(i). Literal closed-neighborhood tests reduce to q+d_i>=k and p-d_i>=k for every i; the only one-sided exceptions are k=1, S=A/B. Otherwise p,q>=k and p=k forces P⊆Q, q=k forces Q⊆P. Binomial enumeration partitions interior and exact boundaries with the diagonal counted once, giving stated bivariate F_{n,k} and D_{×k}, minimum 2k and binom(n,k) minima. Independent direct neighborhood set enumeration for n=3..7 checked all k and every bivariate coefficient; proof is all n>=3.

## originality

PASS

Best-of-knowledge: Chang et al. supply definition and bounds/complexity, not this all-k bivariate crown set classification on inspected material. Published Resultary restrained-crown and complete-multipartite variants use different predicates or graph classes. A full copy of Chang et al. was not retrieved (publisher landing/abstract inspected; HAL access denied), preserved as bibliographic risk.

## value

PASS

Exact all-set side-profile counting of a natural matching-deletion family describes redundancy thresholds and inclusion constraints, giving minimum and every cardinality coefficient for arbitrary n,k. This is motivated finite graph-family structure, not recomputation of a known scalar table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
