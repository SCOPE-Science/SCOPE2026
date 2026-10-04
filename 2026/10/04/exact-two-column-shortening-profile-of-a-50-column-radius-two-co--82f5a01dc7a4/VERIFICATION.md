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

Run `python3 artifacts/verify.py` from the package root.

The verifier uses only the Python standard library and reconstructs the fixed set of 50 decimal columns. It checks that the labels are distinct, nonzero, and below \(2^{10}\), then verifies that the original set covers all \(1024\) syndromes by sums of at most two columns.

As an external anchor, it recomputes the published single-deletion fact: the minimum number of uncovered syndromes after one deletion is \(9\), attained exactly by columns \(381\), \(479\), and \(927\).

For the new claim, every one of the \(1225\) two-column deletions is evaluated twice. The direct route rebuilds the shortened sumset. The incidence route first lists every original representation support of size at most two for every syndrome and then tests whether all supports meet the deleted pair. The verifier requires pointwise equality of the two routes before comparing the complete defect histogram and the exact minimizer list with `artifacts/double_deletion_profile.json`.

The finite domain is exhausted; there is no random sampling or timeout-dependent inference. The computation proves only the stated profile of this fixed seed. It does not test all 48- or 49-column subsets of \(\mathbb F_2^{10}\) and does not establish a new global lower bound for the covering-code length function.
