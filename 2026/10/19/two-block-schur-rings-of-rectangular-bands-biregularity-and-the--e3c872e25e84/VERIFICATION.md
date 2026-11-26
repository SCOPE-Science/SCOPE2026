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

The coefficient of (i,j) in a product of block sums is r_X(i)c_Y(j). Summing each pair of closure tests over one color index shows the row and column degrees separately must be constant within each color, and that condition also suffices. A monochromatic row forces every row meeting its color to be monochromatic; the column argument is the same. Otherwise both degrees are interior and constant. Principal right and left ideals identify the rows and columns, and the relevant transitivity group is the stabilizer of the two colors in S_a x S_b, not the entire product group. In dimensions with a side at most three, every proper regular case is a singleton-neighborhood construction or its complement, with equal multiplicities forcing both flag transitivity statements. Up to transposition the only remaining rectangles below order 24 are 4x5 (no proper degree solution) and 4x4 (matching/complement, eight-cycle, or two four-cycles); in the eight-cycle case rotation and d -> 1-d on column-minus-row residues are transitive within each color. At 4x6 the column pairs form a cubic loopless multigraph on four vertices. Equal degrees force opposite-edge multiplicities to be equal; the three opposite-pair multiplicities sum to 3. Their possible unordered patterns are (3,0,0), (2,1,0), and (1,1,1). The middle pattern has two sizes of column-twin classes, so even its incidence flags cannot be transitive. The other two have both flag transitivity statements. Column labelings give 60, 1080, and 720 matrices, respectively; complementation is fixed-point-free, and the disjoint row and column cuts contribute 7 and 31. This gives 968 total, 428 automorphic and 540 non-automorphic. A separately implemented exact enumeration of all 46656 endpoint assignments also confirmed the census and orbit tests (/workspace/branches/e072f746-98ab-4ebd-9f64-d4da8eba14c6/census.py and census.json). The frozen checker was inspected, not executed. The threshold is for exactly two nonempty unordered blocks of labeled rectangular bands over Q, not arbitrary semigroups or arbitrary block counts.

## originality

PASS

The new content supported by the comparisons is the general two-block structural classification, sharp failure of automorphic realization at size 24, and complete labeled first-case census. The semigroup Schur-ring framework, the row/column product construction, and the two-row positive case are not credited as new.

## value

PASS

This identifies an exact boundary between algebraic closure and realization by automorphism orbits in a standard family. The graph description reduces arbitrary-size closure to a simple incidence test; the minimal witness and complete census show both when the gap starts and that it is not exceptional there. The census is motivated by this threshold rather than an arbitrary rectangle.

The dated certificate retains the supplied scientific assessment, sources and limitations.
