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

# Verification notes
The probability coefficients were independently reconstructed as \(v\), \(3(u-v)\), and \(1-3u+2v\), with \(u=\sum_i p_i^2\) and \(v=\sum_i p_i^3\). The universal proof uses a five-coordinate centered-cubic extremal inequality proved by Lagrange multipliers; it is not inferred from sampled distributions. Polynomial coefficient arithmetic independently verifies the identity \(\Delta(q(t))=48t^3(75t^3+30t^2-27t+4)\) exactly. The cubic factor has derivative at most \(-6\) on \([0,1/5]\), so it stays at least \(2/5\).

`CHECKER.py` executes using the Python standard library and rational arithmetic. Its run reported PASS for the polynomial factorization, skewness branch ordering, 2,997 finite-grid simplex vectors, 230 independently enumerated three-draw cases, and the six-category discriminant \(-1439/810000\). The finite-grid checks cannot certify the universal quantifier; the analytical proof does. No external, independent audit has been performed.
