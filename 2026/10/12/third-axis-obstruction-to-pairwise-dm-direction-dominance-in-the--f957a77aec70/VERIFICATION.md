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

The analytic proof uses only the published single-axis concurrence expressions and elementary monotonicity. For the family \(J_x=0\), \(J_y=-a\), \(J_z=a\), \(D_x=D_y=a\), the \(D_x\) Wootters weights occur in two equal pairs, so its concurrence is exactly zero for every positive temperature. The \(D_y\) sign reduces to the function \(H\) displayed in `RESULT.md`; its derivative is strictly positive for positive argument, which proves the unique threshold without numerical assumptions.

`verify.py` checks the specialized weights, evaluates the strict reversal at \(T=a\), and brackets the root numerically. The decimal root is not used as an infinite-domain proof.

Limits: this verifies the stated one-parameter family and continuity consequence, not a complete ordering theorem for arbitrary XYZ couplings. Independent validation has not been performed.
