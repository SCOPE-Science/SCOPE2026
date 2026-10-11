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

The accompanying `verify.py` requires SymPy 1.14.0 (see `requirements.txt`). Executed with Python 3, it returned `CHECK_OK` after checking the exact exponential compactification, limiting equilibrium relation, four rectangle-face expressions, quadratic Lyapunov identity and the numerical coefficient identity \(27/h^3=12/d\). Direct symbolic residuals were zero.

The global statements are analytic: inward face margins, uniform exponential decay of the lower-order forcing, original-to-stretched-time integrability, and the Lyapunov comparison \(W'\le-\gamma W+\gamma^{-1}E^2\). These imply an infinite stretched-time trajectory but finite original lifespan, and scaled-profile convergence. Neither finite symbolic computation nor the reported illustrative numerical integration certifies the infinite-time dynamics on its own.

Exact applicability: real \(a,\varepsilon\); strictly positive \(b,c,d\); \(0<\eta<1/3\); sufficiently large \(|x_0|\) with the corresponding scaled positive or reflected negative initial-derivative rectangle. No claim is made about all initial data, \(d<0\), global attractiveness, or other chaotic attractors.
