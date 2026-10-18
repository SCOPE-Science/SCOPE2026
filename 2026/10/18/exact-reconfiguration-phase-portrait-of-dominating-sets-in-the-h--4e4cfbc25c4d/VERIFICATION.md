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

# Reproducibility of finite classification

Run `python3 verify.py` with Python 3.10+ (requires `int.bit_count`) from the directory containing `verify.py`. The checker exhaustively tests all \(16384\) subsets by their fourteen closed-neighborhood intersections, reconstitutes all minimal dominating sets independently of the expected geometric constructions, asserts equality with the four constructions, tests every budget up to \(8\), checks the exact component/edge counts, and performs a breadth-first traversal from every state in the main component at budgets \(5\) through \(8\). The observed terminal line is `VERIFY_OK full exhaustive classification`.

As an independent implementation, compile and run `g++ -std=c++17 -O2 verify_fast.cpp -o verify_fast && ./verify_fast`. This builds the Fano plane from nonzero three-bit vectors and uses an incremental bitwise union-of-closed-neighborhoods domination test. It runs all-source BFS over the same budgets and validates all expected aggregate numbers, finishing with `VERIFY_OK C++ independent graph and metrics`. The two checkers have no shared source file, dependency or state and require no external network access. Mathematical consistency checks include the \(21\) minimum dominating sets, the \(65\) inclusion-minimal sets and the \(K_{1,10}\) components at budget \(5\).

The finite cutoff is exact because the universe consists of all \(2^{14}\) bit masks and every adjacent reconfiguration mask is explicitly considered. These checks do not prove any untested infinite-family extension. The direct structural minimal-set overlap lemma in RESULT.md explains the component barriers without making numerical BFS certificates into claims about other graphs. Neither program performs an independent external literature audit, and no independent review has been represented as performed.
