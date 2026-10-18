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

The uniform mathematical argument is supplied in RESULT.md; the executable below checks finite instances and its core incidence lemma independently of the symbolic proof.

Execute `python3 verify.py` in this directory. It requires only Python 3's standard library and prints `VERIFY_OK families=27 exhaustive_labeled_six_vertex_graphs=2992` on success. The checks enumerate connected induced four-vertex sets; test for a face of size five that would contradict the claimed dual dimension; identify for each tetrahedron a triangle used by no other tetrahedron; compare direct enumeration with the degree-and-edge formula; and compute mod-two cut-complex chain ranks for the graphs of order at most ten. The larger high-girth cubic examples check the connected-four count and free-triangle incidence but not their full cut-complex boundary matrices.

Observed larger test values: Heawood graph, \(n=14\), \(c_4=98\), \(B=188\); Möbius–Kantor graph, \(n=16\), \(c_4=112\), \(B=343\). The exhaustive six-vertex test covers all labeled simple graphs satisfying the girth restriction, not only connected graphs.

These are finite reproducibility checks. The unlimited-order conclusions instead rest on the unique free-triangle argument, elementary simplicial collapses, combinatorial Alexander duality, Hurewicz and Whitehead theorems. No computer-assisted exhaustive statement about all graph orders or independently performed external audit is asserted.
