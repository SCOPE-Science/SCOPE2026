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

The ordinary zero forcing rule is evaluated by repeated explicit examination of blue vertices and their remaining white neighbours; the implementation does not use the structural characterization to decide a force. Separately, the predicted classification and the closed-form coefficient formulas are evaluated and compared.

The supplied `verify.py` checked all \(407{,}040\) initial colourings in \(130\) graph parameter triples with \(3\leq m,n\leq7\), \(m+n\leq14\), and every permitted \(t\), reporting `VERIFY_OK`. This independently exercises every stated boundary regime, including \(t=0\), \(t=1\), and full matching deletion.

Finite tests do not establish the theorem for larger parameters; the proof in `RESULT.md` covers arbitrary integers in the stated domain. No external independent validation is claimed. The literature comparison did not include the inaccessible full text of a related thesis; uniqueness is not certified.
