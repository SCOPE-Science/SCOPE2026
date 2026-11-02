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

# Verification and scope

`verify.py` is a standalone Python 3 checker requiring NumPy and SciPy; execute `python verify.py`. The program computes the normalized density matrix using both exact Gaussian moment generating functions and independent 200-node Gauss-Hermite quadrature. It checks matrix positivity, unit trace, Curie--Weiss basis weights, global spin-flip symmetry, and averaged trace nonincrease for 20 combinations of \(N\in\{2,3,4,5\}\) and \(t\in\{0.15,0.75,1,1.75,3\}\). It also tests finite-size trends in the critical \(N^{-1/2}\) correlation coefficient and the ordered/disordered regimes. Recorded result: `PASS 136 independent finite-size and asymptotic checks`; critical coefficient `1.1708286566075286`.

These are deterministic numerical checks and not mathematical proofs of infinite-population convergence. The analytical proof uses the exact kernel, Gaussian integral and Laplace asymptotics. The stochastic construction conditions on the ensemble after averaging; altering that order invalidates the claimed identity. All identities remain within the stated finite-dimensional model and specified limit regimes.
