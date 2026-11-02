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

The analytical argument establishes a universal exponent classification for bounded-increment finite-dimensional Euclidean martingales. The positive range \(p\ge3\) invokes the stated comparison theorem in arXiv:2610.31449v1; \(p=2\) follows from martingale orthogonality. The subquadratic witness and the strict subcubic adaptive witness are given in closed form, with the latter's power series convergent for every \(0<\delta<1/2\). Two-step admissibility follows from a separate affine-majorant argument.

Reproducibility: run `python3 verify_power_threshold.py`; expected output is included in `verification_output.txt`. The verifier checks rational sign patterns, selected high-precision strict gaps, endpoint equalities, and two-step samples. It is a consistency check and not an infinite proof or external validation. Historical-priority comparisons have residual coverage risk.
