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
# Reproduction and verification

Run `python checker.py` with Python 3. The actual run of the bundled script produced:

```text
VERIFY_OK finite_team_symbolic_comparisons 18830 formulas 210
VERIFY_OK qbf_translation_cases 400
```

The first suite generates nonempty teams in pure-equality domains of sizes one to three with one or two free columns, computes the source weak-quantifier semantics by direct element enumeration, and compares it against an equality–constancy evaluator. All team subsets in those finite universes are included. The second suite generates 400 quantified Boolean matrices and checks the guarded two-element translation on domain sizes one through three. Additional cutoff comparisons are carried out inside the script.

The machine checks do not establish arbitrary-size quantifier behavior or complexity lower bounds. Those are proved using profile transitions, a polynomial cardinality cutoff and the explicit polynomial reduction in the mathematical result. Empty teams are handled by the empty-team property and are not used as satisfiability witnesses. No external proof assistant or independent validation is claimed.
