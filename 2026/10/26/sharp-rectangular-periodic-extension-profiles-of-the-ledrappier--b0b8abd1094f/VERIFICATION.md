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

The accompanying `ledrappier_verify.py` is a standalone Python 3 exact finite-field check. Run `python3 ledrappier_verify.py` from the directory containing this file and the script; no third-party dependencies are required. Its successful exact output is:

`VERIFY_OK: n=1..34; widths/heights through min(8,n+3) for n<=16; exhaustive n<=10 tests`

The script computes \(\gcd(t^n-1,(1+t)^n-1)\) over \(\mathbb F_2\), constructs the entire cyclic-kernel basis, tests the rectangular projection ranks directly from the three-dot recurrence for several widths and heights, tests the Mersenne and power-of-two boundaries, and independently enumerates all periodic seed vectors for small periods. It does not prove universal rank and arithmetic claims for arbitrarily large integers; those follow from the constructive proof in RESULT.md. No external proof or independent audit was performed.
