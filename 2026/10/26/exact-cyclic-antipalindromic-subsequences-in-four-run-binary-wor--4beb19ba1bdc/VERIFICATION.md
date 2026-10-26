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
Run `python3 verify.py` with Python 3.10 or later. The checker constructs every binary four-run word with \(1\le a,b,c,d\le8\) and independently solves the longest reverse-complement subsequence problem by interval dynamic programming over each linear cyclic rotation. There are \(4096\) such tuples. It also enumerates every subsequence by its index mask for the \(495\) quadruples whose total word length does not exceed twelve, without using the recurrence. Finally, it checks the exact balanced minimum for every \(2\le s\le50\) and the explicit constructions. Its observed output was:

`VERIFY_OK dp_quadruples=4096 independent_masks=495 balanced_s=2..50`

The dynamic program relies on the elementary endpoint property: one can discard either endpoint, or pair opposite endpoints and recurse; this is an independent computational route to the finite optimum. The infinite exact formula and sharp finite-size bound follow from the mathematical proof in RESULT.md, not finite tests. No external or independent audit is implied.
