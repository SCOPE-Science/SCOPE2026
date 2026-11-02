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

## Reproducibility
The included `verify.cpp` uses only the C++17 standard library. Compile and execute using `c++ -O2 -std=c++17 verify.cpp -o verify && ./verify`.

In ten small cases the program independently builds the original graph, enumerates all vertex subsets, and checks the domination and capacity conditions directly. It separately runs an exact cyclic-column dynamic program over all omitted-state types, including singleton rows, for \(3\le m\le8\) and \(3\le n\le34\). The observed output is:

```
DIRECT_ORIGINAL_GRAPH_EXHAUSTIVE_OK 10 CASES
COLUMN_PATTERN_DP_OK 192 CASES
VERIFY_OK
```

The algorithm makes no claim of checking infinitely many pairs. The universal claim relies on the run-gap inequalities and constructive proof in `RESULT.md`. All counts concern labelled graph vertices. The literature comparison does not establish absolute priority. No independent external audit has been performed.
