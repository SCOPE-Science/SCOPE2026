---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The proof is structural and applies to every finite simple connected complete multipartite graph. The computation below is a finite stress test, not the source of the infinite-family theorem.

`verify.py` reconstructs adjacency from multipartite parts and does not assume the theorem. For all sorted part-size tuples with two to four parts and total order at most six, it enumerates every surjective proper coloring for every possible color count. It computes color-dominating vertices from closed neighborhoods and checks that every b-coloring uses exactly one color per part and has CDV-count multiset equal to the part-size multiset.

It then enumerates non-increasing finite requirement sequences and compares the direct number of labeled realizing colorings with the closed product formula. The stored replay output is:

`ALL CHECKS PASSED; graphs=16; proper_colorings=7200; b_colorings=144; sequence_tests=189`

Unproved by computation: no finite enumeration can establish the theorem for unbounded part sizes or numbers of parts. That generality is supplied by the proof in `RESULT.md`.
