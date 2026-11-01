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

# Reproduction

From the directory containing this document and the included sources, execute:

```bash
python3 check_symbolic.py
c++ -std=c++17 -O2 -Wall -Wextra check_direct.cpp -o check_direct
./check_direct
```

`check_symbolic.py` reconstructs the exact capped-type map, verifies the complete \(722\)-class finite-state dichotomy and all eight formal exponential generating functions by exact polynomial arithmetic, and tests their coefficients for \(2\le n\le20\). The saved `symbolic_output.txt` records the successful run.

`check_direct.cpp` does not use the capped-type transition. It directly checks the labelled graph's vertex-to-vertex adjacency and applies the synchronous inhibitory update to every initial coloring on the five graph sizes with \(2\le n\le6\), totalling \(597861\) labelled states. It checks exact synchronization layers and primitive four-cycle return. The saved `direct_output.txt` records the successful run.

The infinite-family conclusion depends on the proven capped-multiplicity preservation identity, the exact complete finite-state enumeration and the analytic exponential generating-function conversion. Direct small-size tests alone would not prove the theorem. The finite-state checker is an executable exhaustive proof, not an independently certified formal development. No independent validation has been performed.
