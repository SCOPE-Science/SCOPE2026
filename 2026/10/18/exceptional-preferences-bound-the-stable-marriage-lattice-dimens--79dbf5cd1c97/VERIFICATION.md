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

A stable matching agreeing with an injective exceptional assignment leaves a stable residual market. Its master order forces serial choice by the remaining men, proving uniqueness of completion and the (n)_k count. The k=0 and empty-residual cases are included. Testing the full candidate for blocks is essential; with rank tables the per-candidate cost is O(n²). In the classical lattice identity the womenwise join gives each man his worse of the two partners: if a woman who chooses him comes from M, stability of N forces him to prefer his partner in N when the partners differ. Two women cannot choose the same man because this would impose opposite strict preferences on him. Thus a join blocker would block the original matching giving the man that worse partner; the complementary womenwise meet is likewise stable. If the exceptional tuple of N dominates that of M, M∨N has N's tuple, hence is N. This proves order reflection and sublattice closure; the k coordinate-first lexicographic extensions realize the product order on the image. In the one-exception witness each proposed matching is the greedy residual completion. Woman w₀ cannot block with a better-ranked man i>t (he prefers w_i), and man m_t cannot block with any w_j he prefers to w₀ because 1≤j≤t and those women get smaller-index men. In the Boolean witness the earliest block with an external match would have both a man and a woman matched out, forming a block; the two internal states then combine freely. Singleton/complement incomparable pairs give the lower bound k for k≥3, and k=1,2 follow directly. A separately written exact brute-force replay (workspace branch 47b5018a-9565-46aa-af06-0ea1d6758a5c, bounded_replay.py and bounded_replay.out) reproduced n stable matchings for n=1 through 6 and 2^k for k=1 through 3, with the stated matching sets. The frozen script and certificate were inspected without execution; their exhaustive n=2,3 census is finite evidence, not the theorem.

## originality

PASS

Master-list uniqueness and the general stable-matching and rotation-lattice identities are established. The supported contribution is the sharp representation/count package for k specified individual exceptions, especially the coordinate embedding and the extremizers realizing the joint one-exception and dimension bounds. It is not a claim of a new general lattice identity or master-list algorithm.

## value

PASS

For a motivated near-master-list market, knowing only the exceptional partners recovers both the full solution and its order relative to all other solutions. It also gives duplicate-free enumeration via a bounded coordinate search rather than enumeration over all matchings. The sharp counts and Boolean examples show the information and dimension requirements cannot be reduced in the stated senses. This is an XP bound, not an FPT result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
