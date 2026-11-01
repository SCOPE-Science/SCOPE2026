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

# Reproducibility and scope of checks

Run `python3 truncated_cube_checker.py` using Python 3.9 or newer (standard library only). Expected successful final status: `TRUNCATED_CUBE_HARMONIC_INTERVAL_CERTIFICATE_OK 0..5=1,3,5,7,9,11; 9=10; other_ge6=12; tail_ge162; exact_cubic_orbit_resonances`.

The checker uses \(10^{220}\)-scaled outward-rounded integer intervals, an exact integer-square-root bracket for \(\sqrt2\), and the three-term Legendre recurrence to check the positive \(LDL^T\) pivots for every applicable degree through 161. Its exact rational-pair arithmetic in \(\mathbb Q(\sqrt2)\) verifies two independent null vectors. The continuous parameter identity is verified by matching all coefficients of an integer polynomial (including the equality of every normalized diagonal and off-diagonal block). For the second resonance it certifies a ten-by-ten positive minor; positivity and the factored quadratic form provide the two-dimensional nullspace.

The checker verifies the strict dot-product bound \(|t|<\sqrt3/2\) and integer inequality \(484<3\cdot162.5\). The proof uses the stated classical Bernstein inequality and Gershgorin's theorem for all degrees \(k\ge162\). This analytic step is essential: checking degrees 0–161 alone does not imply the infinite assertion.

An executable certificate does not imply formal proof or independent mathematical validation; the proof's mathematical premises and certified arithmetic were reviewed only in the self-review.
