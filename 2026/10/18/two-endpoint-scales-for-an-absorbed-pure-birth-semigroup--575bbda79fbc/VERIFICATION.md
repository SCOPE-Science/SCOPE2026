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

# Verification

The included `checker.py` is a standalone Python 3 standard-library script. Run `python checker.py` from a directory containing that file. It builds the generator on \(n+1\) states, calculates \(e^{tQ_n}\) by a Taylor series with scaling/squaring, differentiates by matrix multiplication and directly takes absolute row and column sums, independently of the probability formulas. Its tests cover dimensions \(n=1,\ldots,10\) and 16 times each, grid checks of the optimized \(\ell^\infty\) constant for \(n=1,\ldots,20\), and finite root checks for several larger dimensions. It reports `CHECKER_OK 2356 finite comparisons` when all assertions pass.

Mathematical completeness depends on the analytic derivation in `RESULT.md`, not on finite checks. The proof accounts for all integer interface ties in the Poisson mode, terminal-column contributions and the large-dimension regime. The first-order \(\ell^1\) cutoff index is not specified explicitly; the assertion is eventual. Neither independent checking nor historical-priority certification has been performed.
