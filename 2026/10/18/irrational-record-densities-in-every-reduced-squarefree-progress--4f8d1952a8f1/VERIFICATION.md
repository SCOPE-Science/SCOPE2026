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

# Finite verification and proof boundary

Run `python3 verify.py` using the standard Python library. The verifier regenerates records with the exact least-missing-prime rule through 30,031, checks 90 residue-class primorial recurrences in eight natural moduli, and computes rational series truncations. All tests terminate and use exact integers or rational arithmetic until decimal display. `VERIFY_OK` signifies agreement only on these finite checks.

The infinite theorem requires the cited primorial-copy theorem, Dirichlet's theorem, and the prime number theorem. In particular, arbitrarily large prime positions in a reduced residue class establish strict positivity of every tail; finite numerical experiments alone would not. An equivalent result in unindexed literature is possible. Independent audit has not been performed.
