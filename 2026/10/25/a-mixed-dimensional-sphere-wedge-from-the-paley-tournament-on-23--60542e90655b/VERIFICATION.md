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

For Q the eleven nonzero quadratic residues modulo 23, the 23 translates v+Q are precisely the out-neighborhoods; independent enumeration gives 42,297 faces and face vector (23,253,1771,6325,10373,10626,7590,3795,1265,253,23). Independently replayed deterministic elementary free-face collapses: 19,184 pairs, 3,929 nonempty surviving faces. A second 1,856-pair Morse matching has a full 3,929-node/14,596-arrow DAG topological order, leaving one 0-cell, 212 3-cells and four 4-cells. Independent exact gradient recursion gave four signed columns with lengths (26,27,55,26), c0-c1-c2+c3=0, and 3x3 unit determinant -1 at critical 3-face masks 8724,133252,270360. Thus integral 4-to-3 boundary has Smith invariants (1,1,1,0). Since the three-skeleton is a wedge of 212 S3, the Hurewicz isomorphism identifies attaching maps by degrees, yielding precisely (∨209 S3)∨S4, no hidden torsion. This does not claim other tournament orders.

## originality

PASS

The out-neighborhood construction of Dochtermann–Singh is known, and Paley cyclic residue blocks are a classical 2-(23,11,5) design. But paper Sections 4–5 enumerate five-vertex tournaments and construct single-sphere examples, not the canonical P23 mixed wedge. Resultary P19 and P31 Paley directed-FLAG homotopies are not the same simplicial complex; no covering formula located.

## value

PASS

Canonical finite Paley tournament is a symmetric, independently motivated design/network object. An exact integral mixed wedge for its natural directed out-neighborhood complex answers an explicit class of homotopy-realization questions left open by the foundational work and is nontrivial beyond face counts or homology over one field; the exact 209/1 split is a useful invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
