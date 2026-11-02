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

# Computational checks and reproducibility

Run `python verify.py` with Python 3 and its standard library. The program independently computes \(\binom{2n}{n}\) as an integer for the first five positive indices of every odd prime below \(5000\), checks the predicted first discrepancy, and directly checks the parity law for the first \(700\) positive indices for each of the primes \(3\) and \(5\). It verifies all sixteen sign patterns, each of multiplicity twelve, by independently evaluating Legendre characters for representatives of the \(192\) units modulo \(840\). Finally, for every \(1\le L\le6\), it enumerates the shifted-index interval, computes binomial residues digitwise, and compares to the three exact count formulas. The largest interval comprises \(7812\) indices.

The executed result was:

```
VERIFY_OK primes_tested= 668 first_failure_counts= {None: 2, 1: 332, 2: 167, 3: 80, 4: 41, 5: 46} exceptional_indices= 1400 dirichlet_patterns= 16 digit_levels= 6 max_shifted_terms= 7812
digit_counts= {1: {2: 1, 0: 1}, 2: {2: 4, 0: 8}, 3: {2: 12, 0: 49, 3: 1}, 4: {2: 32, 0: 272, 3: 8}, 5: {2: 81, 0: 1441, 3: 40}, 6: {2: 204, 0: 7448, 3: 160}}
```

The formulas for infinitely many primes and all positive integer levels are proved mathematically, not by exhaustion. The finite tests neither establish prime density nor assert historical novelty. The primary 2014 source was not fully available, leaving a literature-comparison risk.
