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

The theorem is proved directly by simultaneous affine normalization, the planar support-function area identity, and exact integration. These analytic steps establish the claim for every positive-definite equal-determinant matrix pair; the finite tests below do not replace proof.

Check the following steps independently: (i) the affine reduction takes the matrices to a unit disk and a reciprocal-axis ellipse; (ii) the active-support switch occurs at \(\beta=\arctan\lambda\); (iii) the boundary area integral equals \(2(\lambda-\lambda^{-1})+4\arctan(1/\lambda)\); (iv) its arctangent simplification is the claimed trace law; (v) the derivative and strict comparison bounds hold for all \(D>0\).

Run `python3 verify_elliptic_hull.py` using a Python 3 standard-library interpreter. The checker compares seven independently sampled convex hulls (including sheared, noncoaxial ellipses) with the exact formula and checks five values of the strict sharp-bound ratio. Its polygonal approximations produce small one-sided area errors; neither this test nor any finite computation proves the all-matrix theorem.

The available calculations and the present analytic reconstruction support the stated exact formula and inequalities. Coverage of old unindexed mathematical tables and a separate independent scientific review are not certified.
