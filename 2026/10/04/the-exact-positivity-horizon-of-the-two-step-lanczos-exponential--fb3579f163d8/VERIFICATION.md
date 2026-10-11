---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

The two-step Krylov approximation is exactly the affine Ritz interpolant: polynomial exactness gives \(y_2(t)=q_t(A)b\). With at least three active spectral values, an affine polynomial cannot isolate either extreme eigenspace, so both Ritz values are strictly interior. Since the exponential interpolant is strictly decreasing, every physical-coordinate sign is controlled by \(q_t(L)\), whose numerator is strictly decreasing in time and has the unique stated zero. The active-support size at most two case is exact by the degree-two minimal polynomial. A fresh exact reconstruction of the stated three-dimensional witness reproduced \(\alpha_1=13/7\), \(\beta_1^2=20/49\), \(\alpha_2=37/14\), Ritz values \(3/2,3\), and the negative multiplier \(-1/16\).

## originality

PASS

Classical sources provide polynomial exactness, convergence and reduced Jacobi-coordinate positivity. The closest titled source is Druskin's monotonicity paper, whose indexed scope is Krylov-dimension norm monotonicity/total positivity rather than a physical-coordinate time horizon. Current Resultary and web searches for physical-coordinate positivity, sign loss, affine Ritz interpolation and the exact horizon found no covering theorem. Best-of-knowledge originality therefore survives, with a residual access risk because the closest full article could not be reopened through the available lawful route in this run.

## value

PASS

Coordinatewise positivity is a natural structural constraint for exponential actions arising from diffusion/parabolic models, while standard Lanczos theory controls approximation error or reduced coordinates rather than reconstructed physical signs. The theorem gives the exact safe-time frontier, proves inevitable late-time failure in every nontrivial two-step diagonal case, and identifies the minimal dimension. This is a motivated sharp boundary, not a finite spot check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
