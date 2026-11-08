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
# Verification and limits

Run `python3 verify.py` alongside this file. The program contains no third-party dependencies. Its actual passed output is:

```
PASS: 25 complete maximal-subsequence sets; 11718 common words; 900 independent LCS DP instances; 1600 transfer coefficients
```

The finite checks generate distinct subsequences by a direct set recurrence, determine maximality by attempted insertion of every symbol at every gap, compare every found maximal string against the analytic structural classification, and count them. A separate two-row LCS dynamic program tests the length formula beyond the brute-force range; the rational series is tested via its coefficient recurrence. No finite test is used as an infinite proof; the theorem and recurrence identity in `RESULT.md` are the mathematical proof. All path names are relative to this package. Scientific and bibliographic limitations are described in the result and review. Independent validation has not been performed.
