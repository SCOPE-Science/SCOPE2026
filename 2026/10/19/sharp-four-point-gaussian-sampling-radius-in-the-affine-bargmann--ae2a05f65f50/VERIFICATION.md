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

The proof uses an exact discrete Fourier decomposition of four Gaussian intensity samples, symbolic Gram eigenvalues, a strictly monotone crossing function, and strict monotonicity of the two condition-number branches. These are analytic claims with explicit inequalities, not extrapolations from finite experiments.

`CHECK.py` was executed against these files: symbolic determinant and characteristic-polynomial identities passed, exact rational Taylor certificates passed, 129 direct singular-spectrum probes and 150 Hermitian inverse tests passed. The calculation of the unique critical radius is numerical only after its existence and uniqueness have been proved.

The scientific limits concern equal Euclidean noise normalization, the four-point equilateral design family, and residual priority uncertainty; no other sampling geometry is optimized here. Independent audit has not been performed.
