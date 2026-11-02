---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Using exact Littlestone recurrence on distinct closed radius-two balls, centers restricted to a vertex 1-ball have Ldim<=2, and distance-two center groups outside one branch likewise have Ldim<=2. For centers in B2(p), any query has one branch Ldim<=2, yielding bound 3; a hypothetical global depth-5 shattered tree would require depth 4 below its root positive query, impossible. Counting hypotheses gives order>=16 for Ldim4. Verified actual 16-node 16-center depth-4 witness and path P4/P5/P8 witnesses; independent networkx unlabeled generation and separately coded recursion exhaustively evaluated all 19,320 n=16 classes, recovering counts 1,7,227,18516,569. Leaf extension preserves witness, proving every n>=16 attains 4. The full census is genuine exhaustive finite enumeration, whereas all-n upper bound is analytic.

## originality

PASS

Chalopin et al study fixed-radius tree-ball sample compression with compression size two, a distinct complexity notion not giving Ldim<=4 or the sharp order threshold. Non-clashing teaching maps and randomized Littlestone prediction generalities do not compute this tree radius-two family. Resultary search did not yield an exact matching theorem; case-specific structural proof supplies nontrivial new content.

## value

PASS

Exact online shattering ceiling across every finite tree, sharp minimal tree order 16, and exhaustive distribution among all 19,320 nonisomorphic 16-node trees are natural independent graph-learning invariants. They identify a sharp adaptive-information boundary beyond VC/compression results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
