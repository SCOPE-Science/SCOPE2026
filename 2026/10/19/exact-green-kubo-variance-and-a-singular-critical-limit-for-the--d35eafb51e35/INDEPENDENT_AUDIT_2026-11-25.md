# Independent mathematical audit

## correctness

PASS

The shell transfer equations follow by the three inverse branches, including the missing halving inverse on I_0. The small formal kernel roots are t(z) and 2t(z); substitution into the numerator equations is legitimate since t(0)=0. Subtracting μ²/(1−z) removes the unit pole, and the remaining factors listed in the record do not vanish for |z|≤1 when p>1/2. Independently one can evaluate the sum without the shell resolvent: let r=q/p, K have invariant law (1−r)r^k, and U be independent uniform; X=2^(−K)U has the stated stationary density by mixing the uniforms on [0,2^(−k)]. Halving increases K; doubling decreases positive K, and at K=0 instead replaces U by 2U mod 1. These updates preserve the product stationary law on (K,U). Put δ(k)=2^(−k), m=Eδ, n=Eδ², b=2/(3p−1). For the reflected depth operator Q, (I−Q)H=δ−m with H(k)=−b(δ(k)+k). For R obtained by discounting the doubling-at-zero transition by 1/2, (I−R)L=δ with L=b(3−δ). Both identities follow by substitution also at k=0. Uniform doubling has lag-j centered covariance 2^(−j)/12, so C_l=Cov(δ(K_0),δ(K_l))/4+E[δ(K_0)(R^lδ)(K_0)]/12. Both terms are nonnegative: monotone coupling preserves depth order, and R is positive. Telescoping sums gives C(1)=E[(δ−m)H]/4+E[δL]/12: reflected chains driven by common choices coalesce when the larger depth first hits zero, with pre-coalescence distance bounded by initial distance, and the number of discounted doublings goes to infinity by the positive doubling-minus-halving drift. Thus the two remainder terms vanish by domination. Using m=2(2p−1)/(3p−1), n=4(2p−1)/(5p−1) and Cov(δ,K)=−2pq/(3p−1)² gives the recorded C(1) and the stated Γ=2C(1)−(n/3−m²/4). Numerical cross-check of this independent evaluation and the rational formula at six parameters including p=1, p=3/5 and p=0.500001 agreed within 7×10⁻¹⁵; the identities, not the grid, establish the theorem. The derivative cubic is positive at 1/2 and increasing, while Var(X_0)∼(8/9)(2p−1); at fixed N the variance per step is at most N Var(X_0), verifying both orders of limits with the separate critical atom. Frozen verify.py and VERIFICATION.md were inspected, not executed; the 24 exact-lag comparisons are recorded diagnostics only.

## originality

PASS

The supported distinct claim is the evaluated, invariant-initial infinite covariance sum and singular boundary behavior, not the map, its invariant law, the binary representation or exact finite lags. The earlier same-object article gives exact special lags and the later primary paper’s explicit full position transform initializes uniformly instead of stationarily. General binary-stack machinery makes stationary calculations possible but the inspected older statements do not give the needed stationary projection or infinite sum. A distinct Resultary record has a genuinely covering stationary covariance transform, with a removable unit pole; evaluation there mechanically gives the fixed-p invariant, even though the rational expression is not stated. That catalogue publication is later, so it does not establish an antecedent to the frozen finding. No absolute or unpublished priority is certified.

## value

PASS

The coordinate Green–Kubo intensity is a standard meaningful time-accumulation invariant in an established intermittent random map. An exact finite nonzero critical limit despite vanishing one-time variance gives a quantitative example of noncommuting long-time and parameter limits, with an explicit normalized-correlation-time blowup. Obtaining the exact infinite sum is more than reproducing finite lags or the known stationary density. No quenched result, uniform critical crossover or central limit theorem is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
