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

The accompanying `verify.py` runs with Python 3 and SymPy. Its exact symbolic checks reconstruct the homogeneous defining polynomial and its four partial derivatives; reduce the equation, gradient, and Hessian determinants in each of the three node families; confirm the local leading quartic at the quadruple point; and compute the exact length of the initial homogeneous Jacobian algebra by standard monomials.

Command: `python verify.py`

Expected last line: `VERIFY_OK: gradients, three exact nodal Hessian certificates, tangent cone, Euler data`.

The proof in `RESULT.md`, rather than this finite program, is responsible for exhausting all complex projective critical points and all parameter values. Smoothness of the projectivized quartic tangent cone and the ordinary-multiple-point formula are checked in the proof. Symbolic polynomial arithmetic provides exact identities over the rational numbers, which remain valid over \(\mathbb C\). The genus, exceptional intersection number, discrepancy, and Euler-specialization steps use standard geometric theorems stated in the proof.

The original 2026 manuscript was inspected via its complete arXiv HTML representation, including the smoothness statement and proof in Lemma 3.1. Smoothness of the affine pencil is explicitly credited to the authors; the new result is the detailed singularity basket and its local and topological invariants. Broader historical priority remains provisional. An independent mathematical audit has not been performed.
