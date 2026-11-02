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

# Verification summary

The self-contained `verify.py` uses exact integer counts and rational arithmetic. It independently enumerates every Dyck path through semilength 11; computes ballot-prefix counts, peak totals and final-step counts through length 120 using finite-state dynamic programming; and checks all closed-form conditional expectations and strict grid concavity to semilength 500. It additionally checks the leading scale of optimizing heights at three large sizes.

Execution from the packaged source produced: `PASS: 160183 exact assertions, full-path enumeration to semilength 11, ballot DP to length 120`.

These checks test stated finite cases and the implementation's reproducibility. The unlimited parameter and asymptotic claims require the independent symbolic and analytic proof in `RESULT.md`, not mere extrapolation from experiments. No external or independent audit has been performed.
