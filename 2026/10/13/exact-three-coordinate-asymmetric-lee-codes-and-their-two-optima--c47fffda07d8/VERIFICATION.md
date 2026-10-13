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

# Reproduction checks

Execute `python3 verify_ald.py` using Python 3 and `g++ -O2 -std=c++17 verify_ald.cpp -o verify_ald && ./verify_ald` using a C++17 compiler. These are the actual standalone source paths. The Python program directly implements the bit-pair ALD equation and uses Bron–Kerbosch pivot recursion; the C++ program uses the independent displayed distance matrix and greedy-coloring branch bounds.

Observed Python result: `VERIFY_OK_PY maximum=19 labeled_optima=32 maximal_cliques=618624 orbits=8,24 stabilizers=48,16`.

Observed C++ result: `VERIFY_OK_CPP edges=1752 maximum=19 labeled_optima=32 search_nodes=20812`.

The Python program checks the entire maximal-clique histogram, verifies both representative masks are actual optima, checks all their pairwise distances, evaluates all 384 explicit symmetries, and establishes that their disjoint orbits exhaust the 32 optima. The C++ program performs an independent exhaustive search with a correct upper bound and does not use output from the Python program. All arithmetic is integral. The only searched universe is the 64 quaternary words of length three; no infinite theorem, unexamined parameter range, or external validation is inferred.
