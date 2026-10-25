---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

PASS: In two strict linear orders, a two-move EF game is determined by whether a chosen point admits witnesses in each of four strict quadrants, hence the set of realized four-bit point masks is a complete rank-two sentence invariant. Direct/skew sums update masks with right-above/left-below or right-below/left-above bits respectively. Starting at singleton mask, independently computed the complete finite closure and minimum construction length by dynamic programming: 226 signatures with lengths histogram (1,2,6,19,46,60,50,29,11,2) for n=1..10; closure of all 226×226 pairs under both operations checked. Separately parsed the actual certificate blob and checked every witness, derivation, 102,152 ordered composition transitions and optimality inequality; zero discrepancies. Two extremal permutations [8,9,10,5,6,7,4,1,2,3] and [3,2,1,6,5,4,7,10,9,8] attain minimal length 10. Quadrant signature 37928 of [2,5,3,1,4] is absent. A finite closure certificate is exhaustive because generative composition is proved, not because n≤10 was sampled.

## originality

PASS

Best-of-knowledge claim-versus-prior assessment with direct source comparisons; see four named checks, source inspections and retained risks.

## value

PASS

PASS: Rank-two is the first nontrivial first-order observational depth for permutations as two orders; separable permutations are a canonical recursively composed class. A complete 226-state quotient, sharp shortest-representative bound and concrete nonseparable exclusion are useful precise finite-model-theoretic invariants rather than arbitrary small-case tabulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
