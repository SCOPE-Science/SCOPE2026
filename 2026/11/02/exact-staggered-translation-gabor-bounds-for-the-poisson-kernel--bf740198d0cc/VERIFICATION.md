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

# Verification record

The exact analytical proof is in `RESULT.md`. The Fourier transform convention makes the Poisson-kernel Fourier transform equal to \((\pi/w)e^{-2\pi w|\xi|}\). Poisson summation gives the explicit Zak amplitude; its limiting squared values are \(H_w\) at midfrequency and \(P_w\) at the frequency endpoints. The first is minimized by a strictly convex, increasing scalar map of the cosine; Jensen's inequality is attained at an explicit spatial phase. The second is maximized by the endpoints at half staggering, and an evaluation at the origin strictly distinguishes all competing staggering values.

`CHECK.py` uses only standard-library computations and prints `CHECK_OK` on success. It cross-checks direct truncated Zak Fourier series against the closed expression, sharp minimizing phases, the exact half-shift upper endpoint, and the small-offset asymptotic; the continuum and infinite-dimensional claims are proved on paper, not certified by the checker. Numerical truncation has no bearing on a logical proof of the frame inequality.

The sharp upper-bound function for arbitrary staggering, the complete class of irregular time-translation sets, and further modulation spacings are **not** classified. Priority relative to possibly implicit historical special cases remains a source risk. Independent audit and independent validation are not performed.
