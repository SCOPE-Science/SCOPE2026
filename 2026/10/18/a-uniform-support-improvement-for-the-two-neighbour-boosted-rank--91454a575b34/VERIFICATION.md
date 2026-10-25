---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

Every threshold set S_l of ranks >=l has cardinalities n,n-1,...,1 and the statistic numerator decomposes exactly as sum_l Phi_n(S_l), including the x_(n-1)+2x_n self-neighbour terms. For binary words, the three displayed potentials for (s,t)=(3/2,1/2),(5/2,1),(4,2) have all 8 transition slacks and all 4 endpoint slacks nonnegative; direct independent Fraction check confirmed 24 transitions. Integer rounding yields Phi>=H_n(k) and sum >=L_n. The piecewise affine integrated envelope is 13/24, yielding xi limit -3/8 with the exact (n+1)(2n+3/2) denominator. n>=2; ranks distinct; lower bound only, not attainability. Finite permutation/enumeration checks are corroborative, not proof.

## originality

PASS

Best-of-knowledge noncoverage is supported by the statement-level comparisons below; this is not a proof of absolute bibliographic novelty.

## value

PASS

A genuine uniform combinatorial improvement to the guaranteed support of a widely used nonparametric dependence statistic, by asymptotic 1/8 in the fixed M=2 case. The boundary-aware finite-state potentials are structurally informative; no unsupported claim that the actual minimum is -3/8.

The dated certificate retains the supplied scientific assessment, sources and limitations.
