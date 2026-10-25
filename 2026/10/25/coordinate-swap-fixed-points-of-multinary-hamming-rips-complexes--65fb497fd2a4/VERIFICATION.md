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

# Verification of the coordinate-swap fixed-point homotopy theorem

The included `verify_orbit_complex.py` is a self-contained Python 3 program with no external dependencies. Execute `python3 verify_orbit_complex.py` from the same folder. It independently derives orbit adjacency from the Hamming metric, enumerates maximal cliques with Bron--Kerbosch and compares them to the three exact families of proposed maximal faces; for small alphabets it also reconstructs all simplicial faces and computes mod-two boundary ranks by bitset Gaussian elimination.

An actual invocation succeeded with these exact outputs:

```text
q=2 vertices=6 facets=8 mod2_betti2=1 other_reduced_betti=0 PASS
q=3 vertices=18 facets=30 mod2_betti2=14 other_reduced_betti=0 PASS
q=4 vertices=40 facets=92 mod2_betti2=63 other_reduced_betti=0 PASS
q=5 vertices=75 facets=230 exact_facet_check=PASS predicted_betti2=184 (not calculated)
All checks passed. Finite cases do not prove the all-q statement.
```

The \(q=2\) case is a known binary boundary and is not part of the new theorem's novelty claim. For \(q=5\), the checker verifies facets but does **not** independently compute homology. Higher alphabets have not been exhaustively tested. The all-parameter proof instead uses the orbit-simplex PL identification, a contractible-link deletion sequence, the nerve lemma, the rectangle generators of the complete bipartite graph, integral cellular homology, and Hurewicz/Whitehead. No mechanized infinite formalization or independent scientific audit is claimed.
