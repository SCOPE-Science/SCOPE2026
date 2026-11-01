---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Reconstructed the exact final claim over F7. The cubic F=X^3+XYZ+Y^3+YZ^2-Z^3 has no geometric singularities: on X=0, the common partial vanishing forces YZ=0 and F excludes projective zeros; on X=1, F_X=0 forces yz=4 and y≠0, z=4/y, and the remaining derivative equations reduce to 3y^4+4y+2=0 and y^3+y^2+1=0. Their gcd in F7[y] is the unit ideal, independently checked by modular Euclidean division (the source also supplies a Bézout identity). Euler's identity 3F=∑X_i F_i justifies this Jacobian approach. Independently enumerated all 57 rational projective points and found exactly 12 smooth cubic points and 12 different gradient tangents; full incidence histogram is {1:36,2:9,3:9,5:3}. The three fivefold centers are noncollinear (determinant 3 in F7); every point is covered. For sharpness, an entirely independent exact census of ALL (7^6-1)/(7-1)=19,608 projective coefficient classes of degree-2 homogeneous forms computed smooth rational tangents by gradient, giving maximum union size 36, with count distribution 0:1254,15:1596,36:16758. Every degree-one curve has one tangent line covering only eight rational points; nonzero constants have no curve. This is genuinely exhaustive for degree <=2, not finite sampling of a larger parameter space. The analytic smoothness proof, not the 57-point calculation, handles the algebraic closure. No claim for other fields or uniqueness of the cubic.

## originality

PASS

Best-of-knowledge originality for the exact q=7 smooth cubic realization and sharp degree-3 minimum, NOT for the general notion of tangent-filling, dual blocking sets, or Blokhuis's 12-point bound. Full relevant mathematics of the 2023 original question and 2022 primal blocking-curve paper was inspected; no accessible prior theorem implies a degree-3 tangent-filling curve over F7. A 2022 projective-plane blocking-set census classifies the abstract dual configurations (and may contain the 12-point support) but its accessible abstract does not construct the exhibited cubic or derive tangent realizability. Full paper was inaccessible and remains a specific risk; an earlier unindexed q=7 example may exist.

## value

PASS

This determines the sharp minimum degree in the natural tangent-filling question posed by Asgarli and Ghioca at a prime q=7 outside their q>=11 construction, and exhibits a geometrically smooth genus-one cubic rather than a singular or artificial slice. Its exact 12-element rational Gauss-image realizes the classical sharp nontrivial blocking size 12 in PG(2,7) and has an explicit 57-point incidence profile; the geometric realization, not the already known blocking bound or arbitrary 12-point set, is the meaningful fact. The minimum holds without irreducibility, smoothness or reducedness assumptions for competitors. This sharp naturally motivated finite-field boundary and explicit witness is substantial beyond textbook deductions or a known-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
