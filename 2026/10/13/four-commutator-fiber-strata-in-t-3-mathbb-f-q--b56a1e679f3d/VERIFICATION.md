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

For
\[
A=\begin{pmatrix}a_1&p&h\\0&a_2&r\\0&0&a_3\end{pmatrix},\qquad
B=\begin{pmatrix}b_1&s&t\\0&b_2&u\\0&0&b_3\end{pmatrix},
\]
direct multiplication gives the three commutator coordinates used in the proof. Two common diagonal-shift variables never enter those coordinates, accounting for the final factor \(q^2\).

The critical count is reduced to determinant fibers in \(\mathbb F_q^2\). A zero determinant has \(q^3+q^2-q\) ordered vector-pair representations, while every fixed nonzero determinant has \(q(q^2-1)\). On the exceptional locus where the final linear equation loses both coefficients, the proof explicitly counts triples of vectors with prescribed pairwise determinants. These symbolic counts establish the theorem for every prime power.

`artifacts/verify.py` performs an independent finite replay. It exhaustively enumerates all ten effective coordinates for \(q=2,3,5\), checks every target against the four closed formulas, directly enumerates every ordered pair of full matrices in \(T_3(\mathbb F_2)\), and checks the target-weighted total against \(q^{12}\) for integer \(q\) from \(2\) through \(20\). The recorded successful output is in `artifacts/verify_output.txt` and ends with `VERIFY_OK`.

The finite replay is not an infinite proof and is not used as one. No claim is made for \(T_n(\mathbb F_q)\) when \(n\ge4\).
