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

# Mathematical verification and limits

The analytical proof consists of a uniform Hilbert–Schmidt bound for unit-cell discretization of the finite Cesàro-phase commutator, exact logarithmic-coordinate convolution equivalence, a uniformly trace-class finite Wiener–Hopf boundary defect, cyclic trace-moment convergence, moment-to-threshold-measure convergence, and explicit solution of a quadratic inequality in squared Fourier frequency. Every step is detailed in RESULT.md. The limiting superlevel formula is only at fixed positive levels, and the checker is not an infinite proof.

Run `python3 verify_spectrum.py` without third-party packages to replay 70 finite numerical assertions (frequency sign symmetry, root/density agreement by direct Fourier grids, the two-band boundary, and finite-dimensional Hilbert–Schmidt growth trends). The exact order-two coefficient can also be checked directly by integrating \(e^{-s}|e^{-i\omega s}-1|^2\) on \([0,\infty)\). Root calculations use the quartic denominator after the shift \(v=\xi+\omega/2\), eliminating an otherwise easy factor-of-two error in spectral density.

The source comparisons are documented in REVIEW.md and AUDIT.json. Literature-search incompleteness remains a risk; no independent mathematical or bibliographic audit has been performed.
