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

The theorem is based on an explicit infinite-state transfer/renewal identity and analytic singularity analysis. The script `check.py` is standalone and may be run with Python 3 using `python check.py`. It recomputes finite-step transition coefficients using exact rational numbers and checks the first-return formula independently. It also compares the predicted asymptotics at two interior opening parameters.

The script's recorded output is in `CHECK_OUTPUT.txt`; it ends in `CHECKS_PASS`. Exact rational checks apply to finite indices only; they are not a proof of the all-time asymptotic theorem. The main proof controls the critical analytic singularity, the unique leading singularity, coefficient extraction, and total-variation convergence; it does not certify results about other initial distributions or endpoint-uniform parameters. Independent audit has not been performed.
