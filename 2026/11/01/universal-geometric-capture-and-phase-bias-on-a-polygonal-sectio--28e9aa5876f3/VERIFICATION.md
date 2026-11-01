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

# Reproduction and precise scope

Run `python3 check_exact.py` using Python 3.8+ and its standard library. The observed successful output was:

`EXACT_POLYGONAL_PHASE_LAW_OK: 3636 rational branch tests, 36 parameter pairs, 14 distribution levels`

The executable constructs the original planar map with rational absolute values, iterates it three times, checks the finite graph parametrization and the saturated slope-four conjugacy at each critical branch boundary and at interior rational samples, and checks the two period-three phase points and finite-step probability identities. It uses 36 exact rational pairs with \(a>0\) and \(b>2a\), including ratios very near the boundary.

The **infinite-parameter and all-time proof** is the sign-branch calculation (4)–(5) plus measure pushforward equations (6)–(7) in RESULT.md. The exact total-variation formula follows because arclength on a segment is nonatomic and the limiting phase law is atomic. The finite checker cannot establish any universal or literature-priority claim on its own.

The initial measure is normalized arclength on the two canonical bounded edges, not area on the plane. The time variable \(m\) counts three-step returns. The unique indefinitely uncaptured point is a repelling fixed point of the three-step return, which has zero initial probability. No independent mathematical audit has been performed.
