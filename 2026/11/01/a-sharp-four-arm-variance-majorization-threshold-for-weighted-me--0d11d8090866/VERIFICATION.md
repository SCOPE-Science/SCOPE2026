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

The mathematical proof appears in RESULT.md, including exact integration of same-arm and distinct-arm contributions, the Schur–Ostrowski derivative comparisons, the all-positive rational four-arm counterexample, and the continuity argument for arbitrarily many arms.

The optional reproducibility check is `python verify.py` with Python 3 and SymPy. It independently sums conditional double integrals and compares them with the power-sum formulas, checks symbolic identities, and compares rational majorization transfers. Its execution in the supplied environment returned `PASS 237 exact algebra/integral/majorization checks`.

These finite sample checks and symbolic algebra checks support the published proof; they are not claims of independent review or machine-verified universal certification. The complete proof is mathematical, and historical priority remains subject to the inaccessible full text of some older literature.
