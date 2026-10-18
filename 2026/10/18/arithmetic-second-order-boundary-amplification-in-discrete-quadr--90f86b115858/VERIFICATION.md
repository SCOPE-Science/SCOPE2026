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

The supplied `verify.py` requires only the Python standard library. The checker reconstructs all sample moments with `Fraction`, computes every boundary kernel coefficient independently, verifies row sums and Bernoulli exact-value identities, and tests the asymptotic residual at six increasing grid sizes. Running `python verify.py` returned `PASS: 8461 exact-rational and high-precision assertions`.

Finite tests are not a proof of the universal statements. The exact formula is proved by orthogonal polynomial reproduction and finite quadratic summation. The asymptotic limit set uses a uniform Bernoulli expansion and density of an irrational circle rotation. No independent audit has been performed.
