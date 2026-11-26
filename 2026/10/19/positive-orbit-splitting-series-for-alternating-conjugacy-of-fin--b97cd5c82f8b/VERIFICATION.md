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

The index-two subgroup test is exact for n>=2: an S_n orbit splits iff its stabilizer is entirely even. On a rooted tree or a disjoint union, odd internal automorphisms extend and a coherent swap of two isomorphic size-m pieces has sign (-1)^m. Such internal maps and swaps exhaust the relevant permutations. On a directed cycle only rotations are induced; the least-period rotation coherently cycles t copies of a block of weight w and has sign (-1)^{w(t-1)}. Internal maps are already even, so the choice of lift cannot change the sign. Burnside and period inversion give the two weighted necklace series; uniquely remove an even repeat of a primitive necklace of odd total weight, not a necklace of odd length. The remaining connected types assemble by the stated odd/even multiplicity product. The recursion for R is well-founded by degree; n=0,1 are correctly excluded from the index-two claim. An independent exact rational partition calculation returned split counts (1,4,9,20,45,111,276,666) and totals (4,11,28,67,175,454,1227,3281) for n=2..9. Its replay is to enumerate partitions, use the number of vertices fixed by the d-th power as the choice count on each domain d-cycle, and form both signed and unsigned Burnside sums. RESULT.md proof and VERIFICATION.md/verify_parity.py were inspected; no frozen code was executed. Finite counts corroborate but are not the all-degree proof.

## originality

PASS

Pass the nested parity-restricted classification and positive enumeration, not ordinary functional-digraph automorphism descriptions, unsigned counts, or the signed Burnside formula by itself. The strongest inspected prior results provide structural inputs rather than the parity restrictions and their positive enumeration.

## value

PASS

The natural index-two refinement of endofunction isomorphism has a usable local-to-global criterion and an exact positive algorithm in every degree. It identifies which structures split and where an odd automorphism can arise, rather than just giving a numerical difference of signed sums. This is a modest structural enumeration, not an asymptotic theorem or novelty for signed Burnside.

The dated certificate retains the supplied scientific assessment, sources and limitations.
