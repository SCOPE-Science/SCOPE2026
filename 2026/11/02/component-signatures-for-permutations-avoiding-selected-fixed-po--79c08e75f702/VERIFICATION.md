---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For each forbidden value j, an adjacent exchange cannot change whether j is left or right of prohibited position j without temporarily placing j at position j. Endpoints have forced side. Given any choices for internal forbidden labels, the sorted blocks L increasing, unrestricted U increasing and R increasing form a feasible representative because j in L occupies <=j-1 and j in R occupies >=j+1. Sorting a feasible word by target block order swaps only adjacent inversions: L entries move left, R entries move right, U is unrestricted; within L and R the inequality from feasibility ensures exchanges remain legal. At most binom(n,2) such swaps to canonical representative; component diameter <=n(n-1). Independently generated every F subset and feasible permutation for n=2..7, 252 masks and 421830 feasible graph vertices, confirming exact 2^|F internal| component count.

## originality

PASS

Adjacent transposition Gray codes in derangement literature usually allow different exchanges (unrestricted transpositions or 3-cycles); Clark’s graph derangements concern a different graph-mapping property. None of their inspected statements gives the precise induced permutahedron component classification for arbitrary forbidden-position subsets F.

## value

PASS

An all-parameter exact connected-component invariant and constructive bounded-length paths solve a natural constrained-adjacent-swap reconfiguration problem and sharply distinguish adjacent swaps from broader permutation generation; not a finite or cosmetic special case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
