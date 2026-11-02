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

# Reproduction and limits

Run `python3 verify.py` with Python 3.9 or later; no nonstandard libraries or external files are required. The program builds actual cyclic substring multisets, groups all binary necklaces of lengths at most 16, and compares the resulting inverse class sizes with an independently evaluated totient–binomial formula for every eligible two-run periodic target. A separate constructor redistributes run lengths using a deterministic pseudo-random seed and compares read multisets directly.

Observed execution:

```text
VERIFY_OK exhaustive_parameter_k_cases=568 cyclic_necklaces_examined=8914 independent_constructed_words=26160 max_exhaustive_n=16 max_constructed_t=6
```

The exhaustive ranges are finite and do not establish an infinite theorem by themselves. The general statement instead follows from the run-detection and Burnside arguments in `RESULT.md`. No independent scientific audit has been performed.
