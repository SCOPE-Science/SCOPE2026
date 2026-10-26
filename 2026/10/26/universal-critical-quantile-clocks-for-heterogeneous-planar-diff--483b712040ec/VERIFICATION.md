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

# Verification and reproducibility

The theorem is derived analytically in `RESULT.md`. `verify.py` uses Python 3, SciPy and NumPy; run it as `python3 verify.py` from the directory containing the files. The run in this package completed with `PASS: 75 independent finite numerical assertions`.

The numerical checks independently integrate the continuous radial density over the observation disk, compare the stationary modified-Bessel formula with direct exponential-age quadrature, and compare the renewal formula with an independent integrated relaxation-excess formula. They verify numerical critical-root ordering, the closed-form intercept ratio, and the decreasing finite-error trend toward the critical time expansion across several small critical distances. All tests concern finite parameter sets and numerical tolerances; they are not an infinite-dimensional proof, exact-arithmetic certificate, or independent audit.

A derivation requiring no numerical assumptions establishes the free mass \(F_\beta(t)\), its strictly negative derivative, the monotone stationary fraction, the unique critical root, and the uniform endpoint expansion of the exact relaxation excess. Strict temporal monotonicity and a two-sided finite-window sign bracket prove the crossing-time expansion. For the Bessel normalization and derivative, standard identities for \(K_\beta\) are used.

Scientific limits: instantaneous Poisson resetting to the origin; disk occupation, not first-passage survival; fixed positive observation radius, fixed shape and quantile; no uniformity when physical parameters scale jointly; no operational-time memory. Results about uniqueness and the near-critical limit depend on the displayed analytic proof, not on the finite tests. Independent audit status: not performed.
