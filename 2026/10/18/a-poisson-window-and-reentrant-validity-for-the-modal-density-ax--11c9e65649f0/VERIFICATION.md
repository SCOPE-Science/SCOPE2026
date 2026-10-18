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

# Verification

The standard-library checker `verify_random_density.py` was executed on its packaged source before embedding. It enumerates all loop-free directed relations on 2, 3, and 4 labelled worlds and all truth valuations. It checks frame validity of the modal axiom against the direct no-unwitnessed-arc condition and checks the expectation against the exact first-moment formula at independent arc probability 1/2.

Observed lines:

```
EXHAUSTIVE_MODAL_EQUIVALENCE_OK 2 4 valid 1 E_X 1
EXHAUSTIVE_MODAL_EQUIVALENCE_OK 3 64 valid 2 E_X 9/4
EXHAUSTIVE_MODAL_EQUIVALENCE_OK 4 4096 valid 88 E_X 27/8
RANDOM_MODAL_DENSITY_CHECK_OK
```

The checker prints additional distributions of unsupported-arc counts. The infinite Poisson result is established analytically in RESULT.md; no finite enumeration is offered as a proof of the limiting law. The external literature is not completely accessible; an independent audit has not been performed.
