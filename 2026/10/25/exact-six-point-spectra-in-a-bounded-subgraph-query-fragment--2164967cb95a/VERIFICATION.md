---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

PASS: Complete independent enumeration of labelled simple graphs on 1..4 vertices yields possible positive maximum subgraph edge/vertex densities {1/2,2/3,3/4,1,5/4,3/2} (independent_checks.py: SIX_SPECTRA_OK). For each fixed H, classical subgraph threshold at n^-1/rho_max(H) gives 0/1 occurrence outside these six critical powers; finite Boolean combinations preserve 0/1 limits. The chosen six patterns are strictly balanced with automorphism counts 24,4,6,2,2,2 respectively, checked by independent full label-permutation enumeration, so critical copy counts tend to Poisson means 1/24,1/4,1/6,1/2,1/2,1/2. At each distinct critical alpha, the other five indicators have deterministic limits; direct parity gives e^-1/24, 1-e^-1/4, e^-1/6, 1-e^-1/2, e^-1/2, 1-e^-1/2, all strictly (0,1). The asymptotic theorem is an invoked published theorem, not inferred from finite enumeration.

## originality

PASS

PASS best knowledge, with substantial routine-derivation risk: Yarovikov–Zhukovskii show finite spectrum for all FO depth four and state fixed-subgraph threshold technology, but not the exact bound and six-bit witness for Boolean non-induced occurrence fragment. Strict-balanced Poisson limits are classical. The complete restricted result is an elementary combination of known pieces and independent finite classification; it is not claimed as a new probability limit theorem, nor as a bound for all FO4.

## value

PASS

PASS: The bounded-pattern non-induced graph-query Boolean fragment is natural in sparse random-graph descriptive complexity. Identifying the entire six-point spectral support and one formula attaining every point is a complete exact phase-transition classification for a nontrivial bounded syntax, useful to separate it from full FO quantifier-depth-4 spectra. Uses standard thresholds and small finite graph enumeration, so the contribution is exact fragment-wide synthesis rather than a new asymptotic threshold theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
