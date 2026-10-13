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

The result concerns only finite binary word lengths from three through sixteen. The two standard-library Python programs `verify_dp.py` and `verify_direct.py` were executed from the packaged sources and returned `VERIFY_DP_OK` and `VERIFY_DIRECT_OK` respectively. The first uses an inductively justified subsequence-count update; the second counts every increasing triple by direct index combinations. Both enumerate every possible input word at each indicated length, not a sample. The asserted maxima and the entire length-sixteen fiber-size histogram agree; all arithmetic is exact integer arithmetic. The total number of words recovered from the histogram is \(65536\), and the number of nonempty classes is \(36649\), matching the independently published distinct-deck count. No claim beyond length sixteen, or of independent audit or machine formalization, is made.
