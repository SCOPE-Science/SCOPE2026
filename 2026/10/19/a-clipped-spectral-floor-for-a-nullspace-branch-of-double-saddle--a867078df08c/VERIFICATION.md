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

The standalone file `verify.py` is included. Execute `python verify.py` using Python 3; no nonstandard dependencies, data downloads, or proprietary tools are required. It checks by `fractions.Fraction` arithmetic the blockwise generalized-eigenvalue identities for the two integer parameter pairs \((t,s)=(1,3)\) and \((11,27)\), the nullspace equations, both coupling Gram matrices, the source's contradicted lower bound, and the exact sharpness witness \((a,b,\beta,\lambda)=(3,4,4,2)\).

Successful execution prints:

`VERIFY_OK exact_generalized_eigenpairs=2 nullspace_conditions=2 BBt_identites=2 eigenspectrum_exclusions=2 sharp_floor_equality=1`

The analytical proof in `RESULT.md`, not this finite test suite, establishes the real-eigenvalue bound for all admissible matrices and the parametric unbounded counterexample for every real \(t\ge1\). Floating-point spectral plots, asymptotic extrapolations, and unperformed independent audits are not claimed as evidence.
