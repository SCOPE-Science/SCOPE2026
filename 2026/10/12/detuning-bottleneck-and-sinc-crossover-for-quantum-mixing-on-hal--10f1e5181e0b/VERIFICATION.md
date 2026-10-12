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

# Verification of the magnetic-cycle detuning theorem

Run the embedded standalone `verify.py` with `python3 verify.py` in the same directory. It uses only Python's standard library. A successful run prints:

`VERIFY_OK instantaneous_darkness=24 half_flux_distance_entries=88 gap_pairs=3144 quadrature_checks=24 max_quadrature_error=2.9e-08 max_scaling_error=2.25e-05 critical_limit_n4_s073=0.143393432078`

The checker independently verifies direct half-flux antipodal amplitude cancellation at several times, the stationary matrix for all vertex separations on even cycles \(n=4,6,\ldots,18\), the lower gap bound at positive and negative detunings, independent time-domain quadrature of the spectral average, and the critical-window sinc limit for selected scaled times.

**Proof checks independent of floating point.** The exact spectrum is \(2\cos(\theta+2\pi k/n)\). At half-flux, equal eigenvalues occur only at paired indices \(k\) and \(n-1-k\); their antipodal Fourier factors have opposite signs. For nonzero detuning up to \(\pi/(2n)\) in magnitude, the sine-product identity yields a gap of at least \((8/\pi)\sin(\pi/n)|\delta|\). The finite-time dephasing bound and Duhamel difference bound prove the upper and lower cutoff estimates. Keeping only the \(n/2\) nearly degenerate pairs proves the scaling profile. These algebraic and analytic steps, not the finite checker, establish the theorem for all even \(n\ge4\).

**Limits.** A test over finitely many sizes, times and detunings is not an exhaustive or infinite-domain certificate. The checker uses floating-point tolerances. There are no explicit optimal constants for the threshold, and no claim of independent review.
