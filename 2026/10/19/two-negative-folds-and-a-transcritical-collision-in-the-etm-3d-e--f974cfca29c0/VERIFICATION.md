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

# Executable verification and boundaries

Execute `python CHECK.py` with SymPy available. This checks, with exact integer and rational polynomial operations: elimination to the quartic; its \(12000P\) discriminant; squarefreeness and the two negative roots of \(P\); exact counts at \(\rho=-3,-3/2,-1\); vanishing-abscissa exceptional parameters; the linear subresultant yielding fold abscissae; strict rational interval bounds for the two folds' nonzero \(F_{\rho},F_{xx},c_2\); and the exact left/right origin eigenvectors and nonzero center coefficients at \(\tau\).

All certificate inequalities come from rational interval enclosure, not decimal output. The finite number of symbolic Sturm evaluations controls the entire real half-line because the quartic leading coefficient is constant and all possible parameter root collisions are contained in the isolated discriminant zeros. This is a same-model reproducibility check, not an external independent audit.

The computation does **not** certify global trajectories, invariant measures, or chaotic attractors. The scholarly overlap review cannot exclude undiscovered equivalent published treatments.
