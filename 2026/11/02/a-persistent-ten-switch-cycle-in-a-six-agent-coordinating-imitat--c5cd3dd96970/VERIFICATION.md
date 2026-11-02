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

# Reproduction and boundaries

The included `verify_cycle.py` is a self-contained Python 3 exact-integer checker, requiring no nonstandard packages. Execute `python verify_cycle.py`. It checks symmetry and simplicity of the nine-edge graph, all six opponent-coordination inequalities, the ten specified state changes, strict best-response improvements, unique imitation maximizers, the idle sixth-player update, and exact periodic return under the eleven-activation fair word. The run passed with `PASS: strict 10-switch orbit, fair 11-activation periodic schedule; exact integers`.

The verification establishes a finite counterexample to the universal deterministic convergence proposition. It does not prove minimality of the six-vertex graph or quantify the likelihood of the periodic schedule in a stochastic model. Neighbor-only imitation must not be confused with the distinct rule requiring a neighbor to earn strictly more than the imitator. The proof and the verifier establish the exact former rule, with no external certification or independent audit.
