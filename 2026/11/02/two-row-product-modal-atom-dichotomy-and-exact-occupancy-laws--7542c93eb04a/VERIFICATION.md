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

# Reproduction and limits

Run `python3 checker.py` with the Python standard library. It enumerates all \(17{,}208\) colourings in the indicated finite configurations, iteratively refines the propositional partition under both modal relations, tests the predicted atom count and least modal depth for every colouring, and compares the empirical exhaustive count distribution with the exact Stirling-number formula. The expected summary is `ALL_CHECKS_OK complete_coloured_models= 17208`.

A separate support-set sweep considered every nonempty ordered-pair support for three colours (511 cases) and four colours (65,535 cases), and agreed with the structural formula. That separate sweep was used as corroboration; `checker.py` already reproduces the central exhaustive comparisons.

These computations cannot establish claims for unbounded column count. The complete proof uses explicit depth-one/depth-two formulas, modal-bisimulation preservation, surjective occupancy, and a uniform omission estimate. No external audit or independently certified proof is claimed.
