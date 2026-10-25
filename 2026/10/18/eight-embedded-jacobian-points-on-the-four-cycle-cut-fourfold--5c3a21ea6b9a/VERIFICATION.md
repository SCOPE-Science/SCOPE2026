---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

The C4 cut ideal is the codimension-three complete intersection z1=z2=z3=z4 in eight homogeneous coordinates with zi=xi yi (Sturmfels–Sullivant Example 1.2). Jacobian derivative pair columns share one of four rank-3 vectors, and every three distinct index-group vectors have determinant +/-1 even in characteristic 2; exactly 32 degree-three maximal minors are all products from three distinct groups. Radical is the squarefree ideal (z1,z2,z3,z4)+minors, yielding 24 coordinate lines indexed by K_{2,2,2,2}. Away from eight coordinate points, local elimination is reduced along each line. At an affine chart of any coordinate point, the 12 two-by-two minors kill all cross-group quadratic monomials of six variables in three pairs, while 2 relations identify three same-pair products to one nonzero tau. Every local variable annihilates tau, so tau^2=0 and nilradical length1 at each of exactly eight vertices; no other nonreduced support. Direct determinant/multigrading checks reproduce 32 global cubic minors, 12 local minors, 24 lines and local Hilbert degree2 = seven. The normalization of 24 P1 components at eight 6-fold axial crossings gives chi_red=24-8*5=-16, genus17; adding eight square-zero skyscrapers increases chi to -8, genus9, degree remains24. Coefficient determinants are units over Z, ensuring arbitrary characteristic.

## originality

PASS

Sturmfels–Sullivant provide cut ideal and graph polytope, and existing cycle cut classifications describe reduced lines. The exact eight length-one nilpotents and singular-scheme arithmetic genus are additional data not implied by the cited reduced support. Similar Resultary discotope embedded-point example concerns a different algebraic variety.

## value

PASS

Detects subtle eight-point embedded Jacobian scheme structure invisible from reduced singular-support classification and quantifies a genus shift 17 to 9 for a canonical toric cut variety. Scheme-theoretic singularities are a natural invariant and this calculation is substantive beyond a reduced variety census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
