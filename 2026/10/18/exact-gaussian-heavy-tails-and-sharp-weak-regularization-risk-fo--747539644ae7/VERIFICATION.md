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

The exact proof is in `RESULT.md`. Run `python verify.py` with dependencies from `requirements.txt` in the same directory.

`verify.py` performs 375 rational oracle-path checks of the residual identities and the unrestricted/singly regularized/symmetrically regularized image outputs. The conditional mean/variance identities are checked by rational arithmetic. Deterministic Gaussian quadrature at four ridge strengths tests convergence toward both closed-form weak-penalty coefficients; the last observed absolute coefficient deviations were approximately \(3.710\times10^{-4}\) and \(3.711\times10^{-4}\).

All quadratures are finite numerical checks. The \(T^{-1}\) tail law, sharp moment cutoff, and \(\lambda^{-1/2}\) asymptotics are established analytically in the proof, not certified by simulations. Other stochastic-noise distributions, longer AA histories, and safeguarded implementations are outside scope.
