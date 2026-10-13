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
The bundled checker `artifacts/verify.py` reconstructs the two Leibniz brackets and exhaustively determines their algebra automorphism groups over
\[
\mathbf F_2,\quad\mathbf F_3,\quad\mathbf F_5,\quad\mathbf F_7,\quad\mathbf F_{11}.
\]

For every displayed coalgebra parameter, it independently checks the Leibniz coalgebra identity and both compatibility identities from Definition 2.4 of the lead source.

It implements bialgebra pushforward and verifies
\[
\gamma\mapsto t^3\gamma
\]
on the first algebra,
\[
(A_0,\gamma)\mapsto(t^2A_0+t(t-1)\gamma,t\gamma)
\]
on the first family of the second algebra, and parameterwise fixedness of the second family.

The exact replay rows are:
\[
\begin{array}{c|cc|cc|c}
q&\#A&\#(A/\!\cong)&\#B&\#(B/\!\cong)&\#\text{ total classes}\\
2&2&2&5&5&7\\
3&3&2&11&8&10\\
5&5&2&29&12&14\\
7&7&4&55&16&20\\
11&11&2&131&24&26
\end{array}
\]
matching the formulas
\[
1+\gcd(3,q-1),
\qquad
2q+\gcd(2,q-1),
\]
and
\[
2q+1+\gcd(2,q-1)+\gcd(3,q-1).
\]

The checker returns `VERIFY_OK`.

Finite enumeration is replay evidence. The arbitrary-field orbit classification follows from the symbolic automorphism and pushforward formulas in `RESULT.md`.
