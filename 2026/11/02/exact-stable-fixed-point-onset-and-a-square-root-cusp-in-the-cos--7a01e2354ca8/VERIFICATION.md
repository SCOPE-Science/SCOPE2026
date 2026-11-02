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

The mathematical proof in `RESULT.md` reduces the full fixed-point census to the strictly convex scalar equation and a unique double-root curve. Its strict derivative bounds establish stability without relying on the finite calculation. The curve derivatives and cusp follow from differentiation and Taylor expansion. The proof includes all assumptions and parameter boundaries.

The standalone `certify_bounds.py` uses exact rational arithmetic and the alternating Maclaurin series to certify all five strict derivative and value enclosures appearing in the proof; it passed. The standalone `verify.py` uses 60-digit mpmath arithmetic and passed 1316 assertions for five interior endpoint parameters, checking both sides of the threshold, both fixed point multipliers, right-branch repulsion, and square-root onset. Run with `python certify_bounds.py` (no external packages) and `python verify.py` (with the open-source mpmath package installed). No claim of interval-certified floating-point arithmetic is made. Finite tests are not an exhaustive numerical proof, and no independent audit has been performed.
