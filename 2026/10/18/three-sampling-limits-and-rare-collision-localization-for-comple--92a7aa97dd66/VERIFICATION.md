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

# Reproducible mathematical checks

Run `python check_angles.py` using Python 3 with the standard library only. The script independently enumerates every strict coordinate ranking and every canonical Minkowski-sum supporting vertex of the graph associahedra for eight graph sizes: \((1,1),(1,2),(1,3),(2,2),(2,3),(2,4),(3,3),(3,4)\). It identifies the recursive elimination-tree keys and tests the exact equality of the two equivalence relations, checks the full vertex-count spectrum and each factorial permutation fiber, and calculates collision probabilities as exact rational numbers. The eight enumerations passed, with successful terminal marker `ALL EXACT CHECKS PASSED`.

The script also evaluates four finite scaled collision sums at balanced orders \(m=5,10,20,50\). Those are numerical consistency observations, not exhaustive proofs of any infinite statement. The arbitrary-order formulas follow by counting all labeled brooms. The limits use fixed-index factorial estimates, a summable \(1/r!\) majorant for uniform vertices, and the ratio/tail argument for the collision-conditioned deficit. These analytical steps, rather than finite experiments, establish the asymptotic results.

Mathematical limitations: the laws concern isotropic Gaussian exposed vertices of the specified nested-fan realization; no arbitrary-direction or nonbalanced-scaling limit is asserted. Independent mathematical validation has not been performed.
