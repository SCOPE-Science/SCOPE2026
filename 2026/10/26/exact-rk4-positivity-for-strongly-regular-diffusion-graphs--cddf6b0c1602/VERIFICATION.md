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

# Reproducibility and scope

Run `python verify_srg_rk4.py` after installing `sympy` (for example, from the supplied `requirements.txt`). A successful run reports 23 exact strongly regular test graphs, 9,976 off-diagonal rational checks, symbolic expansion into \(I,A,J\), the quadratic discriminant, the derivative-ratio identity, and the triangular nine-vertex boundary polynomial. This program directly constructs the finite matrices and does not assume the numerical claims when checking them.

The universal assertions are derived in `RESULT.md` from the exact strongly regular adjacency algebra, positivity of a quadratic with strictly negative discriminant, and a spectral-projector inequality guaranteeing a strictly decreasing adjacent-entry cubic. Finite checks alone cannot establish results for all vertex counts. The reference date is taken from the original 2001 paper's publication notice; it is not inferred from a subsequent reprint or website upload.

Limitations: There is no independent audit, no external formal proof certification, and no claim about different integrators, nonuniform weights, directed graphs, or positivity of internal RK stages.
