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

# Reproducibility checks and proven limits

Run `python verify.py` with `numpy`, `scipy`, and `mpmath`. The exact proof is the spherical boundary-integral calculation in `RESULT.md`; numerical diagnostics independently test its central geometric identities.

- Direct planar convex hulls of twelve projected cuboctahedron vertices: 2,400 random Haar-normalized directions, exact combinatorial classification and area formulas, with numerical area error less than \(3\times10^{-12}\).
- Independently parametrized spherical chamber: fifty-digit quadrature checks the exact area and all first moments with absolute difference below \(10^{-44}\), and the predicted weighted chamber integral \(\pi/2\).
- Scrambled Sobol sample with \(2^{19}\) spherical directions checks the octagon frequency and the two exact weighted means, within explicitly asserted sampling tolerances.
- Exact sign uses only \(\arcsin(1/3)>1/3\), \(\pi<22/7\), and \(7\sqrt3>12\), so does not rely on floating-point sign detection.

These finite diagnostic tests do not establish all-directions validity, exhaust random orientations, or prove historical originality. No external mathematical audit has been conducted.
