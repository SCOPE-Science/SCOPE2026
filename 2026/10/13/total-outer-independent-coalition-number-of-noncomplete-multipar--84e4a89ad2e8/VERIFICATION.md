---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

PASS: For r>=3 complete multipartite, D is total outer-independent dominating iff Y=V\D is contained in one part: independence gives necessity, and at least r−1>=2 fully selected other parts ensure sufficiency for total domination. Taking y,z in different parts and the partition (V\{y,z},{y},{z}) yields 3 non-TOIDS blocks with each a coalition partner. For any supposed >=4-block partition take coalition A,B; all other blocks lie in the one part P containing V\(A∪B). A remaining C cannot partner A (or B), because B and an additional remaining block lie in the complement of A∪C, forcing B⊆P and then A itself TOIDS. Nor can two remaining blocks C,E⊆P be total dominating (all vertices inside P have no neighbor in C∪E), contradiction. Hence at most 3. Independently enumerated all set partitions and definition-level predicates for K(1,1,2), K(1,2,2), K(2,2,2), K(1,1,1,3): maxima 3. All-part-size conclusion rests on symbolic proof. Complete graphs excluded as prior-covered and r=2 separate.

## originality

PASS

PASS best-of-knowledge: Buntina–Golmohammadi's initiating July 2026 full primary arXiv text defines this precise TOI-coalition invariant and gives C_t^{oi}(K_n)=3 and C_t^{oi}(K_{r,s})=s+1 but no r>=3 complete multipartite formula. Its general bounds C≤alpha(G)+2 and C≤n−gamma_t^{oi}+2 do not imply constant 3 as the largest part grows. Here the proof uses an additional complementary-part rigidity argument. Resultary and topic-alias searches gave other domination parameters, not this coalition invariant's exact multipartite classification. Priority from possibly unindexed work remains a residual risk.

## value

PASS

PASS: Distinguishing r=2 vs r>=3 is a meaningful structural boundary for a newly defined graph coalition invariant. Unlike the unbounded bipartite value s+1, all noncomplete multipartite graphs with >=3 parts collapse to the sharp constant 3. The proof explains this discontinuity through support rigidity of complements, rather than merely computing tiny graph instances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
