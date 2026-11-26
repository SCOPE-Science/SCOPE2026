# Independent mathematical audit

## correctness

PASS

There are m comparisons on m+1 observations, but m points in the empirical measure. On digit branch j, x<T_b x iff x>j/(b-1); j=b-1 is excluded, and the omitted endpoints are null. Each survivor branch maps onto (j/(b-1),1), so admissible paths are exactly weakly nondecreasing labels. Inverse composition gives interval length (b-1-j)/[(b-1)b^m] for a path ending at j. Summing over paths ending at j, and writing b-1-j as a count of upper labels, gives the binomial coefficient by two hockey-stick sums. Full visitation requires a positive composition of m with b-1 parts and all such paths have the same final label and weight. Its conditional probability is the stated ratio and tends to one. The normalized distinct integer cut locations tend to uniform order statistics (sampling with and without replacement differ by O_b(1/m)); their spacings are Dirichlet(1,...,1). The sum of deviations from each branch fixed point is bounded by a geometric series below b/(b-1) per contiguous block, giving the claimed coupling cost; summation by parts on the spacings gives the uniform-sum law and moments. The one-label case b=2 is included. Read RESULT.md, VERIFICATION.md and verify.py without executing uploaded code. Independently checked 152,993 base-adic cells over (b,m)=(2,13),(3,8),(4,7),(5,6),(6,6),(7,5),(8,5),(10,4), with exact integer endpoints on the common denominator (b-1)b^m: for cell r use floor(r/b^(m-t)) at time t, take the maximum lower bound from the comparison inequalities and sum the surviving lengths. All eight interval sums gave the stated numerator; this checks finite probabilities, not the limit.

## originality

PASS

The exact ascent probability is also in later indexed work and a tripling-case overlap should be credited. The supported distinct claim is the conditional weak limit of the actual orbit empirical measure, with its explicit random masses, finite occupancy description and coupling estimate. The checked symbolic pattern results, exact run laws and ordinary uniform-spacing facts do not supply that orbit-level conclusion.

## value

PASS

The measure theorem answers what long monotone runs actually select, beyond how often they occur. The selected orbits spend random macroscopic fractions near several deterministic repelling fixed points, rather than converging to a single deterministic mean or an unconditioned invariant law. The uniform composition mechanism, quantitative concentration estimate and orbit-average law make the distinction usable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
