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

# Reproducibility and limits

Run `python verify.py` using Python 3 and SymPy. The verifier exhaustively forms every nonempty positional subsequence of each tested source word, deduplicates palindrome strings and weights all source words using exact rational probabilities. It independently builds the formal expectation coefficients from geometric probability series and compares them term by term.

Test distributions and maximum source-word lengths: \((1/2,1/2)\) through length 10; \((1/3,2/3)\) through 9; \((1/3,1/3,1/3)\) through 7; \((1/2,1/3,1/6)\) through 7; four equal quarter probabilities through 6. In total, 15,091 source words were examined (including length zero separately for each distribution). The same verifier computes seven exact rational values of the sharp \(z=4/5\) inequality and symbolically checks the four-uniform rational specialization.

Expected final line:

`VERIFY_OK distributions=5 exhaustive_source_words=15091 sharp_bound_trials=7 exact_q4_gf=true`

The infinite claim is proved by geometric waiting-time independence, the even/odd palindrome decomposition, strict nonnegative coefficient arguments, and the exact square-deficit identity. Tests only check representative cases and cannot establish originality or independent certification. The real analytic pole argument requires at least two positive source probabilities; deterministic singleton sources are excluded.
