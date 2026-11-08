---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Reconstructed the four-state stationary forced-reversal Markov generator: rate lambda changes velocity sign and redraws positive magnitude uniformly from {c,cq}; finite-state Feynman–Kac eigenvalue s(k) near zero has simple real analytic even branch. Expansion of the exact rational spectral equation yields K2/t=c²(3q²-2q+3)/(4lambda) and K4/t=3c⁴(3q⁴+28q³-78q²+28q+3)/(16lambda³), with derivative-bounded O(1). I independently expanded the determinant of the 4x4 tilted generator and verified coefficient identities. P(q)/q²=3(q+1/q)²+28(q+1/q)-84 gives exactly one sign crossing at q≈1.847356; H'(q) factor gives one maximum at (7+2sqrt10)/3 and H=7/3. At the zero critical P, conclusion only leading coefficient vanishes and kurtosis O(t^-2); not strict sign at q_c.

## originality

PASS

Best-of-knowledge qualified PASS for sharp forced-sign redraw fourth-cumulant threshold/maximizer. Classical Goldstein–Kac q=1 is prior; Stadje/Zacks 2004 considers random velocities and is the main plausible overlap, but its accessible abstract identifies distribution and first two moments, not this fourth cumulant or forced alternating redraw model. Full technical Stadje/Zacks unavailable (authorized retrieval vpn_disconnected). Sim et al 2015 have trajectory-level random speed law, not iid post-reversal redraw; De Bruyne et al focus first-passage.

## value

PASS

An exact model-sensitive change of kurtosis sign in a persistent transport process with a unique optimal two-speed contrast quantitatively distinguishes Gaussian convergence corrections and is a natural full-parameter classification, not a numerical artifact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
