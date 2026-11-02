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

# Verification evidence

Execute `python3 checker.py` using a standard Python 3 installation. No third-party libraries or external data are used. The checker constructs all BALFI unary-table pairs on Boolean reducts with one and two atoms and tests eight terms and all one-variable valuations, giving exactly 41,568 evaluation/compression cases. It then tests 2,000 randomly generated instances on reducts with two to six atoms using a fixed seed. It checks coordinate separation, operator-table completion, local identities, induction over subterms, certificate consistency and preservation of counterexamples. It also independently checks a formula that distinguishes one- and two-atom countermodels. The recorded successful output is:

```
EXHAUSTIVE_CASES=41568
SEEDED_RANDOM_CASES=2000
ONE_ATOM_INSUFFICIENCY_WITNESS=OK
ALL_CHECKS_OK
```

This is finite test evidence only. No numerical experiment proves the theorem for unbounded formula size or Boolean atom count; that guarantee comes from the separating-coordinate construction and completed-operator proof in `RESULT.md`. The result depends on the established BALFI completeness and coNP-hardness of RmbC. No independent audit was performed.
