# Self-review

## Correctness: PASS

The quantified domain is \(n\ge2\), \(\alpha>0\), \(0<t<1\), and \(\varphi\in C^2([0,1])\) with positive curvature in the interior. Symmetric Dirichlet neutrality gives the conditional regression \(g(s)\), which is strictly convex. A size-biased beta comparison proves \(g(0)>\mathbb E F_\varphi\) without relying on the uniform-simplex translation available only at \(\alpha=1\); strict convexity gives the other endpoint inequality. A three-sign-interval argument for \(g-\mathbb E F_\varphi\), followed by tail integration, proves exactly one covariance zero and strict opposite signs on either side. Independent direct beta-tail integration and algebraic differentiation confirm the exact quadratic formula. The extracted verifier passed 4,156 exact rational comparisons. These finite cases corroborate, rather than replace, the analytical proof.

## Originality: PASS with residual historical risk

The closest preceding claim, *A universal one-switch covariance law for large spacings and convex spacing tests* (`8cec2684-e10a-4f25-bc74-47e4588a92c0`), proves the universal assertion for \(\alpha=1\) and already owns the special Greenwood threshold \(2/(n+2)\). It is neither reasserted as new nor an implication covering the entire \(\alpha>0\) family. Royen (arXiv:1008.4059, Sections 1, 4–6) gives marginal distributions and quantiles of the Dirichlet quadratic score but no joint threshold-count covariance. Hashorva (arXiv:1404.3304, Sections 1–3) concerns tail asymptotics of Dirichlet power aggregates, again not the finite exceedance-count dependence. Searches of general covariance, beta-tail, exceedance, Dirichlet, Greenwood and convex-score formulations did not reveal stronger published coverage. A standard beta Stein identity can simplify the explicit quadratic calculation, and implicit historical coverage remains possible; negative searches alone are not treated as proof of novelty.

## Value: PASS

The question is motivated by dependence between exceedance-count diagnostics and convex diversity/concentration scores for normalized gamma samples. The new statement applies to every symmetric Dirichlet shape, not merely the uniform-simplex case, and proves the existence and uniqueness of a covariance sign change simultaneously for an infinite class of convex scores. For the classical quadratic statistic the entire parameter-dependent phase boundary is explicit: \((\alpha+1)/(n\alpha+2)\), strictly shifting with concentration from \(1/2\) toward \(1/n\) when \(n>2\). This identifies a sharp finite-sample limitation of inferring global concentration from threshold counts and is not merely a numerical restatement of the marginal Greenwood distribution. It does not establish asymptotic power, stochastic dominance, or conclusions for asymmetric Dirichlet laws.

Self-review: passed. Independent audit: not yet performed.
