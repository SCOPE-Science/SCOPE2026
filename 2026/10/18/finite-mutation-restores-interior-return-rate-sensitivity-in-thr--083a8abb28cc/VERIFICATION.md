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

From the same directory, execute `python verify.py` (standard-library-only Python 3). It checks the one-step hypergeometric payoff expressions, differentiates exact stationary birth-death balance products with rational arithmetic, and compares the result to both the stationary drift identity and the proposed universal closed form for 140 distinct three-person cases; 32 additional two-person comparisons confirm independence from the interior return. It verifies the exact two-sign counterexample, the mutation boundary, and two optional floating-point equilibrium estimates at selection strength 0.01.

The exact chain and drift tests are independent **finite** checks over enumerated parameter combinations, while the accompanying analytic proof establishes the result for every integer population size and all admissible positive mutation probabilities and return triples. No finite test proves the all-parameter statement. The current report uses a self-review; no independent scientific audit or publication-priority certification has occurred. The theorem concerns first-order behavior near zero selection only.
