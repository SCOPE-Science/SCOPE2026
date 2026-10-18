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

# Verification of the cyclic-companion local-exponent result

The result gives exact algebraic identities, an analytic limiting argument, and an explicitly cited seed power-set theorem. The following independent-of-external-packages finite diagnostics were actually executed from the accompanying `checker.py`:

```
PASS: 1148 finite algebra and Fourier assertions
Excluded: infinite-dimensional power-set and compactness proofs; these are analytic.
```

The diagnostics test the cyclic power identity, block resolvent factorization, discrete Fourier recovery, and nilpotent zero-seed boundary on finite coordinate truncations for several block counts. All tests completed successfully. To reproduce, run `python checker.py` using Python 3 and its standard library.

The analytic derivation of the operator-resolvent estimates and local exponent formula is written in `RESULT.md`; the example's infinite full-power-set conclusion uses the explicitly cited published decreasing-weight theorem. The polynomial resolvent lower bounds prove that the seed satisfies the required uniform growth limit. Compactness and noncompactness assertions follow from the direct-sum block structure and infinite-dimensional identity corner, not from finite truncations.

Limits: finite diagnostics do not prove an infinite-dimensional result; the cited external theorem is a mathematical premise rather than a software certificate. No independent mathematical audit, external certification, or exhaustive publication-priority determination has been performed.
