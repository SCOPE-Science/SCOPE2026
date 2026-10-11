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

Normalize the regular simplex by
\[
\lVert v_i\rVert=1,
\qquad
v_i\cdot v_j=-\frac1n\quad(i\ne j),
\qquad
\sum_i v_i=0.
\]
Its reflected-intersection kernel is exactly
\[
K_n=\{x:|v_i\cdot x|\le1/n\}.
\]
Thus every defining support hyperplane has distance \(1/n\) from the origin, giving the inradius.

With
\[
y_i=n\,v_i\cdot x,
\]
the tight-frame identity gives
\[
\sum_i y_i=0,
\qquad
|y_i|\le1,
\qquad
\lVert x\rVert^2=\frac{\sum_i y_i^2}{n(n+1)}.
\]
The remaining optimization is therefore the squared radius of the central cube section. Its extreme points have at most one nonsaturated coordinate. When \(n+1\) is even, balanced cube vertices lie in the section. When \(n+1\) is odd, the saturated coordinates must balance and the lone remaining coordinate is zero. These two cases give the exact formulas in the finding.

`verify.py` independently constructs the zero-sum simplex model, verifies its Gram matrix and frame operator, enumerates all cube-section vertices for \(2\le n\le10\), and checks both the maximum squared norm and the exact number of maximizers.

The enumeration is diagnostic only. The parity argument proves the result for every \(n\ge2\).
