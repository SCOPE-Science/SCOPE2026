---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The bulk backward-generator equations for up/down/horizontal velocities were checked independently by exact rational substitution at 41 positions; entering at a wall in the inward state gives E[B]=2W/v and the stopped horizontal velocity-corrector martingale gives E[H²]=v²E[B]/lambda. For a random wall stay S, telegraph sign covariance exp(-beta|t-s|) integrates exactly to E[J²|S]=2 vbar²/beta [S-(1-e^{-beta S})/beta]. Independent, centered regenerating cycles of mean duration b+m and finite second time moment give D=(E H²+E J²)/(2(b+m)); this is the formula. Strict convexity of e^{-beta S}, Jensen, two-point increasingly variable laws and Laplace uniqueness establish the order, sharp bounds and identification. Independent algebra checks corroborated generator and Laplace identities. This depends on complete directional resetting, finite second moments and fixed positive beta; there is no extension to correlated wall histories or continuously oriented swimmers.

## originality

PASS

Pietrangeli et al. 2024 derive the exponential-release formula and explicitly identify non-Poisson wall escape as omitted. Datta–Beta–Großmann 2025 arXiv v3 contains general arbitrary-run/turn waiting-time Laplace-transform diffusion Eq.(28), but the turn state has zero propulsion and no reflecting slit/bulk-wall path geometry or persistent longitudinal sliding; its formula is not the current model specialization. General regenerative renewal methods and Laplace identifiability are classical, so novelty is limited to the exact coupled slit-wall model and its sharp convex-order/identifiability consequences, not the method itself.

## value

PASS

Wall residence variability at fixed mean is a concrete transport-control variable in confinement. Equal bulk occupation does not imply equal longitudinal diffusion, and the exact Laplace transform controls an experimentally relevant difference; sharp monotone distributional ordering and an inverse response curve are useful model-specific results. A non-Poisson extension was explicitly raised in the original model paper; the theorem answers it within clear idealized assumptions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
