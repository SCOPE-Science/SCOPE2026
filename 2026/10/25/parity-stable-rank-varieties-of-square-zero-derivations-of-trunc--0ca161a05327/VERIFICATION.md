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

# Reproducible verification

Run `python3 verify_square_zero.py` using the standard Python library. The program independently enumerates the coefficient vectors for every derivation of \(\mathbb F_q[t]/(t^n)\) for \(q=2\), \(2\leq n\leq12\), and \(q=4\), \(2\leq n\leq7\). For each vector, it checks the truncated multiplication identity \(ff'=0\), builds the actual derivation matrix over the corresponding finite field and computes the rank by Gaussian elimination. The program compares the resulting rank histograms against the closed formula for all seventeen cases and prints `SQUARE_ZERO_DERIVATION_RANK_OK` only if all pass.

The script never uses the valuation-rank formula to determine an observed rank: only the test comparator uses the closed formulas. The infinite-family proof instead rests on the exact identity \(D_f^2(t)=ff'\), the odd-coefficient vanishing criterion, rank of multiplication on even powers, and the explicit rank-stratum charts. The computation does not test scheme-theoretic nilpotents, non-finite or characteristic-odd fields, or publication priority. No independent mathematical audit has been conducted.
