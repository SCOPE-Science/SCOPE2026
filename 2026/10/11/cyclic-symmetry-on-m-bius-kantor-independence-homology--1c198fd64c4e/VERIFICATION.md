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

For G=GP(8,3) with 16 vertices and 24 edges, the complete finite complex has f-vector (16,96,272,376,240,72,16,2), 1090 nonempty faces and 4272 Hasse covers. An independently implemented greedy matching yields 542 pairs, is acyclic on all faces, and leaves one critical 0-face, four critical 3-faces and one critical 4-face. Exact integer elimination gives Morse d4=(0,0,0,0), so H3=Z^4 and H4=Z and other positive homology vanishes. Independent full boundary-rank elimination modulo 3 yields (15,81,191,181,58,14,2), compatible with exact integral certificate. Independent oriented fixed-simplex traces for the eight powers of the canonical rotation give L=(-2,0,2,0,-2,0,2,0). A nonboundary degree-four mod-3 cycle transforms to minus itself modulo degree-five boundaries (and not plus), so the integral rank-one H4 action must be sign. Consequently chi3=1+chi4-L=(4,0,0,0,4,0,0,0), chi4=(1,-1,1,-1,1,-1,1,-1), giving the rational C8 decomposition 1 ⊕ sign ⊕ Q[x]/(x²+1). This is an exhaustive finite theorem for the stated graph, not a family extrapolation.

## originality

PASS

Best-of-knowledge original equivariant refinement: earlier same-graph work fixes the nonequivariant wedge-of-spheres type but does not specify how the canonical order-eight rotation acts. Independently checked complete C8 characters are not implied by homology dimensions alone. The exact original finding appears as a self-match in the published Resultary index; this is not treated as independent prior evidence. No earlier inspected source establishes the target rational module decomposition.

## value

PASS

The canonical order-eight rotation is intrinsic to the G(8,3) model of a highly symmetric 16-vertex cubic graph. A full C8-character calculation distinguishes the negative action on its unique H4 generator and an order-four rational 2-dimensional summand of H3, data invisible to the already known 4-sphere Betti summary. This is a natural, bounded and independently useful equivariant invariant and gives a benchmark for future full automorphism-module calculations; it does not need to imply a larger theorem to matter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
