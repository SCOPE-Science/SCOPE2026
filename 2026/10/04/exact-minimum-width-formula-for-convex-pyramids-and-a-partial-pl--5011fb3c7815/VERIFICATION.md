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

The argument is analytic. The critical calculation is the exact width in direction
\[
u=re+\sqrt{1-r^2}\,n:
\qquad
w_K(u)=r a(-e)+\max\{r a(e),h\sqrt{1-r^2}\}.
\]
The switch occurs at \(r=h/\sqrt{h^2+a(e)^2}\). Before the switch the expression is concave in \(r\), so its minimum is at an endpoint; after the switch it is linear and nondecreasing. This yields the exact formula without discretizing directions.

If the apex projection is outside the base, strict separation supplies \(e\) with \(a(-e)<0\), and the tilted widths \(h\sqrt{1-r^2}+r a(-e)\) are strictly below \(h\) for sufficiently small positive \(r\).

The packaged `verify.py` performs supplemental finite checks on several polygonal bases by comparing the formula to a direct dense directional sweep and by checking the one-dimensional branch minimum. These checks passed when replayed from the packaged path. They are not used to infer the theorem for arbitrary bases or dimensions.
