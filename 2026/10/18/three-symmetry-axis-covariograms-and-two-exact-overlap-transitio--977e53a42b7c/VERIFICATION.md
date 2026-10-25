---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

Full analytical proof was reconstructed with correct ray/euclidean scale. A(t)=2−2t+t³/3 on [0,1], (2−t)³/3 on [1,2]; F(t)=(1−t)(2−t) on [0,1]; D(t)=2−3t on [0,1/2] and 4(1−t)³ on [1/2,1], zero past respective supports. Axis profile uses fixed (y,z)-fiber length 2(1−max(|y|,|z|)) and distribution H; facet normal uses u=(x+y)/2,v=(x−y)/2 and Jacobian 2; diagonal uses ρ=max(|u|,|v|,|u−v|) hexagon shell density 6s. Fixed Euclidean r rescales F(r/√2), D(r/√3). Exact difference D−F=(r/2)(α−r) below √3/2; polynomial inequalities show D>A to α. F−A has a concave positive bracket to r=1 and strictly decreasing cubic branch 1..√2 with unique zero β; D loses to F until β and to A thereafter. At internal support breaks A is C² not C³, D is C¹ not C². Independent half-space intersection convex-hull volume checks of original 12 inequalities and translated copies match analytic A/F/D for several t, including both nonzero branches. Numerical checks only corroborate the exact algebraic continuum inequalities.

## originality

PASS

Bianchi proves that covariograms determine three-dimensional convex polytopes, and Averkov–Bianchi study determination from restricted functions; neither inspected theorem tabulates the explicit three ray profiles or the fixed-distance three-axis crossing. The published hypercube covariogram phase diagram relies on Cartesian factorization and concerns a different body. An unindexed crystallography spline or autocorrelation table could contain the same formulas, so priority is best-of-knowledge.

## value

PASS

Three symmetry-axis autocorrelation/covariogram functions and their exact positive-overlap transition distances are natural lattice-cell geometric invariants. The precise piecewise profiles, differentiability orders and nontrivial D→F→A maximizer sequence within all crystallographic axis types can be used directly in overlap and scattering computations; it is not a claim of full-sphere angular optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
