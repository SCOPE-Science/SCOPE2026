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

The proof is self-contained in `RESULT.md`, including the exact matrix resolvent, sign discriminant, constructive nonnegative potential, and near-critical two-variable optimization. To check its finite computations, run `python verify.py` with NumPy and SciPy installed; the script needs no other input files.

The matrix computation checks 72 independent parameter combinations for the complex resolvent and its imaginary part. A separate grid checks twelve velocity–diffusivity conditions on the sign classification. Fourier quadrature verifies the negative spectral integral for localized, nonnegative interactions at three widths. Direct numerical optimization of the power envelope for five near-critical values approaches the proved coefficient, with ratios about 1.020883, 1.006196 and 1.002059 at the final three choices of reduced distance to criticality. The numerical tests address finite computations only. Uniform limiting expansions and universal quantifiers over probe potentials are established analytically; no finite sampling is presented as an exhaustive proof.

The external scientific assumptions are limited to the ideal dilute bath and leading weak-potential response. Independent audit is not performed.
