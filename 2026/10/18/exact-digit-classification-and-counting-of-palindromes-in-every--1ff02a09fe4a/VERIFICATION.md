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

# Reproducibility

Run `python3 verify_palindromes.py` from the directory containing this file and the standalone checker. It uses Python standard-library exact integers only. Expected line:

`VERIFY_OK numeric_profiles=138 tested_integers=216390 accepted=632 symbolic_profiles=2128`

The numerical part checks canonical expansions by repeated division in two bases, independently compares raw digit-palindrome truth with the structural word criterion, and counts accepted integers for small parameters. The symbolic part constructs equality constraints on digit positions without using the proposed closed formula as the source of the equivalence relation. The checker was executed successfully against the packaged source.

These checks cover finitely many bases and lengths; the universal theorem is established by the constructive digit-reversal proof, not by the finite computations. No independent proof validation has been performed.
