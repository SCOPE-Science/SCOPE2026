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

The proof was replayed exactly from the displayed norm.

1. For \(uv\ge0\), the two comparison residuals are
\[
\|w\|_{2,\infty}^2-H(w)^2=\frac{(u-v)^2}{4}
\]
and
\[
\frac32H(w)^2-\|w\|_{2,\infty}^2=\frac{u^2+6uv+v^2}{8},
\]
both nonnegative.

2. For \(uv\le0\), after writing \(a=|u|\ge b=|v|\), the residuals are
\[
\|w\|_{2,\infty}^2-H(w)^2=\frac{(a-b)(a+3b)}{4}
\]
and
\[
\frac32H(w)^2-\|w\|_{2,\infty}^2=\frac{(a-3b)^2}{8},
\]
both nonnegative.

3. The quadratic form for \(H^2\) is positive definite, so the ordinary Ptolemy inequality applies to \(H\). Combining the two pointwise norm comparisons on the two numerator factors yields the global upper bound \(3/2\).

4. For \(x=(-1,-1)\), \(y=(2,-2)\), \(z=(1,-3)\), the six relevant norms are \(3,3,2,2,\sqrt2,\sqrt2\), giving Ptolemy ratio \(9/(4+2)=3/2\).

No computation, search result, or inaccessible source is used as a substitute for a proof step. Literature-access limitations affect only the originality comparison.
