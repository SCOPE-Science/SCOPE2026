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

# Exact arithmetic verification

Execute `python3 verify.py` using only the standard Python library. The script constructs Möbius values, computes the gcd-one subset count independently by inversion, computes divisor-sum and gcd-coprimality counts, checks the exact gcd-stratum identity through index 240, and exhaustively enumerates all nonempty subsets up to index 16.

Observed output: `VERIFY_OK mobius_and_gcd_strata=240 brute_force_subsets_n1to16=131054 parity_cases=237`.

The finite code checks all index boundaries required by the analytic argument but is not a proof for infinitely many indices. The mathematical proof in RESULT.md supplies that universal argument. No independent mathematical audit has been performed.
