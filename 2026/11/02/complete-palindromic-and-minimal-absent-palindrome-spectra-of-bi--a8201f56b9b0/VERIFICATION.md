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

# Reproducibility and evidence boundary

The included standalone `verify.py` requires only the Python standard library. Run it with `python verify.py` after extracting the files. It checks all triples of integers \(1\le a,b\le7\) and \(1\le k\le8\) for \(W=(0^a1^b)^k\). Direct literal enumeration produces the full set of contiguous factors, the distinct palindromic factors, and all missing palindromic one-letter extensions of occurring palindromes. The results are compared against the independently constructed two-wing families, every coefficient of the predicted length polynomial, the total count, and the maximal MAPW length.

Observed output:

`VERIFY_OK cases=392 distinct_palindromes=14504 distinct_MAPW=15680 length_checks=14504 total_n_plus_four=True longest_n_minus_min_plus_two=True`

All checks completed successfully. This test set is finite and cannot establish correctness for unbounded exponents; the proof in `RESULT.md` supplies the infinite-parameter argument. The literature comparisons in `REVIEW.md` are provisional rather than a certification of absolute novelty. No independent audit has been performed.
