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

# Verification of the completed temporal equal-shares theorem

A standard Python 3 interpreter can run `python verify.py` without any third-party packages. The program constructs exact affordable-price fractions by sorting approving balances and solving the appropriate water-filling branch. It tests OIIA (single nonwinner approval deletion), the impossibility of a profitable unilateral current-round lie, and dynamic fair-output examples, including early MES exhaustion, and a contrast with a manipulable anti-approval fallback.

Observed result: `PASS: fixed-budget profiles 66288 loser-deletion checks 184734 OSP checks 1187136 dynamic histories 22894 safe and unsafe fallback witnesses verified`.

The finite domain includes two and three voters, two and three alternatives, several discrete nonnegative frozen balance vectors, multiple price levels, and all current approval reports over the corresponding nonempty subsets. Dynamic checks use complete two- and three-round elections with explicit fixed-budget continuation after the first unaffordable round. These tests are finite consistency checks only. The theorem's universal quantifiers are justified by the candidate-separability and earliest-large-payment proofs in RESULT.md. The strengthened inherited wEJR+ axiom rests on the published theorem cited there; no independent validation was performed.
