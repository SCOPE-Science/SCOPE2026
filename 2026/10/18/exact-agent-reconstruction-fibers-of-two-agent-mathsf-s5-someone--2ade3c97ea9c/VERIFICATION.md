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

The full powerset map U↦B_E,F(U) determines at each labeled world w the two inclusion-minimal true neighborhoods {E[w],F[w]}; incomparability ensures both occur, and rules out nontransverse alternative pairs. Form a loopless bipartite multigraph with each distinct recovered block as vertex and each world as labeled edge. Proper two-colorings correspond bijectively to all ordered E,F reconstructions; two blocks of the same color are disjoint, and each color partitions W. Components of this graph exactly encode E∨F components. A connected bipartite component has exactly two colorings, so fiber size is 2^c, and global agent swap quotient 2^(c-1). Every block must meet >=2 blocks of other color, so each component contains >=4 worlds, achieved by K2,2 grids with repeated cells; max 2^floor(n/4) and sharp first nonglobal at 8. Source partition checker covers all pairs through six worlds and explicit grids through 12 as corroboration; universal proof is graph reconstruction.

## originality

PASS

PASS as a best-of-knowledge fixed-labeled-fiber theorem, not novelty of local minimal neighborhoods. Ågotnes–Wáng 2021 already gives neighborhood-core semantics and representation, later modal/hypergraph frameworks also cover existence. The new inverse problem counts ALL ordered two-S5 reconstructions of the full Boolean operator and shows componentwise coloring is the only freedom. A highly relevant 2023 hypergraph paper remains unavailable in full, so the priority conclusion is expressly qualified.

## value

PASS

It gives a complete inverse-identifiability invariant for two hidden S5 agents under full powerset observation: an exact fiber and its nonglobal ambiguity onset at eight labeled worlds. This is a mathematically motivated reconstruction/classification problem, not a restatement of representability and not merely a small enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
