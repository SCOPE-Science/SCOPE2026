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

The three specified finite cycle types and the full cycle at infinity exhaust the ramification sum 2n−2 for n=d+4. Centering the degree-d critical point and subtracting its value gives the asserted sparse support. Vladimirov's Propositions 4.1 and 4.6 give the exact braid-class count and the normalized even C₁ characterization. For the first representative, the product with rightmost factor applied first is the full cycle in order n,d+3,d+2,d+1,d,1,…,d−1. Products of two c-conjugates of b give all pivot three-cycles on T, generating A_T. Products of A_T-conjugates of a give the pivot three-cycles attaching d+3, and conjugation by b and then a gives overlapping alternating subgroups attaching d+1 and d+2. Alternating groups supported on sets overlapping in at least three letters generate the alternating group on the union (use three-cycles based at a common pivot and conjugation within either set). Thus parity gives A_n for odd d and S_n for this even class, including d=3 and d=4. For even d=2k the signed-pair triple has an m-cycle on blocks in its product and odd total flip, hence a 2m-cycle: it satisfies the genus-zero polynomial passport. The k conjugates of the unsigned swap between B_{k−1} and B_k avoid the sign wrap and, with the remaining swap, generate unsigned S_m. Comparing the signed k-cycle to its unsigned version supplies a single flip; conjugation adds all independent flips. This gives equality with the full wreath product, not only containment. The imprimitive group cannot be in the S_n braid class, so C₁ is the remaining class. Hurwitz moves preserve the generated group and the affine normalizations do not change the cover group.

## originality

PASS

The prior passport classification provides the class count, a branch-cycle representative, and the even quadratic-composition identification. The supported contribution is the evaluation of the generated permutation groups in those classes, especially the distinction between containment in a signed wreath product and generation of its full base and top groups. The inspected broader composition results do not establish this equality or the trichotomy for this passport.

## value

PASS

The topological class count naturally raises the group question: the same even passport can produce a full symmetric group or an imprimitive group. Establishing the full signed group, rather than a block system or a loose kernel bound, and completing the natural-action classification in both parities supplies information not given by the class count or by generic sparse-system monodromy. It is an exact classification on a nontrivial infinite passport family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
