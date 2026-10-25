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
Run `python3 verification/verify.py` with Python 3.10+; no third-party packages are needed. The verifier independently performs direct subsequence universality tests over all allowed words at \(0\le n\le12\), \(1\le R\le6\), and checks against the displayed coefficient polynomial. A separate state-machine dynamic program checks length/index coefficient arrays to length 96 for run caps up to 12; it verifies the maximum support and two endpoint examples through index 14. Expected output: `RLL_BINARY_UNIVERSALITY_PASS` with recorded check counts. These finite calculations do not prove the all-length theorem. The formal-series recurrence and leading-coefficient proof are given in RESULT.md; no external code or data are required.
