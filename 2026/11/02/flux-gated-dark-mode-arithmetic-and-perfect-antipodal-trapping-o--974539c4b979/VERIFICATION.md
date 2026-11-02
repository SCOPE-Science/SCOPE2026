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

# Verification notes

The included `verify_flux_sink.py` ran with `python verify_flux_sink.py` and reported `PASS 3183 finite checks`. Its tests use NumPy/SciPy, independently construct the hopping matrix, evaluate every tested sink-node condition and eigenspace dimension, check orthonormality and eigenvalue equations, and compare the predicted dark projection and direct dissipative evolution for selected ring sizes. The exact theorem follows from the Fourier pair-congruence and semigroup arguments in `RESULT.md`; no finite calculation proves all possible integer sizes or all real fluxes.

The reviewed model has an explicit local sink projector \(\Gamma\ge0\) and strictly positive rates on every listed loss site. These assumptions are necessary to equate zero decay with zero sink amplitude. The proof excludes accidentally degenerate generic flux values analytically. The classification applies to the one-particle subspace and does not certify higher excitation sectors.

The source date is the publicly listed first submission on 2026-04-20; subsequent revisions were not used to determine eligibility. Literature comparison explicitly acknowledges preexisting zero-flux cyclic trap arithmetic. Residual priority uncertainty concerns more general graph-controllability theorems and a relevant abstract-only 2026 chiral-walk manuscript.
