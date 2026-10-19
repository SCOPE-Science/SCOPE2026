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

# Verification record

Run `python3 verify.py` with Python 3.8 or later; the program uses only the standard library. It independently computes the circular BWT by exhaustive rotation sorting, derives the structural BWT decomposition from maximal circular runs, and compares their full output strings. An additional independent cyclic suffix-doubling algorithm checks longer examples with larger ordered alphabets and independent letter-exponent vectors.

Observed output:

`VERIFY_OK full_multialphabet_BWT_decomposition exhaustive_cases=38792 randomized_suffix_doubling_cases=220 sharp_h1=01`

The exhaustive parameter domain is every mixed binary word of lengths 2–9, every mixed ternary word of lengths 2–7, and every mixed four-letter word of lengths 2–6, each with four exponent vectors. The randomized domain uses 220 deterministic seeded words of length 15–100 over alphabets of size 2–6 with exponents 2–8. The separate sharpness test compares `01` and `0011`.

No physical or empirical test proves the all-length claim; its proof is the complete rotation-order and BWT decomposition argument in `RESULT.md`. No external or independent audit has been conducted. Reproducibility requires no third-party packages.
