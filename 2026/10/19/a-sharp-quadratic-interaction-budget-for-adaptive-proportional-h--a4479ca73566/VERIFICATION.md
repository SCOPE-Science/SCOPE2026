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
# Verification

The full proof in `RESULT.md` establishes the conditional first and second moments and the stopped quadratic-potential identity for arbitrary finite systems. The bound is not inferred from a finite experiment. Run `python verify.py` in the same directory with Python 3; the supplied program prints `PASS: 4888 exact rational assertions`. It checks all mixed group compositions with \(1\le a,b\le14\) at five rewiring probabilities, and solves finite-state exact expectation systems on explicitly defined small fixed and topology-switching hypergraphs. It also checks equality on connected fixed pairwise systems and the sharp one-hyperedge construction.

The result assumes an active-hyperedge event count, proportional unanimous adoption and a fixed conditional propagation probability. The continuous-time expectation statement assumes a unit-rate clock per active hyperedge; neither a precise consensus-time distribution nor a general upper bound for inactive-group update attempts is certified. Independent audit: not performed.
