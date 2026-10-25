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

# Verification of finite-state chiral fourth-cumulant law

A fresh execution of the embedded `CHECKER.py` in a Python environment with SymPy prints exactly:

`PASS: 236 exact algebraic and independent Poisson-recursion checks`

The checker evaluates the radial fourth-cumulant contraction, its strictly negative symbolic factorization, axial–diagonal agreement, and the exact turning-rate threshold. Independently, for six unequal/equal positive integer rate pairs and three planar projection vectors, it constructs the genuine four-by-four Markov generator and solves the centered eigenvector Poisson equations to fourth degree; the results are compared with the symbolic global formula as exact rational identities. It checks representative angular-sign regions but no finite parameter grid is claimed to prove the universal signs.

For a complete reproducible proof, reconstruct \(Q\), calculate the explicit tilted characteristic polynomial in `RESULT.md`, differentiate the analytic Perron branch (zero simple and other roots in the open left half-plane), and use exact elementary inequalities \(0<|a-b|<a+b\). The radial contraction follows by taking the fourth derivatives of the full bivariate branch and the exact fourfold-rotation covariance symmetry. The stationary initial heading ensures exact fourfold distributional invariance at every finite time. A long-time theorem does not imply finite-time sign classification at or near the critical direction. No independent audit or externally certified proof has occurred.
