---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For n>=3, centers have distinct closed neighborhoods: duplicate adjacent centers would have unequal connections to a third vertex in a tree. Any query v divides centers into N[v] and B_v=V\N[v]. The positive branch has Ldim<=2 because every second query retains at most two centers on one side (neighbors in a tree have no triangles); it has Ldim exactly two iff degree(v)>=3. The negative branch has Ldim>=2 iff a query w splits B_v into two sets of size >=2, exactly 2<=|N[w] intersect B_v|<=|B_v|-2. A depth-four tree is excluded since its positive branch can never reach depth three. A depth-three root exists exactly when both positive and negative conditions hold. For n>=4 a leaf query has two positive and n-2 negative centers, so depth>=2; n=1,2 are singleton classes and n=3 has Ldim1. The eight-vertex witness degree>=3 and |B_v|>=4 are necessary, hence no seven-vertex witness. If three query vertices were shattered, the all-one center would force a missing exactly-two trace by the uniqueness of a path in a tree, so VC<=2. Independently reconstructed the full online-minimax recursion and canonical Prüfer-tree enumerator: all 23 unlabeled eight-vertex types matched, exactly 12 attained dimension three; all types of order<=7 matched the trichotomy.

## originality

PASS

The established static VC/compression statements are fully credited. The online three-level threshold and first sharp witness survive mathematical implication comparison as a plausible original claim.

## value

PASS

Adaptive Littlestone depth, unlike static VC dimension, governs realizable online mistakes. The universal three-round cutoff on a natural graph concept class and the sharp eight-vertex first VC/Ldim separation identify a motivated structural boundary, not a routine numeric lookup.

The dated certificate retains the supplied scientific assessment, sources and limitations.
