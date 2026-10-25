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

The C++17 enumerator `verify_n5.cpp` generates 126 five-coordinate nonnegative vectors of total five, forms the complement of the unit-transfer conflict graph, and exhaustively enumerates cliques of size 26. Greedy proper-color bounds are safe upper bounds on clique cardinalities of remaining candidate sets. It returned exactly six candidates after 3,154,612 recursive calls. Every returned candidate is a 26-vertex clique.

`verify_additive.py` is an independently implemented standard-library crosscheck: from all 120 permutations of field labels it reconstructs exactly six distinct checksum codes and verifies equality with the six enumerated sets, verifies all pairwise distances, computes each positive-coordinate partition profile, and checks every one of 70 possible length-four multiset outputs occurs in exactly one deletion shadow. The recorded output ends in `VERIFY_OK`.

To replay: `g++ -std=c++17 -O2 verify_n5.cpp -o verify_n5`, then `./verify_n5 > verify_n5.out`, then `python3 verify_additive.py verify_n5.out`. This executable uses the `unsigned __int128` compiler extension. Exact finite enumeration is the proof of six-code exhaustion; correctness of the color-bound branch logic is explained in `RESULT.md`. No statement for other alphabet sizes or blocklengths is certified by these tests.
