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

# Reproducibility

Run `python verify.py` with Python 3; only the standard library is required. The script constructs the canonical witness for each valid histogram through \(m=28\), uses an independent two-bit-state dynamic program to enumerate all attainable histogram vectors through \(m=40\), and enumerates literal binary words through length 16. It additionally tests all length-\(2h+1\) words for widths \(3\le h\le8\) against the one-extra-occurrence obstruction.

Expected successful output:

```text
VERIFY_OK constructive_histograms=28273 DP_degrees=1..40 DP_distinct_profiles=113650 literal_words=131064 boundary_binary_words=174720 windows=3..8
```

These finite checks test the construction, cardinality formula, and boundary but cannot establish validity for arbitrary lengths. The full infinite assertion rests on the explicit proof in RESULT.md. The extra profile forbidden at width four is `(1,1,2,1,1)` for six width-four windows. No proof assistant or independent expert audit is asserted.
