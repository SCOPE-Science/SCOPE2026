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

# Verification of the alternating binary palindrome formulas

Running `python verify_alternating.py` constructs every distinct scattered subsequence of \(w_N\) for \(N=0,1,\ldots,22\) by explicitly extending a set of strings. Literal palindrome filtering yields \(p_{N,k}\). Separately, coefficient recurrence for the proposed rational bivariate generating function reproduces the full exact length distribution for every tested \(N\). The two parity-resolved Fibonacci formulas and the first ten values of the published binary maximum-count table also agree. Expected success output is `VERIFY_OK alternating_prefix_lengths=0..22 exact_length_spectra=TRUE Fibonacci_formula=TRUE original_table_n=1..10=TRUE`.

These finite computations do not certify the all-length theorem by themselves. The infinite proof requires the coordinatewise optimal greedy embedding, the unique decomposition of palindromes into outer half and center, correct treatment of even and odd centers, the minimal-cost-to-prefix cumulative transform, and valid coefficient extraction. Each step is given in `RESULT.md`. Independent external auditing has not been performed.
