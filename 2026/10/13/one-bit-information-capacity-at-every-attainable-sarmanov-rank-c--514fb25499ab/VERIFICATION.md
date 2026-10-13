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

The theorem is proved analytically in `RESULT.md`. The essential-limit positivity argument supplies the conditional densities for the latent Bernoulli separator, and the equality case uses equality in two data-processing bounds. The rank calculation uses the exact extremal integral of a bounded weight on the unit interval. The complete real-parameter construction is verified algebraically.

Run the self-contained finite checker with `python checker.py`. Its exact `fractions.Fraction` arithmetic verifies 12 rational rank values, including both admissible endpoints and zero. For each it independently calculates rectangular cell masses, uniform row and column marginals, the raw \(\mathbb E[UV]\) integral used in Spearman correlation, and Kendall's concordance-minus-discordance double cell sum. It verifies that all active density cells have height two and total probability one, giving mutual information \(\log2\). Last tested result: `Exact rectangular-copula rank and MI coefficient checks PASS: 12 parameters`.

The checker does not decide any nontrivial claim for irrational parameters, arbitrary measurable kernels, infinite-dimensional function spaces, or source originality. Those points are addressed by the proof and cited literature comparison. Independent audit is not performed.
