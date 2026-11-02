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

The proof in `RESULT.md` contains an all-parameter certificate: a leading-principal-minor identity, a factored determinant identity, strict monotonicity of the root-defining cubic, the exact comparison at both candidate boundary points, and a monotone parametrization of the global maximizer. These identities cover all \(v>0\) and \(z>0\), not just tested values.

The included `verify_rk2.py` was executed from this exact document package with SymPy and NumPy. The recorded output was:

`VERIFY_OK symbolic identities, 12 boundary points, 108 two-sided spectral-norm samples; sharp optimum and resonance`

The script checks the mathematical certificate symbolically, including \(I-R^{\mathsf T}R\), the determinant, the optimal matrix and its eigenvalues/singular values. Its finite numerical comparisons are only sanity checks around the analytical frontier. Run `python verify_rk2.py` after installing `requirements.txt`. No machine-verified infinite proof or independent scientific assessment is claimed.
