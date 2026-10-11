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

The proof was checked from the defining geometry. For \(-b<y<a\), the triangle's horizontal width is \(2w(a-y)/(a+b)\), so removing the cap above \(x=he^t\) gives
\[
f(t)=\frac{w}{a+b}\big((a+b)^2-(a-x)^2\big).
\]
Differentiation with respect to the dilation parameter gives the exact factorization
\[
f f''-(f')^2=-\left(\frac{w}{a+b}\right)^2 2x\left(ax^2+(4ab+2b^2)x-ab(2a+b)\right).
\]
The quadratic factor is strictly increasing for \(x>0\), so its unique positive zero is the claimed threshold. The equality case was checked separately: when \(h=h_*\), every sufficiently small negative parameter has \(he^t<h_*\), producing positive logarithmic curvature and therefore defeating two-sided local log-concavity.

The symbolic checker `verify_threshold.py` replays the factorization, confirms the two radical formulas for \(h_*\) are identical, and checks the published special case \((a,b,w,R,S,h)=(3,2,5,6,3,1)\), for which \(h_*=4/3\) and \((\log f)''(0)=26/441\).

The proof does not use enumeration, floating-point optimization, or a timeout as evidence. It does not establish global log-concavity outside the local one-active-side regime.
