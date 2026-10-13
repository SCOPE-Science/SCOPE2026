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

# Reproduction and limitations

The standalone `verify.py` file needs Python 3 and no third-party modules. Execute `python3 verify.py` from the same directory. It prints one `VERIFY_OK` line or stops at a failed assertion.

The checker directly constructs the word using the bit length and separately evaluates the four-state automaton at inputs \(0\) through \(65535\). For factor lengths \(1\) through \(48\), it enumerates all factors within the first \(8192\) letters, evaluates their Parikh vectors, and checks: the three full two-letter Parikh boundaries of cardinality \(3n\); the upper bound \(P(n)\leq5n+2\); all sums \(0,\ldots,2n\) under the weights \(0,1,2\); and the collision-bound inequality for every ordered triple of integer weights in \(\{-3,-2,\ldots,3\}^3\). For positive tested collision counts it also verifies the explicit two Parikh vectors with equal weight.

**What is proved, not merely tested:** the unbounded consecutive power-of-two runs realize the three complete boundary edges for every length; a gcd parameterization yields distinct collisions for every injective integer valuation; a four-state automaton evaluates all inputs by their binary length; direct finite starting-position counting bounds all factors. The infinite theorem depends on these arguments. The checker does not explore all lengths or all valuations and supplies no independent audit.
