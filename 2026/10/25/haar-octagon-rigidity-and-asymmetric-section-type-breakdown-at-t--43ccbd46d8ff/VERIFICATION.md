---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For a>b>d>0 sorted absolute plane-normal components, enumerating actual face vertices yields complete step functions: if c=1+s<2, N=4+2[d>sb]+2[b<sa]+2[d<sa]; if c=2+delta>2, N=4+2[a<b+delta*d]+2[b>d+delta*a]+2[b+d>delta*a][a>d+delta*b]. At c=2 the 12 cuboctahedral vertices give exactly eight crossed faces generically. Non-8 angular cones exist for every other c. On the cube side N=4 iff b+d<delta*a, six signed-axis cones; their solid angle is the stated arctangent and gives p4=(3/pi)delta²+O(delta⁴). Linearized boundaries a=b and b=d in the 48 Haar chambers have exact strip integrals 1/(2sqrt3), (1-1/sqrt3)/2, 1/sqrt3 and 1/sqrt2-1/sqrt3; multiplying by 12/pi yields all stated one-sided coefficients and the ratio sqrt2, with crossing corners O(epsilon²). Independently enumerated vertices/facets/edges of K_c for seven c values and checked 3,850 random generic section normals; all exact side counts agreed, and 100,000 directions at delta=0.4 gave p4 0.14137 vs exact 0.14160076. Numerical normals cannot prove the coarea remainder or all-c property.

## originality

PASS

Statement-level implication and object/parameter comparisons checked in cited primary literature and Resultary; novelty is best-of-knowledge, with named inaccessible full texts and generic-theorem risks. The previously known subclaims are explicitly excluded from the novelty claim.

## value

PASS

The cuboctahedron is an exact rigidity point for a classical one-parameter regular-solid interpolation: almost every central section has the same polygon type only at c=2. Sharp asymmetric slopes resolve how two distinct kinds of section topology appear on either side, and an elementary complete quadrilateral probability holds for the entire cube-side range. These are natural geometric observables beyond an isolated artificial numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
