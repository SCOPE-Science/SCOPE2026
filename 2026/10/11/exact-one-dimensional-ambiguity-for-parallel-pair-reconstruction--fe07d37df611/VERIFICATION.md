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

For
\[
F=(Y-\alpha)(Y-\beta)
\]
and
\[
H=aX^2+bXY+cY^2+rX+sY+t,
\]
the checker symbolically differentiates and verifies
\[
J(F,H)=-(2Y-\alpha-\beta)(2aX+bY+r).
\]
It then verifies that every kernel element is a unique combination of \(1,F,Y\) after coefficient comparison.

For the source's Example 7.6 it checks
\[
J(Y^2-1,X^2-1)=-4XY,
\]
\[
J(Y^2-1,4X^2-Y^2+6Y-9)=-16XY,
\]
and the normalized difference
\[
\frac14(4X^2-Y^2+6Y-9)-(X^2-1)
=-\frac32-\frac14(Y^2-1)+\frac32Y.
\]
Thus the example occupies the nonzero class \(\lambda=3/2\).

The symbolic checks are supplementary. The proof for every field of characteristic different from \(2\) is the exact polynomial-factor and coefficient argument in `RESULT.md`; no finite experiment is used as an infinite proof.
