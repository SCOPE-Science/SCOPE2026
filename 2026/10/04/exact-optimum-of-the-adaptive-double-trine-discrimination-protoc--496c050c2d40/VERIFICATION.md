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

The analytic proof was reconstructed from the source's displayed branch probabilities, normalized postmeasurement states, and binary Helstrom formula. The exact scalar error function was differentiated symbolically by hand-algebraic reduction, and the squared stationary equation factors into two linear terms. The endpoint root introduced by squaring fails the unsquared sign condition; the remaining root is the unique interior optimum.

`verify_double_trine_optimum.py` uses only the Python standard library. With 60-digit decimal arithmetic it reconstructs the posterior probabilities, overlap, \(Q\), \(S\), \(p_*\), \(E_*\), and the one-way gap. It also checks the derivative equation and performs a \(200001\)-point numerical grid stress test. The grid is supplementary and is not used to infer the infinite-domain optimum.

The direct archive-era source was inspected at the protocol and minimum-error pages. The exact constants are not asserted to be independently audited.
