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

# Reproducibility and limits

The proof calculates the stochastic covariance operator over **all** real symmetric two-by-two matrices. Its diagonal block is similar to \(\begin{psmallmatrix}(1-2h)^2&2h\\2h&(1-(1+\lambda)h)^2\end{psmallmatrix}\); the off-diagonal eigenvalue \((1-2h)(1-(1+\lambda)h)-2h\) is bounded in modulus by the Perron eigenvalue of that block. Its characteristic crossing at unity has determinant \(4h^2 F_\lambda(h)\). The boundary case is handled through the additive forcing and the left Perron eigenvector, not through a numerical timeout.

Run `python verify.py` with Python 3 and NumPy. The program implements the full three-component symmetric covariance operator and tests the stable/unstable regime against a direct eigenvalue computation in 72 parameter configurations. It also uses Python's exact `Fraction` arithmetic to check 1,500 randomly generated rational stationary-covariance equations, normalized bias equalities, and overdispersion inequalities. The output is saved verbatim in `verification-output.txt`. No randomness or finite verification is used to infer the universal quantifiers: those follow from the exact algebra in `RESULT.md`.

No claim is made about higher moments, the full stationary density, joint law convergence outside square-integrable classes, or the behavior of higher-order/splitting numerical integrators. The independent audit remains unperformed.
