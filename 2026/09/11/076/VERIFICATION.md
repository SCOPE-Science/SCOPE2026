---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

Choose the representative row of each of the two row cycles, and let p be its permutation of the ten symbols indexed by column group and residue c mod 5. Equivariance generates the other four rows in that cycle. In each representative column of residue zero the five contributed entries from this row cycle are obtained from its five inputs v at residues c by shifting the symbol phase by -c. Thus it is necessary and sufficient that the resulting symbol masks have five distinct entries each and that the two row cycles' masks are complementary in each of the two representative columns. I wrote and ran a separate enumeration: loop over the 10P5 ordered half-rows, reject a repeated shifted symbol, and histogram by original-symbol set s and shifted-symbol mask a; for the normalized first half also require p[0]=0. Multiply half-row counts for original sets s and its complement to build the row table for mask pairs (a,b). Multiply row counts against their complementary mask pairs to count the squares. This gives 29,420 normalized first-row-cycle states and completion histogram (45:1125, 55:2750, 65:7500, 70:7000, 75:6500, 90:4500, 225:45), yielding 2,082,000 normalized and 20,820,000 when both rows are unrestricted. Independently the symbol centralizer acts transitively, using within-cycle rotations and exchange of the two cycles, proving the factor of ten. The two committed census output lines are consistent with this fresh run; no historical PASS, orthogonal-mate obstruction, or triple result is used.

## originality

PASS

The best-supported distinct result is the exact multiplicity for the specified fixed action (and equivalently its normalized multiplicity). The known exact cycle profile catalogues establish occurrence, and prior general enumeration methods do not supply this coefficient. This is a bounded best-of-knowledge assessment, not a priority claim.

## value

PASS

The diagonal, fixed-point-free order-five action is a natural order-10 automorphism stratum recognized by the cycle-structure literature. An exact fixed-set size supplies the quantitative information absent from an existence classification and a useful independent benchmark for automorphism-stratified enumeration of order-10 designs. This is a full count of that motivated stratum, not a sample or arbitrary truncation; it neither needs nor claims a solution to the orthogonal-mate or triple question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
