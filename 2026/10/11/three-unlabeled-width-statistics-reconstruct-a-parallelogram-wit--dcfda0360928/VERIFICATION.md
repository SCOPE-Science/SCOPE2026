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

The analytic derivation establishes the width identity, the exact three scalar measurements, the strictly positive scalar derivative, the inverse reconstruction, and the optimal Hölder exponent. No finite computation is used to establish an infinite quantifier.

For a reproducible numerical supplement, place `verify.py` next to this document and run `python3 verify.py`. The script uses only the Python standard library and returns `VERIFY_OK 7019` on success. It checks numerical angular integrals, limiting maxima, the inversion for 2,000 pseudorandom positive parameter choices, a 1,001-angle monotonicity grid, and the equal-sided quadratic perturbation. The grid does not prove monotonicity; the displayed symbolic derivative does.

Boundary cases \(a=b\) and \(\phi=\pi/2\) are handled by the proof. Degenerate segments are excluded. Roundoff sensitivity increases near zero angle or exact equality of side lengths; the script is illustrative, not a validated numerical inverse under noise. No independent audit has been performed.
