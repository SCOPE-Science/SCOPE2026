---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

With b⁰=Au, the first measurement pivot β=(bε)p and the first solution pivot u_g are both nonzero. The normalized right basis column is u/u_g. The measurement vector remaining after subtracting its component at p is ε(e_p b⁰−b⁰_p e)/(βu_g); it vanishes at p but is nonzero as a vector because b⁰ and bε are not collinear. Thus the algorithm reaches the ridge solve, with h₁=b⁰_p/u_g and h₂=O(ε). Solving this scalar ridge problem gives coefficient β b⁰_p/[(b⁰_p)²+u_g²(h₂²+μ²)] on u. For small ε, p is in the maximizer set for |b⁰_p|, and every g has |u_g|=||u||∞, giving the claimed limit also at ties. The isometry and norm inequalities bound q; a flat input mapped to a coordinate vector and a coordinate input mapped to a flat vector realize the opposite endpoints. The maximum over orientations is therefore the larger of the two endpoint deviations from 1/2. For z=μ² it is uniquely minimized by balancing the strictly opposing endpoint deviations, i.e. (z/n)(mz)=1; substitution and μ=1/q give the stated minimax value and calibration identity.

## originality

PASS

The prior work supplies Hybrid LSLU and its coordinate-space penalty, and already gives basis-conditioned residual bounds. The distinct result is an exact all-orientation solution filter in the isometric first-stage limit, sharp attainability in both dimensions, and the resulting minimax obstruction against the classical ridge solution. The identity μ=1/q is a corollary, not a separate novelty claim.

## value

PASS

This quantifies a coordinate-dependent regularization effect that survives condition number one. The sharp dimension endpoints and the nonvanishing optimal worst-case discrepancy specifically tell a reader when simply retuning a single orientation-independent scalar cannot reproduce the classical ridge solution. The separate calibrated μ clarifies that the obstruction is to universal scalar choice, not to all parameter selection.

The dated certificate retains the supplied scientific assessment, sources and limitations.
