---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Shortest means shortest in the K-gauge (RESULT.md assumptions), so v is primitive and can be extended to a lattice basis. Projection of the second basis vector has absolute length det(Lambda)/|v|, and the interval of half-height h has covering radius this spacing divided by 2h. The first minimum is |v|/a from the central chord. Thus the deficit is exactly area(K)/area(P)-1, with P inscribed by symmetry and convexity. Send its independent half-diagonals to the coordinate vectors. If a point of the normalized body has diamond gauge s>1, the triangle over the sign-selected supporting edge has area (s-1)/2, lies in the exterior closed half-plane, and belongs to the body; its negative belongs to the body in the disjoint opposite half-plane. Added to the diamond area 2 this gives s<=1+2epsilon, irrespective of how the top point was chosen. At epsilon=0 the two inclusions force equality; the converse is immediate. In the supplied K_t the only added area beyond the diamond is the pair of triangles of combined area t, for 0<t<=1; K_t is inside the unit coordinate square, so e_1 is gauge-shortest for the integer lattice. The gauge of (1,t) is 1+t, attaining the bound as epsilon=t/2 tends to zero. The script was inspected, not rerun: it reports 2,589 finite rational polygon checks, with a selected top vertex, not all top points or a lattice search. Neither that finite scope nor the source's unperformed formal/expert verification affects the analytic proof.

## originality

PASS

Pass for the optimal global containment coefficient with respect to each specified lattice-selected inscribed parallelogram. The mixed product inequality and qualitative equality geometry are prior; no checked source yields the quantitative centered area-to-gauge relation with this witness quantifier. The comparison does not establish historical priority.

## value

PASS

A usable near-equality estimate should control geometry for a lattice-selected witness, not merely identify an equality body. This gives a centered global dilation guarantee for every permissible extreme point, even with nonsmooth bodies or nonunique shortest directions, and the explicit positive-deficit hexagons fix the optimal linear coefficient. The elementary proof does not make the optimal stability assertion a consequence of the scalar inequality alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
