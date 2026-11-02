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

For a fixed compact nondegenerate convex polyhedron, decomposing the ordered surface-pair integral into pairs of planar facets yields an exactly local polynomial of degree at most four. The diagonal facet covariogram has area-loss coefficient -(2/3)perimeter(F) r^3 and each adjacent ordered facet pair contributes (2/3)L_e(pi-alpha_e)/sin(alpha_e) r^3 via a transverse wedge Jacobian; cross-pairs touching only at vertices are O(r^4), while disjoint pairs vanish near zero. Thus the CDF equals (pi/A)r^2+(4/(3A^2))sum_e L_e((pi-alpha_e)/sin(alpha_e)-1)r^3+C4(P)r^4 at 0<=r<r0(P), with all higher coefficients exactly absent. The inequality delta/sin(delta)>1+delta^2/6 on (0,pi), sharp as delta tends to zero, supplies the strict 2/(9A^2) squared-bend bound. Direct independent rational/numerical cube coefficient and small-bend checks agreed. Assumes maximal planar facets, ambient Euclidean rather than geodesic distance, and radius threshold depending on P; C4 is not explicitly computed.

## originality

PASS

No checked prior source implies the full exact small-radius law for arbitrary three-dimensional convex polyhedral surfaces with the edge-dihedral cubic coefficient. The known cube specialization is expressly prior work; coplanar polygon pairs, smooth surface correlations, and intrinsic surface geodesics do not dominate this extrinsic noncoplanar statement. Qualified priority due to uninspected specialized older stereology literature.

## value

PASS

The coefficient exposes a quantitatively sharp edge-weighted bending signal from extrinsic sampled distances, and the exact degree-four locality is a structural theorem for the entire class of three-dimensional convex polyhedra, not an isolated constant. This is a natural benchmark for stereological reconstruction and polyhedral correlation functions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
