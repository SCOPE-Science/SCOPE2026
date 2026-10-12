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
The packaged checker `artifacts/verify.py` reconstructs the Jordan identity and the Rota–Baxter basis equations symbolically from the displayed multiplication.

It verifies the automorphism form
\[
\begin{pmatrix}1&0\\t&s\end{pmatrix},\qquad s\ne0,
\]
and the exact conjugation formula.

It then exhaustively enumerates all \(2\times2\) maps over
\[
\mathbf F_2,\quad\mathbf F_3,\quad\mathbf F_5,\quad\mathbf F_7,
\]
checks the Rota–Baxter identity on all ordered basis pairs, enumerates every algebra automorphism, and constructs all conjugacy orbits.

The observed counts are:
\[
q=2:\ 6\text{ operators and }4\text{ classes};
\]
\[
q=3:\ 9\text{ operators and }3\text{ classes};
\]
\[
q=5:\ 25\text{ operators and }3\text{ classes};
\]
\[
q=7:\ 49\text{ operators and }3\text{ classes}.
\]

The checker returns `VERIFY_OK`.

Finite enumeration is only a replay check. The arbitrary-field classifications and all-prime-power formulas are proved symbolically in `RESULT.md`.
