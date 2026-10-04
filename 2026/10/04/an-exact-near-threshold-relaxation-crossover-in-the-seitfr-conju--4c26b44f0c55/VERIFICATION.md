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
# Verification

`verify.py` reconstructs the five-dimensional tangent matrix \(J_{\mathrm{tan}}+\mu I\) from the published baseline parameters using exact rational arithmetic. Each matrix entry is represented as an affine polynomial in \(\mathcal R_0\). The script expands the determinant over all \(5!\) permutations, confirms that the result is affine, computes its unique rational zero, and checks that it equals
\[
\frac{386467087274709075099662209}{386355335676178838352248250}.
\]
It also checks the determinant is positive at \(\mathcal R_0=1\) and strictly between \(1\) and the root, zero at the root, and negative at \(\mathcal R_0=1.01\). Successful replay prints `VERIFY_OK`.

The checker verifies the exact algebraic certificate, not the whole nonlinear dynamics. The spectral interpretation additionally uses the elementary fact that a real odd-dimensional matrix whose eigenvalues all lie in the open left half-plane has negative determinant. The claim is limited to the linearized spectrum and the stated baseline parameter path.
