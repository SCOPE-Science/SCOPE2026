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

The complete result is derived in `RESULT.md`, including the exact stationary distribution of the finite excursion-state chain, closed cylinder probabilities, the elementary Perron equation, and asymptotic coefficient. This is a mathematical proof, not an assertion inferred from finite samples.

Run `python verify.py` in the same directory. It uses only the Python standard library and returns:

`VERIFY_OK 434 rational word comparisons; reversal-constraint rank 23 ; 10 high-precision parameter identities`

The verifier builds a stationary hidden Markov model on states \((b,k,j)\), with state probability \(q_k/(2\mu)\), deterministic within-block transitions, and independent next blocks. For seven rational excursion-length laws it checks all \(434\) word-reversal comparisons at lengths one through five exactly. It also verifies the signed discrepancy and the eight-pair total-variation formula.

Independently, it constructs the rational stationarity and global-bit-flip constraints on all binary word coordinates, performs exact elimination, and verifies the entire reversal-difference table without relying on any stochastic model. The resulting length-five constraint rank is \(23\); the remaining reversal-difference space has rank one. Ten decimal high-precision parameter checks corroborate the algebraic root identity. These are genuinely executed checks of the included source code, not references to external logs.

Limitations: the finite checker alone cannot prove convergence for all integers or imply statistical independence; those claims, insofar as used, are established directly in the analytical argument. Independent scientific review has not been performed.
