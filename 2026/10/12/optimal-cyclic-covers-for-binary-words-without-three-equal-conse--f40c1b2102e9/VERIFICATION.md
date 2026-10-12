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

# Reproducible checks

Run `python3 construct.py` and `python3 independent_optimality.py` using Python 3.9 or later. Both files are complete, standalone, and use only the Python standard library; each prints `VERIFY_OK` only after its asserted calculations finish.

`construct.py` checks \(3\le n\le14\), creates each admissible overlap graph, adds every explicit balancing path, checks the source-to-sink endpoint bijection, produces an Euler tour, checks its edge count, and directly scans every cyclic length-\(n\) factor and every wraparound triple. `independent_optimality.py` independently enumerates the restricted graphs for \(3\le n\le13\), obtains shortest surplus-to-deficit paths by BFS, and solves the minimum perfect matching by a separate Hungarian algorithm; its values equal the stated Fibonacci optimum. The \(n=2\) base is explicitly the cyclic word `0011`.

The first test covers constructed optima and direct admissibility; the second checks optimal extra traversals by a distinct graph algorithm. Finite checks do not prove the infinite statement. The algebraic source-to-endpoint bijection, path length lower bound, and Fibonacci coefficient argument in RESULT.md establish the full quantifiers. No independent external audit has been conducted.
