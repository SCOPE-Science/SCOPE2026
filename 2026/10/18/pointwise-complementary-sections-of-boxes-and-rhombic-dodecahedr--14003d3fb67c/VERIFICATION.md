---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For each of 12 cube edges, its endpoints and two rhombic-dodecahedron axial-corner edges contribute exactly one plane crossing for a generic normal, as shown by three sign possibilities. Every rhombic edge belongs to exactly one such pair, establishing N_C+N_R=12; replacing the normal by T^T u proves affine-matched pointwise identity. A generic cube central cut has 4 or 6 vertices, hence its rhombic partner has 8 or 6. A Haar great-circle separation probability equals the angle between endpoint rays divided by pi, and summing 24 edges yields P_R(6)=(4/pi) sum_i arcsin(a_i/sqrt(sum a^2))-2 for diagonal T. Maximizing sum arcsin x_i on positive unit octant gives only critical x_i=1/sqrt(3), with boundary value pi/2, and logarithmic Taylor expansion yields coefficient 1/(pi sqrt(2)). Independently checked integer-normal edge crossings and exact symbolic Hessian; no finite sampling was used as proof.

## originality

PASS

The single-body box Haar hexagon law and cubical optimizer are explicitly previously known, not novel. The surviving distinction is the pointwise twelve-edge complement under every COMMON invertible affine map, transporting box events to a different polytope and deriving its sharp logarithmic Hessian. Full prior record checked; no implication alone gives new incidence identity.

## value

PASS

A same-normal edgewise combinatorial correspondence between two classical nonisomorphic polytopes is a structural geometric identity, giving the entire Haar section type law of an affine rhombic dodecahedron and exact stability of the symmetric extremizer; the result is useful beyond merely recomputing the known box probability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
