# Self-review

## Correctness

**PASS.** For all integers \(m\ge3\), \(\ell\ge1\) and real \(t,B>0\), an exact cut-edge resistance decomposition reduces the full Kirchhoff index to the three-class strictly convex objective. The two regimes solve the complete KKT system, including the inactive inner-clique conductance at equality. Strict convexity of \(\operatorname{tr}(L+J)^{-1}\) on the connected domain, together with injectivity of the edge-to-Laplacian map, rules out all asymmetric alternative optima. The long-tail limit follows from a \(\pi/8\) beta integral. The embedded `verify.py` runs 7,437 finite checks of the formulas and full matrices. Numerical checks are not the infinite proof.

## Originality

**PASS with residual risk.** Full primary material inspected: Ghosh–Boyd–Saberi (2006) §V solves an *equal-price symmetric barbell*, not a clique joined to an arbitrarily long path with a variable relative inner-clique cost; Yang (2014) §2.2 treats the *unweighted extremal graph* with prescribed clique number, not conductor allocation; Bianchi et al. (2016) §2 studies an *alternative degree-weighted index* on a fixed lollipop. Neither their theorems nor the located mathematical-record summaries give the claimed explicit unique optimizer, threshold, and long-path budget exponent. An unindexed equivalent specialization is possible; completeness of the literature cannot be certified.

## Value

**PASS.** Lollipop graphs are natural bottleneck and commute-time extremizers, so a resource-allocation rule separating their expensive dense-core edges from their essential path is motivated independently of the computation. The exact threshold \(t_*>2\), forced complete deletion at/above it, and \(\ell^{-3/2}\) optimal core-budget scaling quantify a structural support change and severe allocation imbalance. This is a natural all-order classification for two geometric sizes and a real cost parameter, not a single small example, cosmetic bound, or renamed standard tree-only formula.

## Relationship and scientific limitations

The convex formulation, symmetry averaging, and cut-edge identities are classical. This claim does not include arbitrary edgewise prices, multiple pendant paths, or simultaneous large-size limits. The main residual risk is equivalent treatment within less searchable network-design literature; the cited closest primary work has different hypotheses and conclusions.

Self-review: passed. Independent audit: not yet performed.
