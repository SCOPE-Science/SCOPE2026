---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Automorphisms of K_m square K_n are independent row/column permutations, augmented by global swap iff m=n; this includes K_2 square K_2. Unique landmarks pointwise fix their occupied rows and columns. For m!=n, marked-neighbor common counts n-2 vs m-2 distinguish which coordinate matches a landmark in round two. For square nonattacking F, first-round adjacency labels unordered coordinate-category pairs and swap realizes exactly their orbits. For square attacking F, two marked squares determine a first-round-definable shared row; intersecting it with each off-row marked neighborhood yields first-round singleton crosspoints, which let round two distinguish columns and then rows. Thus the class counts AB or binomial(A+1,2) and sizes follow. Explicit nonsquare single-marker and square 4x4 three-marker configurations establish 2-round sharpness. An independent direct orbit/refinement implementation tested 891 finite marked patterns, including the sharp 4x4 example.

## originality

PASS

Tinhofer result for Johnson graphs J(n,2)=L(K_n) is not a theorem for rook graphs L(K_{m,n}); even a general Tinhofer statement would imply eventual orbits but not the sharp uniform two-round class census. Counting-logic foundational references distinguish graph identification from within-graph orbit refinement. No matching arbitrary-landmark rook depth theorem was found by actual named and semantic search.

## value

PASS

An exact all-marking orbit recovery theorem for a natural highly symmetric graph product supplies a sharp constant-time refinement complexity and complete stabilizer class profiles with an exceptional square nonattacking symmetry regime. Unlike a simple one-marker observation it treats all subsets and all sizes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
