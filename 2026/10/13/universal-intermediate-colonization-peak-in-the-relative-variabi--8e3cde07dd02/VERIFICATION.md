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

The standalone source `verify_extinction_cv.py` was executed with Python 3 and no external packages. The observed output was:

```
VERIFY_OK connected_labeled_counts= [(2, 1), (3, 4), (4, 38), (5, 728)] two_patch_exact_points=7 additional_examples=4
```

For each labeled connected simple graph through five vertices, the checker forms the exact zero-colonization backward recurrences for the first and second moment derivatives at zero and verifies the universal singleton identities. It then solves the exact finite-state moment equations for the two-site edge at seven rates and for selected three- and four-site landscapes at two rates each.

The unrestricted graph-order theorem uses the independent birth-path and regenerative-cycle reasoning in the proof; no finite census is substituted for that infinite family of graphs. The high-rate convergence is analytic and has no numerical cutoff claim. The demonstrated maximum of \(5/4\) is specific to the two-site edge; it is not a universal upper bound for larger networks.
