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

Run `python3 verify.py` using Python 3 standard library. The checker executes Simpson quadrature of the midpoint/gap density against the exact two-node survival formula, fixed-seed Monte Carlo of the same two-node law, and basic Lagrange basis identities. The mathematical proof, not simulation, establishes the all-\(n\) moment threshold and exact endpoint divergence. No claim is made about uniform complexity, numerical conditioning of floating-point interpolation, or an independent audit.
