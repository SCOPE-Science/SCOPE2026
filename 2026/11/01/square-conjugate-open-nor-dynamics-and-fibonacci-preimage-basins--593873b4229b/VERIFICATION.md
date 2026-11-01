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

# Reproducibility and limits

The main proof is symbolic and self-contained. It uses the antitone polarity relations and exact path edge-cover enumeration, so it is valid for all finite bipartite graphs and all stated paths, respectively.

Run `python3 checker.py` to exhaustively enumerate all 682 bipartite graphs with both part sizes between one and three, verify maximal-independent-set fixed counts and square involution, then check all individual output fibers of paths \(2\le n\le15\). The recorded result is `checker_py.out`, ending `PASS bipartite_graphs=682 output_words_checked=65532`.

Compile and execute `checker.cpp` with a C++17 compiler (`g++ -std=c++17 -O2 checker.cpp -o checker && ./checker`). It enumerates every state for paths \(2\le n\le19\), compares the actual preimage frequency with the independent Fibonacci-run implementation, and tests the involution and square count. The recorded result `checker_cpp.out` ends `PASS total_initial_configurations=1048572`.

Finite runs are corroborative only. They neither enumerate arbitrary graph sizes nor constitute an independent scientific audit. No claim is made about stochastic or closed-neighborhood NOR dynamics, or about unspecified larger graph classes.
