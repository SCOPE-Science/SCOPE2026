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

# Reproducible finite verification

The Python and C++ programs each enumerate all 45 ordered integer pairs \(2\le m<n\le11\). For every pair, a FIFO breadth-first search begins with both complete state sets, applies the two declared transition functions to subsets, records newly discovered states and their predecessor, and stops at the first dequeued pair of singletons. The returned distance is minimal because the entire reachable search frontier at smaller distances was exhausted before the first goal could be dequeued. Each program then replays its witness against both complete automata.

Run in the directory with the embedded source files:

```sh
python3 verify_python.py
g++ -O2 -std=c++17 verify_cpp.cpp -o verify_cpp
./verify_cpp
```

The programs create `table_python.csv` and `table_cpp.csv`, respectively. Use a CSV parser to compare all records against `table.csv`, allowing for system-specific line endings. Each row includes the exact length, a lexicographically earliest shortest word, and the count of subset-pair states discovered before goal dequeue. Equality on all 45 rows was observed. The largest pair has 10 and 11 states, and a finite subset-pair universe with fewer than \(2^{21}\) vertices. There is no timeout-based nonexistence inference and no reliance on a partial enumeration.

The exhaustive claim is restricted to \(2\le m<n\le11\). Independent mathematical audit is not performed. The all-size divisible-size zero-overhead lemma follows separately from the classical Černý reset word, and is not contingent on the finite computation.
