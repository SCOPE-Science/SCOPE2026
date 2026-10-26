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

An all-size analytical derivation appears in RESULT.md. A separate pure-Python verifier constructs the killed generator on all ordered distinct-vertex pairs, rather than relying on the lumped two-class generator. For each test graph it uses exact Fraction Gaussian elimination to compute first and second moments and the killed-resolvent Laplace transforms at three rational positive parameters. It verifies 1,190 exact identities across eight graph families: (r,m)=(3,1),(4,1),(5,1),(2,2),(3,2),(4,2),(2,3),(3,3).

Run: `python3 meeting_checker.py`. Expected: `PASS: 8 graph families, 1190 exact rational moment/transform identities.` No external packages.

The finite arithmetic tests are corroborating examples, not an exhaustive proof for all graph orders, not experimental evidence for priority, and not independent scientific validation.
