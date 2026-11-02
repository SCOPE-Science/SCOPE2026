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

# Verification record

The supporting program `verify_even_orders.py` requires only Python 3.9 or newer. Run `python3 verify_even_orders.py trees.json` in the artifact directory. The program reconstructs even permutation words from inversion parity and every pairwise precedence predicate, applies the complete Boolean shattering recurrence, and rejects each depth one larger than those asserted for labels one through seven. For the two smallest sizes it checks depth one fails.

The witness data `trees.json` contains complete branch-specific query trees with an explicit even permutation at every leaf. The checker ensures every query is valid, every leaf witness is even, every answer along the branch is correct, and all root-to-leaf witnesses are distinct. `generate_even_trees.py` regenerates those witness trees deterministically; it is not relied on by the standalone checker except for generation.

The checker separately enumerates static support signatures for all edge subsets of size at most \(n-1\), for every \(2\le n\le6\), and matches each to the unrestricted structural proof's parity prediction. Sets of more than \(n-1\) edges contain an undirected cycle and are proved unshatterable without enumerating them.

The successful local replay yielded `ALTERNATING_COMPARISON_ALL_CHECKS_PASS 1317 1322`, with 121,279 memoized states in the seven-label upper-bound test. Full stdout is in `even_order_check_output.txt`. Computations do not establish general values for \(n\ge8\), and cannot certify historical novelty or independent review.
