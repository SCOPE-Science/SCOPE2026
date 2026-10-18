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

Run `python3 checker.py` from the folder containing the accompanying files. The output must match `checker_output.txt` byte-for-byte. The checker enumerates scattered subsequences of both strings and tests all possible one-letter extensions, compares the resulting maximal sets with independently constructed ascent/descent words for 15 parameter pairs, and compares independent walk counts with the ternary binomial formula through repetition count 40. The mathematical proof is in `RESULT.md`. Finite enumerations do not replace that proof and cannot establish literature novelty. Independent scientific validation has not been performed.
