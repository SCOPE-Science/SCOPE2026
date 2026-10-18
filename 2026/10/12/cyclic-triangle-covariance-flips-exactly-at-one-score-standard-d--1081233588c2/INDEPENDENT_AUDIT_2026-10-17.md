# Independent mathematical audit

## correctness

PASS

Conditioning on one vertex outdegree k gives E[C_n|D_v=k]=binom(q,3)/4+k(q−k)/2, since every mixed neighbor pair forms a cycle with probability 1/2. Subtracting E[C_n]=binom(n,3)/4 yields [q−(2k−q)^2]/8, proving the master covariance by exchangeability. The two-vertex score-class joint probability is p²[1−(2k−q)^2/q²] using the common-edge orientation; summing indicators yields Var(N_k)=n p[1−p(1+δ²/q)]. Distinct triangle indicators are pairwise independent even when triangles share one edge (one required orientation of each disjoint pair after conditioning on shared edge), so Var(C_n)=nq(q−1)/32. The displayed Corr and CLT profile follow algebraically; exactly |k−q/2|=sqrt(q)/2 gives zeros, not independence. Independently enumerated every tournament at n=3,4,5 using edge coins, counted cycles directly from triple orientations, and matched all covariance and variance formulas; inspected full supplied n<=6 checker.

## originality

PASS

Classical score identity C_n=binom(n,3)−sum_v binom(D_v,2) gives deterministic dependence of cyclic triangles on outdegrees but not automatically the random score-class covariance. Older random tournament motif papers study subgraph counts and score structure generally, but the exact mixed class covariance, one-standard-deviation sign rule, and asymptotic profile were not located. Bounded best-of-knowledge originality, with material risk that classical second-moment score identities already imply the formula after routine specialization.

## value

PASS

An exact covariance law for a natural score-class statistic and cyclic triangle count, with sharp one-standard-deviation sign reversal and universal local-CLT profile, clarifies how cyclicity favors central rather than extreme vertex scores. It provides a reusable joint-moment benchmark, not an arbitrary small instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
