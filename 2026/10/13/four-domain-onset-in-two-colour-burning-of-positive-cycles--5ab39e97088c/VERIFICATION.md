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
# Verification scope

The attached `verify_burning_cycles.py` explores the entire finite successor-state graph at orders \(3\)–\(10\), recording every reachable terminal sign word and its cyclic boundary count; it also checks all \(2^n\) candidate words against that exact terminal set to obtain the covering radii. The implementation asserts the complete size sequence, the zero/two/four-boundary counts and four cyclic run-length classes for order ten.

The separately written `verify_burning_cycles_independent.py` uses ternary-integer encoding and memoized recursive exploration, rather than the primary tuple-based breadth-first search. Its exact output sets are compared to the primary sets by `crosscheck_burning_cycles.py`, which prints `ALL_TERMINAL_SETS_MATCH`. Recorded, reproducible text outputs are embedded as `bfs_output.txt`, `dfs_output.txt`, and `crosscheck_output.txt`.

Correctness of the finite case follows from the complete successor relation (one legal ignition after a simultaneous spread, unless fully burned) and strict increase in the number of burned vertices at each nonterminal round; the implementation explores all such choices, without pruning. The separate all-order construction is a direct proof for arbitrary \(n\geq10\), not a numerical extrapolation. No results beyond the declared finite exact code/radius range are experimentally or analytically certified.

Run all three scripts from the same directory with Python 3.10+; no external dependencies are needed. Their printed outputs must match the embedded output files. This is reproducible self-review, not an independent external audit.
