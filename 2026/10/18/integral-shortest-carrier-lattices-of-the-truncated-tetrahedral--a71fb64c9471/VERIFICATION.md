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

Use Python 3.11+ with the pinned dependency in `requirements.txt` and execute `python3 verify.py`. The script constructs the twelve graph vertices, all eighteen graph edges, all 1009 nonempty matching simplices, and the entire nonempty Hasse face poset. It checks 493 matching pairs, acyclicity of all 3558 directed cover relations, and the critical-cell multiplicities \(1\) in dimension \(0\) and \(22\) in dimension \(3\).

The complete enumeration of graph \(P_3\)-factors produces 111 distinct eight-edge supports, each a join of four zero-spheres. Each of the 111 explicit sixteen-simplex signed fundamental cycles has zero simplicial boundary. Integer algebraic-Morse reduction annihilates the boundary of all 144 four-dimensional simplices; all 111 projected cycles have coordinate gcd one. The complete 22-by-111 coordinate matrix has 22 unit Smith invariants, and the specified 22-column submatrix has determinant \(+1\).

All 24 permutations of four symbols are applied to all 111 supports. The exact eight-orbit partition and integral ranks are checked. Every union of two and of three orbits is processed by integer Smith form, not by floating-point rank or modular rank alone. Four of the 28 pairs and 19 of the 56 triples span integrally or rationally respectively, and the sole non-saturated full-rank triple has Smith factors \((1,\ldots,1,2)\).

The flag-support lemma and its equality characterization are written and proved in `RESULT.md`; their conclusion is not inferred from checking this finite complex. All package checks concern this exact graph and no infinite-family claim. Publication priority and independent external validation have not been certified.
