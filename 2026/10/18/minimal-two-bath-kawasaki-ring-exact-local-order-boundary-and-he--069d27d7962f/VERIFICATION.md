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

# Verification of finite two-bath Kawasaki-ring identities

Reproduce with Python 3.10+ and SymPy 1.12+: `python check.py` in the same directory as this document. The checker has no external data input. It constructs the complete six-state generator from the four-spin energy and Metropolis exchange rule, verifies the proposed distribution against every original stationary master equation, and recomputes four local spin products and the hot-edge energy flux. It symbolically tests equilibrium, hot-bath derivative and entropy-optimization identities. It solves eighteen independent six-by-six exact rational stationary systems and checks associated Schnakenberg entropy-production rates, and enumerates the smaller cyclic sectors to confirm the claimed minimality. All these checks passed when executed on the packaged source.

The all-parameter inequalities and unique dissipation maximum follow from algebraic proofs in RESULT.md. The finite program is a check of identities and sample parameters, not an infinite-domain numerical proof. No thermodynamic-limit result, independent scientific audit, or externally certified calculation is asserted.
