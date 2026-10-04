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
The proof is symbolic and does not depend on finite enumeration.

For a diagonal matrix
\[
D=\operatorname{diag}(a_1,\ldots,a_n)
\]
and
\[
f(x)=\sum_kA_kx^k,
\]
the \((i,j)\)-entry of \(f(D)\) is
\[
\sum_k(A_k)_{ij}a_j^k.
\]
Thus each column of the null ideal is controlled by one scalar vanishing polynomial
\[
h_j(x)=\prod_{a\in X_j}(x-a).
\]

The packaged checker `artifacts/verify.py` exhaustively enumerates all subsets of the diagonal algebra for
\[
(q,n)=(2,2),(2,3),(2,4),(3,2),(4,2).
\]
It independently evaluates the coordinate-projection criterion and the inclusion-exclusion count. The exact total numbers of core subsets are
\[
10,\quad196,\quad63778,\quad290,\quad42610.
\]
It also constructs explicit column-transfer obstructions for sample noncore sets.

The checker returns `VERIFY_OK`.

Finite computation is not used to prove the theorem.
