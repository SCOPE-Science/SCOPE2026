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

Execute `python3 verify_density.py` with Python 3.9 or later. The script uses only the standard library. Its integer certificate checks all \(5896800\) capped prime-exponent vectors, including \(2096262\) vectors whose first-ten-prime ratio is at least one and six equality vectors. It derives the exact \(\pi^{-2}\) coefficient of the cylinder lower bound, computes an upper bound for the reciprocal-prime-square tail by a verified sieve to \(100000\) and a convergent integer tail, and checks a rational conditional-Markov upper bound. It certifies the strict inequalities \(77/100<L\) and \(U<4/5\) without floating-point comparisons.

The infinite assertions rely on the separate proof: multiplicative prime-power identities, exact densities of finite valuation cylinders, the Euler product for squarefree tails, uniform convergence of the tail first moment, and Markov's inequality. Computation does not prove the existence or numerical value of the exact comparison density. No independent audit has been carried out.
