---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

A fixed representative is exactly a point of (I-R)^(-1)Z^2 in the half-open square. For u=cot(theta/2)>0 the integer labels obey 0<=a<3 and -1<b<2, with a=0 forcing the origin. Of (1,0),(1,1),(2,0),(2,1), (2,0) lands on the excluded right edge, and the others pass the half-open inequalities exactly at u<2,1,1/2 respectively (none at equality). Coordinate exchange conjugates the opposite rotation; the half-turn has exactly the four half-lattice representatives. At an interior fixed point the rotation followed by its integer correction rotates the entire boundary-distance open disk onto itself, and this radius is maximal among centered disks contained in Q. The displayed coordinate distances give the radii. Disjointness also follows directly: a shared point of two such disks would have the same unique floor correction for two distinct centers, impossible since I-R is injective. The area sum and normalized area invariance follow; each new radius vanishes linearly at its own threshold, with nonzero slope because |du/dtheta|=(1+u^2)/2.

## originality

PASS

The supported distinct contribution is the exhaustive strict three-transition census and the resulting sharp disjoint fixed-center disk-area law. Blank already gives the first existence threshold/construction and the invariant-neighborhood mechanism. A prior limiting quarter-turn disk also matches one specialization. Neither supplies the other two branches or the exhaustive fixed-center census, and the adjacent indexed area laws are for different maps/periods.

## value

PASS

For a standard square piecewise isometry, the full angular classification determines precisely when new fixed centers and explicit invariant absolutely continuous probabilities appear. The disjoint sharp radii give a directly usable area lower bound for invariant regions, with a quantitative onset at each birth rather than just a point-existence result. This is not a claim about all periodic islands or globally invariant Lebesgue area.

The dated certificate retains the supplied scientific assessment, sources and limitations.
