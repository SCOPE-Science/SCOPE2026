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

I checked the profile table in all dimensions by translating the first vertex to the empty set. For the second vertex D of size 2t, put x=|Z intersect D| and y=|Z minus D|; the distances are x+y and 2t-x+y, with x+y even. Testing distance 2 at both ends, or distance 2 at just one end with Z distinct from both, gives the claimed 11 and 10/01 support. For 00 the two distances must both be at least 4. Their sum 2t+2y makes this impossible in the exceptional cases (t,d)=(1,4),(2,5),(3,6) and in their smaller dimensions. Witnesses at and above the asserted thresholds are obtained by choosing (x,y)=(1,3),(2,2),(3,1),(4,0), respectively for t=1,2,3 and t>=4. Equal pairs are handled separately. From d=7 the four ordered-pair types are equal, adjacent, distance 4, and distance >=6. Transitivity lets Duplicator match the first vertex, the common inventory matches the second, and the pair profile matches all equality and adjacency bits of the third. The six threshold sentences distinguish the initial classes. In the last separator the two third-vertex subformulas are parallel under a common pair of quantifiers, so depth is three. Orders are 2^(d-1); the minimum 64 for the last class is within this family only.

## originality

PASS

The audited contribution is the exact ordinary rank-three partition of halved cubes and sharp first dimension 7, not the halved cube itself, its intersection data, the EF method, or the number 64 in isolation. The closest indexed comparisons concern different adjacency or a different quantifier rank. The primary papers examined do not establish the logical classification.

## value

PASS

This gives the complete rank-three equivalence relation of a standard family, not just a finite pair check. The support rather than number of common extension vertices is the relevant logical invariant. The dimension-six antipodal exception shows why merely finding distant nonadjacent pairs or importing stabilization from ordinary cubes gives the wrong sharp cutoff. The result supplies the smallest family-relative test suite for all rank-three sentences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
