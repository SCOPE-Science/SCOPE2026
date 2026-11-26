# Independent mathematical audit

## correctness

PASS

A literal border of a Dyck word has nonnegative height as a prefix and nonpositive height as a suffix; it is therefore balanced and itself Dyck. A shortest nonempty proper border is unbordered, since a shorter border of it would border the parent word; overlapping copies would also create a shorter border. Peeling the two copies leaves a Dyck center at the same zero height, and any construction bvb with b an unbordered nonempty Dyck word and v Dyck has shortest border b. This proves C=1+U+C·U(z²) in semilength. If any candidate maximal decomposition used a longer outer block b, its prefix and suffix s equal to the shortest border would be nonoverlapping, so b=sys. The s and the second s (and y if nonempty) can all be used as successive paired blocks in place of the single pair b, strictly increasing width. A bordered word can also improve over leaving the entire word as one center. Induction gives the unique maximum-width decomposition, with empty width zero and optional nonempty unbordered center. Each pair contributes z^(2j)t², giving the stated bivariate GF. Set G=U(z²), analytic for |z|<1/2 by the Catalan bound; α=G(1/4) is in (0,1). U=(1−G)C−1 gives leading square-root coefficient −2(1−α); for odd width 2k+1 multiplication by G^k changes it by α^k, whereas even width 2k uses only the analytic G^k. The pointwise limits exhaust total mass. Differentiating at t=1 gives [U(1+G)+2G]/(1−G)²; its Catalan multiplier at 1/4 is (1+α)/(1−α). Nonnegative coefficients and G(1/4)<1 give a disc strictly larger than radius 1/4 with denominator nonvanishing, so the transfer for the mean is justified, not inferred from weak convergence. Independent replay `python3 /workspace/reproduce_reviews.py 5` maximized over every matching split (not greedy peeling) for 23714 Dyck words including the empty word at n=0..10, matched the width histograms, and checked coefficient sums through n=100. Exact rational truncation with error ≤(4/3)4^(-101) corroborated the supplied decimals. The frozen verifier was read, not executed; finite checks do not prove the transfer or uniqueness.

## originality

PASS

The generic unbordered shortest-border method and width recurrences are prior. The supported distinct claim is their use on literal Dyck borders to obtain exact Catalan-restricted width counts and a limiting odd-geometric law and mean. None of the inspected prior theorem statements determines that Dyck-restricted law. Exact sequence and one nearby chapter could not be fully resolved; this is a bounded comparison rather than a priority guarantee.

## value

PASS

The complete histogram of the largest-width invariant in the natural Catalan ensemble is useful in its own right. More than a small census or conditioning notation is supplied: literal borders close inside the class, and exact finite distributions lead to a limiting odd-supported law with an explicit parameter and mean. The vanishing even-width mass and persistent geometric tail distinguish the asymptotic structure without claiming a result for other Dyck ensembles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
