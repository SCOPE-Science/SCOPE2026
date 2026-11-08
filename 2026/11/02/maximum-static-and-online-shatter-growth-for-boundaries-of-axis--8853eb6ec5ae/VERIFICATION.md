---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The five-dimensional lift v(x,y)=(x²,y²,x,y,1) along a first-quadrant circle arc lies in four-dimensional hyperplane. The restricted functions 1,t,t²,sqrt(1-t²) form a four-point Chebyshev family: four zeros would force a nonzero third derivative to vanish, impossible for t in (0,1). Thus every four distinct lifted rows are independent and have a unique ellipse kernel close to (1,1,0,0,-1). For finitely many sample tuples, sufficiently small perturbations preserve positive quadratic coefficients and nonempty nondegenerate conics; all five-fold determinants are nonzero on a dense-open choice because the determinant is a nonzero polynomial (an explicit five-point witness). For every selected <=4 subset, avoid the remaining finite proper hyperplanes in its valid-ellipse coefficient subspace. No five positive incidences survive; all <=4 subsets do. A dimension-5 lifted representation gives upper VC 4; along all-positive branch depth 5, each negative alternative forces next independent row, contradiction for all-positive leaf, bounding Littlestone 4. Both Sauer bounds yield exact n-polynomials. Independent rational determinant checks on seven witness points confirmed all 35 quadruple positive ellipse kernels and 21 fivefold nonincidences; the theorem for all n is analytical, not extrapolated.

## originality

PASS

PASS best-of-knowledge: primary prior Guingona–Kolesnikov–Nierwinski–Soucy explicitly establish ellipse VC/Littlestone dimension 4 and maximum growth for the LARGER class of unrestricted zero sets of five functions. Their Example 6.2 flags positivity-restricted ellipses as not covered by that maximum theorem. Present generic perturbation completes this restricted-subfamily gap, not a fresh claim for dimensions alone.

## value

PASS

The exact growth, not only VC/Littlestone dimension, is a natural combinatorial invariant of ellipse-boundary incidence. Establishing all-size maximum growth for the geometrically constrained positive-coefficient subfamily resolves a concrete gap explicitly signposted in primary prior work, with a useful perturbative interpolation witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
