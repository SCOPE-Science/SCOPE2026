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

# Verification notes

The proof derives the infinite-series normal-angle curvature radius from the exact Minkowski decomposition. Its critical ingredients are the geometric summability of ellipse perimeters, the local estimate at vertical normals with \(N=\lfloor\log_{a/b}(1/|t|)\rfloor\), and the identity \(d\kappa/ds=-\rho'/\rho^3\). These exact steps, including both endpoint cases, establish infinite-parameter statements; numerical experiments do not substitute for them.

A self-contained file `verify.py` checks selected ellipse support-function finite differences, representative radius values, and perimeter majorants. Run with `python3 verify.py`. Results recorded: all assertions passed for the representative pairs \( (a,b)=(0.8,0.4),(0.8,0.6),(0.8,0.68),(0.8,0.75)\). Neither these pairs nor finite ellipse truncations establish universality or originality.

The source material inspected includes the 2023 original full HTML, the 2022 thesis diagonal-example and curvature sections, the 2023 persistence theorem's text, and the 2021 full finite-Minkowski paper. External scholarly priority remains subject to independent confirmation. No independent mathematical audit was performed.
