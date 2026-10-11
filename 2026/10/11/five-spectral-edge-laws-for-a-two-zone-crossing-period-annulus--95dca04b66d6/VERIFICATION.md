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

For any fixed \(a,D,\kappa>0\) and \(\tau\in\mathbb R\), the derivation can be checked by substituting the stated fundamental solutions into \(u''-\tau u'+Du=0\) and checking \(u(0)=0,u'(0)=1\). The quadrature \(W=\int u\), first-return identity \(v=r u-aW\), and right-zone time-reversal scaling constitute a complete analytic reconstruction. The logarithmic concavity proof is independent of numerical tests. Domain restrictions and the five asymptotic limits are stated explicitly in the theorem.

The included standard-library script `verify.py` tests the closed-form integral against independent Simpson quadrature, numerically verifies the right-zone reflection and left-flight endpoint conditions for representative focus, defective-node and distinct-node cases, and checks the characteristic asymptotic ratios. Run `python3 verify.py` from this directory; success is indicated by `CHECK_OK`.

These are finite diagnostics. They do **not** prove a global inequality by sampling, prove originality, or constitute independent audit or external certification. Full original derivations and the identity for every parameter are in RESULT.md.
