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

# Verification record

The proof is self-contained in `RESULT.md`: its crucial determinant/cofactor identity, the two positive-order characteristic coefficients and the stationary-trace interpretation are all stated and derived for arbitrary positive rates. These steps imply the all-rate, all-dimension law without finite enumeration.

`verify.py` is a standalone exact-rational Python 3 script requiring only the standard library. It constructs generators independently of the closed-form law, uses an exact Faddeev–LeVerrier characteristic polynomial for small matrices and checks coefficient equality, two-hop neutrality, the sharp direction of each sign, worst-shortcut adjacent comparisons, and heterogeneous counterexamples. The observed outcome was `PASS 9920 exact rational assertions`. Those tests verify the implementation on a finite sample, not all integer sizes and positive real parameters.

This record does not constitute independent peer review or formal certification. Remaining scientific limitations include unsearched or inaccessible specialized antecedents and noncovered mixing metrics.
