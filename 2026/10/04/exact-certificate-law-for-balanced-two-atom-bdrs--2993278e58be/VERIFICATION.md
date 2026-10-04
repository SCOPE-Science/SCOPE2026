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

The proof was replayed from the packaged formulas rather than from prior-run calculations. The central algebraic checks are:

1. For \(K_\varepsilon=\begin{pmatrix}1&z\\z&1\end{pmatrix}\) and \(t=q\mathbf1\), equation (15) gives \(A=[2q(1+z)]^{-1}\mathbf1\) and then \(B=q\mathbf1\).
2. The resulting \(Z\) has every row and column sum exactly \(1/2\), so \(\delta=0\).
3. The direct primal cost equals \(\Delta z/(1+z)\), while the dual potentials cancel the arbitrary scalar \(q\) and give \(L=-(\eta/p)\log(1+z)\).
4. Differentiation of the resulting \(G\) gives three strictly negative terms for every \(p>0\).
5. Because \(G\) is strictly decreasing, the first integer iteration satisfying a fixed tolerance is the ceiling of the corresponding affine threshold in \(p\).

The packaged `verify.py` performs independent floating-point reconstructions over multiple \((\Delta,\eta,\lambda)\) choices, checks marginals and formula identities to tight tolerances, checks monotonicity on deterministic grids, solves several tolerance thresholds by bisection, and checks the exact ceiling formulas. It prints `VERIFY_OK` on success.

Finite numerical tests do not prove the analytic monotonicity, asymptotic expansion, or all-parameter stopping law. Those statements are established symbolically in `RESULT.md`. No claim is made beyond the balanced two-atom setting.
