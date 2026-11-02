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

# Reproducible checks and proof boundary

Use the standalone `VERIFY.py` with Python 3 and no third-party packages. It performs the complete midpoint–difference fixed-point iterations using 95-digit decimal arithmetic at 21 parameter combinations \(T\in\{2.0001,2.01,2.1,2.5,3,10,100\}\) and \(\alpha\in\{10,12,20\}\). It evaluates both one-step return equations to residual below \(10^{-72}\), checks all box and exponential-location bounds, confirms strict quadrant signs, and verifies the matrix perturbation bound against \(T-2\). It also checks the three numerical universal constants used in the analytical contraction and hyperbolicity proof.

The exact all-parameter result is not inferred from this finite test grid. Its critical certificate consists of the strict monotonicity identity excluding period two for every \(T\le2\), the globally invariant closed box and Banach contraction for every \(T>2,\alpha\ge10\), and the complex-vector derivative lower bound at both orbit members. The verification program checks formulas and example implementations; it does not independently certify publication priority or the infinite analytic theorem. No independent mathematical audit has been performed.
