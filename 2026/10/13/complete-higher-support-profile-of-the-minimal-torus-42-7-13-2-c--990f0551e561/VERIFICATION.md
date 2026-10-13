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

It constructs the fourteen cyclic facets
\[
\{i,i+1,i+3\},\qquad\{i,i+2,i+3\},\qquad i\in\mathbb Z/7\mathbb Z,
\]
and generates every nonempty face. It checks the f-vector \((7,21,14)\), that every edge is in exactly two triangles, every vertex link is a six-cycle, and that the triangle orientations can be chosen consistently.

The face-incidence generator is checked to have length \(42\), rank \(7\), row weight \(13\), and ordinary weight distribution
\[
1+7z^{13}+42z^{20}+43z^{21}+21z^{24}+14z^{25}.
\]

Every positive-dimensional subspace of \(\mathbb F_2^7\) is generated once in reduced-row-echelon form. The dimension counts
\[
127,\ 2667,\ 11811,\ 11811,\ 2667,\ 127,\ 1
\]
are checked against Gaussian binomial coefficients. Every subcode support is computed as the union of the supports of its RREF basis words, and the complete histograms are compared with `artifacts/certificate.json`.

Successful replay prints `VERIFY_OK`.
