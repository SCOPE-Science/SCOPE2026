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
# Verification and reproducibility

The analytic reconstruction checks the entire-trajectory coding with unit-speed edges and a uniform suspension phase; exact balance at every vertex; condensation-graph cancellation of transient flux; SCC reachability with the **all backward trajectories** quantifier; incidence-rank dimension; stationary Markov entropy envelope; and the Perron--Frobenius relative-entropy identity including zero weights.

The accompanying standalone `verify.py` evaluates (i) the three-loop bouquet, (ii) the two-vertex graph with two forward and one reverse edge, and (iii) two loops with a one-way connector. It checks Kirchhoff balance, exact rational ranks and entropy endpoints to floating tolerance. This is a finite illustration, not exhaustive graph enumeration and not an infinite-proof certificate. The complete proof is in `RESULT.md`.

Only finite directed graphs in which every vertex is on a directed cycle and unrestricted unit-speed switching trajectories are considered. The maximum entropy is over all stationary trajectory **lifts** of each state marginal. Originality was checked against the accessible text and statements listed in the audit; a full-text comparison with all possibly dominating sources remains a limitation.
