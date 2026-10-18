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

The accompanying `verification.py` is self-contained (Python standard library). Running `python verification.py` enumerates all three-voter ranking profiles for three and four alternatives and tests each possible core for exact equivalence of Smith-set membership with internal strong connectivity and external dominance. It checks 1,512 and 207,360 core-events, respectively. It also uses exact rational inclusion-exclusion to check the anchored-cylinder expansion for seven independent rational scales: the tested example has quadratic coefficient \(289/200\) and cubic overlap correction \(199/300\).

The analytical argument in RESULT.md, not a computer experiment, supplies uniform convergence on bounded score sets, the global integrable upper bound, positivity, and total-variation convergence. General-dimensional symbolic enumeration, external proof certification, quantitative rates and independent validation were not performed.
