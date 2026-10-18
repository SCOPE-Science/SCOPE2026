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

# Verification of the exact normality criterion and enumeration

Running `python3 verify.py` requires only the Python standard library. It exhausts ordered pairs of partitions of \(n\) labelled points for \(1\le n\le 6\). It checks pointwise nesting versus incidence-graph leaves, checks equality of bundled and distributed-knowledge operators on every proposition when nesting holds, checks the coefficient recurrence, and for \(1\le n\le 4\) directly checks the meet law for all ordered pairs of propositions, both positive and negative cases.

The expected counts at \(n=1,2,3,4,5,6\) are \(1,4,19,111,774,6229\). The checker prints `BUNDLE_NORMALITY_CENSUS_OK` on success. The attached mathematical argument establishes arbitrary finite size; exhaustive finite checks independently test the definitions but do not replace the all-size proof.

No independent audit has been performed. Priority against every historical result is not certified.
