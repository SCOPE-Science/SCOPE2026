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

Run `python VERIFY.py` from the directory containing this file. This dependency-free script uses exact rational arithmetic to invert the three-state transient generator from separately encoded Markov transitions and compare against the closed formula, testing positive rates, both boundary allocations, the central allocation, the critical threshold, the signed gap, and strict orderings across a finite rational grid. Observed output: `VERIFY_OK assertions=73158`.

A separate symbolic simplification confirmed that substituting the area-dependent rates into the first-step rational mean yields the polynomial formula. All universal claims follow from the displayed analytic proof, not from the finite grid. The verifier does not test arbitrary real inputs exhaustively, does not certify historical originality, and does not constitute independent mathematical review. The model has no field-data or external validation.
