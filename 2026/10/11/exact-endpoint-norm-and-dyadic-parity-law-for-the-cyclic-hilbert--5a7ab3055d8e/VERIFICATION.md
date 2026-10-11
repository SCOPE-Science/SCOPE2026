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

The analytic proof is primary. The bundled `verify.py` is a finite regression checker that independently reconstructs the multiplier kernel and tests the displayed exact and asymptotic formulas.

Checks performed by the script:

- Direct inverse-DFT reconstruction of the cyclic Hilbert kernel for many odd and even cycle sizes.
- Comparison with the closed cotangent/tangent kernel formulas.
- Comparison of the direct absolute row sum with the stated exact formulas for \(L_N\).
- Numerical verification of \(L_{2N}=L_N\) across many odd \(N\).
- Convergence checks for the three displayed \(N^{-2}\) coefficients after subtracting the corresponding logarithmic main terms.

The finite checks do not prove the universal theorem or the asymptotic remainder. Those follow from the finite sine-sum identities, exact convolution-norm witnesses, harmonic-number expansions, and midpoint Euler--Maclaurin argument in `RESULT.md`.
