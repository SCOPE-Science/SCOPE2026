# Independent mathematical audit

## correctness

PASS

The undirected degree-one leaf count of the initial-edge uniform recursive tree has exact Markov update k to k+1-B with B conditional Bernoulli(k/m). Induction from L2=2 and deterministic L3=2 gives mu_m=m/2+1/(m-1) and v_m=m/12-1/(m-1)^2 for m>=3 (v2=0 exceptional). Conditional on the common prefix T_t, the two futures are independent and E[L_n|T_t]=n/2+(t-1)(L_t-t/2)/(n-1); total covariance gives the exact t>=4 rational expression and t<=3 independence (the law depends only on deterministic L_t). Synchronous coupling k->k+1-1{U<=k/m} is monotone even across adjacent k, giving all increasing-transform covariance inequalities. Bounded martingale increments with m/(n-1) weights, predictable quadratic variation and Lindeberg give the joint normal with correlation (t/n)^3; Gaussian orthant formula gives limiting arcsin expression, also at alpha=0,1. Independent rational n=9 checks gave mu=37/8, variance 47/64 and exact covariances for all t. These finite checks alone do not prove CLT.

## originality

PASS

Shared-prefix uniformly growing graphs were introduced by Rácz–Sridhar, but their examined full paper emphasizes whole-graph correlation/detection and structural statistics; it does not supply these explicit two-leaf-count formulas in the inspected sections. Bäumler et al analyze per-step-correlated rather than common-prefix trees, so their bivariate leaf CLT does not imply the same covariance under a changed coupling without derivation. Marginal recursive-tree leaf CLTs are prior art; the new claim is the coupled exact covariance, association, and cubic Gaussian memory law. Best-of-knowledge PASS with risk of implicit older joint generating-function formulas and inaccessible Bäumler full text.

## value

PASS

Leaf counts are a natural, low-dimensional summary of random growing trees. Exact independence for prefix at most three, strict positive association thereafter and macroscopic alpha^3 dependence quantify which aspects of shared history are observable even when trees themselves remain dependent. The result clarifies a structural asymptotic signal and avoids overclaiming a full graph-detection threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
