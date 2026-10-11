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
The derivation uses affine invariance of planar convex-hull vertex count, a projective transformation of the apex, planar Cauchy density, and elementary integrals. The final optimizer is characterized as the unique positive root of a strictly decreasing scalar equation, with derivative sign shown explicitly in the mathematical document. The fixed-area derivative is positive on the complete positive parameter domain, and the thin-base limit follows by asymptotic substitution into the exact root equation. Run the bundled `verify.py` using Python 3 without third-party dependencies. It independently projects the five original 3D vertices along pseudorandom sphere normals and counts the vertices of the projected convex hull; evaluates the closed formula; isolates maximizing heights and tests strict neighboring loss; checks a numerical derivative against the closed derivative; and checks the asymptotic coefficient. These are finite diagnostics, not exhaustive computational verification. Source originality and general analytic proof are not certified by finite tests. Independent audit: not performed.
