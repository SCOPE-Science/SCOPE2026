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

The proof is the exact partial-transpose block decomposition in `RESULT.md`; finite computation is corroborative only.

For each \(0\le i<j<k\), the pair block is \(\begin{pmatrix}h_k&g_k\\g_k&h_k\end{pmatrix}\) with
\[
h_k=\frac{p(1-q)+(1-p)q}{dk}+\frac{pq}{d^2},
\qquad g_k=\frac{(1-p)(1-q)}k.
\]
Its unique possible negative eigenvalue has magnitude \([g_k-h_k]_+\). There are \(k(k-1)/2\) such blocks and no other possible negative eigenvalues. This proves the negativity formula for all parameters, not merely those checked numerically.

The finite difference of \((k-1)(\Delta-kpq)\) is \(\Delta-2kpq\), which proves the exact discrete rank optimization. At symmetric noise the equation \(\Delta=2kpq\) solves to \(t_k=d/(d+1+\sqrt{2k+1})\).

The bundled checker independently constructs the full two-qudit post-channel density matrix, performs its partial transpose, and compares numerical spectra with the exact formula for multiple dimensions, supports, and noise parameters. It also tests the transition ordering and exact qutrit rational witness. `artifacts/requirements.txt` documents its sole external dependency. These examples are not used as infinite proofs.

No assertion is made about all-input optimality, or novelty of the already known channel-level entanglement-death boundary.
