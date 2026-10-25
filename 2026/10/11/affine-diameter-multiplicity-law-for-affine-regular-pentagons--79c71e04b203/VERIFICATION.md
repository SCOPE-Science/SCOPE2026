---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

For a nondegenerate affine image of a regular pentagon, every generic diameter is a unique edge-to-opposite-vertex chord, so the multiplicity equals the sum of five triangle-family indicators outside a finite union of exceptional chords. The 5 internal pentagram diagonals are each shared by two swept triangle boundaries, making generic multiplicity odd; the maximum is five and a boundary-near cell has multiplicity one. Independently split the entire explicit affine-model polygon by all five diagonal lines, generating exactly eleven positive-area open cells: five count-one, five count-three, one count-five. Exact Q(sqrt(5)) polygon clipping gives total area 5/2, each triangle sqrt(5)/2, central fivefold cell area (35-15 sqrt(5))/4 and hence probabilities 5-2 sqrt(5), (7 sqrt(5)-15)/2, (7-3 sqrt(5))/2. Direct exact moment recomputation gives E=sqrt(5), Var=20-8 sqrt(5). All fivefold-cell vertices and 11 cell measures are recovered independently of the package verify.py. Finite exceptional diagonals have Lebesgue measure zero; this exact planar arrangement exhaustion verifies the claimed a.e. distribution, not claims about boundary multiplicity or arbitrary pentagons.

## originality

PASS

The original complete three-level probability law and pentagram-region measure are not implied by the inspected earlier parity and first-moment theorems. Critically, Martini–Soltan (2003) already proves almost-everywhere odd affine-diameter multiplicity for ALL convex polytopes; parity by itself is not a new contribution. Bárány–Hug–Schneider (2014/2016) already proves the edge/opposite-vertex triangle sweep mechanism and mean. The surviving claim requires computing which polygonal overlap cell has multiplicity five and its exact area; this supplies the missing parameter in the three-level distribution. Search and relevant full-text inspection found no independent earlier table/theorem giving that distribution. The same-result Resultary hit is a mirror of the assessed research record, not an independent earlier source. Publisher-access limitations and possible unindexed classical pentagram exercises remain residual risks.

## value

PASS

The average number of affine diameters is a recognized invariant, and the natural affine-regular pentagon is a canonical convex polygon beyond the triangle where its generic pointwise multiplicity is nonconstant. An exact classwise area distribution has intrinsic geometric meaning: it completely answers the generic random-point count for this object, identifies the full fivefold central cell, and yields a second moment and variance not determined by existing mean and oddness results. The finding is a motivated finite classification, not an arbitrary slice or a mere rephrasing of the known parity theorem. It gives no all-polygon generalization and does not determine exceptional-point counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
