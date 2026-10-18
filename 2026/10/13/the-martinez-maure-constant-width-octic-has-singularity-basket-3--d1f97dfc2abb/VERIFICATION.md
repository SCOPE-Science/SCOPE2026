---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For the specified degree8 affine F(s,q) from the 2021 support function h(theta)=8-sin(3theta), the homogeneous degree8 projective parametrization [U:V:W] has no base points and substitutes to zero. Rational (u,v) elimination agrees with F; subresultant of the two degree6 parameter equations is generically linear and its z coefficient at z=1 is 151552 !=0, hence the map is birational. Exact Jacobian solutions give 9 finite singularities in 3 cyclic orbits: 3 real E6 cusps at rotation orbit of (0,9) from local branch orders (3,4), plus 6 complex A1 nodes from nonzero Hessian determinants at (0,-9±6i sqrt3). At two points at infinity [1:±i:0], corrected local parameters have orders (2,7) hence A6. Independent SymPy localized series/Hessian/subresultant computations reproduce the essential coefficients, and δ total 3·3+6·1+2·3=21 equals plane octic arithmetic genus, excluding further singularities. Claim over C only.

## originality

PASS

Martinez-Maure 2021/22 gives support parametrization and explicit affine degree8 equation, not the complex singularity basket; Bardet–Bayen 2013 gives general properness/minimal degree analysis but not analytic ADE types of this specialization. Inspection of source full text and Resultary semantic query found no implied exact 3E6+6A1+2A6 invariant. Genus/degree are prior knowledge; singularity classification is the proposed new part.

## value

PASS

The singularity basket of the specific minimal-degree noncircular algebraic constant-width curve is a natural intrinsic algebraic-geometry invariant. The complete local ADE types and genus-defect exhaustion distinguish real convex points from complex projective geometry, useful for curve normalization/classification beyond the original convex geometric construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
