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

A nonsingular affine map preserves the four independent uniform side parameters, containment, and normalized area. On the square the four omitted corner triangles have disjoint interiors. Conditioning on one intercept gives the stated corner integral and summing the two active corners in the wedge gives the frozen depth formula, with continuous zero depth on the boundary. Both wedge derivatives are positive where needed to reach the unique maximum at the center. There the logarithms expand to give a uniform quadratic deficit with coefficient 4 in both affine coordinates; localization and disk comparison give the upper coefficient π/4. On y≥η>0 the inverse low-depth width is uniformly ε/log(1/ε). For y≤√ε the inequality D≥2x bounds the area by O(ε^1.5), and for √ε≤y≤η the further log(y/x) term bounds the scaled width by 2. Eight wedges therefore give the lower coefficient 4. This proves the two limits for the pointwise depth at an independent area-uniform point, not for the area of the random hull. The frozen checker.py and VERIFICATION.md were inspected, not executed; reported Monte Carlo and numerical integration are supplementary only.

## originality

PASS

Best-of-knowledge pass for the four-side depth-level result, with the exact depth field providing its derivation. The closest same-date triangular profile contains the identical elementary corner calculation, which receives no originality credit. Applying it around the square is direct; the claim of interest is the resulting full four-side field with its two sharp area-of-level-set laws. No inspected source gives or implies those endpoint evaluations in this model.

## value

PASS

For a natural sampling model these quantify where almost no realizations and where nearly all realizations cover an independent location. The exact constants and distinct boundary and center rates are not supplied by the expected hull area or an area density. The lower limit in particular must control the corners, where naive uniform edge inversion fails.

The dated certificate retains the supplied scientific assessment, sources and limitations.
