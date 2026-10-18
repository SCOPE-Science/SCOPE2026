# Independent mathematical audit

## correctness

PASS

PASS: For each real symmetric A, r^TAr-tr(A) is invariant under r -> -r and has the uniform finite distribution on antipodal classes. Any coupling of the scalar class values can be lifted to a genuine coupling of uniform sign vectors by a common independent global sign; the uncrossing inequality establishes the sorted least-squares cost. For n=1,2,3, the signed-coordinate-permutation action on 1,2,4 antipodal classes is respectively S1,S2,S4 (in n=3 the kernel is {+I,-I}, so 48/2=24). Thus a deterministic signed coordinate permutation realizes a minimizing scalar coupling for every A,B. For n=4, directly evaluated Walsh lists with c=(-2,2,-3,2,2,2), d=(-1,2,2,3,-3,3) have sorted squared matching sum 16, while enumeration of all 192 induced maps has least sum 24. Multiplying by 4 epsilon^2 /8 yields 8 epsilon^2 vs 12 epsilon^2. Gershgorin row absolute offdiagonal sums <=8 prove I+epsilon C,I+epsilon D SPD for 0<epsilon<1/8. My independent enumeration recreated the 16/24 gap and 192 maps, not merely replayed VERIFY_OK. The ratio 3/2 belongs only to the displayed pair, not a global worst-case theorem.

## originality

PASS

PASS best-of-knowledge: the Wasserstein/rearrangement optimum is classical, the small signed-cube group action is classical, and trace-difference variance formulas are prior; the novel claim is exact realizability of every sorted coupling via fixed signed coordinate maps through dimension three and an explicit dimension-four SPD first obstruction. The inspected Dynamic Trace Estimation paper defines controlled probe reuse and variance bounds, while XTrace develops exchangeable multi-probe trace estimation; neither material establishes the small-dimensional universal implementability frontier. A semantically similar record was not returned by the published-record search; absence is not proof of priority.

## value

PASS

PASS: Fixed signed coordinate maps preserve each Rademacher marginal and evaluation count, so whether they realize the minimum variance among all admissible joint probe laws is a motivated question for paired trace differences. The exact first obstruction at dimension four and a 3/2 variance loss even for arbitrarily well-conditioned positive-definite pairs are mathematically informative boundary facts. It does not claim feasible optimal coupling discovery in matrix-free algorithms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
