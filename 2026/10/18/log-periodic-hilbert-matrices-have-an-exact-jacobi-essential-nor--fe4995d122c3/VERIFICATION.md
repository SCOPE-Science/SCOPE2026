---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For omega>0 and real |epsilon|<1, the half-line row-weighted Hilbert matrix differs by a Hilbert-Schmidt cell-discretization and compact averaging/multiplier terms from the Carleman compression. The logarithmic change of variable gives convolution with K(t)=1/[2cosh(t/2)]; translations by a full modulation period furnish weak-null norm witnesses proving half-line essential norm equals the full-line norm. Positive periodic multiplier bounds all Floquet fibers by the zero-phase fiber, whose Fourier matrix is B=(I+epsilon(S+S*)/2)diag(pi sech(pi omega j)). Norm-perturbation and the finite-section tail yield the certified bound. The simple top eigenvalue of B*B at epsilon=0 and two ±1 couplings give quadratic coefficient (1+3r²)/(4(1-r²)); sign-conjugation eliminates odd orders. Independent finite sections tested several omega and amplitudes; infinite assertions rest on functional analysis, not numerical SVD.

## originality

PASS

No inspected primary or indexed result was shown to imply the exact final claim (not merely its tools, endpoints, or analogous construction). Structured same-object, broader-implication, equivalence, and table comparisons below document precise boundaries; best-of-knowledge and residual risks explicitly retained.

## value

PASS

A positive periodic row multiplier defeats the usual scalar slowly-varying-coefficient reduction. The operator-valued Floquet norm identity, explicit compact Jacobi matrix, exponential finite-section error and frequency-dependent small-amplitude curvature give mathematically meaningful, reusable spectral data for a natural Hilbert-matrix family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
