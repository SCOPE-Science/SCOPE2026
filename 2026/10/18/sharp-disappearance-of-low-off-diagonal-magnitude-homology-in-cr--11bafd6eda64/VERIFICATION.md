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

# Reproducibility checks

The included `VERIFY.py` is a stand-alone Python 3 program requiring SymPy for integer Smith normal forms. It constructs the underlying graph and independently obtains the shortest-path metric by breadth-first search, enumerates admissible magnitude chains and signed boundaries, and compares the ranks over three distinct prime fields. For \(n=3,4\) it also obtains exact integer Smith invariant factors. Every representative ordered endpoint class is tested, using only obvious index permutations and exchange of the bipartition classes. The tested sizes are \(n=3,4,5,6\).

Run with `python3 VERIFY.py`. Successful execution ends with `CROWN_MAGNITUDE_LOW_OFF_DIAGONAL_CHECKS_OK`. All tested cases yielded the theorem's predicted Betti ranks, and every computed nonzero Smith invariant factor is one. Such bounded computation cannot establish a theorem quantified over all \(n\); the proof's symbolic chain and cocycle calculations provide the all-parameter argument. Neither a proof assistant nor external validation is asserted.
