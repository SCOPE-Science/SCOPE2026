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

# Reproducibility and limits

The standalone program `verify.py` uses only Python's standard library and performs three complementary tests: exact full-factor coverage of all candidate position pairs for \(1\le a,b,c,d\le6\), a separate literal factor-occurrence test for \(1\le a,b,c,d\le3\), and explicit three-position cover verification whenever the analytic phase predicts minimum three. It tests all cases, not a sample, **within these finite parameter domains**. The observed output is:

```
VERIFY_OK quadruples=1296 exact_two_pair_tests=125496 literal_pair_tests=2376 phase_three_cases=325 three_upper_witnesses=TRUE
```

Run `python3 verify.py` after extracting the embedded files of this finding. The program is an independently structured consistency checker for finite cases. Infinite quantifiers, novelty and broader literature coverage are established or limited by the separate mathematical argument and source comparisons, not by these finite checks. Independent scientific audit has not been performed.
