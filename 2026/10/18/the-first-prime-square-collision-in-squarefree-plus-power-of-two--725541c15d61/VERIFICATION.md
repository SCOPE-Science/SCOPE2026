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

The standalone `verify.py` performs exhaustive residue checks for \(1\le d\le20\) and all candidate primes below \(1024\), enumerates all \(2^{18}\) exponent subsets for the special modulus \(25\), and checks the collision correction in a finite rational product model with sixteen other primes. It must return `VERIFY_OK`. The proof of infinite prime relative densities requires Siegel–Walfisz and the fixed-shift moment bound stated in `RESULT.md`; finite tests do not establish those results. No independent audit has been performed.
