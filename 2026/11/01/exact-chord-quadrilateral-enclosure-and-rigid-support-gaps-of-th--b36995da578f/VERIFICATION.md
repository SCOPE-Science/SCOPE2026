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

# Reproducible checks and boundaries

Execute `python3 verify_heptagon.py` using Python 3's standard library. The certificate computes exact rational enclosures for \(\pi\), \(\sin(j\pi/7)\), and \(\cos(j\pi/7)\) for \(j=1,\ldots,6\), with a uniform fixed-point scale of \(10^{18}\), outward rounding, and explicit analytic Taylor/alternating-series remainders.

The program exhausts 511 bounded four-support chord configurations. Its output reports exactly seven edge-supported winners and 504 strict competitors; every competitor has a certified area difference exceeding \(1/40\) in unit-circumradius normalization. The closest indexed competitor is \(\{0,3,7,11\}\), whose certified gap lower bound at scale \(10^{18}\) is 25947319986048213.

The reduction to the 511 candidates is proved geometrically in `RESULT.md`. The symbolic trigonometric and cubic identities are written there and do not depend on finite numerical sampling. The computation itself is exhaustive **only for that finite support-index list**, and it does not verify any unrestricted enclosing-quadrilateral theorem or the general chord conjecture.

An independent audit has not been performed.
