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

# Reproduction and proof boundary

Run `python verify.py` with Python 3's standard library. The supplied `verification_output.txt` records the observed deterministic result: `PASS 2372 deterministic scalar/vector/rational checks`. The program checks exact rational telescoping, one-step algebraic formulas, auxiliary-energy identities, two-dimensional preconditioned instances, and the predicted large-step asymptotics.

**Important scope:** finite numerical iterations cannot certify convergence for all future iterations or prove an exact asymptotic. The infinite-horizon conclusions instead follow from the first-exit and telescoping-tail arguments in `RESULT.md`. All packages' references refer to source publications, not to external proof or independent certification. Independent audit has not been performed.
