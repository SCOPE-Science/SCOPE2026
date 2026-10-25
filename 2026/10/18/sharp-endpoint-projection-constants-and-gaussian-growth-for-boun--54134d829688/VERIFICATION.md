---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Actual frozen RESULT.md 0ea184... decomposes product functions into mutually annihilating P_B (coordinate mean-zero and averaging idempotents), so Q_d projects exactly onto low-order ANOVA interactions. Averaging any competing real projection over G=∏Sym(X_i) preserves the range and cannot increase its ℓp norm; the G-commutant is exactly span of the 2^r mutually orthogonal P_B, forcing Q_d. Finite kernel at equality set A is M^(−1) sum_{j≤d} e_j(z(A)), multiplicity ∏_{i∉A}(m_i−1); symmetric kernel gives matching ℓ1/ℓ∞ norms. Fixed d,q centered variables Y_i and generating-function CLT give Hermite limit, L² orthogonality gives uniform integrability. Independently constructed Q2 as sum of tensor E/D matrices and checked exact norms 9/4 (binary r4), 91/27 (ternary r4), and 25/9 (mixed sizes 2,3,2,3), with idempotence residual ≤7e−16. Infinite Gaussian limit proved by CLT, not by finite checks.

## originality

PASS

Theorem 16 of Kozdęba–Kozdęba (2025) treats all-but-one-coordinate interactions, whereas this theorem is any intermediate 2≤d≤r−2 and supplies exact endpoint constants plus fixed-order Gaussian sharp growth. Earlier Hamming P2 formula is a primitive (homogeneous exact-degree-2) projection, not cumulative low-order Q_d.

## value

PASS

This gives a natural complete answer for least-norm projections onto ≤d-variable interaction models on finite product sample spaces, a class explicitly proposed for further study in a 2025 primary paper. Sharp endpoint amplification and Gaussian growth explain dimension dependence for low-degree ANOVA approximation. It is not merely renaming the classical Hermite limit, since it evaluates global projection minima.

The dated certificate retains the supplied scientific assessment, sources and limitations.
