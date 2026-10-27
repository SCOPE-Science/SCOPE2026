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

# Verification

The standalone `check.py` uses standard-library exact rational arithmetic and checks the trace, second elementary singular-value invariant, vanishing determinant, the order-independent sweep characteristic-polynomial coefficients, and the monotone ordering of six sweeps on independently constructed nonsingular rational unit-row triples. It also exercises a rationally parametrized full-rank family approaching the sharp \(\sqrt2\) penalty. To reproduce: `python3 check.py`.

The universal real-parameter claim is proved analytically by the projector trace calculation, exterior-power identity, feasible Gram determinant, strict monotonicity of the larger singular-value root, and the explicit limiting family. Finite rational checks are corroboration, not an infinite certificate. No floating-point or long-horizon performance claims are made.
