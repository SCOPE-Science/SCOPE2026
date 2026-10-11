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

The analytic argument checks the first-return radius at each half-turn by explicit sine/cosine solutions; its period in original physical time is \(\pi\). The arcsine law is verified analytically by the change of variable \(r=\sin^2(\pi u)\). Fourier orthogonality gives every indexed correlation, not just the tested cases. A direct integration over the no-reset phase region yields the Cartesian correction term. These steps are self-contained and do not depend on numerical convergence.

The included standard-library program `checks/verify.py` tests explicit physical half-flights, finite trigonometric orthogonality instances, probability moment values, and selected physical-time correlations against direct deterministic quadrature. Invoke `python3 checks/verify.py`. A successful run prints `CHECK_OK`. This finite check is not an exhaustive or infinite proof and is not an independent audit. The published source's full return map, rather than any numeric log, supplies the literature starting point.

No assertion of uniqueness among invariant measures or mixing of the hybrid flow is made beyond the displayed stationary measure and the proved non-mixing consequence.
