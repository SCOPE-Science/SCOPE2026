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

# Reproducibility

Run `python3 verify_yule_cherry_cophenetic.py` with Python 3 and its standard library. The verifier generates Yule tree shapes by exact uniform leaf-splitting probabilities, separately computes common-ancestor-depth sums from leaf paths through eleven leaves, compares the formula with exact shape distributions through fourteen leaves, and independently checks the mixed-moment recurrence through 300 leaves.

A completed execution passed 4,746 exact integer/rational assertions. Finite checks are not a proof for arbitrary tree size; the analytical proof is in `RESULT.md`. The asymptotic correlation also uses previously established marginal variance asymptotics. Scientific priority is limited by the available inspected literature, with possible equivalent older work not excluded.
