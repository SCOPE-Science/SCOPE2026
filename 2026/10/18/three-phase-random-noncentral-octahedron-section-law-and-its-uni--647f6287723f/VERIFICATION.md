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

The analytic proof reduces the vertex count to \(M(5-M)\) crossed octahedral edges and derives the threshold overlap probabilities by differentiation under the integral sign using the uniform conditional circle law. The explicit antiderivative \(J'(t)=\arcsin(t/\sqrt{1-t^2})\), the exact support thresholds and strict derivative sign changes give the full theorem and its unique optimizer.

The included `checker.py` runs under Python 3 standard library only (`python checker.py`). It constructs the twelve edges directly, rather than computing the predicted polygons from the proposed overlap formula, and compares 250,000 independently seeded random normal vectors at each of eight offsets. On the delivered artifact the largest empirical-versus-closed-form discrepancy was below 0.0012, and normalization, optimizer location and exact-expression numerical identities passed. Stochastic agreement is not an exhaustive or infinite proof; all generality derives from the explicit analytic derivation.

No independent audit or third-party validation is claimed.
