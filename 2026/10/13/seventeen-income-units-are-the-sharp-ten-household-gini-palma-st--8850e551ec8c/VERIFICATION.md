---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

With ten equally weighted households and no partial quantiles, Palma is the largest income divided by the sum of the four smallest; at common S, the Gini denominator is 10S and its numerator is the sorted linear form sum_i(2i−11)x_i for i=1,...,10. I inspected the frozen proof, verification notes and checker without executing that checker. An independent census built sorted profiles by incrementing one entry and sorting, starting from ten ones. Completeness follows by decrementing an entry above one and sorting in the reverse direction. The layer sizes for S=10,...,17 were 1,1,2,3,5,7,11,15. Exact pair comparisons gave no strict reversal until S=17, and exactly the two displayed pairs there, with numerator pairs (53,51) and (45,43) and Palma pairs (1,5/4) and (3/4,1). The first tie split at S=14 was also confirmed (Gini numerators 32 versus 30 at equal Palma 3/4). Replay: python3 -I /workspace/review_math.py 5. No threshold is asserted for other household counts, income grids, or unequal totals.

## originality

PASS

The supported distinct fact is the sharp same-total integer boundary and complete first layer, not generic Gini–Palma disagreement or the definition of Palma. The strongest inspected direct comparison treats near-empirical equivalence and decile sensitivities, not exact order equivalence or a discrete first inversion. Nearby exact results concern different indices and/or a different household count. No inspected result covers this boundary.

## value

PASS

Ten equally weighted units are the smallest population that realizes both Palma percentile cuts without interpolation. Fixing resources and positivity, the minimum integer resolution and complete first strict layer give clean test cases for separating tail rank from dispersion rank. Both witnesses keep the bottom-four sum at four, so the disagreement is already attributable to how the maximum and the broader spread are ranked, not a change in lower-tail normalization. The result is an exact finite benchmark, not a monetary cutoff or an empirical claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
