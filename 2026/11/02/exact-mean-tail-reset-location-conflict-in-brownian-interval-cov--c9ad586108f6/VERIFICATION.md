---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For all L,D,r>0 and 0<=z<=L, the two-single-target-minus-first-either-target survival identity follows from inclusion/exclusion without an independence assumption. Nonreset hitting transforms solve D f''=q f with one absorbing/one reflecting boundary, and the resetting renewal mean (phi(r)^(-1)-1)/r gives the exact displayed three-cosh mean. Setting C=cosh(s/2), a=C^2-1, t=cosh(s(u-1/2)) reduces the derivative sign to a quadratic in t^2, with one positive root; P_a(1)=5a^2-1 and P_a(C^2)=-1 yield the claimed spinodal and absence of interior minima. The exact endpoint-minus-midpoint difference (C-1)(2C^2-C-2)/C yields s*=2 arcosh((1+sqrt(17))/4). For tail, the one-sided killed reflected-reset diffusion admits a simple Perron decay rate; monotonicity of one-sided nonreset survival in starting distance propagates through renewal-root monotonicity. The two-sided first-hit survival exponent is strictly faster than each one-sided exponent, so inclusion-exclusion leaves min(lambda_left,lambda_right), uniquely largest at midpoint. Checked boundary initial-hit convention and p=1 not applicable. Independently evaluated dense grids of mean curves across both thresholds and confirmed optimizer switch and equality at s*. These grids do not establish spectral asymptotics or global uniqueness; the analytic proof supplies those.

## originality

PASS

PASS best-of-knowledge for sharp fixed-rate reset-position phase diagram and all-position exponential-tail optimizer, not for known cover mean/renewal formulas. Read closely relevant primary PDFs and compared parameter that is optimized (position versus frequency), reset location and retained endpoint flags.

## value

PASS

A reflected interval with two targets and reset-position design is a natural stochastic search setting. The exact discontinuous mean-optimal-site switch and the contrary universally center-optimal tail decay expose distinct risk-sensitive optimization criteria. This is a substantive structural transition beyond routine substitution of the already-known mean; proof of tail noncancellation and location monotonicity is essential. No claims beyond Poisson resets/persistent memory or for finite-time quantiles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
