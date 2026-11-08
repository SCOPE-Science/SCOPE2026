---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The 8 stated vertices have common norm and exactly 16 edges of equal length. Each generic central section polygon has one edge per transversally cut polyhedron edge. Rescaling the z coordinate preserves oriented signs. All 56 ordered triple-determinant signs are nonzero in Q(sqrt2), so 8 great circles are in general position, yielding at most 8*7+2=58 normal chambers. Independently enumerated locally realized signs at all 28 great-circle pairs and both antipodes, obtained exactly 58 distinct chambers with edge-cut histogram {6:24,8:34}; exhaustion follows from the independent arrangement count. Each edge is cut with Haar probability alpha/pi; all edges share cos alpha=(2sqrt2-1)/7, hence E[N]=16alpha/pi, fixing both probabilities. Finite exact symbolic enumeration is exhaustive here; 250000-point simulation from repository is not its proof.

## originality

PASS

General polytope slicing-cell machinery and analogous exact Haar laws for other solids are known; their algorithms and distinct vertex configurations do not state this specific two-point antiprism support and probabilities. The exact chamber census plus single-angle expectation produces a natural geometric probability absent from inspected sources, best of knowledge.

## value

PASS

Exact shape-type probability of a classical regular Archimedean solid is a natural geometric invariant; the complete two-outcome support and 58-cell certificate give a usable exact distribution, not merely an isolated simulation or area estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
