# Independent mathematical audit

## correctness

PASS

The published utility formula u_i=1−q∏_{j∈N(i)}(1−p/d_j) yields component utilities for an isolate u0=1−q, a matched-edge vertex u2=1−q(1−p), and a triangle vertex u3=1−q(1−p/2)^2. Replacing one matched edge plus the isolate by a triangle changes total expected utility by 3u3−2u2−u0=q(p−3p²/4), strictly positive for the entire admitted range 0<p≤1/2. The original Dwork et al Appendix C AM–GM proof bounds the optimum average by u2 for any graph, while (n−1) edge-paired vertices of M_n contribute (n−1)u2/n and isolate contribution is nonnegative. This proves both inequalities for every odd n>=3; the constants remain positive for fixed p,q and give Θ(n^-1). Independent exact rational component checks confirm the algebra, not the AM–GM argument itself. No global identification of the optimal odd graph is needed or asserted.

## originality

PASS

Best-of-knowledge independent claim-versus-prior implication comparison: O(1/n) upper alone does not imply Ω(1/n); the triangle substitution establishes that the published rate is asymptotically non-improvable for fixed admissible p,q. The result is a complementary corollary-scale bound, not the full optimum classification. Closest exact antecedents are explicitly credited and risks retained.

## value

PASS

The fixed-parameter welfare gap between an easily described efficient-even-n matching and the true unknown optimum at odd n is a natural asymptotic approximation question. Showing a positive constructive lower bound forces the exact inverse-population order, improving a known one-sided rate and preventing false conjectures of o(n^-1). Although the witness is short, it settles the natural order-of-magnitude boundary uniformly over all odd n and all admissible fixed parameters, rather than evaluating an arbitrary tiny example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
