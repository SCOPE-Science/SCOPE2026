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

The analytic verification begins with the double-brane expressions for \(c_{\mathrm{eff}}\), \(c_{\mathrm{cap}}\), and \(c_{LR}\), substitutes the symmetric radii, and eliminates the fixed tension sum in favor of \(t=c_{LR}/c\). The remaining coordinate \(d=(x-y)/2\) gives the identity
\[
\frac{c_{\mathrm{cap}}}{c}=\frac{r^2}{t}-r^2td^2.
\]
The strict Israel intervals are then intersected with the fixed-sum line, yielding exactly \(r/(1+2r)<t<r\) and \(|d|<1-|1/t-1-1/r|\). Since the quadratic coefficient of \(d^2\) is strictly negative, the equality and sharp-infimum statements follow globally.

The accompanying `artifacts/verify.py` checks the symbolic rearrangements numerically over deterministic feasible samples and verifies the source's two displayed examples, including \(35/48\). These finite checks only guard arithmetic and parameter conventions; the universal claim rests on the analytic derivation above.
