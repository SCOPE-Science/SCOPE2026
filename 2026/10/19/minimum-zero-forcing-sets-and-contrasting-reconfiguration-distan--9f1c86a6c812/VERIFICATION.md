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

# Executed verification and boundaries

The supplied C++17 checker independently constructs the incidence graph, evaluates all \(\sum_{k=1}^{7}\binom{18}{k}\) candidate subsets using exact integer masks, and builds both exchange graphs. Its breadth-first searches visit all \(6912\) roots separately for each movement rule. The complete stdout is `verification/cpp_output.txt`.

The supplied Python 3 checker independently constructs the graph using an alternative point/line indexing and set-valued closure. It verifies every one of \(216\) distinct explicitly constructed incidence-preserving permutations; the optimal sets form \(35\) permutation orbits. Independent breadth-first searches from representatives produce identical eccentricity distributions, counts, edges and connectedness. The complete stdout is `verification/py_output.txt`.

Replay from the directory above `verification/`:

```
g++ -O3 -std=c++17 verification/verify_pappus_cpp.cpp -o pappus_check
./pappus_check
python3 verification/verify_pappus_python.py
```

The two implementations are independently structured executable finite proofs, not evidence for infinitely many graphs. Literature comparisons do not constitute independent publication-priority certification or an external audit.
