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

Independently reconstruct the overlaps from the coordinate-pair presentation of all 27 lines. A point on a line with a zero coordinate has exactly two zero coordinates, in one pair. There are six choices of zero pair and three nonzero ratios, giving 18 points on three lines each. At an all-nonzero point, a matching between coordinates determines at most one line, and determines a line exactly when its two pairs have opposite cubes. For odd characteristic, two qualifying matchings force two cubes equal to the first cube and two to its negative, and no third matching qualifies. Normalizing x0=1 gives 3·3³=81 such double points. In characteristic two two qualifying matchings instead force all cubes equal, giving 3³=27 further triple points and no double points. Thus in the split cases the union counts are 27q−90 and 27q−63. In the nonsplit cases a rational point on a nonfixed line is also on its conjugate. With two nontrivial roots the lines are skew; with one nontrivial root the intersection has the corresponding zero pair and belongs to the fixed line for that matching. The three fixed lines form a triangle in odd characteristic and concur in characteristic two, giving 3q and 3q+1. Subtracting from q²+7q+1 and q²+q+1 in the respective split and nonsplit cases gives the stated four counts. The roots in the admissible prime powers are precisely 2,4,7,13,16. Over extensions of a nonsplit base the coefficient of q^n is −11−9(−1)^n and the constant is 46+45(−1)^n or 32+32(−1)^n; on a split base the coefficients are −20 and 91 or 64. Applying the logarithmic series gives exactly the four rational zeta functions.

## originality

PASS

Credit the complete, characteristic-sensitive arithmetic of the geometric line complement, in particular the nonsplit descent that determines its odd-extension counts. The classical geometry, the full-surface count, the split Eckardt-count formula, and the formal passage from counts to zeta are not original. Do not award independent priority for the split point-free cases or for the characteristic-two exceptional fields. Related later catalogue records do cover the arithmetic explicitly; the inspected earlier material does not establish an equivalent all-fields result.

## value

PASS

The line complement is a natural open cubic surface. Knowing exactly when it contains a rational point distinguishes fields where every point is supported on the line arrangement, and the nonsplit counts control arithmetic over odd extension degrees that cannot be read from the split census. The zeta expressions package the count, not a separate source of value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
