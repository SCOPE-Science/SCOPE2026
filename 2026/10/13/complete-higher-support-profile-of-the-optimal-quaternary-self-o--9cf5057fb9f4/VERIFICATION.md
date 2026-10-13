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

It realizes
\[
\mathbb F_{16}=\mathbb F_2[\beta]/(\beta^4+\beta+1)
\]
and verifies that \(\beta\) has order \(15\). The embedded subfield
\[
\mathbb F_4=\{0,1,\beta^5,\beta^{10}\}
\]
is identified with
\[
\{0,1,\omega,\omega^2\}.
\]

The verifier forms
\[
R=\{0,1,2,3,4,5,6,8,9,12\}
\]
and rebuilds
\[
g(x)=\prod_{i\in R}(x-\beta^i).
\]
It checks that all coefficients lie in \(\mathbb F_4\), converts them to the recorded degree-ten generator, verifies divisibility by \(x^{15}-1\), rank \(5\), and Euclidean self-orthogonality.

All
\[
4^5=1024
\]
codewords are enumerated, giving
\[
1+45z^8+210z^9+270z^{11}+210z^{12}+270z^{13}+18z^{15}.
\]

For every
\[
1\le r\le5,
\]
all \(r\)-dimensional subspaces of \(\mathbb F_4^5\) are generated exactly once in reduced-row-echelon form. The checked counts are
\[
341,\ 5797,\ 5797,\ 341,\ 1.
\]
For each basis the coordinate support union of its codewords is computed and compared with the complete histogram in `artifacts/certificate.json`.

The total number of positive-dimensional subspaces checked is
\[
12277.
\]
Successful replay prints `VERIFY_OK`.
