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

The r+2 column maps are exactly r identities, one capped successor g, and a zero reset. An m-digit column is nonconstant iff there is no reset and no more than d successors; choosing j successor positions gives precisely the claimed binomial D_m, including m=0. Constant columns are c0 through c_{m-1} before saturation and c0 through c_{d+1} afterward; injectivity of distinct column functions on the full-alphabet fixed sequence proves K_m and 2d+3 kernel size. Power g^{d+1} is constant, so on unequal-letter pairs discrepancy operator equals rI plus nilpotent upper-step transitions, spectral radius r. Primitive aperiodic height-one conditions checked, allowing the published Gröger–Krawczyk Theorems A/B to yield ac and null/tame equivalence. Independent explicit enumeration of 84 r,d,m cases (r=1..3,d=1..4,m=0..6) matched both D_m and K_m, not treated as proof of the all-parameter theorem.

## originality

PASS

Gröger--Krawczyk give general asymptotic growth order Theta(m^ds lambda^m), numerical spectral rule and an earlier linear example, but their identified Theorems A/B/Proposition 5.6 do not present the explicit two-parameter saturated-successor/reset family or its exact finite-depth binomial and kernel formulas. Asymptotic growth type alone does not imply the exact coefficients. The inherited tame/null/amorphic classification is explicitly credited, not claimed new.

## value

PASS

The construction realizes every positive polynomial discrepancy exponent alongside every positive integer base within a single primitive aperiodic automatic family, while giving exact all-depth counts and a finite kernel. This is a motivated parametric realization and a useful separation of amorphic complexity from polynomial discrepancy degree, not just a generic restatement of spectral-radius theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
