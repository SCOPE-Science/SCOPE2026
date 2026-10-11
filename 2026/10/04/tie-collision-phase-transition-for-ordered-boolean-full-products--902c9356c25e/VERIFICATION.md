---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

Cameron--Gewurz--Merola's product-action formalism gives all-tuple orbit count F_n^d and inverse Stirling transform for distinct tuples; weak orders give the same model directly. For d>=3, a prescribed pair is tied in all coordinates with probability (F_{n-1}/F_n)^d, so the expected number of common-tie pairs is asymptotic to (log 2)^d n^(2-d)/2. Any two distinct pair events, overlapping or disjoint, collapse exactly two degrees of freedom and have probability (F_{n-2}/F_n)^d; summing O(n^4) such intersections is o(n^(2-d)). Bonferroni therefore gives the stated first deficit. A fresh exact Stirling replay through n=80 produced scaled deficits approaching the constants for d=3,4,5. The d=2 constant is the prior incidence-matrix asymptotic.

## originality

PASS

The exact product-action orbit formulas are prior work and are not claimed as new. Cameron--Gewurz--Merola's full preprint explicitly discusses A, A×A, A×A×A,... and the weak-order/Stirling machinery; Cameron--Prellberg--Stark supply the d=2 incidence-matrix asymptotic. Neither inspected source states the d>=3 rare-common-tie asymptotic or phase-transition law. Resultary searches found no equivalent higher-dimensional first-deficit theorem.

## value

PASS

The theorem gives the sharp first collision scale across the full fixed-dimensional family and identifies d=2 as the unique critical dimension. The invariant is natural in oligomorphic product actions and weak-order intersections, and the explicit d>=3 constant is useful for comparing asymptotic orbit geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
