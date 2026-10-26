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

# Verification and scope

Run `python3 quiver_matroid_verify.py` from the directory containing this file. The saved output `quiver_matroid_verify_output.txt` is produced by that program; its principal success markers are:

```
STAR_QUIVER_PROJECTIVE_SUPPORT_CHECKS_PASSED cases=3 subsets=41088
INDEPENDENT_ENDOMORPHISM_IDEMPOTENT_CHECK_PASSED supports=128 bad=92 idempotent_eigensupports=28
```

It performs complete projective-support enumeration in the listed \((q,r)\) prime-field cases and counts matrices/tested idempotent eigensupports independently over \(\mathbb F_2\). It computes finite probabilities using independent surjection/Stirling counts. It does not enumerate arbitrary-length quiver representations, all finite fields, or prove any infinite limiting statement; these follow from the displayed proof's finite-cover argument. The direct count of distinct maximal line–hyperplane supports is \(Dq^{r-1}\), with maximal size \(H+1\). The formula requires fixed \(r\ge3\), nonzero arrows and source labeling. Scientific claims have received self-review only; external independent audit is not performed.
