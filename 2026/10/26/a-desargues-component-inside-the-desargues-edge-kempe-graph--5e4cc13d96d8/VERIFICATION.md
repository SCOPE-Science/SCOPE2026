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

# Exact finite verification

`certificate.json` is a complete list, not a partial test: `base_edges` records all thirty edges of \(\operatorname{GP}(10,3)\); `colorings` lists all 32 canonical three-class partitions as three 30-bit masks; `kempe_edges` lists all 36 unordered reconfiguration edges; `components` partitions the 32 states; `desargues_isomorphism` is a bijection from the 20-state component to the vertices of the original graph.

`verify_factorizations.py` proves completeness by recursively branching over every edge at the least unmatched vertex until no vertices remain, and by splitting every complementary even cycle in all two alternating ways. It checks all colorings, all three color pairs per coloring, every connected bichromatic cycle, every resulting quotient state, the complete component partition, and preservation and reflection of adjacency under the explicit isomorphism.

`verify_direct_colors.py` uses a different search space: each edge is assigned a color subject to local vertex constraints. Global color permutations are eliminated uniquely by fixing distinct colors on the three edges incident to vertex zero. It visits every compatible edge-color assignment by finite backtracking, independently builds every bichromatic cycle through edge-connectivity searches, compares all 32 states and 36 edges to the certificate, checks the explicit isomorphism, and recomputes all large-component distance distributions.

Run `python3 verify_factorizations.py` and `python3 verify_direct_colors.py` from this directory. Their captured standard outputs are stored in `factorization_output.txt` and `direct_output.txt`. The certificate's SHA-256 is `d34d0c2b0fe953fa127ef17e6bfe64d7350aae19b36bad29f0d48f937ed44f6c`.

**Limits.** These exhaustive algorithms establish the specified finite result, not its historical originality or any infinite generalization. No independent external validation has been performed.
