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
The mathematical proof in `RESULT.md` is the primary verification.

`verify_chain_preconditionals.py` provides an independent finite replay. For each \(2\le n\le8\), it constructs all activation patterns, checks the five preconditional axioms, conditional identity, semicomplementation, and double-negation inflation, and confirms the count \((n-2)!\). For \(2\le n\le6\), it separately exhausts all row maps satisfying the elementary chain constraints and filters them by importation, then checks exact set equality with the activation construction.

The finite replay does not prove the unbounded theorem by exhaustion; it checks the derived normal form and small cases against a separately generated search space.
