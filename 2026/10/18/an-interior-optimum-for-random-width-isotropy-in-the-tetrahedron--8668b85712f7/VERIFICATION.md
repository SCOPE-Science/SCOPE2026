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

# Reproducible arithmetic and geometric checks

Run `python verify_truncation_width.py` with a current standard Python 3 interpreter; the checker uses no nonstandard packages.

The exact rational calculations use Machin's identity for \(\pi\), integer square-root bounds, and alternating Taylor bounds for \(\arctan\) to certify that \(0<E<D\), where \(D=\alpha C-\beta B\) and \(E=\beta A-\alpha B\). Reported certified enclosures include \(0.195313965128<t_*<0.195313965398\). The exact checks terminate with `CERTIFIED_RATIONAL_UNIQUE_INTERIOR_OPTIMUM_OK`.

Independent finite cross-checks compare 18,000 direct 12-vertex support evaluations with the asserted formula, 12,000-node Simpson integrations of the five spherical moments, 40,000 direct convex-hull directional-width extrema comparisons, and 10,001 normalized-variance grid evaluations. On successful completion the program prints `ALL_TRUNCATION_WIDTH_CHECKS_OK`. Finite sampling and quadrature are not all-orientations proofs; that proof is given in `RESULT.md`.

This package has not received independent external validation.
