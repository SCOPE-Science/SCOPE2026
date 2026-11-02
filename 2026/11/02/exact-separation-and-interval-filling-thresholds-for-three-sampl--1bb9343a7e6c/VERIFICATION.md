---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and boundaries

Run `python3 verify.py` using Python 3 with its standard library only. The checker uses `fractions.Fraction`, enumerates the six compositions of the component maps, verifies all five scaled gaps at eight rational parameters, tests the exact algebraic stationary variance identity and 56 finite-epoch moment sums, checks both disjointness and interval-filling comparisons, and brackets both unique polynomial roots with rational endpoints.

The **universal** correctness evidence is the algebraic proof in `RESULT.md`: the six maps have a common strict contraction, the enclosing interval has explicit endpoints, adjacent interval gaps are exact, and the two threshold polynomials are strictly decreasing on the full admissible parameter range. The dimension assertion relies on the standard self-similar dimension theorem under strong separation. The finite verification does not establish these infinite claims by enumeration; nor does it test absolute continuity, intermediate-regime dimensions, or higher-dimensional objectives.

Self-review: passed. Independent audit: not yet performed.
