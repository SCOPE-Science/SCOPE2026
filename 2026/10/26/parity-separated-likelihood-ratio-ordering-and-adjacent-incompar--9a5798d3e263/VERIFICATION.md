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

# Exact verification

Run `python3 verify.py` using the Python standard library. The script produces:

`VERIFIED: 128 checks, including exhaustive matchings through 14 endpoints`

The checks compare exact factorial probabilities with enumerated matchings, normalize probability distributions, verify mean and two-step likelihood-ratio identities, and test the asserted stochastic comparisons for sizes up to seven chords.

This is finite corroboration only. The general proof is the double-factorial cross-pairing enumeration, likelihood-ratio factorization with a positive derivative, the shared-parity boundary mass, and the adjacent upper/lower tail witnesses. No external or independent audit has been performed.
