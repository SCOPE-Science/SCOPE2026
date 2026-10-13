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

Run `python verify.py` after installing the SymPy dependency listed in `requirements.txt`. The script reconstructs the positive equilibrium and original three-variable Jacobian, verifies the symmetric/antisymmetric spectral splitting, verifies the fixed-point and transversality data, and differentiates the actual planar rational vector field in canonical coordinates to cubic order to recompute the exact first Lyapunov coefficient. Its successful result is `VERIFY_OK`.

The exact sign of the first Lyapunov coefficient depends on the declared positive coordinate normalization; the script and proof use the same canonical coordinates, so both report \(-40879/532480\). An independent complex-eigenvector cubic-form calculation also yielded a negative coefficient in another normalization. No finite symbolic test establishes nonexistence of arbitrary periodic orbits or global convergence by itself; these rely on the analytic ratio identity, Dulac computation, and the planar limit-set argument in `RESULT.md`. No experimental claim or independent validation is made.
