---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For nondegenerate alternating B on F_2^(2d), prescribing a functional on any t-dimensional U yields exactly 2^(2d-t) solutions by dual surjectivity. For d,e>=q-1, a q-round EF game preserves a span isometry for first q-1 moves: before the last, t<=q-2 and a prescribed pairing fiber contains a vector beyond span; at last, with t<=q-1, 2^(q-1)>q possible responses allow preserving equality/adjacency even if linear dependence changes. For d<e, Spoiler chooses d+1 distinct independent isotropic x_i in S_e, which forces a nontrivial linear relation among pairwise orthogonal y_i in S_d; a final incompatible pairing functional exists on independent x_i, so Spoiler wins at move d+2. When d=1 the graph is K_3, detected by a nonedge at rank 2; all d>=2 contain both edges and nonedges. Induced claw in S_3 vs its absence in S_2 was independently enumerated; unrestricted proof is linear-algebraic.

## originality

PASS

Published binary symplectic graph results inspect switching, strongly regular spectra, graph isomorphism and 2-ranks; they do not identify the exact all-rank FO separations. The sharp degree threshold, q-1 classes and finite-size representative cutoff require the span-extension argument beyond the graph-family definition. A model-theory treatment of alternating bilinear forms/reducts may yield an alias and is a documented residual risk.

## value

PASS

The canonical symplectic strongly regular graph family has a natural unbounded dimension parameter; knowing exactly the rank at which first-order adjacency can distinguish ambient dimensions is a nontrivial logical rigidity/classification fact. It also demonstrates how hidden linear dependence becomes visible at one extra quantifier after maximal isotropic rank.

The dated certificate retains the supplied scientific assessment, sources and limitations.
