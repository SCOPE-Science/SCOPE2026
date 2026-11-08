# Independent mathematical audit

## correctness

PASS

Index cars on a cyclic synchronous Rule-184 ring. Exact lifted recursion p_i(t+1)=min(p_i(t)+1,p_(i+1)(t)-1) yields by induction p_i(t)-t=p_i(0)+min_{0<=j<=t}Σ_{r<j}(g_(i+r)-1). For k<=n/2, increments δ_i=g_i-1>=-1 sum to h=n-2k>=0, so every running minimum is attained during one k-gap cycle. Last first minimum τ_i<=k-1 gives T=max τ_i<=k-1. T=k-1 iff a designated root has all nonempty backward partial sums strictly negative. Two distinct roots would partition the k increments into two strictly negative arcs, impossible because their total h>=0, so the root is unique. Reversed negative-prefix sequences biject with preorder outdegree sequences of rooted plane ordered trees on k vertices; final gap is uniquely forced and nonnegative. There are n root site choices, hence n Catalan_(k-1) indexed extremizers. Particle-vacancy involution handles k>n/2; the exact binomial ratio gives the fixed-h limit 2^(-h-1). Independent from-recurrence direct Rule-184 finite-state enumeration over every indexed configuration for each 2<=n<=12 matched maximum T=m-1 and exact n Cat_(m-1) counts at every fixed density. This finite enumeration corroborates but is not an all-n proof.

## originality

PASS

A tagged-car first-passage distribution, mean global relaxation time and coarse finite-time density-classification bounds are precedents but not the exact joint maximum-and-indexed-extremizer result. The first-passage literature contains Catalan-related combinatorics and might imply the result under a different presentation, retained as a risk.

## value

PASS

The maximum global relaxation delay of deterministic fixed-density periodic traffic and the precise multiplicity of achieving configurations are natural global dynamical invariants. The unique bottleneck car/Catalan plane-tree bijection yields a nontrivial exact classification, and the balanced critical probability tends to 1/2. This is not a routine first step of simulation and no claim of broader continuous-time traffic is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
