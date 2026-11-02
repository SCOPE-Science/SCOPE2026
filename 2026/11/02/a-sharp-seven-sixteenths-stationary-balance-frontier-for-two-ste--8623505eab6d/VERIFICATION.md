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

# Verification procedure and limits

Execute `python3 verify.py` with Python 3 and no third-party dependencies. The verifier performs 2,637 exact-rational comparisons including a direct matrix inverse of \(I-h\beta_2Q\), the predicted scalar moment formula, every vertex of the two-history simplex square, rational examples at the stationary-balance threshold \(m=7/16\), and explicit finite-time negative-coordinate witnesses beyond both method-parameter boundaries. Expected output:

```
PASS: 2637 exact-rational identities, boundary and matrix checks
```

The proof of all-step, all-history preservation is the exact convex interpolation and affine-extrema argument in RESULT.md; the test grid alone cannot certify the infinite parameter domain. The value \(7/16\) follows algebraically from the nonempty-intersection criterion for the two sharp parameter inequalities. Independent audit has not been performed.
