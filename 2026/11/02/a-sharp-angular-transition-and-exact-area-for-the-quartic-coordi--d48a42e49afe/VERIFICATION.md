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

The proof starts with the explicitly normalized quartic spatial pairing. It reduces the exchange operator to a one-parameter family of centered ellipses, optimizes the support function by differentiating a rational function, and independently proves that all vertical sections are filled intervals with a strictly concave upper boundary. Thus convexity is proved for the numerical range itself. The exact area follows by an indicated elementary substitution.

The supplementary `CHECK.py` runs 821 finite checks: numerical maximization in 421 directions, 398 boundary-to-ellipse substitutions, area quadrature, and inradius evaluation. Running it requires Python 3 with SciPy and the standard library. Command: `python CHECK.py`. Finite tests cannot prove global uniqueness, strict concavity, continuum support, or the integral identity; these are established analytically in RESULT.md.

No external independent audit or validation was performed. The principal scientific limitation is publication-priority uncertainty: the closest paper already supplies a general ellipse parametrization, although not the optimized numerical-range geometry asserted here.
