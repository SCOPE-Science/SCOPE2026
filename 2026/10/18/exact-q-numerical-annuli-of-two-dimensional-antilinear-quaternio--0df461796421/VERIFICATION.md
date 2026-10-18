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
# Mathematical verification

The canonical reduction is established directly in `RESULT.md`, using \(A^2=-\rho^2I\), operator-norm attainment in complex dimension two, and the eigenspaces of \(A^*A\). For each \(|q|\le1\), a complete parametrization of constrained pairs reduces sharp extremal moduli to the norm-one circle identity \(k^2+|q|^2=1\). Compactness and rotational connectedness establish the full annulus, not just its two boundary radii.

Run `python3 check.py` from the extracted package using the standard Python library. The program checks the antilinear square exactly up to roundoff for sampled vectors, constrained inner products and norms, explicit inner and outer radius attainments, complex phases, the hole-collapse boundary and a rational numerical example. Its checks are finite and exploratory, not an exhaustive proof or independent certification.

All claims are confined to two-dimensional complex Hilbert spaces and antilinear operators whose square is a strictly negative real scalar. The completeness and novelty comparison of earlier literature retain the limitations described in `RESULT.md` and `REVIEW.md`.
