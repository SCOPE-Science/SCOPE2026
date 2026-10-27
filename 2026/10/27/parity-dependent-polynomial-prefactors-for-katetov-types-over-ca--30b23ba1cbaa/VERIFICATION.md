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

`verification.py` uses only the Python 3 standard library. It independently counts admissible distance assignments both by direct enumeration of distance vectors and by a finite-state exact recurrence retaining the last \(D\) values and a minimum over older values. It tests \(D=2,\ldots,7\) and \(n=1,\ldots,6\), for 36 direct comparisons. It independently recomputes the special odd-diameter defect-span convolution for \(D=3,5,7\) through \(n=14\), verifies the closed diameter-three formula through \(n=24\), and prints the predicted constants for \(D=2,\ldots,7\).

The replay command is `python3 verification.py`. The recorded output is in `verification_output.txt`. The program does not certify the asymptotic claim for infinitely many \(n\); the proof uses triangle inequalities, a finite span decomposition, and elementary spectral estimates.
