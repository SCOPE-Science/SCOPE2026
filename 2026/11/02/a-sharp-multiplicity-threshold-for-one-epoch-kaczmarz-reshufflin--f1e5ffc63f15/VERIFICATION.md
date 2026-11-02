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

# Verification record

Run `python3 verify.py` from this extracted package. No nonstandard Python dependencies are required. The checker uses `fractions.Fraction`, exhaustive word enumeration for manageable sizes, and an independent dynamic program for the number of projection-line switches.

The executed script completed with `PASS: 245 exact-rational assertions`. It compared exact projected iterates against transition-polynomial predictions for \(m=2,3,4,5,6\), verified the symbolic coefficients and switch-count moments over \(m=2,\ldots,14\), and confirmed the three-distinct-row positive risk gap as an exact fraction.

These computations are finite diagnostics. The arbitrary-size threshold uniqueness follows from the derivative and convexity argument; the superexponential threshold and the limiting risk ratio follow from the coefficient estimates and rare-event Poisson limit respectively. No external certification or independent scientific audit was conducted.
