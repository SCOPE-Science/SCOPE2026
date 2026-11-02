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

## Reproducibility

Use the Python 3 standard library: `python3 verify.py`. The program exhaustively enumerates all flip sets for each count and the two possible initial spins using exact `fractions.Fraction` weights. It compares the direct conditional laws with independent Gaussian-binomial expressions for chain lengths \(2\) through \(11\) at \(q=1/2,1,3/2,2\). It checks odd/even paired equality, symmetric masses, strict stochastic tail comparison and monotone likelihood ratios, and independently tests the four-site condition on geometric and nongeometric odds triples.

## Observed check

`PASS exact assertions: 986`.

## Limits

Finite exhaustive enumeration does not prove results for arbitrary length or arbitrary real positive parameters. The all-length and all-parameter claims are justified by the complete algebraic arguments in `RESULT.md`; no external audit was performed. This verification does not establish historical priority.
