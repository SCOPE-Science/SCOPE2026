---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For H_{a,b}, each edge meets three different (unlabelled) parts, all parts having size 1 or 2. In a four-round EF game, preserving previously chosen vertices and the size and identity of each represented part is a partial isomorphism; at most four new parts of either size can be entered, so a,b may be truncated at four. There are exactly 19 allowed capped pairs because a+b>=3. Independently implemented complete rank-zero atomic diagrams (equality and ternary edge bits) and iterative all-vertex extension types T_{r+1}(tuple)={T_r(tuple,y):y vertex} partition those 19 cases into exactly twelve equivalence classes, with minimum representative vertex sizes 3,4,4,5,5,6,6,7,7,8,8,9. The complete Hintikka/EF recursion, unlike sampling, decides rank-four equivalence for those finite cases. The new independent enumeration agrees with source direct and orbit-compressed codes and confirms sharp nine-vertex representative bound inside this family. No expansion to arbitrary multipartite sizes or rank five is claimed.

## originality

PASS

Matching-deletion complete triple systems are a canonical two-parameter family, and the contribution is the exact twelve-class rank-four theory partition and sharp nine-vertex representation bound. General finite-model-theory bounds and hypergraph edge-ideal classifications do not compute that partition.

## value

PASS

Exact four-round logical indistinguishability is a natural invariant of a canonical complete hypergraph perturbed by a matching. The full infinite two-parameter family is classified, including structural mergers and optimal representative bound, yielding a finite-model-theory small-model benchmark with mathematical interest independent of arbitrary finite tables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
