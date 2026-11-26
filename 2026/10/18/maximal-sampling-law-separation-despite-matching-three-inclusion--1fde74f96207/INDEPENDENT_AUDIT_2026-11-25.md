# Independent mathematical audit

## correctness

PASS

For t≤3 distinct points the t−1 differences from the first point are independent over F₂. Counting nonzero normals in their annihilator with one forced intercept gives (N/2^(t−1)−1)/(2(N−1)), equal to the simple-random-sampling ratio at each stated order. The pairwise-coordinate Walsh sum factors into m four-term sums; each coefficient is ±√N, with coefficient +√N at frequency zero. The two intercepts give totals 0 and √N with equal probability. The population variance with divisor N−1 is 1, giving SRSWOR total variance N/4 and mean √N/2. The positive count in SRSWOR is hypergeometric (not Gaussian at finite N); the sampling and positive fractions tend to 1/2 and the bounded centered values meet the finite-population CLT condition. The closed set {−1,1} has Gaussian mass zero, so its SRSWOR mass tends to zero and tests total variation up to a vanishing error. Independent finite corroboration at m=2 counted all 30 hyperplanes, 696 subsets of sizes 1–3 and 16 Walsh coefficients, with 15 totals at 0 and 15 at 4. This was a separate enumeration, not execution of the supplied checker; universality follows from the proof.

## originality

PASS

Pass for the combined fixed-size order-three counterexample with an exact two-point law and maximal asymptotic separation, not for the ingredients or the earlier order-two phenomenon. Chen explicitly proves the order-two case, and the closest inspected design and triplewise-independence statements do not supply this combined claim.

## value

PASS

Resolves the first additional inclusion order beyond the cited order-two counterexample under bounded deterministic outcomes, a fixed sampling fraction, and identical finite-size variances. The exact two-point law and asymptotically maximal separation give a usable benchmark for design-based CLT criteria, rather than just a change in higher moments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
