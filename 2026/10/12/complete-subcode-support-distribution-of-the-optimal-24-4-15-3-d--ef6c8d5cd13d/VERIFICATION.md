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

It implements
\[
\mathbb F_{27}=\mathbb F_3[X]/(X^3+2X+1)
\]
and the absolute trace
\[
\operatorname{Tr}_{27/3}(x)=x+x^3+x^9.
\]

It reconstructs
\[
D_1=\{(x,1):x\in\mathbb F_{27}\setminus\mathbb F_3\}
\]
and the four generator rows corresponding to
\[
(1,0),\quad(\alpha,0),\quad(\alpha^2,0),\quad(0,1).
\]
The verifier checks length \(24\), rank \(4\), and the published ordinary weight enumerator
\[
1+16z^{15}+54z^{16}+8z^{18}+2z^{24}.
\]

All subspaces of \(\mathbb F_3^4\) are generated in unique reduced-row-echelon form. The dimension counts are checked as
\[
40,\quad130,\quad40,\quad1.
\]
For each basis the union of the corresponding codeword supports is computed, and the resulting complete histograms are compared with `artifacts/certificate.json`.

The minima are checked to be
\[
(15,21,23,24),
\]
matching the source hierarchy.

Successful replay prints `VERIFY_OK`.
