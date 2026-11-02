---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For regular n>=5 polygon circumradius R and edge unit tangents t_j, perpendicular projection onto edge j lies in the segment precisely when |y·t_j|<=s=R sin(pi/n). Strict satisfaction yields a normal from each of n edges and each of n vertices; no face can give >1 normal by base point, so maximal generic count 2n. The closed simultaneous strip intersection S_n is contained in P_n because its circumradius is R sin x/cos(x/2) (odd) or R tan x (even), each <= R cos x for stipulated ranges. Directions mod sign yield regular 2n-gon (odd) or n-gon (even), with inradius s. Computing area (perimeter*inradius/2) yields 2 tan x tan(x/2) or tan² x, with Taylor coefficients 5/12 and 2/3 at x^4. Independently reconstructed clipping intersections and area ratios for 12 orders 5..30. Chamber boundaries measure zero and are not claimed to have exactly 2n distinct normals.

## originality

PASS

Best-of-knowledge comparison of the mathematically precise additional claim, not of a matching title, with the inspected primary papers and published research. The result is an elementary but motivated geometric derivation from known active-region technology. It is not a formal substitution in existing average-normal formula, because mean and maximal-chamber area do not determine each other.

## value

PASS

Measures the size of the natural region attaining the sharp face-based count 2n, complementing the established average number of normals. The exact polygonal geometry and odd/even fourth-order asymptotic split are invariant data not determined by face count alone; though elementary after projection-strip reduction, this is a motivated whole-family geometric classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
