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

# Verification details

Run the standalone `verify.py` with Python 3. It requires only the standard library. The finite test uses integer square roots for the Sturmian ceiling of \(\alpha=(\sqrt5-1)/2\), exactly enumerates rational Parikh classes for \(2\le q\le13\), and tests period-dividing-q candidates for \(1\le q\le13\) against the first 260 mechanical symbols. Its success output is:

`VERIFY_OK Lyndon_extremal_cases=12758 golden_periods=1..13 accepted_words=5873 rigid_q=[2, 5, 13]`

The mathematical proof is in `RESULT.md`; finite tests are diagnostic only. The exact beta-shift membership of a general infinite periodic sequence is not certified merely by passing 260 finite prefix comparisons; the proof of universal admissibility and exclusion is analytic. No third-party independent audit is asserted.
