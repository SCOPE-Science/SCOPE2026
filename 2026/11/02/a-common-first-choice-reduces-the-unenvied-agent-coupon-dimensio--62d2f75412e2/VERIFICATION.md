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

The exact mathematical statement is in `RESULT.md`, with definitions, hypotheses, coupling steps and all-size quantifiers. Run `python3 verify.py` in a folder containing the package files; `verify_output.txt` preserves the genuine output of the same source. The verifier performs full enumeration for every flagged-position subset and every admissible strict preference tuple at \(n=2,3,4\), computes RSD and the unenvied count directly, and compares each histogram with a separately calculated exact-rational coupon absorbing-chain distribution. It verified 810,521 cases with no discrepancies.

The finite checker does not establish a theorem about larger markets, and its output should not be read as a proof by exhaustion of infinite sizes. The general result is supported by the raw-stream coupling and removal of the shared, necessarily repeated favorite school, as explained in `RESULT.md`. The reference coupon-singleton formula is taken from Myers and Wilf, arXiv:math/0304229v1, Section 4, formula (49). No independent external scientific audit or validation is claimed.
