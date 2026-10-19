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

# Reproducibility and verification

Run `python3 verify_cycles.py` with Python 3.10 or later. It needs only standard-library `fractions` and `itertools`, and does not rely on floating-point rounding, network access, external packages, or stored output logs.

The verifier independently builds the three complete supporting lines, computes projections as dot products, compares exact squared distances to decide the farther target, and implements the fixed-on-tie rule. For each of twelve rational heights it enumerates every cyclic length-three and length-four line itinerary with unequal adjacent line labels; it computes the unique affine periodic-point candidate, applies the actual dynamical map, and deduplicates cycles by physical-coordinate cyclic rotation. It separately checks the theorem's explicit rectangle and three-cycle representatives against actual map iterations.

Checked heights: \(51/100,11/20,3/5,63/100,16/25,2/3,4/5,1,5/4,13/10,3/2,2\). The predicted pairs of primitive orbit counts for periods three and four were reproduced in all twelve cases: the first four have \((2,1)\), the next five have \((2,0)\), and the last three have \((0,0)\). These are illustrative **finite checks only**.

The all-parameter assertion rests on the analytical itinerary exhaustion, unique affine return fixed-point calculation, strict four-branch test, leg-exclusion perfect-square obstruction, and three-cycle branch inequalities in RESULT.md. The exact radical endpoints are determined symbolically by solving the displayed quadratic inequalities, not inferred from the finite test set. No external independent audit has been performed.
