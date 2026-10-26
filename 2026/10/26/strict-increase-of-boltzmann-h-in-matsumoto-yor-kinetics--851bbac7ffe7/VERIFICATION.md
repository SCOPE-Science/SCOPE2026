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

The proof establishes exact algebraic identities for the Matsumoto–Yor map, followed by a strict covariance argument and a quadratic KL upper bound. The finite checking script is a supplementary consistency test.

Execute `python verify_kinetic_entropy.py` with Python 3, NumPy, SciPy, and SymPy installed. The deterministic checker tests the involution, conservation law, Jacobian and stationary monomial by exact symbolic simplification; integrates the reference GIG/Gamma normalization; verifies the sign of the linear coefficient in the special case \(p=1/2,c=2\); and compares two independently evaluated initial entropy derivatives at three positive perturbation sizes.

Observed: symbolic tests passed, normalization passed, \(B=0.322978440288\), and positive unweighted derivatives \(0.0006458287588,\;0.003226100332,\;0.01605638976\) at perturbations \(0.002,0.01,0.05\), respectively. The corresponding relative-entropy derivatives were negative. The quadrature error on the equilibrium logarithmic-Jacobian mean was about \(2.1\times10^{-8}\).

Finite quadrature and symbolic reduction of identities are not an exhaustive solution of the kinetic equation. The all-parameter strict sign follows from the analytic proof in `RESULT.md`. No independent mathematical audit has been performed.
