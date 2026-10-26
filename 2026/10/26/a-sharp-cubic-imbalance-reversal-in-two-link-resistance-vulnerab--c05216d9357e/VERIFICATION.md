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

# Reproducibility and limits

Execute `python verification/check.py` in the package root with SymPy installed as specified in `verification/requirements.txt`. The program checks symbolic formulas for the three edge motifs, each interaction, all three critical damage differences, the positive-coefficient certificate, the cubic signs and integer bracket, plus 100 independently inverted rational Laplacian examples and 52 exact integer-boundary checks.

Observed execution: `VERIFY_OK 152 exact direct and integer-boundary checks; all symbolic identities and positive coefficient certificates`.

The checks evaluate exact rational identities, not floating-point fit. The all-parameter argument is the spectral-projector, rank-two-inverse and sign proof in `RESULT.md`. Direct inversion on finite graphs is evidence for formula implementation, not an exhaustive infinite proof. The matching-deletion disjoint motif was previously treated in the cited literature; complete priority for the comparative ordering has not been externally established.
