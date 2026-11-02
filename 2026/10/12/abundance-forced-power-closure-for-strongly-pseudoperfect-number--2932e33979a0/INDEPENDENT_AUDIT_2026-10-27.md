# Independent mathematical audit

## correctness

PASS

For n>1 strongly pseudoperfect, the complement of every complement-closed divisor representation has positive-or-zero mass A=sigma(n)-2n. Each omitted nonsquare orbit contributes d+n/d<=A, giving d^2-Ad+n<=0 and roots (A±sqrt(A^2-4n))/2 when A>=2sqrt(n); if A<2sqrt(n) no two-member orbit may be omitted. The square-root singleton is expressly excepted. When sigma(n)<=3n, A<=n<n+1, hence the (1,n) orbit is in every representation; Wang--Zelinsky Theorem 5 applies to any one such representation and proves strong pseudoperfectness of n^k for all integers k>=1. For n=720, sigma=2418, A=978 and the five omitted orbits (1,720),(10,72),(16,45),(18,40),(20,36) sum to 978 and are pairwise disjoint; the retained complement-closed divisor set sums to 1440. Independently implemented exact set-valued subset-sum DP over every integer 2<=n<720, removing distinguished orbit (1,n) and allowing each other complement orbit independently, gave zero escape candidates; an independent integer bitset DP agreed on each of 719 integers 2..720. Each orbit including square-root singleton is considered exactly once, so this proves the finite leastness claim. Neither the finite calculation nor the checker proves an unbounded power theorem; that step comes from cited Theorem 5.

## originality

PASS

Best-of-knowledge qualified PASS applies to the natural representation-level least-escape boundary 720 in conjunction with the global abundance region. The omitted-mass bound and quadratic band are elementary observations already essentially present as the inequality used in Wang--Zelinsky Proposition 15; they are not credited as standalone major novelties. The sigma<=3n power consequence is likewise a short corollary of Theorem 5 plus the elementary mass bound. Nevertheless, the exact least n>1 admitting ANY strongly pseudoperfect representation with (1,n) omitted, including the five-orbit witness and exhaustive lower bound, is not stated or implied by the inspected primary text, known full published Resultary cases, or the OEIS entry; it identifies a natural sharp first failure of representation-wise forcing relevant to Theorem 5. No assertion is made that 720 lacks another representation containing (1,n), or that power closure fails at 720.

## value

PASS

The object is the standard complement-closed strong-pseudoperfect divisor representation; the distinguished (1,n) orbit is exactly Wang--Zelinsky Theorem 5’s hypothesis for power closure. The abundance threshold provides a clean structural region where that hypothesis holds for EVERY representation, and the independently verified first integer permitting its failure in some representation is precisely 720 with an explicit five-pair witness. The number 720 is not an arbitrary slice: it is a natural first boundary for an inclusion property singled out by the motivating open question. The exact cutoff serves as a small reproducible benchmark for studies of representation quantifiers and non-forced-pair phenomena. Standalone innovation in the one-line omitted-pair bound is modest and must not be overstated. No claim that 720 disproves extremely strong pseudoperfectness or power closure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
