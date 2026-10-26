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
The exact labelled histogram follows by choosing level sets and parent assignments. The conditional Poisson cascade is exact for every positive Boltzmann parameter. The proof of the quantitative bound invokes only the standard Poisson multiplicative Chernoff estimate and Stirling's local mass estimate, with all asymptotic parameters explicitly defined.

`checker.py` exhaustively enumerates every unary function on \([n]\), for \(1\le n\le6\), at maximum heights three and four. It independently computes each function's depth vector and compares its complete frequency histogram with the multinomial–parent formula. Expected terminal output: `ALL PASS; enumerated 100138 raw functions, 118 nonzero level-profile coefficients`. It uses Python 3 with standard-library imports only. These experiments do not prove any large-\(n\) assertion.

The conditional local-mass bound requires \(h\) fixed and \(\mu_{0,n}\) growing faster than any power of \(\log n\); both are explicitly proved. Independent audit remains unperformed.
