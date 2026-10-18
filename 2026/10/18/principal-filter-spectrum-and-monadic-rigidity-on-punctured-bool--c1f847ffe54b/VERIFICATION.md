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

Run `python3 verify.py` using Python 3 and its standard library. The script enumerates all candidate coordinate tuples for \(n=2,3\), explicitly reconstructs their filter-valued operators, checks the defining quasi-modal axioms and counts those with entirely principal outputs. Independently, it tests the published monadic operator axioms in the Boolean-quantifier and original relational formulations and checks the exact Bell counts and the unique principal monadic case.

Observed output:
```
n=2 QMO=16 necessity=9 prediction=9 monadic=2 monadic_necessity=1
n=3 QMO=512 necessity=175 prediction=175 monadic=5 monadic_necessity=1
VERIFY_OK
ORIGINAL_RTM 2 monadic 2 principal 1
ORIGINAL_RTM 3 monadic 5 principal 1
ORIGINAL_RTM_OK
```
The verifier is a finite check, not a proof of any universal claim. The full proof is supplied in RESULT.md. Historical priority remains subject to independent scholarly comparison; no independent audit has been performed.
