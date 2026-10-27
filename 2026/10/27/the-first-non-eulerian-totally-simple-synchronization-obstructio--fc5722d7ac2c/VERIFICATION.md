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

# Finite evidence and its logical boundaries

The C++ enumerator generates the complete labeled target-pair space \(inom{n+1}{2}^n\) at each \(n=2,3,4,5\), retains one representative per vertex-isomorphism orbit, and decides strong connectivity, period, lumpability and every coloring. The program uses exact integer arithmetic. Stored canonical graphs and summary tables are included for crosschecking; they are not themselves independent proof of full coverage without executing the enumerator.

The independent `scripts/check.py` rechecks **every** stored representative, permutation-orbit size, primitive property and normalized positive left eigenvector, then uses a pair-merger fixed-point test for synchronization rather than the enumerator's full-subset BFS. For all orders it checks proper block partitions separately. This replay printed `INDEPENDENT_CHECK_PASS` and identified four non-Eulerian five-state simple non-total classes, with stationary spectra and counts 2+2. The primary five-state marginal counts also match the previously published 1,220 and 890.

Reproduction: compile `scripts/enumerate.cpp` with `g++ -std=c++17 -O2`, run it with arguments 2, 3, 4, 5 to regenerate `data/graph_N.csv`, compare `data/stats_N.txt`, then run `python3 scripts/check.py --data-dir data`. These are finite exhaustive procedures, not assertions about larger graphs. No external independent scientific audit has been performed.
