# Independent mathematical audit

## correctness

PASS

Greedy embedding gives one canonical mask per distinct descendant. Classifying by adjacent, nonadjacent, and final-pair deletions yields the two endpoint and interior singleton penalties, including n=2. Alternating positive run compositions then give the full marked series; sampling distinct coordinates without replacement gives the mean, with the disjoint-pair term absent for n<4. For the limit, conditioning on the endpoint types turns floor(R/2), up to an integer shift, into a hypergeometric variable with population n−2, k−1 successes, and n−k−1, n−k, or n−k−2 draws respectively. This follows by complementing one run-composition binomial. Each endpoint law gives transition variance asymptotic to 4n alpha²(1−alpha)² and mean 2k(n−k)/n+O(1), so the hypergeometric CLT gives the same limit in the mixture. The bounded-by-O(n) singleton corrections and centered quadratic remainder vanish on the n^(3/2) scale. Multiplication by the limiting derivative 2 alpha(1−alpha) gives exactly the claimed centered Gaussian variance. A separately written prefix-subsequence DP reproduces the full histograms, means, and transition moments for all 16,380 words at lengths 2–13.

## originality

PASS

The per-word run identity and runs CLT are not credited as original. The supported distinction is the fixed-content law of distinct descendants, with the marked exact spectrum, mean and composition-dependent normal limit together. Prior inspected laws either omit the source-weight coordinate, enumerate a different ball, or condition on the received word. The foundational Swart–Ferreira text was not accessible; no inference about its whole contents is made.

## value

PASS

Fixed composition is a natural coding constraint that removes the random weight component of variation. The exact distribution across each weight class gives ball sizes and probabilities unavailable from the unconditional law; the limit quantifies nonzero residual fluctuations and how their leading scale changes with density. This is a complete conditional classification, not just an isolated conditional moment or a new proof of the run identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
