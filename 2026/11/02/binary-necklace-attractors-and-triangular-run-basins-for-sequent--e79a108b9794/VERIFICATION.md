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

# Verification evidence and limits

The proof is self-contained in `RESULT.md`; its central recurrence and every quantifier are stated explicitly. The following independently structured computational cross-checks can be rerun from the packaged standalone sources:

```sh
python3 checks/check_python.py
c++ -O2 -std=c++17 -Wall -Wextra -pedantic checks/check_cpp.cpp -o check_cpp
./check_cpp
```

The Python implementation separately calculates local populations for the sequential sweep and checks every state for \(3\le n\le12\); it also tests fiber counts and per-cycle triangular-run basin sizes using its own orbit traversal. Its captured output is `checks/python_results.txt`. The C++ implementation separately recomputes each vertex update and traverses all configurations for \(3\le n\le18\); it checks one-step image cardinality, rotation action, predecessor fibers and the partition into basins. Its captured output is `checks/cpp_results.txt`. Both emit a final PASS line.

These are finite experiments. They do not certify infinite families independently or replace the explicit mathematical proof. There is no claim that checked finite instances establish a novelty or significance judgment.
