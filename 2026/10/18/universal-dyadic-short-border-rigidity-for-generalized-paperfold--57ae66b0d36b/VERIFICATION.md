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

# Reproducibility and scope

Run `python3 verify.py` with standard-library Python 3. The verifier directly constructs generalized paperfolding words from the 2-adic index definition. It checks all 16 initial instruction choices of depth four (with zero tail), each distinct observed factor at each dyadic length from 4 through 128, against all its proper borders. It also checks an explicit shortest-border-three example at lengths 8 through 1024. An independent run returned `VERIFY_OK instruction_prefixes=16 dyadic_lengths=4..128 factor_tests=16064 sharpness_lengths=8..1024`.

The finite search does not establish exhaustive coverage of the uncountably many infinite instruction streams. The theorem's universal quantification follows from the mathematical induction in RESULT.md, not from the tests. Source inspection was limited to the materials identified under references; unindexed equivalents are a residual risk. An independent scientific audit has not been performed.
