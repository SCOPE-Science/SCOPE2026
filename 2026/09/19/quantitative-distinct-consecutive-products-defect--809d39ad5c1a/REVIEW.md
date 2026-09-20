# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The argument preserves Chojecki's construction and collision-free proof and changes only the quantitative choice of the short/long prime-gap threshold. Li's public manuscript proves that intervals of backward length n^(1/24+epsilon) contain primes for all but O(X(log X)^(-B)) integers in a dyadic interval. For every fixed theta>1/24 this implies an O_B(X(log X)^(-B)) total-length bound for prime gaps longer than p^theta by charging most interior integer endpoints of each such gap to Li-exceptional intervals.

For short rejected gaps, Chojecki's raw-witness curve count is O(X^(1/2+6 theta+o(1))) when theta is left symbolic. His branch, contraction and equal-chain arguments likewise remain valid with rho=(2-theta)^(-1). The raw-root forest exponent is maximized at zero unequal edges because

C_raw=(6 theta^2+3 theta-1)/(2(theta-1))>0

throughout 1/24<theta<1/16, giving 1/2+8 theta. The long-parent exponent is also decreasing because

C_long=(5 theta^2-10 theta+1)/((theta-2)(theta-1))>0,

and its maximum 1-rho+5 theta is strictly below 1/2+8 theta. The algebra has been checked symbolically in the included artifact. Letting theta approach 1/24 proves the 5/6+epsilon short-loss exponent. Combining short and long gaps gives the stated defect bound and the super-logarithmic corollary.

No empirical computation is used as a substitute for the proof.

## Originality

**PASS, to the best of our knowledge.** Chojecki's inspected preprint explicitly proves O(X^(9/10+o(1))) for the total length of short rejected gaps at theta=1/20 and then concludes only density one after adding a qualitative long-gap estimate. Li's inspected manuscript proves the 1/24 almost-all short-interval theorem but does not discuss the consecutive-product problem. Searches using exact and synonymous formulations, the exponents 9/10 and 5/6, “quantitative density”, “complement/defect”, “consecutive block products”, and the 1/24 short-interval input did not locate an earlier statement of the present quantitative strengthening. Public summaries and a public reconstruction/formalization located during the check concern the density-one theorem itself rather than these defect estimates.

Residual risk remains because both the motivating proof and the newest short-interval manuscript are recent enough that concurrent applications may not yet be indexed. An older public predecessor manuscript by Chojecki gives a conditional density-one strategy, but the located material does not provide this unconditional 5/6-plus-epsilon short-loss bound or the all-log-powers global defect estimate.

No inaccessible source was identified whose title or available description specifically suggests the same quantitative theorem. This does not establish exhaustive literature coverage.

## Value

**PASS.** The result turns a qualitative density-one conclusion into a strong quantitative one for the same canonical set, shows that the complement beats every fixed logarithmic proportion, and improves the structured short-gap exponent from 9/10 to the limiting value 5/6. The proof also isolates a reusable parameterized version of the witness-forest calculation, making future improvements in almost-all prime-gap exponents immediately translatable into sharper deletion exponents.

## Limitations

The 5/6 exponent is not claimed optimal. The full defect is not shown to satisfy a power-saving bound because the long-gap input has only an arbitrarily strong fixed logarithmic exceptional-set saving. The result applies to Chojecki's canonical greedy set and inherits the cited integral-point and short-prime-interval theorems. No independent validation or formal proof-assistant verification is asserted.
