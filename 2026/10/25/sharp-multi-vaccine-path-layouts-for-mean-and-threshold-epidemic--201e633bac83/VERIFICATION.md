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

Run `python3 verify.py` in the directory containing `verification_certificate.json`. Its standard-output JSON must match that file after stripping the terminal newline. The verifier uses Python standard-library `fractions.Fraction`, not floating point; direct edge-state enumeration gives 168 cases, and optimization over 31,584 gap compositions gives 168 parameter configurations.

Analytically, the decisive steps are enumeration of maximal edge-open runs, the strict risk-reduction identity \(c-a(t-1)=-(t-1)p^t\), and the discrete mean convexity \(H(L+2)-2H(L+1)+H(L)=2p^{L+1}\). The general result is a pencil-and-paper theorem, not a conclusion extrapolated from tests.

No independent audit has been performed.
