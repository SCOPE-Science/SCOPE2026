---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

The finite recurrence is logically exhaustive: each linear ternary word has one three-symbol starting prefix, and each next length-4 window covers a nonempty subset of the 16 four-bit factors. A valid exact-once word has pairwise disjoint new coverage sets at every step; thus no valid path is pruned. Conversely, a terminal union of all 16 factors is a disjoint partition and therefore exactly one hit per factor. Nonempty sets force at most 16 appended windows, hence length at most 19. The implementation uses exact 16-bit masks; a separately written set-based enumerator independently visited 15,840 states, found 385 strings and exactly the 10 coefficient pairs (4,4):1,(8,3):4,(11,2):4,(11,3):16,(14,2):8,(15,1):16,(16,1):8,(17,1):8,(18,1):64,(19,0):256. Each string was independently rechecked against all 16 binary factors and multiplicities; the generated complete witness list and 32 orbit representatives have exact pinned Git blob hashes 77e7067bdd9d98b8c3110e0e47db88bb63f969eb and 3daef4c501807e19acb73b5b44e765c886625326. Under reversal and complement the orbit sizes are exactly {1:1,4:96}, with 32 nontrivial orbits. All 10 pinned source file blobs, both pinned and current tree, and reconstructed tree SHA b52db21856a79c03545c47e938cd0a704469b49b agree. Finite exhaustion proves only binary, factor length four, linear windows; no infinite factor-order claim.

## originality

PASS

Primary-source statement/implication comparison supports a best-of-knowledge novel finite exact length-by-wildcard enumerator and complete orbit census for LINEAR binary order-four universal partial words. Chen–Kitaev–Mütze–Sun give individual n=4 witnesses, construction/obstruction theorems, and explicitly call for classification, but not the ten-term joint polynomial. Goeckner et al. explicitly pose how many universal partial words exist for fixed alphabet and order, without establishing this exact binary n=4 result in the material read. A 2026 later paper settles a CYCLIC n=4 equivalence problem, not the much larger linear enumerator. The ordinary no-wildcard 256 term is classical and credited. Searches of published related findings returned distinct invariants and no equivalent covering result; failed indexing alone is not proof of novelty. Prior unpublished author-hosted n=4 computations and unindexed tables remain priority risks.

## value

PASS

The number and length distribution of universal partial words at fixed alphabet/order is a natural object posed directly in Goeckner et al. Question 6.5 and motivated by Chen et al. Section 6 classification programme. Binary order four admits nontrivial 1-,2-,3-wildcard families: a complete joint length/diamond count shows exactly which compression lengths occur and all multiplicities. The 32 symmetry orbit types and full witness list are independently useful finite data for construction and benchmarking higher-order counting methods; prior papers provide existence examples and obstruction patterns rather than this complete census. The classical de Bruijn 256 case is not claimed new. No paper-sized generalization is required for this motivated unknown exact complete finite classification. Scope excludes cycles, larger orders and nonbinary alphabets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
