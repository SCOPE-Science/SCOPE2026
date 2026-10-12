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

The proof uses the multiplication table of \(\pi_3\) and no numerical approximation. `artifacts/verify.py` first solves all basis Leibniz identities for a general \(5\times5\) matrix and recovers a six-dimensional derivation space over \(\mathbb Q\).

For a local derivation \(L\), the definition implies \(L(v)\in\{D(v):D\in Der(\pi_3)\}\) for every \(v\). The script imposes this condition on the ten vectors displayed in `RESULT.md`. Exact nullspace elimination leaves a seven-dimensional necessary space and verifies that it is precisely
\[
\begin{pmatrix}
x&0&0&0&0\\
p&2x&0&0&0\\
r&q&3x&s&0\\
0&0&0&x&0\\
t&0&0&u&2x
\end{pmatrix}.
\]
Because these are necessary pointwise constraints, every genuine local derivation lies in this space; no sufficiency assumption is used in the obstruction.

The script next verifies symbolically, for indeterminate \(\tau\), that the matrix of \(\Phi_\tau\) preserves all \(25\) ordered basis products and is invertible. It verifies by differentiation that
\[
\exp\!\begin{pmatrix}3x&s\\0&x\end{pmatrix}_{1,2}
=s\frac{e^{3x}-e^x}{2x}
\]
for \(x\ne0\), and checks the exact vanishing after substituting \(e^x=-1\). Finally it verifies directly that \(D_0=\operatorname{diag}(i\pi,2i\pi,3i\pi,i\pi,2i\pi)\) satisfies every Leibniz identity and that \(\exp(D_0)=\Phi_0\).

The replay uses SymPy 1.14.0 and terminates with `CHECK_OK`. The computation is exact symbolic/rational algebra; no finite experiment is used as an infinite proof. The scientific limitation is that the full exponential image is not classified, and the analogous \(\pi_2\) assertion is not assessed.
