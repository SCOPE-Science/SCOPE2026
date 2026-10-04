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

The proof is analytic. The key exact reduction is
\[
\frac1q\,\partial_v\log P_q
=
\frac{(1-u)(u+v)^{q-1}+u(uv)^{q-1}-1}
{(1+v)[1+(u+v)^q+(uv)^q]}.
\]
All denominator factors are positive in the interior parameter region. The proof therefore depends only on the sign of the numerator.

For \(0\le q-1\le1\), convex interpolation between \(\Phi_0=1\) and \(\Phi_1\le1\) gives the sign. For \(-1<q-1<0\), the convex tangent bound at zero and \(\Phi'_0\le0\) give the opposite power-sum sign required by the entropy normalization. The weighted AM–GM step proving \(\Phi'_0\le0\) was checked independently against its arithmetic mean \(\Phi_1\).

`verify.py` evaluates the derivative identity by centered finite differences on a deterministic parameter grid, tests the \(\Phi_r\) sign inequalities at representative orders in both regimes, and checks the resulting entropy monotonicity on a dense deterministic grid. It also verifies representative \(q>2\) local failures. The script prints `VERIFY_OK` on success.

The finite grid is not an exhaustive proof and is not used to infer the theorem. It is only a reproducibility check for algebra, sign conventions, and implementation of the formulas. The \(q=1\) Shannon endpoint and the \(q>2\) sharpness obstruction are literature inputs identified in arXiv:1810.09791.
