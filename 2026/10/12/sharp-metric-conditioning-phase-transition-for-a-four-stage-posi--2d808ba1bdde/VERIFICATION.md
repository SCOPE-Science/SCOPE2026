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
This finding is established by a complete analytic optimization, not by a finite sample. The standalone `verify.py` checks exact rational consequences and numerical instances of the closed-form formula.

For the rational system
\[
G=-I_4+2N,\qquad P=\operatorname{diag}(1,2,8,16),
\]
the weighted Lyapunov symmetric part is the rational matrix
\[
G^{\mathsf T}P+PG=
\begin{pmatrix}
-2&2&0&0\\2&-4&4&0\\0&4&-16&16\\0&0&16&-32
\end{pmatrix}.
\]
Its generalized eigenvalues against the positive diagonal matrix \(P\) are exactly
\[
0,-1,-3,-4.
\]
The checker reconstructs the characteristic polynomial of \(P^{-1}(G^{\mathsf T}P+PG)\) with rational arithmetic; consequently the symmetric congruence by \(P^{-1/2}\) has the same real generalized eigenvalues, and the displayed certificate is negative semidefinite.

The metric has condition number exactly \(16\). The analytic minimax formula gives \(R(16)=1/2\), while \(\gamma/w=1/2\), so this is the exact nonexpansion boundary.

Other checks compare the two formula branches at \(K=2\), evaluate the Perron eigenvalue using its quadratic equation, verify the derivative's predicted scalar minimizer at a selection of budgets, and check a fixed deterministic grid of alternative feasible metrics. Those samples are supporting diagnostics only. The proof of necessity for **all** positive diagonal metrics with condition number below the threshold is the analytic reduction in `RESULT.md`.

The theorem concerns weighted operator-norm nonexpansion, not the absence of all ordinary Euclidean transients or finite-precision guarantees.
