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

# Reproducible checks and limits

Execute `python3 verify.py` with Python 3 and no third-party libraries. The code works over the prime field of order \(1000003\); for each \(2\le n\le20\), it constructs explicit coefficients \(a\), forms \(A,S,W\), checks \(\deg W=3n-2\), and verifies that \(A\), \(S\), and \(W\) have no unwanted shared or repeated factors. An actual execution produced `VERIFY_OK`.

These are exact arithmetic tests for finitely many degrees and do not imply the theorem for all \(n\). The general proof uses the factorization of the stationary equation, the degree cancellation, nonvanishing at infinity, and a generic two-jet incidence argument. The main remaining uncertainty is bibliographic, not a known computational counterexample. No independent audit has been performed.
