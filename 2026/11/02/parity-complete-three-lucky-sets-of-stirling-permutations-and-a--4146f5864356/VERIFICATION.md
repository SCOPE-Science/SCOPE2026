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
# Reproduction

Run `python3 verify.py` in the directory containing this file and the standalone script. Python's standard library is sufficient. The script validates actual Stirling nesting and all car parking outcomes for each construction in orders 3 through 60, for 112520 case/parameter combinations. Its separate recursive maximum-pair insertion enumerator examines all Stirling permutations for orders 3 through 8, including the 2027025 permutations of order eight. It reproduces the parity-sector counts and verifies the claimed sufficient even-even region at those small orders. The run must finish with `VERIFY_OK`.

This verifies finite computations and reproduces the constructive witness formulas; it cannot by itself certify the theorem for all orders. The infinite proof is supplied in RESULT.md. The original source's two-lucky construction and necessary lemmas were independently checked against the original open-access full text.
