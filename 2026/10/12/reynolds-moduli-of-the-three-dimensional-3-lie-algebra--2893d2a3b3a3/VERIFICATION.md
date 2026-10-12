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
The packaged checker `artifacts/verify.py` constructs the alternating bracket
\[
[e_1,e_2,e_3]=e_1
\]
and the four-term Reynolds defect.

For a general \(3\times3\) matrix \(R\), it verifies symbolically that the entire defect is determined by
\[
\det(R)e_1-(\sigma_2(R)-\det(R))R(e_1).
\]

It then exhaustively checks every \(3\times3\) matrix over
\[
\mathbf F_2
\qquad\text{and}\qquad
\mathbf F_3
\]
against both the direct Reynolds identity and the structural criterion.

The totals are
\[
208
\qquad\text{and}\qquad
3537,
\]
with rank profiles
\[
(1,49,150,8)
\]
and
\[
(1,338,2928,270).
\]

The checker also verifies the closed total and rank formulas for
\[
q=2,3,5,7.
\]

It returns `VERIFY_OK`.

Finite exhaustive checks are replay evidence. The arbitrary-field theorem and all finite-field formulas are proved in `RESULT.md`.
