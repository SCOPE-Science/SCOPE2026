---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For every d>=3 and 1<=a<=c, the center is the unique degree-d vertex and the first refinement separates center, internal degree-2 vertices and leaves; subsequent color at round r is exactly the truncated rooted neighborhood type, encoded for leaves by (leaf,min(L,r)) and for internal arm position x by (internal,min(x,r),min(L-x,r)). The arm-to-center and arm-to-leaf distances are distinguished by endpoint degree and potential differences beyond the center are too deep to break an asserted descriptor equality early. If c=a, each arm has unresolved internal middle interval r<=x<=a-r, size <=1 precisely for r>=ceil(a/2). If c>a, short and long leaf colors first separate at r=a+1, and the long internal middle ceases to collide by ceil(c/2); these two necessary conditions suffice for stable orbit classes, giving max(a+1,ceil(c/2)). Independent direct 1-WL implementation tested all d in {3,4,7}, 1<=a<=13, a<=c<=41 (1,365 parameters) without discrepancy, plus code inspection of pinned verifier; this corroborates infinite proof.

## originality

PASS

The almost-equilateral spider family is a one-exception-arm tree subdivision, so general rooted-universal-cover equality specializes to an algorithm for its colors; the explicit a,c formula requires a separate family-specific derivation. General 1-WL local-universal-cover characterization determines colors abstractly but does not directly assert a stopping time max(a+1,ceil(c/2)) or ceil(a/2). From the prior universal-cover theorem one still must prove the typed clipping descriptors and exact first round in which no middle positions or different arm-length tips split. Primary text inspections and Resultary cross-checks found no exact or dominating theorem for the complete claim; this is a best-of-knowledge PASS with the listed explicit literature and accessibility risks, not proof of absolute novelty.

## value

PASS

This describes each color class at every round and the exact stopping time of a natural spider-tree subdivision with one exceptional arm; it isolates a sharp discontinuity between equal-length and almost-equal arms. Exact 1-WL iteration counts are relevant to the structure and worst-case behavior of refinement algorithms, rather than an arbitrary graph instance or mere computer output.

The dated certificate retains the supplied scientific assessment, sources and limitations.
