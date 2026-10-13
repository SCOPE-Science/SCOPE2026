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

The universal proof is analytic and is fully stated in `RESULT.md`.

For the exact central path of the sample integral program,
\[
A=\begin{pmatrix}1&0&0\\0&1&-1\end{pmatrix},\quad
x=(1,\mu,\mu)^\top,\quad s=(\mu,1,1)^\top,
\]
the prescribed partition is \(J=\{1\}\) for all small positive \(\mu\). The source matrices reduce exactly to
\[
H=\operatorname{diag}((1+\mu)^{-1},2\mu),
\quad
G=\operatorname{diag}((1+\gamma_1\mu(1+\mu))^{-1},0),
\]
\[
Y=\operatorname{diag}\left(\frac{1+\mu}{1+\gamma_1\mu(1+\mu)},\frac{2\mu}{\gamma_1}\right).
\]
Their exact limiting condition-number coefficient is \(\gamma_1/2\).

For the general theorem, \(G\) is asymptotically the orthogonal projector onto the span of positive optimal columns, and \(H\) has a \(\mu\)-scaled positive-definite compression \(Q_\perp\) on the orthogonal complement. Near-identity block elimination gives the complete small-singular-value limit; finite computation is not used to infer this fact.

`artifacts/verify.py` uses only Python's standard library and exactly checks the sample's central path, integer constraints, source block formulas, prescribed partition, and several rational-gap condition numbers. It reports `VERIFY_OK` on success. The checker is a finite replay, not an independent mathematical proof.

Limitations: the finding does not address the running complexity of a quantum algorithm, arbitrary preconditioners, or paths without the stated strictly complementary limit.
