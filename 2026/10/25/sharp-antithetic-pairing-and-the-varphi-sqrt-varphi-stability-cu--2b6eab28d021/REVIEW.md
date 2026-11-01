# Independent mathematical audit

## correctness

PASS

PASS for the stated iid-across-iterations two-component, equal-step, planar bilinear model. With J²=-I, the one-step product is ((1-eta²uv)I-eta v J); its squared norm has no cross term. Averaging the complete 2-by-2 fixed-uniform-marginal coupling matrix gives affine q(theta), so a linear objective selects endpoint coupling except at eta²=2/(a+b)². Exact polynomial factorization P(r)/r²=(r+1/r)²-2(r+1/r)-4 orders the three stability thresholds, yielding iff 1<r<phi+sqrt(phi), plus strict rational witness at a=1,b=2,eta=3/5: 751/625,109/100,1223/1250. Independently recomputed 36 rational parameter/coupling checks; these checks alone are not an all-parameter proof.

## originality

PASS

Best-of-knowledge PASS for exact optimization over within-iteration joint laws with fixed uniform marginals, the antithetic-only stability interval and phi+sqrt(phi) heterogeneity cutoff; earlier work has conventional same-sample/independent-sample stochastic extragradient analyses but does not in inspected material establish this pair-law optimization. Qualify because newer Yoon-Loizou full text was not accessible.

## value

PASS

PASS. The bounded but natural optimal-coupling question distinguishes two conventional two-oracle stochastic extragradient schemes from a third equally costly coupling. A sharp explicit threshold and rational strict-separation witness are informative about sampling correlation and mean-square stability rather than mere normalization or a textbook sign check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
