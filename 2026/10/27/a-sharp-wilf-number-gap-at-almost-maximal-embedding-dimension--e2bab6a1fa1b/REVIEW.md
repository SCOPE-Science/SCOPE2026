# Independent mathematical audit

## correctness

PASS

A positive Apéry member is either a minimal generator other than m or the unique decomposable member w. In any two-positive-summand decomposition of w both summands must lie in Ap(S,m) (subtracting m from a non-Apéry summand would put w−m in S). The smaller summand u satisfies 2u≤w≤c+m−1 and u<c. The progression from u contributes h≥1 left elements disjoint from q=ceil(c/m) multiples of m. Its first term not below c is u+hm, giving c≤(2h+1)m−1. Thus if q≤2h then W≥(m−1)h−q≥h(m−3); if q=2h+1 the offset −1 gives the same bound. Equality requires h=1 and c≥m+3, so q=2 or 3. For q=2 the left set has size 3, c=2m, and the tail elements of potential generating size 2m+s, 1≤s<m, decompose exactly at s=r and, when available, s=2r; this gives e=m−1 precisely for 2r<m. For q=3 equality gives N=4, c=3m−1, and u=2m−1 by the two inequalities for u. In the resulting Apéry set only 4m−2 decomposes: for 3m+r with 1≤r≤m−3 any possible summands are drawn from m, 2m−1, 2m, and their pair sums miss it. Both families are closed, have the claimed conductor and give W=m−3. Inspected the frozen bounded Kunz verifier but did not execute it. Independently enumerated direct closed left sets for 4≤m≤8 and c≤3m−1 with /workspace/branches/independent_replay.py, obtaining equality counts 2,3,3,4,4 exactly as classified. This bounded check is not the proof for unbounded c or m.

## originality

PASS

Best-of-knowledge pass for the sharp gap together with all positive-gap extremizers in the canonical almost-maximal embedding-dimension stratum. Qualitative positivity can already be obtained from a general type-based equality theorem; it is not the contribution.

## value

PASS

The natural first stratum below maximal embedding dimension is solved exactly for every m, with complete and explicitly different attaining families at conductors 2m and 3m−1. This gives usable quantitative separation from Wilf equality beyond existing positivity and shows why the exact optimum is attained rather than only a nonsharp lower estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
