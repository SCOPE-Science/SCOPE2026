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

The standard-library script `check.py` was executed successfully against the source and comparison laws stated in the finding. Its exact-rational part verified 240 algebraic/moment assertions, and three further numerical tolerance assertions passed. The script prints convergence profiles at \(n=1000,4000,16000\) for three finite critical-window parameters and a supercritical example. The observed values and all assertion counts are stored verbatim in `check_output.txt`. These finite checks are not an infinite proof. The proof in `RESULT.md` establishes the full limiting statement using a real-rooted generating function, an exact second-moment identity, a Bessel central limit theorem, a Gaussian likelihood-ratio tilt, and a supercritical mean-separation estimate. Independent validation has not been performed.
