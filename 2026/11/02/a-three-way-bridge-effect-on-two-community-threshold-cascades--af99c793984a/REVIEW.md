# Independent mathematical audit

## correctness

PASS

PASS — For K_n an isolated seed set fills iff k≥r_n=ceil(phi(n−1)). When the clique has one added external bridge edge, the nonbridge threshold is r_n and its gateway threshold R_n=ceil(phi n), R−r∈{0,1}. Classify local configurations into unassisted U_n=D_n−H_n and externally rescuable E_n=L_n+H_n, where L_n=1[R=r] binom(n−1,r−1)z^{r−1}, H_n=1[R=n]z^{n−1}. Two communities fill iff at least one is unassisted and the other is unassisted or rescuable; two mutually blocked rescuable configurations do not start. Hence F_bridge=U_aU_b+U_aE_b+E_aU_b, and subtracting D_aD_b gives L_aU_b+L_bU_a−H_aH_b. Because R=r and R=n cannot coexist for n≥3, the difference is coefficientwise positive exactly when L_a or L_b appears; strictly negative −z^{a+b−2} when both H appear; zero otherwise. The minimal full-cascade seed size drops by one only in the beneficial case. Independently enumerated 20 combinations of two-clique orders and rational thresholds from actual adjacency/iterative activation and matched the closed polynomial exactly. General proof is the exhaustive local category argument for all a,b≥3, 0<phi≤1; finite tests alone cannot prove that quantification.

## originality

PASS

PASS, qualified. Prior dynamic-monopoly/threshold-contagion work establishes threshold models and community initiation effects but not a labeled all-seed-set polynomial and exact sign classification under adding one edge. A published Resultary zero-forcing polynomial concerns the same underlying barbell graph but a different forcing rule, and complete multipartite k-conversion deals with different topology. Exact-model queries did not find dominating coverage, though unindexed exact barbell threshold enumeration remains a risk.

## value

PASS

PASS — A complete coefficientwise law for all initial sets across all clique sizes and all positive fractions shows how adding a single natural social bridge can increase, preserve or decrease ultimate adoption. This is a motivated exact structural enumeration with a sharp one-seed threshold and one uniquely lost configuration, not simply a textbook monotonicity observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
