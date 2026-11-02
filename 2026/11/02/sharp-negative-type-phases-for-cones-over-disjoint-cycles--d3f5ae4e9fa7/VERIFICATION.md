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
# Verification of the analytical claim

The result is proved by the finite graph metric's anchored Gram matrix and its exact invariant Fourier eigenspaces, with an arithmetic argument excluding equality of the two competing thresholds. No finite computation is represented as a proof for unbounded cycle sizes or counts.

Run from the extracted package root:

```sh
python verification/verify.py
```

Observed output:

```text
VERIFY_OK: 499 independent finite Gram-eigenvalue tests over cone cycles; locality-to-global transition verified
```

The standard-library script independently assembles all hub-to-rim and rim-to-rim distances from the cycle data and uses Jacobi rotations to estimate the Gram eigenvalues. It checks the full predicted spectrum, positivity before the sharp threshold, endpoint nullity, negativity beyond the threshold, and localized-to-global cases with appended triangles. Numerical comparison tolerance is at most \(3\times10^{-7}\); it is a robustness test, not a formal interval certificate. No independent audit or validation has been performed.
