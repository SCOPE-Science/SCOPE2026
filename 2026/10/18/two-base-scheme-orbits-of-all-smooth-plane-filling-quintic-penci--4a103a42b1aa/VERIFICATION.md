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

The frozen result counts two-dimensional vector subspaces with exactly four rational members, each geometrically smooth. The fresh exact reproduction checks rank 13 of the planar evaluation map in degree five and rank 8 of A↦det(X,X^[3],AX), with scalar kernel. At a rational point p its differential is det(v,p,Ap), so a rational eigenline forces a singularity. The converse follows from Homma–Kim Theorem 3.2 and was separately checked by computing all three affine singularity ideals of representatives of the two no-rational-eigenline form orbits (432 and 144). The complete independent RREF sweep checks all 896260 two-spaces, accepts exactly 2016, and full enumeration of the projective group of order 5616 gives orbit sizes 1872 and 144 and stabilizers 3 and 39 for the displayed representatives. Rational base points are transverse: dependent differentials over F3 would give a singular rational member. Smooth independent degree-five curves have no common component, so Bézout leaves length 12 after those 13 points. Exact chart Gröbner checks give eliminants Z(Z−1)(Z+1) times the frozen irreducible P12 or P3^4, respectively. On that residual locus Z³−Z is a unit and the Gröbner relation is linear in the other coordinate, so the localized quotient is respectively F3[Z]/(P12) or F3[Z]/(P3^4). This certifies Frobenius support and scheme length, not just point counts in a sampled extension; the total Bézout length excludes extra support at infinity. The reduced case additionally has unit base-intersection Jacobian ideal on all three charts. Finally the differential from any system to a fixed rational point's two-dimensional cotangent space has nonzero kernel in vector dimension at least three, ruling out higher-dimensional rationally all-smooth systems.

## originality

PASS

Credit prior coverage of individual smooth plane-filling curves and, after translating and normalizing spread sets, the underlying two-orbit alternative. The supported distinct finding already stated in the frozen record is the geometric base-scheme classification: the two pencil orbits give precisely one reduced degree-12 point versus one degree-3 point with geometric local length four. The checked prior orbit classifications and individual-curve invariants give no such joint scheme statement or automatic determination of the residual Frobenius orbit and local algebra. The census alone and the cotangent obstruction are not the reason for passing.

## value

PASS

The natural family of maximally dimensional smooth pencils through the entire rational plane has identical rational base geometry and total intersection length, yet in its two orbits the residual scheme differs in both Frobenius support and geometric multiplicity. Determining that joint invariant exactly is useful independently of the older algebraic classification: it specifies the nonrational centers and their scheme thickness for the two types, data a computation of the spread sets or of individual-curve invariants does not by itself provide. This is not value assigned solely to recounting the conjugacy orbits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
