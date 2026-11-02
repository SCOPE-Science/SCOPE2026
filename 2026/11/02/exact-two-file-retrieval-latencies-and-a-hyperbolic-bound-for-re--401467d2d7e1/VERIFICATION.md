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

# Mathematical verification

The exact expectations were independently evaluated by finite-state absorption recurrences over all subsets of sampled labeled columns, with repeated proportional columns treated as separate coupon labels. `verify.py` uses exact rational arithmetic. Its first stage checks 297 parameter cases against the beta formulas and against the strict bound; its second stage checks an extended rectangular grid of dimensions and multiplicities. `verification_output.txt` records outcomes. The proof of every parameter uses the explicit Poissonization and inequalities in `RESULT.md`; no finite sweep is claimed to prove the general theorem. Source comparison does not exclude unindexed priority.
