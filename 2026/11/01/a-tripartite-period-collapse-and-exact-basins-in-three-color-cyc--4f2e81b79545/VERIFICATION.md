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

The included `verify.py` runs with standard Python 3. It constructs and exhaustively verifies 2,151 seven-support truncated multiplicity cases, all 343 tripartite support configurations, 64 shore-size parameter triples for the two closed counting formulas, and 25,137 directly simulated microscopic initial configurations. The output is recorded verbatim in `verification_output.txt`; its last line is `CCA_TRIPARTITE_CERTIFICATE_OK`. The reduction lemma, rather than the bounded direct simulations alone, supplies the infinite-family justification.

No independent audit or external certification has been performed. The formulas make no assertions about unexamined alternative update rules or individual three-cycle attraction-basin sizes.
