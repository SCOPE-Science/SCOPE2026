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

For a unit vector and a fixed weave, set
\[
E=\sum_{j\in\sigma}\|\Lambda_j f\|^2+\sum_{j\notin\sigma}\|\Gamma_j f\|^2,
\qquad
S=B_\Lambda+B_\Gamma.
\]
Dual reconstruction, the two Bessel inequalities, and Cauchy-Schwarz give the chain
\[
1\le\sqrt{x(B_\Gamma-y)}+\sqrt{y(B_\Lambda-x)}\le\sqrt{E(S-E)}.
\]
Therefore \(E(S-E)\ge1\). Duality also gives \(B_\Lambda B_\Gamma\ge1\), hence \(S\ge2\), and solving the quadratic proves
\[
E\ge\frac{S-\sqrt{S^2-4}}2.
\]

For sharpness at arbitrary admissible bounds \(L,G\), choose \(\lambda,\gamma\in\mathbb R^2\) with squared norms \(L,G\) and dot product \(1\). The matrix
\[
M=\lambda\lambda^{\mathsf T}+(J\gamma)(J\gamma)^{\mathsf T}
\]
has trace \(L+G\) and determinant \(1\). Its smaller eigenvalue is therefore the claimed lower constant. Choosing the index-coordinate basis from its corresponding eigenvector produces a two-index scalar dual pair whose selected weave has exactly that energy.

Checks include the boundary \(LG=1\), the case \(S=2\), arbitrary countable index sets, and complex Hilbert spaces for the inequality. The extremal construction needs only the real one-dimensional special case. No computation beyond the displayed algebra is required. The theorem does not claim the exact weaving bound of a fixed pair when more geometric information than \(B_\Lambda,B_\Gamma\) is available.
