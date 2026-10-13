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

The proof is analytic. The executable checker performs two finite stress tests without being used to justify the infinite quantifier.

First, for every ordered pair \(2\le m,n\le100\), it verifies by exact integer arithmetic that
\[
\begin{pmatrix}
2n&2n&0\\
m-1&m+n-2&n-1\\
0&2m&2m
\end{pmatrix}
\begin{pmatrix}
n(n-1)\\
(m-1)(n-1)\\
m(m-1)
\end{pmatrix}
=
2(m+n-1)
\begin{pmatrix}
n(n-1)\\
(m-1)(n-1)\\
m(m-1)
\end{pmatrix}.
\]

Second, for every \(2\le m\le n\le6\), it explicitly constructs \(F_2(K_{m,n})\), checks connectivity and the parity bipartition, checks the three cell degrees and neighbor counts, and verifies the lifted positive signless-Laplacian eigenvector exactly.

The checker does not attempt to determine the full Laplacian spectrum. Its finite tests are consistency checks only; correctness for all \(m,n\ge2\) rests on the proof in `RESULT.md`.
