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
The packaged checker `artifacts/verify.py` starts from
\[
e_1\circ e_1=2e_2
\]
and a general matrix
\[
R=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix}.
\]

It reconstructs all four ordered basis-pair Rota–Baxter defects and verifies the complete scalar system.

For odd prime fields it independently derives the predicted solution set, rank distribution, and automorphism orbits under
\[
\phi_{s,t}=
\begin{pmatrix}
s&0\\
t&s^2
\end{pmatrix}.
\]

It exhaustively checks every \(2\times2\) matrix over
\[
\mathbf F_2,\quad
\mathbf F_3,\quad
\mathbf F_5,\quad
\mathbf F_7.
\]

The direct operator counts are
\[
16,\quad15,\quad45,\quad91.
\]
The odd-field rank profiles are
\[
(1,8,6),\quad
(1,24,20),\quad
(1,48,42),
\]
and the odd-field automorphism-class counts are
\[
6,\quad10,\quad14.
\]

For \(\mathbf F_2\), all \(16\) matrices are Rota–Baxter and the checker finds exactly \(6\) similarity classes, agreeing with
\[
q^2+q.
\]

The checker returns `VERIFY_OK`.

Finite enumeration is a replay check. The arbitrary-prime-power formulas are established by the field-level proof in `RESULT.md`.
