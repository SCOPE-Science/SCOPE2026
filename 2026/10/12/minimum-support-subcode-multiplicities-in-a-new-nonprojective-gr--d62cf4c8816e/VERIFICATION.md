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
`artifacts/verify.py` uses only the Python standard library.

For each test instance it reconstructs
\[
D=
\mathbb F_p^n
\setminus
\left(
\mathbb F_p^m\times0
\;\cup\;
\{(-1,\ldots,-1,j,0,\ldots,0):1\le j\le t\}
\right).
\]

It enumerates every message subspace in reduced row-echelon form. For each subspace it computes the support directly by evaluating all defining-set columns, then records the minimum support and the number of subspaces attaining it.

The tested instances are
\[
(3,4,2,1),\quad
(3,4,2,2),\quad
(3,5,3,2),\quad
(5,4,2,1),\quad
(5,4,2,4).
\]

For every subcode dimension, the direct census agrees with
\[
d_r=
p^n-p^m-t-p^{n-r}+p^{\max(0,m-r)}
\]
and with the closed multiplicity formulas in `RESULT.md`.

The finite replay verifies the implementation and representative parameter regimes. The all-parameter theorem is proved by the graph-count argument in `RESULT.md`.

Successful replay prints `VERIFY_OK`.
