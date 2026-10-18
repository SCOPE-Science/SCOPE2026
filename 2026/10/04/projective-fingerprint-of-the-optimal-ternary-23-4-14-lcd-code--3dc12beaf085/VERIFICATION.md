---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Independently recomputed the given 4×23 ternary generator matrix rank four and Gram determinant 1, all 81 codewords and their exact Hamming weights 0:1,14:18,15:28,16:22,17:6,18:4,22:2. All 23 columns are distinct in PG(3,3); enumerated all 130 lines, obtaining intersection multiplicities 0:10,1:11,2:43,3:62,4:4, and all 40 projective hyperplanes (counts 1:1,5:2,6:3,7:11,8:14,9:9). Independently enumerated all four automorphisms of the colored 23-vertex incidence graph and confirmed each lifts to an invertible projective matrix: group has identity plus three involutions, hence Klein four. Finite exhaustive classifications are exactly finite claims, with no extrapolation.

## originality

PASS

An–Hong–Kim–Lim publish existence, a concrete generator and the optimal minimum distance, not its full weight enumerator, all-line incidence spectrum or exact PGL stabilizer. Earlier Li–Shi–Liu bounds precede that specific representative; related results for a different code C3,2 do not determine C3,1.

## value

PASS

The exactly specified new distance-optimal code is a natural inequivalence benchmark among many [23,4,14] representatives. Its entire projective line-incidence distribution and small symmetry group give information independent from the known minimum distance and can distinguish later constructions. This is not a random slice or mere known-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
