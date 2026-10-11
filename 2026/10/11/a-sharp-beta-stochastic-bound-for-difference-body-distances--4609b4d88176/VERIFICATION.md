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

# Verification record

The proof is analytic and valid for all integer dimensions \(d\ge2\); `verify.py` is a supplementary reproducibility check and not an exhaustive proof.

Executed from this package using Python 3's standard library: `python3 verify.py`.

Actual output:

```
VERIFY_OK: exact beta normalization/moments in dimensions 1..40;
exact planar-square CDF gap; 100000 seeded simplex Monte Carlo samples
```

The checker verifies rational beta CDF normalization and first/second moments, and the simplex variance identity, in 40 dimensions. It verifies the polynomial identity for the planar square exactly. The simulated test draws barycentric uniform points in five dimensions (20,000 point pairs per dimension) and checks sample means against the exact beta means with a specified absolute tolerance. This simulation is diagnostic only; the strict stochastic comparison for arbitrary convex bodies relies on the fully stated concavity, conditional-likelihood-ratio and equality arguments in `RESULT.md`.

Critical mathematical boundaries: no numerical sample verifies a universal quantifier; the Rogers–Shephard equality case is used as a cited classical theorem rather than re-proved; older equivalent published statements might exist. Independent audit has not been performed.
