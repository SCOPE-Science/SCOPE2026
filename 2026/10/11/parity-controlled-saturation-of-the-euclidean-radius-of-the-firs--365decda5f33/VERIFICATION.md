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
# Mathematical verification

Run `python verify.py` in a Python environment with SymPy installed. Its exact rational-field checks reconstruct the quartic five-dimensional certificate, its discriminant factorization, the two-eigenspace first-variation constant, and the three-dimensional scalar quadratic. Additional NumPy matrix regression checks are optional, and their results are not used to infer statements in untested dimensions.

All-domain verification remains the analytic proof in `RESULT.md`: absolute-value comparison, spectral gaps of parity path blocks, and a sharp nonnegative certificate in five dimensions. No independent audit has been performed. No finite sample is asserted to prove the infinite family or its asymptotics.
