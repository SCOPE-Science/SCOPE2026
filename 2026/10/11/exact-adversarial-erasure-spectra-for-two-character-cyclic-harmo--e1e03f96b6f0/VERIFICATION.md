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

# Finite checks and proof boundaries

Run `python3 verify.py` from the directory containing the embedded files. No third-party package is needed. The checker exhausts every labelled deletion mask for cyclic orders \(3\) through \(12\), all nonzero frequency differences and all deletion counts. It compares the measured maximum root-sum modulus with the closed arc formula and counts every maximizing mask. It additionally enumerates capacity vectors for several quotient sizes and multiplicities.

The recorded outcome is `VERIFY_OK index_cases= 635 index_masks= 81920 capacity_cases= 246 max_numerical_error= 2.1e-14`. Finite calculations are consistency tests only: for unrestricted cyclic orders the proof uses the exact Fourier character identity and the circular rearrangement argument. No numerical tolerance is used to establish a general implication. The case of a complete deletion has zero retained eigenvalues; the one-ray residual case has zero lower bound.

The result assumes unweighted rows, two-dimensional complex signals, and labelled erasure indices. In particular, an index whose analysis vector lies on the same complex projective ray as another index remains a distinct available coefficient. The values of all discrete parameters and the distinct-frequency hypothesis are stated in `RESULT.md`.
