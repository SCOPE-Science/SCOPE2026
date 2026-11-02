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

The theorem has been checked by reconstructing the finite-subformula Horn lemma, establishing both directions of the certificate-to-model argument, and verifying that a single finite generator suffices in the canonical rule-generated closure semantics. Propositional restriction establishes NP-hardness for satisfiability and coNP-hardness for validity. Direct bounded derivations and finite Horn saturation were compared on 1,568 cases over all sixteen choices of axiom schemes using `checker.py`; the expected output is `ALL_CHECKS_OK`.

The finite checks do not certify arbitrary-size expressions or the correctness of the literature comparison; the proof and cited semantic completeness theorem carry those obligations. The result does not claim complexities for extensions with modal inference rules or arbitrary-premise consequence.
