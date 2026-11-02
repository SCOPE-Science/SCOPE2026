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

Run `python3 verify_markov_pal.py` from the extracted package. The script is standard-library-only and checks actual **sets** of scattered subsequence strings rather than positional embedding counts. Exhaustive lengths 1–12 comprise 8,190 binary source words. A second interval recurrence independently evaluates all 32,768 words of length 15. The exact rational tests use transition probabilities \(0,1/4,1/2,3/4,1\). Positive-root monotonicity on 100 grid points is a numerical stress test, not the proof of strict monotonicity. The algebraic proofs of the asymptotic and monotonicity are contained in RESULT.md.

Expected successful terminal output:

`VERIFY_OK explicit_words=8190 explicit_n=1..12 interval_words=32768 interval_n=15 probability_cases=5 coefficient_comparisons=70 monotone_root_grid=100`

The verification does not certify independent review. It does not prove facts beyond its finite ranges, and the results make no claims for other Markov source families.
