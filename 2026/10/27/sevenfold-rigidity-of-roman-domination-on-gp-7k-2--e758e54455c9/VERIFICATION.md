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

The standalone file `critical_cycle.cpp` builds every four-column state and allowable five-column transition, verifies each nonnegative reduced cost, and identifies every strongly connected component of the zero-slack subgraph. Compile under C++17 with `g++ -std=c++17 -O2 -Wall -Wextra -pedantic critical_cycle.cpp -o critical_cycle` and execute `./critical_cycle`. The recorded output `critical_cycle.out` was reproduced by executing the packaged source; its central counts are 6,561 states, 48,681 arcs, 14,744 zero-slack arcs, and one directed seven-cycle as the only cyclic component.

Run `python3 independent_critical.py`; its pure-standard-library implementation independently generates the transfer graph, computes potentials by queue relaxation, and computes components by a reversed-edge search. The resulting `independent_critical.out` agrees with the C++ certificate on all critical counts.

Compile `independent_bruteforce.cpp` under C++17 and run it. The program independently uses closed-neighborhood bit masks and the canonical property that any label-one vertex adjacent to a label-two vertex could be lowered to zero in an optimum. Its result `independent_bruteforce.out` gives exactly seven optimum configurations at lengths seven and fourteen, with respective minimum weights eight and sixteen. Its \(n=8\) census is only a boundary check, not a general statement.

These are complete finite checks of the 6,561-state lemma, but the infinite theorem also requires the mathematical correspondence between cyclic RDFs and closed walks, telescoping of the potential, and the fact that a closed walk in the tight graph must lie in its unique cyclic component. Executing code or inspecting a log alone does not establish those deductions. No independent external audit has been performed.
