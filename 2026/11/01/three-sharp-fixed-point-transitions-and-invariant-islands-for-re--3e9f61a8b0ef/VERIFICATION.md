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
# Verification and reproducibility

The mathematical classification follows from the proved finite integer-label reduction, not computer sampling. A fixed point of the reduced rotation satisfies \((I-R_\theta)z\in\mathbb Z^2\). For \(0<\theta<\pi\), the positivity and size bounds on this lattice label leave precisely the candidates \((1,0)\), \((1,1)\), \((2,1)\), plus the origin; their admissibility gives the three strict thresholds. Exact coordinate interchange proves the opposite-angle case. The central half-turn and excluded identity angles are treated separately.

The accompanying `check.py` uses only Python's standard library (`fractions`, `itertools`). Execute `python3 check.py` to reproduce exact-rational center enumeration, exact branch equations, radius calculations, pairwise disjointness, and the half-turn four-point census. It passes 23 finite parameter cases spanning the three threshold values and both orientations.

The proof separately establishes that each open disk is mapped onto itself by a Euclidean rotation, not merely kept within an approximate or numerical neighborhood. The area formula is the sum of the measures of these disjoint disks. It is a lower bound on total invariant area, not a full invariant-set classification. Independent scientific validation has not been performed.
