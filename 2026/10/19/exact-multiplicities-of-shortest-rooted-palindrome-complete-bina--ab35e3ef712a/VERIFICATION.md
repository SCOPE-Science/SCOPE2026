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
# Exact verification

The complete finite search is executable from `verify_rooted_counts.cpp`. Compile it with `g++ -O2 -std=gnu++17 verify_rooted_counts.cpp -o verify_rooted_counts` and run `./verify_rooted_counts`. It enumerates all reachable augmented de Bruijn states and all two-bit successors, starting after a compulsory \(0^k\) loop, and counts shortest paths using GCC unsigned 128-bit arithmetic with overflow checks. No randomized sampling, cutoff within an order, or heuristic pruning is used. The output must end with `VERIFY_OK rooted_palindrome_complete_counts_k=2..8`.

An independent Held–Karp tour program in `verify_overlap_tsp.cpp` obtains the same shortest cyclic lengths for every \(2\le k\le8\), checks the numbers of optimal tours, constructs an optimal cycle at each order, and directly checks coverage of every required palindrome. Its output ends with `VERIFY_OK independent_overlap_TSP_k=2..8`.

The observed rooted path counts are \(1,2,2,8,40,6272,768\) in increasing order, and the optimal lengths are \(4,8,12,22,32,60,74\). The two computations are independent formulations and agree. These finite programs do not establish general results for arbitrary larger \(k\), and have not been independently audited.
