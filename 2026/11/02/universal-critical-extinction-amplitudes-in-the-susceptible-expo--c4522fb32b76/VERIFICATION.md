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
# Verification record

The theorem follows from the exact drift identity \(\dot W=-(1-S)(\beta_1 I+\beta_f F)\), positive-cone invariance, Perron-mode separation of the three infectious variables, asymptotic slaving of the susceptible deficit, and the resulting inverse-mass derivative. The proof covers every seeded initial state in the stated biological domain; no finite enumeration is used to extend that quantifier.

Run `python verify_seif.py` with `sympy`, `scipy`, and `numpy` installed. The script symbolically checks the exact identity, nullvectors and center coefficient and integrates three critical parameter examples with two initial states apiece. These finite-time integrations do not prove the infinite-time asymptotic. Neither independent mathematical auditing nor independent experimental validation has occurred.
