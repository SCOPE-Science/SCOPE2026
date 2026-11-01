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

Reconstructed the 32x128 distinct two-deletion incidence matrix from all 21 retained-coordinate pairs per seven-bit word. Independently checked all six explicit codebooks satisfy every row load<=L and cardinalities (5,11,16,21,26,32). Independently checked every 128 pointwise nonnegative rational dual inequality for each L and strict upper bounds 256/45, 666/59, 452/27, 1160/53, 1430/53, 2340/73, each strictly below the next integer. For L=2, independently checked all 32 primal inequalities, all 128 variable bounds, and rational objective 666/59. Thus finite exact certificates prove both integer optima and fractional gap 17/59 without trusting a solver or extrapolating.

## originality

PASS

Lin 2026 derives asymptotic rates for exactly the same list-decodable deletion-hypergraph model but no fixed seven-bit exact profile; Guruswami–Håstad construct asymptotic two-deletion codes. The closest indexed six-bit exact capacity of seven does not imply length-seven low-list capacity or exact LP fractional value. Originality is best-of-knowledge with potential old finite table risk.

## value

PASS

A natural complete first seven-bit two-deletion list-size profile extending the previously known six-bit case, and an exact integrality gap for the canonical LP relaxation. Both the full finite spectrum and the fractional obstruction are meaningful reproducible benchmarks for short deletion codes; no general rate theorem is required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
