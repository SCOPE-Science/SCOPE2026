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

The exact rational identity checks in `verify.py` compare each of the symbolic differences needed for the classification with an independently written target expression. The program checks the sign-based allocation table for 16,170 pairs of sizes and compares 1,876 full grounded-Laplacian inverse traces, evaluated by exact Gauss–Jordan elimination over rational numbers, against the closed formula.

Executed command: `python verify.py` (SymPy installed).

Recorded output:

`VERIFY_OK symbolic_identities=5 exact_phase_cases=16170 dense_grounded_inverse_cases=1876`

The proof is analytical for all integers \(2\le p\le q\), and the finite experiments are consistency tests only. No external mathematical audit has been performed. Calculations do not address other leader budgets, nonunit conductances, or other stochastic models.
