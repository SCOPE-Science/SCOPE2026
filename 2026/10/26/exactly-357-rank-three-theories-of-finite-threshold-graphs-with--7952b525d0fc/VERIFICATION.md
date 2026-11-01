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

Independently checked the rank-three invariant: tuple rank-zero types are exact equality/adjacency diagrams, their one-extension sets give rank-one pair types including z=x,y equality cases, rank-two vertex types collect all pair extensions, and the set of vertex types is equivalent to rank-three sentence type. An independent Python implementation used direct integer adjacency masks to form all four distinct-third-vertex adjacency patterns, unary neighbor/nonneighbor flags, and the full set of pair types. Breadth-first search from K1 with isolated and universal append operations stabilized after exactly 357 distinct signatures, with all 714 outgoing successors matching prior states. The maximal first-reached word length was 16 (17 graph vertices), with exactly two classes and precisely the published order distribution. Crucially, the three-pebble EF composition under an added isolated vertex, and its complement dual for a universal vertex, prove each append is a congruence for rank-three equivalence, so closure of all successors proves the result for creation words of arbitrary length. BFS shortest-path property proves the threshold-graph-only 17 sharpness. Compared against actual verify.py rank-Hintikka recursion and manifest schema/first states; did not treat pre-recorded VERIFY_OK or cutoff enumeration alone as proof.

## originality

PASS

General EF finite-index and Hintikka recursion appear in Pikhurko–Verbitsky’s graph logical-complexity survey, while threshold graph binary construction appears in Fürer and classical Chvátal–Hammer work. Those are prior structural tools. The inspected published results do not give this exact rank-three quotient, complete minimal-order distribution or 17-vertex kernel, and the survey’s general bounds do not determine these values. Other exact logical-depth classifications of paths and complete multipartite graphs are different families. A finite-model-theoretic classification of threshold graphs under another name or earlier computational model enumeration remains a priority risk.

## value

PASS

A complete sharp finite quotient for a classical infinite graph family is a meaningful exact logical invariant. The 357-state closed automaton supplies a finite representative set for testing every rank-three sentence, while its two 17-vertex extremal classes certify minimal kernel size; this is much more than a finite test through order 17, because the closure lemma proves universality. No claim made for rank four, counting logic or arbitrary graph representatives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
