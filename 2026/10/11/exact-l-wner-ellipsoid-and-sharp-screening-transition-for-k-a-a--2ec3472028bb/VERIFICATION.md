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

The algebraic certificate appears in the proof in `RESULT.md`: (i) spectral eigenvalues of the covariance Laplacian in the exact zero-sum metric; (ii) the strictly concave scalar determinant optimization; (iii) exact leverage conditions for the two signed-edge orbits; (iv) the trace–determinant global optimality bound. The argument holds for all integers \(a\ge2\), \(b\ge1\).

The included `verify.py` independently constructs the actual edge-root covariance matrix for all \(265\) parameter pairs with \(2\le a\le11\), \(1\le b\le3a+7\). It numerically diagonalizes the matrix and verifies the predicted eigenvalues and multiplicities, all signed edge-root contact equations or strict inequalities, probability-weight normalization and inverse-covariance moment identities. Run `python3 verify.py` with NumPy available; the expected terminal status is `PASS 265 parameter cases: all eigenvalues, facet contacts, and covariance moment identities`.

An unrestricted-precision SLSQP optimization initialized at the proposed precision matrix was also checked on the six cases \((2,1),(2,4),(2,5),(2,6),(3,7),(3,8)\). It converged successfully to matching determinant objectives within ordinary floating-point tolerance. This secondary numerical optimizer is a corroboration, not a substitute for the analytical global optimality certificate or a proof of uniqueness.

The finite floating-point matrix tests are not claimed to certify infinitely many cases, exact zero eigenvalue multiplicity outside numerical tolerance, or literature priority. No independent external audit has been performed.
