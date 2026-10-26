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

The standalone `check.py` enumerates all surjective-on-block maps for nine profiles and independently computes the predicted regular totals by summing over the lower maps. It performs explicit generalized-inverse searches in four small profiles; compares the complete upper-to-lower target multinomial in two profiles; and evaluates the limiting regular-density expression against the proved total-variation bound for three fixed backgrounds and twelve upper-block counts each. The companion `check_output.txt` records the actual replay output.

The checker handled 19,954 full maps across its nine direct cases. The mixed profile \((1,1,2,3,3)\) has exactly 6,400 maps and 4,166 regular maps; the exact probability \(2083/3200\) agrees with the proof. The infinite-dimensional theorem, the analytic error bound and the full conditional law follow from the written proof rather than finite sampling.

The package does not contain any independent audit. Reproducing finite counts cannot establish literature priority.
