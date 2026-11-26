---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For two distinct positive queries, disjoint edges have at most one common center (two bridges force a triangle or square); incident edges leave only their common star, in which a new query isolates or co-isolates at most one center. This precludes online depth four. After a positive root uv, queries outside both endpoints hit at most one candidate and queries through u other than uv hit just the other u-edges, excluding themselves. A depth-two split of this positive space therefore requires degree at least four at one endpoint and at least two at the other. That proves the subcubic cap and supplies a fixed shattered pair: two edges a,b at the high-degree endpoint have traces 01,10,11,00 from a,b,uv and an extension at the opposite endpoint. The general lower bound VC <= Ldim and the depth-one case cover the remaining dimensions, including the empty-class convention. The exact nine-vertex depth-three certificate checks out; depth three requires eight distinct edge functions, excluding all smaller trees.

## originality

PASS

The standard VC lower comparison is not novel. The distinct contribution is the girth-dependent online upper bound, its degree and VC refinements, and the exact online sharpness for trees. The strongest same-day comparison on the same incidence relation bounds all induced subgraphs of the triangular graph by four, not three, and supplies no degree or VC-relative refinement. No implication-level match emerged in the available comparisons.

## value

PASS

These are sharp structural thresholds for adaptive edge identification: maximum degree alone excludes depth three below four, and girth forces the adaptive advantage over fixed queries to at most one. The P5 and minimum-order nine-vertex tree show that the advantage is genuine even among trees and certify where the higher online rank starts; the result is not a computation of two arbitrary trees.

The dated certificate retains the supplied scientific assessment, sources and limitations.
