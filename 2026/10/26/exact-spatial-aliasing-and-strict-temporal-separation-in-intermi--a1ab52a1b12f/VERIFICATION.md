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

# Verification and limitations

`CHECK.py` is a standalone script depending on Python, NumPy, SciPy, and SymPy. Invoke `python CHECK.py` from the extracted artifact directory. A successful execution prints `PASS: 622 exact symbolic / independent matrix-generator assertions`.

The script verifies the stationary Fourier formula and its exact factorization on the balancing surface, the variance criterion for unique spatial aliasing, the integrated time-correlation gap, and the exact maximum-lag condition. Separately, it constructs a three-state transition generator and solves independent first-/second-moment balances, evaluates a six-dimensional matrix exponential for the stationary lag correlation, and solves the complex stationary Fourier generator for distinct frequencies, using both balanced and unbalanced parameter sets. These computations passed in the packaged version.

The analytic proof is contained in `RESULT.md`; numerical checks sample finitely many parameters and cannot establish an identity for every real positive parameter. No stochastic simulation, independent peer audit, or external formal certification has been performed. The exact theorem does not address asymmetric heading selection, non-Poisson resets, higher dimensions, or nonstationary correlation functions.
