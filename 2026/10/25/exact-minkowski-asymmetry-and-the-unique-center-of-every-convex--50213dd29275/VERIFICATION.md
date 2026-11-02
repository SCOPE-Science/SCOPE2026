---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

Every nondegenerate convex quadrilateral is affinely equivalent to Q=conv{(1,0),(0,1),(-p,0),(0,-q)} for ordered shorter-to-longer diagonal ratios 0<p<=q<=1. Four explicit facet support inequalities for z=(s+1)c give a valid three-normal positive dual certificate proving s>=1+(1-pq)/(1+p); the displayed z=(s-1,1-q) satisfies the fourth inequality with slack (1-q^2)/q. Strict positivity of three weights for pq<1 forces all three active, proving uniqueness. Parallelograms p=q=1 uniquely centered at their symmetry center. Range [1,2) is attained by p=q=2-s. Independent checks: Independently formulated the 4-constraint linear program from vertex coordinates, solved it with scipy.optimize.linprog at (p,q)=(1,1),(0.3,0.7),(0.8,0.6),(0.12,0.99),(0.35,0.35); calculated optima match the proposed formula to floating precision. Read actual exact-Fraction checker source checks/verify.py Git blob 86c15fe9e5e5d061db4b0413094bd8fd7e99ddbb. The full continuum follows from explicit primal-dual proof, not finite examples.

## originality

PASS

Brandenberg–von Dichter–González Merino arXiv:2006.07259v2 §2 gives general optimal containment contact criteria, Cor.2.5, not an exact arbitrary-four-vertex diagonal-ratio formula nor uniqueness for this entire class. Caragea et al. 2025 distinguishes point-inversion alpha_0 from reflection alpha_1. Resultary related quadrilateral Makai product and centroid-chord profiles are different functionals. Residual limits explicitly listed in originality.residual_risks.

## value

PASS

Complete affine two-parameter classification and uniqueness for every convex quadrilateral, the smallest planar nonsimplex family, with exact dual support-contact certificate; could be reused as a benchmark for general Minkowski-center optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
