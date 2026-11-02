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

# Reproducibility and checks

Run `python verify_bicylinder_general.py` using Python 3 with SymPy, SciPy and NumPy installed. The script is supplied in full and fixes its pseudo-random seed.

The actual execution returned:

`VERIFY_OK 4791 checks; exact identities, independent optimization, contacts and containment`

The checks include exact symbolic differentiation of the determinant objective, a stationary-equation identity, normalized two-layer covariance identities, independent bounded scalar numerical minimization at \(144\) dimension/shape test cases, polynomial stationarity residuals, both endpoint inclusion equalities, random interior-section tests, points on the continuous contact ridge, the sharp limiting ratio bounds, and strict sample-wise monotonicity. The code's low-dimensional regression cases also check the familiar scalar setting without including it in the proposed theorem's scope.

No finite test certifies the continuum of radii, arbitrary dimensions, historical priority, or any independent mathematical validation. Universal correctness follows from the explicit proof in `RESULT.md`. The full unrestricted John–Löwner optimality follows from uniqueness plus body symmetries, and is cross-checked by positive normalized contact certificates.
