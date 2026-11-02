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

# Verification of the genus-five \(\mathbb F_5\) example

The packaged `verify_finite.py` runs with Python 3 and the standard library. It independently reevaluates the three forms and their symmetric matrices at all 781 rational projective points, enumerates the 31 rational quadric-net directions, checks their ranks, and computes the four relevant nonsquare determinants. The observed outputs were `NET_RANK_COUNTS {4: 4, 5: 27}`, the directions \([1:0:0]\), \([1:0:1]\), \([1:4:0]\), \([0:1:2]\) with determinant classes \(2,3,3,3\), exactly the two stated rational curve points, and `FINITE_VERIFY_OK`.

The packaged `verify_smooth.py` runs with Python 3 and SymPy 1.14.0 (or a compatible version). It evaluates all ten \(3\times3\) Jacobian minors, dehomogenizes in all five standard projective charts, and checks that the generated ideal has reduced Gröbner basis \(\{1\}\) over \(\mathbb F_5\). Each chart returned the unit ideal, followed by `GEOMETRIC_SMOOTHNESS_VERIFY_OK`. This is an algebraic-closure smoothness argument, unlike a finite-point-only test.

Published Lemma 6.6 of Faber and Grantham provides the necessary degree-four pencil criterion. Arithmetic gonality five follows from this criterion, the computed net classification, the canonical geometry of genus-five complete intersections, and Riemann–Roch. The verification does not prove that this is the first such example in the entire literature, nor does it replace independent assessment.
