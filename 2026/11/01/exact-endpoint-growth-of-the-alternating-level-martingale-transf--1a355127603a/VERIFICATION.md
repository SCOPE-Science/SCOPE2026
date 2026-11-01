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

The self-contained verifier is `verify.py` and uses only the Python standard library. It constructs every tested transform entry afresh from the conditional-expectation definition, compares exact rational absolute row sums with the closed expression, verifies attaining sign vectors, and checks the exact depth increments. Observed result: 20 configurations and 1,182 exact-rational assertions passed. The proof in `RESULT.md` covers all positive integer branching factors and depths; finite tests are independent spot checks, not exhaustive infinite certification. No external independent audit has been performed.
