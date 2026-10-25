---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

Vertex-by-vertex affine determinant reduces unrestricted tetrahedra to four listed polytope vertices. A 2+2 split has sixfold determinant h|det_2(b-a,d-c)|, maximized by vertices of regular difference bodies P_n-P_n: regular n-gon of longest-chord length L_n when n even, regular 2n-gon when n odd. Relative longest-chord angles range over theta+eta_n Z, giving exact cosine-distance envelope. A 3+1 split is at most (3sqrt3/2)hR² in sixfold volume; even n>=4 lower bound 4R²cos(pi/n) exceeds it; odd n>=3 lower bound 4R² cos^3(pi/2n) meets it only n=3 at farthest twists. Independently enumerated every tetrahedron for n=3..13 and five different twists, 55 configurations, all matched formula and n>=4 layer split. Finite enumerations corroborate but infinite n proof uses the difference-body inequalities.

## originality

PASS

Prior prism geometry provides vertical structural conditions but not the angle-dependent exact two-chord determinant envelope for two independently rotated regular bases; earlier single-polygon difference-body/rectangle results do not imply the combined rotated-body optimization. No matching stronger theorem found in source/Resultary queries, subject to normal historical-priority risk.

## value

PASS

The arbitrary-n and continuous-twist sharp classification answers a natural volumetric extremal problem for prismatoids. The odd/even longest-chord dichotomy, 3+1 exclusion and twist reversal are structural information applicable beyond a single arbitrary computed solid; it supplies an exact invariant future geometric optimization can use.

The dated certificate retains the supplied scientific assessment, sources and limitations.
