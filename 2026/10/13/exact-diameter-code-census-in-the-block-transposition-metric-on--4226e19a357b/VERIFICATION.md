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
# Verification

`verify.py` uses only the Python standard library and reconstructs the result from the block-transposition definition.

It checks all \(120\) permutations, all \(20\) generators, the exact distance histogram \(1,20,68,31\), the \(1860\)-edge distance-three compatibility graph, and every maximal clique. Bron--Kerbosch enumeration gives maximal-clique histogram \(2:60,4:540\). A separate increasing-order four-clique enumeration returns the same \(540\) maximum codes.

The program then implements the six toric maps and reversal, verifies their distance preservation on every vertex pair, combines them with all right translations to obtain \(1440\) distinct isometries, and computes maximum-code orbit sizes \(180\) and \(360\). Published work gives the full Cayley-graph automorphism-group order as \(1440\), so the constructed action exhausts the full isometry group.

Among the \(18\) maxima containing the identity, direct multiplication-table closure finds exactly \(4\) subgroups, each with element orders \(1,2,4,4\). Their right cosets are enumerated explicitly: each subgroup has \(30\) distinct cosets, the four coset families are pairwise disjoint, and all \(120\) coset codes lie in the \(360\)-element orbit.

Limits: the computation is exhaustive only for \(S_5\). The finite census does not establish any general formula for larger \(n\). The external full-automorphism-group order is cited rather than independently re-proved.
