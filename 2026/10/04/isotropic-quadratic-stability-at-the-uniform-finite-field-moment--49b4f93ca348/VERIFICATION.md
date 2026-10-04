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

The proof is analytic and applies to every admissible \(d\ge2\) and prime power \(q=p^n\) with \(p>d\).

The packaged checker independently verifies the closed curvature coefficient in several admissible finite cases. It constructs
\[
F_{d,q}(\theta)
=
\sum_{t\in\{1,\ldots,q\}^d}
M(t)\prod_j\theta_{t_j},
\]
differentiates this finite polynomial exactly at the uniform law, evaluates the second derivative in the tangent direction \(e_1-e_2\), and compares the resulting coefficient with the formula
\[
C_{d,q}
=
\frac{q^{2-d}}4
\sum_{s=2}^{d}
\binom ds^2 B_{d-s,q-2}
\frac{s(s-1)}{2s-1}\binom{2s}{s}.
\]
All arithmetic is rational.

The finite replay is a consistency check only. The general statement follows from permutation symmetry, the exact pair-merging identity, the explicit \(H_s\)-polynomial, and Taylor expansion.

The literature-comparison limitation is separate from mathematical verification: the complete 1973 Schur-concavity antecedent was not accessible during this review.
