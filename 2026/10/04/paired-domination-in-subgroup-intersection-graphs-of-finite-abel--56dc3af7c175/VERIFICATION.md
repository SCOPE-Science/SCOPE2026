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

The proof has four critical checks.

1. **Nonsquare-free exponent.** The socle contains every subgroup of prime order and meets every nontrivial subgroup. Except for \(C_{p^2}\), there is a second subgroup vertex, so the universal socle and that vertex form an adjacent dominating pair.

2. **Square-free composite exponent.** The Sylow factors are elementary abelian. With at least three primes, two complementary products intersect in the remaining factors. With exactly two primes, a higher-rank Sylow factor supplies a nontrivial proper subspace that makes the two-subgroup cover adjacent. The only rank-one exception is \(C_{pq}\).

3. **Elementary abelian groups.** For \(C_p^d\) with \(d\ge3\), the \(p+1\) hyperplanes through a fixed codimension-two subspace form a clique and dominate. If \(p\) is odd, their number is even and they pair perfectly. If \(p=2\), paired sets must have even size, so the lower bound \(3\) becomes \(4\); adjoining the common subspace attains \(4\).

4. **Exceptional graphs.** \(C_{p^2}\) has one subgroup vertex, \(C_p^2\) has only pairwise-disjoint one-dimensional subgroup vertices, and \(C_{pq}\) has two disjoint subgroup vertices. Hence no paired dominating set exists in exactly these cases.

The standalone checker reconstructs the complete subgroup lattice from the group operation, builds the intersection graph, and searches paired dominating sets exactly for ten small finite abelian groups.

Exact output:

```text
VERIFY_OK
C4: vertices=1 paired_domination=none
C8: vertices=2 paired_domination=2
C2xC2: vertices=3 paired_domination=none
C2^3: vertices=14 paired_domination=4
C3^2: vertices=4 paired_domination=none
C3^3: vertices=26 paired_domination=4
C6: vertices=2 paired_domination=none
C2^2xC3: vertices=8 paired_domination=2
C30: vertices=6 paired_domination=2
C4xC2: vertices=6 paired_domination=2
```

The finite checks are corroborative only. The classification for arbitrary finite abelian groups is proved symbolically.
