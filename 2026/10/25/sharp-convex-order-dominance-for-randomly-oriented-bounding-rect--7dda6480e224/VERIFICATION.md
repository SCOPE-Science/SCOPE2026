---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

By Cauchy projected-perimeter identity, w_K(theta)=1/2∫|cos(theta−phi)| ds and the normalized bounding-box perimeter is Z(theta)=∫q(theta−phi)dnu(phi) with q(t)=|cos t|+|sin t|. Uniform-rotation Jensen proves E Phi(Z)<=E Phi(q) for every convex Phi and identical mean 4/pi. The Fourier expansion q=4/pi−(8/pi)Σ_{m>=1}cos(4mt)/(16m²−1), Parseval, and |c_m|<=1 give Var Z=(32/pi²)Σ|c_m|²/(16m²−1)² and maximum 1+2/pi−16/pi². First harmonic defect gives 64/(225pi²) double integral of sin²(2(phi−psi)); equality |c1|=1 forces all arclength tangents in two perpendicular axes, so a full-dimensional convex body must be a rectangle. Strict convex Jensen equality implies the same variance equality, and trigonometric inversion yields survival 4/pi arccos(t/sqrt2) on [1,sqrt2]. Independently checked the exact rectangle mean and variance by integration.

## originality

PASS

Classical Cauchy widths and Jensen’s inequality provide direct proof tools, but Akiyama–Kamae optimize dispersion of a single random-direction width and Audet–Hansen–Messine optimize deterministic minimum width. Their results do not imply the complete convex-order distributional comparison for the sum of two perpendicular widths, aspect-ratio-independent rectangle law, and exact stability spectral defect. Best-knowledge originality, with explicit chance that general harmonic convolution contraction is known in another form.

## value

PASS

Bounding rectangles are canonical enclosing shapes. The theorem simultaneously solves all convex orientation penalties for any planar convex body, proves the unusual aspect-ratio-independent extremizer law, and gives a quantitative first-harmonic stability test. This is a natural probabilistic geometric extremal problem, beyond a single numerical variance calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
