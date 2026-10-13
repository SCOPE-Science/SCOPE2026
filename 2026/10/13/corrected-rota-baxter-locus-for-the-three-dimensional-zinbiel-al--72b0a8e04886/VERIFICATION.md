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
The packaged checker `artifacts/verify.py` reconstructs the multiplication and the weight-zero Rota–Baxter defect directly.

For a general matrix
\\[
R=\\begin{pmatrix}a&u&v\\\\ b&c&d\\\\ e&f&g\\end{pmatrix},
\\]
it verifies that the basis-pair equations reduce over a field to
\\[
u=v=0,\\qquad 2ad=0,\\qquad a(a-2g)=0.
\\]

It evaluates the printed-family witness
\\[
\\begin{pmatrix}1&0&0\\\\0&0&1\\\\0&0&1/2\\end{pmatrix}
\\]
over \\(\\mathbb Q\\) and confirms failure at \\((e_1,e_1)\\).

It exhaustively enumerates all linear maps over \\(\\mathbf F_2\\) and \\(\\mathbf F_3\\). The exact solution counts are
\\[
64,
\\qquad
891,
\\]
and the rank histograms agree with the closed formulas in `RESULT.md`.

The checker returns `VERIFY_OK`.

The arbitrary-field theorem is proved symbolically; finite enumeration is only a replay check.
