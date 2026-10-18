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

# Reproducible verification

Run `python verify_negation.py` with Python 3. The program independently enumerates labelled height-at-most-two incidence frames with 1–3 maximal points and 0–4 nonmaximal points, plus frames with 4 maximal points and 0–3 nonmaximal points. Every nonmaximal point has a nonempty maximal-successor set; every such labelled assignment is included. The program constructs actual upper-closed subsets and negates them by requiring disjointness of the corresponding principal upset, not by applying the claimed formula as an oracle. It then checks the predicted output map, exact fiber sizes, Möbius-recovered incidences, and normalized probabilities.

Observed standard output:

`VERIFY_OK exhaustive_labelled_two_level_frames=6543 independently_enumerated_upsets=224635 height_three_boundary=3`

The test additionally checks a three-point-chain boundary with a non-power-of-two fiber. It is a bounded consistency test, not a proof for arbitrary sizes. The full proof is in `RESULT.md`, including the necessary and sufficient recognition conditions and the unordered-output counterexample. Independent external audit and independent validation have not been performed.
