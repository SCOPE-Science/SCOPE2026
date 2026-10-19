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
# Verification of the reset lattice-walk crossover

Use Python with `numpy>=1.24` and `scipy>=1.10` and execute `python artifacts/verify.py`. The source file is a standalone checker; it does not depend on a different research artifact or another entry. The calculation uses an independently assembled finite-ring Liouvillian with site-projector dephasing and reset source, compares against an infinite-line FFT inversion, evaluates independent time-integrated Bessel amplitudes at zero dephasing, and verifies exact second/fourth moments. It separately integrates the complex-branch cut formula and numerically tests the crossover near the weak-dephasing limit. Output observed on the packaged source:

`VERIFY_OK finite_lindbladian=28 bessel_integrals=5 stationary_moments=4 tail_checks=7 branch_cut=15 crossover=3 max_error=1.4e-09`

Finite rings only approximate the infinite line for sites whose distance is small compared with the ring circumference, and these tests span finite grids only. The \(m\to\infty\) asymptotics, contour inversion and universal double scaling are established by analytic identities and estimates in `RESULT.md`, not by numerical extrapolation. The displayed maximum error measures the finite-ring comparisons, not a universal mathematical error bound. No independent audit was performed.
