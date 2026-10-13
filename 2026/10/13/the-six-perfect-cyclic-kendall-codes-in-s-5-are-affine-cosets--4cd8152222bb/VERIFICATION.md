---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The finite domain is the symmetric group \(S_5\), represented by all \(120\) one-line permutations of \(0,1,2,3,4\). The verifier constructs each cyclic Kendall closed radius-one ball by applying the five swaps of cyclically adjacent positions. It checks that every ball has six distinct elements.

Perfect codes are enumerated as exact covers of the \(120\) vertices by these balls. The search is exhaustive: it selects an uncovered vertex, branches over every still-compatible ball containing it, and removes precisely the balls that intersect the chosen ball. The replay visits \(254\) search nodes and obtains exactly six exact covers, each with twenty centers. It then directly checks pairwise ball disjointness and full coverage for every returned code.

Separately, the verifier constructs all affine permutations \(x\mapsto ax+b\) of \(\mathbb Z/5\mathbb Z\), checks that the twenty maps form a subgroup under standard function composition, computes all six left cosets, and checks set equality between those cosets and the six exhaustive-search solutions. It also verifies that left multiplication is transitive on the six codes and that the affine code has stabilizer exactly the affine subgroup, of order \(20\).

Expected replay line:

`VERIFY_OK vertices=120 ball_size=6 exact_cover_nodes=254 perfect_codes=6 code_size=20 affine_cosets=6 left_orbit=1 stabilizer=20 census_sha256=89d75eb3fe7b76ae2723a55ba872eb3cdd98efb1ef1ac2ca6b363844ec16f7d8`

The computation establishes only the complete finite degree-five classification. It is not evidence for existence or uniqueness in larger symmetric groups.
