---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

With C_k the coefficient of e^(ikt) in the intensity, each k=2n−j>n has only the term b·conj(a_j), recovering the head even if it contains zeros. At smaller positive lags, subtract the fixed head products; the data for z=a_n are conj(a_(n−k))z for k<n and conj(a_0)z+b·conj(z) at k=n. The squared change on a perturbation h is S|h|²+|conj(a_0)h+b·conj(h)|². On the unit circle the cross term ranges over its full phase, so the claimed squared extremes are attained, including when a_0=0 or the middle is empty. At rank loss, S=0 and |a_0|=|b|. Rotate z by a unit square root of b/conj(a_0); the remaining positive lag fixes the rotated real part and C_0 fixes the modulus. Exactly the stated reflected pair results, possibly coincident. On the full sequence this is conjugate reversal times the unique phase preserving b and a_0. A 4n+1 grid separates the Fourier modes −2n through 2n. With m≥2n+1 every reference-to-unknown lag exceeds n and separates. All arguments include n=1.

## originality

PASS

Pass is for the all-signal classification at exact support-distance equality and the residual singular values there. Strictly separated reconstruction, finite inverse Fourier inversion, and conjugate reversal itself are known and not credited. The inspected plausible matches use strict geometric separation, different measured data, or generic uniqueness rather than this single reference and touching lag.

## value

PASS

The neighboring outer-lag method ceases to isolate one coefficient at exactly the critical spacing. A complete classification there for arbitrary complex data, including zero coefficients and singleton fibers on the reflection axis, is a natural inverse-problem boundary result. The exact conditional spectrum quantifies ill-conditioning near the exceptional stratum, which the mere symmetry or generic uniqueness would not show.

The dated certificate retains the supplied scientific assessment, sources and limitations.
