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

The mathematical proof is in `RESULT.md`. Running `python3 verify.py` reproduces the finite checks using only Python's standard library. It independently constructs the ordinary cut complex from the graph for each case, compares the signed simplicial Lefschetz trace with the claimed group-character formula for every tested symmetry, and checks binary boundary ranks for all cases of at most ten vertices. Successful execution terminates with `VERIFY_OK`.

The tested cases are a seven-cycle, a seven-vertex path, the Petersen graph, the Heawood graph, a seven-vertex star, two disjoint five-cycles, and a five-cycle with two isolated vertices. A total of 374 explicitly enumerated automorphisms were checked. Complete homology ranks were independently checked over the field with two elements for six examples (all but the Heawood graph); these finite checks do not replace the integral proof over the whole graph class.

The key general steps requiring mathematical scrutiny are: (i) the Alexander dual contains exactly the connected induced triples as two-faces; (ii) the missing endpoint edge of each two-edge path is a distinct free edge when four-cycles are forbidden; (iii) elementary collapses yield a graph with the stated cycle rank; (iv) the complete lower skeleton and integral duality promote homology concentration to a wedge homotopy type for \(n\ge7\); (v) equivariant Alexander duality produces the ambient permutation-sign twist. No independent audit has been performed.
