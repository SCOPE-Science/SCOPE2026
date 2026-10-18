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

# Reproducibility and exact limits

The included C++17 full orbit/enumeration source is `smooth_cubic_pencils_f3_v2.cpp`; its exact stdout/stderr are `smooth_cubic_pencils_f3_v2.out` and `smooth_cubic_pencils_f3_v2.err`. It emits `smooth_ids.txt`, listing all 16,848 normalized smooth ternary cubic forms.

The independent `verify_geometric_smoothness.py` calculates all three affine-chart Gröbner bases over the field of three elements for each of the 25 orbit representatives. `verify_geometric_smoothness.out` records ten geometrically smooth orbits (16,848 forms), fifteen singular orbits (12,676), and the complete total 29,524.

The independently programmed `verify_direct_tally.py` enumerates every ordered pair of the 16,848 smooth projective cubic forms rather than relying on projective-orbit weights. Its saved output `verify_direct_tally.out` reproduces all base-point counts and the total 87,348,456 ordered generator pairs. Every final stratum count is an exact integer quotient by twelve.

The main C++ checker tests singular points over extensions of degrees at most three. This is sufficient for a geometrically singular plane cubic over the field of three elements: an absolutely irreducible singular cubic has a unique singular point, necessarily rational; a reducible cubic has intersecting line/conic components defined over extensions of degree at most three, forcing a singular intersection in one of those extensions. Independently, the Gröbner checker proves the geometric smoothness status without relying on this extension bound.

The explicit sharpness pair was separately checked by affine-chart Gröbner calculations for each of its four rational members; its four common rational points are listed in `RESULT.md`.

All claims are finite-field exact statements for the specified pencils. An independent audit of the mathematics and bibliographic priority has not been performed.
