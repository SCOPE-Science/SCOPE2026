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

# Computational corroboration

Run `python3 verify_odd_bipyramid.py` with Python 3; no third-party libraries are required. The script constructs convex hulls by monotone chain and independently checks their vertices against the supporting-side criterion for 40,000 random-view cases, with a fixed seed. It compares empirical frequencies to the exact probability, locates stationary heights, and tests the claimed large-order constants for multiple odd polygon orders.

The proof, not the script, establishes the infinite family, uniqueness, and asymptotic behavior. Float arithmetic cannot certify exact equality at degenerate viewing directions (which have Haar measure zero), and numerical sampling cannot establish historical originality. Independent mathematical audit has not been performed.
