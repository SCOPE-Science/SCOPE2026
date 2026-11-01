---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

The Desargues graph is the 30-edge bipartite inclusion graph on 2- and 3-subsets of [5], and its independence complex is flag. A minimal-support nonzero H5 class needs at least 2·5+2=12 vertices; an equality support must be an octahedral S5 from a six-edge induced matching. An independent enumeration yielded induced matching counts [30,255,700,615,42,5,0] in sizes 1..7; the five six-edge matchings are the M_i obtained by fixing the omitted element i. Their signed 64-term sphere cycles are genuine 5-cycles. The integral ranks of ∂5,∂6,∂7 are forced to 932,383,97 by mod-101 lower bounds and the rank 388 primitive lattice L=im∂6+ΣZz_i; its exact 388×388 minor has determinant −1. I independently regenerated the 388-row and 388-column minor directly from the actual certificate indices and performed 388 exact integer unit pivots, obtaining −1. Thus L=ker∂5 as saturated equal-rank lattices and H5=Z^5 with the five specified integral generators. The S5 action exactly permutes the matching spheres, and complementation reverses all six chosen edges with net −1, giving Z[X]_perm⊗sgn_C2. The known H4=Z and nonequivariant homotopy type are not claimed new.

## originality

PASS

Earlier exact same-object homotopy calculations determine H5 rank five, but not the minimum-support spheres, primitive integral basis, or S5×C2 module exhibited and certified here. General incidence-graph Alexander duality also does not imply those concrete integral representatives. This surviving contribution is narrower than the previously known homotopy type; priority is best-of-knowledge.

## value

PASS

Minimum-support cycles and their integral permutation-with-sign module are natural geometric/topological invariants for this symmetric named graph. A primitive integral basis is strictly stronger than a rank-five rational homology assertion, and the full S5×C2 action is useful for equivariant topology. It is not a recomputation of the previously known homotopy type.

The dated certificate retains the supplied scientific assessment, sources and limitations.
