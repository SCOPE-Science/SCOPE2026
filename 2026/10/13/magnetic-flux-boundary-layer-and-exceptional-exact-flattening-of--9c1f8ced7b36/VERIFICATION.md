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
# Verification of the flux-window cycle theorem

The analytic proof in `RESULT.md` is the primary verification. The implementation in `verify.py` uses the exact spectral pair integration and an independent composite-Simpson quadrature of the state-amplitude Born probabilities, with no numerical matrix packages needed. Run:

```
python3 verify.py
```

A successful execution reports `VERIFY_OK chiral_cycle_flux_window=passed`. Cases exercised include a range of cycle dimensions, finite-window normalizations, generic-flux infinite-duration approximations, weak-flux inverse-duration scaling, and integer-multiple resonances for the three exceptional dimensions. Representative non-resonance tests are finite checks only. They cannot certify uniqueness across all integers or a continuum of scaled times; that uniqueness follows instead from Fourier invertibility, the zeros of the integral kernel, and algebraic-integer obstruction given in the written proof.

Scientific limitation: the phase model is a uniform nearest-neighbor magnetic ring with fixed finite size, and all zero-error resonances refer to an asymptotic boundary-layer distribution, not to an exact finite-duration experiment. Independent external assessment is not included.
