# Independent mathematical audit

## correctness

PASS

Read exact RESULT.md at assigned source and verify layer cake/coarea proof: translation by c gives support h_K(u)=1/2 sum_{ij}w_ij|u_i-u_j| on mean-zero H; central symmetry averages any inscribed ball center back to zero. Each u in H integrates centered superlevel indicators v_S, whose norms are sqrt(|S|(n-|S|)/n). Discrete coarea plus triangle inequality yields TV(u)>=min_S [w(dS)/||v_S||] ||u||; u=v_S for a minimizing cut attains equality. Connectivity and positive edges make intrinsic dimension n-1, so formula is exact in all dimensions. Independently checked sample weighted P4/K4 cut and integer vector bounds; source verify.py exact finite n=2..5 is corroboration only.

## originality

PASS

Best-of-knowledge mathematical comparison of the complete statement and stronger potential prior claims: Their published polytope/combinatorial and graph-Cheeger statements are not strong enough to yield the claimed normalized metric invariant as a corollary; proof uses their objects but different quantity.

## value

PASS

Natural Euclidean radius of a standard combinatorial polytope identified exactly with a normalized cardinality-cut expansion invariant across arbitrary weighted connected graphs; bridges convex width and graph total variation. This is more than renaming a constant because the intrinsic Chebyshev-ball identification and equality/center are proved, and the graph cut formula is independently usable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
