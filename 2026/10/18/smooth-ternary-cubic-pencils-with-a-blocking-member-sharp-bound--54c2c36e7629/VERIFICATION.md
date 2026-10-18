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

# Verification of exact enumeration

Run `python verify_ternary_pencil.py` with Python 3 and SymPy. The script completes exhaustive cubic-form normalization, finite incidence tests, PGL-orbit enumeration, exact modular Gröbner chart tests, and all complementary pencils for one smooth blocking cubic. Its expected asserted output includes: 29524 ternary cubics, 936 blocking curves without rational lines, a single orbit of size 936, 1152 generators surviving only the rational singular-point sieve, 936 geometrically smooth admissible complementary generators, 312 pencils through the fixed blocking cubic, and 292032 total pencils; the per-blocking-fiber profiles are 24, 132, 42, and 114. The rational sieve is necessary only for efficiency, not for proving smoothness.

Exact geometric smoothness is checked in the polynomial ring over F3 by finding the unit Gröbner basis for the cubic and its partial derivatives in each affine projective chart. The verified orbit statement reduces every smooth blocking cubic to the explicit one; the threefold overcount is exact because every F3-pencil has four projective parameter points. The thirteen rational points provide a finite exhaustive incidence universe; they do not suffice by themselves to test geometric singularities, which are separately checked.

Verification does not include independent expert checking or validation of a publication's novelty; those remain open.
