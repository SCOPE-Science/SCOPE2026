---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The restriction axiom is pointwise on N_0^n; every count vector has strictly positive probability for positive finite Poisson intensities, so the a.s. bound is pointwise. On the all-positive vector the nonempty stopping set must be a singleton {j}. Comparing configurations differing only at j shows j belongs to every output; a fixed positive value at j forces immediate singleton output. The zero fiber is again a stopping-set map on n-1 coordinates, so induction yields one uniquely determined partial permutation stopped at first positive count. Conversely each such prefix map satisfies restriction; one-atom-at-a-time exploration yields it pointwise. The cardinality is sum_{r=0}^n n!/(n-r)!; budget two admits the explicit parity-dependent second query.

## originality

PASS

The finite-atomic one-occupied-LOCATION rigidity, unique partial-permutation parametrization, cardinality and exact pointwise realization are not supplied by the inspected prior diffuse at-most-one-POINT theorem. This is a best-of-knowledge distinction, not an assertion that no classical finite decision-tree normal form exists.

## value

PASS

The sharp budget-one rigidity and unique normal form determine all allowable observation rules, not merely a numerical toy case; A_n supplies an exact classification for every finite atomic space. The parity counterexample demonstrates that allowing two occupied sites fundamentally changes adaptability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
