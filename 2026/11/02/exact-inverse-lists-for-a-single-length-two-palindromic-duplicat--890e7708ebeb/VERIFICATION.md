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

Execute `python verify.py` in the directory containing the verifier. The program enumerates every \(q\)-ary received word in 19 parameter cases: \(q=2\), \(4\le m\le12\); \(q=3\), \(4\le m\le9\); and \(q=4\), \(4\le m\le7\). It computes the set of distinct one-step parents directly from four-letter palindrome windows, separately computes the run statistic, checks their exact equality for each received word, and checks the derived sharp maximum and aggregate incidence count in every case.

Actual execution result:

```text
VERIFY_OK cases=19 received_words=59420 all_parent_sets=checked exact_peak=checked exact_incidence=checked
```

These checks are finite and do not establish the unrestricted integer-domain theorem. The complete all-length argument is given in `RESULT.md`. No independent audit has been performed.
