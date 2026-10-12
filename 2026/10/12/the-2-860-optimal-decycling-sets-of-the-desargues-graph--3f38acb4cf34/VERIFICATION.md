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

# Reproducibility and proof limits

All finite checks refer to the twenty-vertex Desargues graph whose two classes are respectively the ten two-subsets and ten three-subsets of a five-element ground set, with containment edges.

The algebraic lower bound uses, for any deletion set \(S\) of size \(k\), the exact remaining-edge formula \(30-3k+e(S)\). If its complement is a forest with \(c\) components, then \(2k=10+e(S)+c\), implying \(k\ge6\) and exactly two possible structures at \(k=6\).

`verify.py` constructs this incidence graph and a separately specified \(GP(10,3)\) graph, and checks their explicit isomorphism. On all \(\binom{20}{6}=38,760\) deletion sets it compares a component/edge-count forest predicate against a union-find cycle test in the second graph. It reports exactly 760 independent deletion sets leaving two components and 2,100 one-edge deletion sets leaving a tree, total 2,860. The program checks 240 explicit automorphisms and verifies the 19-orbit cover, size distribution, and representatives.

`verify_gp.cpp` independently constructs \(GP(10,3)\), considers every deletion set of cardinality \(0\) through \(6\) (60,460 total), and tests the complement using union-find. It reports no successful set of size below six and exactly the same 2,860 optima, split 760/2,100.

Reproduction commands executed against these package sources:

```
python3 verify.py
c++ -O2 -std=c++17 verify_gp.cpp -o verify_gp
./verify_gp
```

The Python verifier prints `VERIFY_OK graph=Desargues=H(5,2)=GP(10,3)`, `sharp_candidates=38760`, `minimum_FVS=6`, `optimal_sets=2860`, `independent_6_2component=760`, `one_edge_6_tree=2100`, `automorphisms=240`, and `orbits=19`. The compiled verifier prints `VERIFY_GP_OK candidates_0_through_6=60460 optimum_size=6 optimum_sets=2860 edgeless_deletions=760 one_edge_deletions=2100`. File `orbits.csv` stores the 19 canonical orbit representatives. For the ordering convention, see `RESULT.md`.

The finite enumeration is exhaustive for the one graph and the specified candidate layers. It is not an infinite-family proof, a check of every other generalized Petersen graph, or an independent human audit. The prior-work comparison cannot exclude unindexed or unpublished duplicate enumerations.
