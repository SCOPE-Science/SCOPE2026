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

The standalone Python standard-library certificate `verify_uncentered_prism.py` was run from its supplied directory. It exhausts every one of the 46,656 uncentered row-ball selections; fraction-free integer elimination proves that 46,638 selection matrices lie strictly below squared norm \(81/50\). The 18 remaining matrices have the same exact factored characteristic polynomial and explicitly permuted positive Perron vectors.

The verifier also uses exact rational interval arithmetic around the isolated cubic root to check all 540 strictly active-versus-competing ball inequalities. An independent 729-selection integer test establishes a strict centered squared-norm upper bound of \(3/2\). The source code regenerates the graph and balls and depends on no external numeric package or precomputed data.

Expected output:

```text
CERTIFICATE_OK selections=46656 strict=46638 exceptional=18
CERTIFICATE_OK characteristic=[1,-48,675,-2868,4288,-2048,0]
CERTIFICATE_OK active_competitor_inequalities=540 rays=18 orbit_types=6+12
CERTIFICATE_OK centered_strict_lt_3/2=729 uncentered_gt_81/50
```

The finite enumeration is exhaustive only because six vertices have exactly six distinct containing balls each. It is not a claim about larger prism graphs or general metric spaces. The root identity, Perron argument and reduction of nonlinear maximization to finite matrix norms are supplied in the proof. Independent scientific validation has not been performed.
