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

# Reproducibility and mathematical boundaries

Run `python3 verify_triangle.py` with `mpmath` available. The script evaluates the exact triangle Fourier-integral expression at four reciprocal-lattice nodes; checks both complex first derivatives, the universal radial second derivative, and the coefficient of the affine weight; and independently locates the real zeros predicted by the fold theorem in the cases where the sign allows a pair. It also checks one non-affine polynomial weight and enumerates lattice-sector incidences at radii \(20\), \(100\), and \(250\).

Successful execution reported the nodal counts \((1148,868)\), \((30876,23192)\), and \((194968,146314)\), with the second entry being the positive-unfolding class. These are *finite* demonstrations only. They neither prove the infinite lattice asymptotic nor exclude unseen zeros in a neighborhood. Both unrestricted conclusions instead follow, respectively, from the strict convexity/implicit-function proof and from sector lattice-point area comparison in `RESULT.md`.

For reproducibility the transform is unnormalized (the triangle has mass \(1/2\)), and all Fourier arguments are angular frequencies. The program's numerical tolerances are not substituted for any exact algebraic identity. The coefficient \(\operatorname{Re}\widehat{g}(\lambda)\) must be nonzero for the two/no-zero classification; at a vanishing coefficient the generic theorem does not claim an answer.

The independent mathematical audit has not been performed.
