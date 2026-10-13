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

# Reproduction and limits

With Python 3, execute `python3 verify.py`. Successful output is:

`VERIFY_OK independent_predicate_n=1..12 OEIS_n=1..12,16,18,20 parameter_models_match_formulas`

Two different implementations recognize the same language through length twelve: the first scans all binary words and checks periods and direct palindrome splits; the second generates every palindrome-pair root and its periodic extension. Root-model cardinalities are independently asserted at every tested root length. The counts at lengths sixteen, eighteen, and twenty reproduce the published OEIS A374495 values 10444, 25488, and 60690. The published first twelve values are also compared.

This experiment only checks finite identities. The universal asymptotic proof rests on exact model counting, reflection matching, and the graph-component reduction stated in RESULT.md. Those steps, including the fixed-cutoff limiting order, must be reviewed independently for a fully independent mathematical audit.
