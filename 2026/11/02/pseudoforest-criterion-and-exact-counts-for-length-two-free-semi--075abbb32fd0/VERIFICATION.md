---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Reconstructed the exact word-set factor rank as min_B(|B|+|W|-e_W(B)): a length-two target is either itself a generator or concatenation of two length-one generators. Induced sparsity is precisely pseudoforest, and a proper nonempty tight B is equivalent to a nontrivial factorization, so one spanning cycle is precisely irreducibility. Enumerating oriented Hamilton cycles and rooted-tree cycle species yields the EGF exp(-T^2/2)/sqrt(1-2T). Independently enumerated n=1..4 distinct image sets with rank-preserving counts 1,6,72,1274 and irreducible counts 1,1,8,48; checked Stirling asymptotic. n=1 loop and n=2 opposite edge pair handled separately.

## originality

PASS

Bell-Foster-Reidenbach supply the general rank-preserving factor-basis/composition condition, a substantive ancestor, but their read main theorems do not state the exact length-two graph characterization or enumerations. Classical Cayley unicyclic species tools are known and properly credited.

## value

PASS

The natural algebraic irreducibility question receives a complete graph-theoretic characterization with exact all-rank counts and exponential rarity, not merely a routine renaming of the general factor-basis criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
