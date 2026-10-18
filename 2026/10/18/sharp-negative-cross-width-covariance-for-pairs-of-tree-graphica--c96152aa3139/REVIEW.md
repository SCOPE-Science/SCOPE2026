# Self-review

## Correctness: PASS

The claim is the full sharp covariance minimum over *pairs* of labelled spanning trees, not a one-tree variance result. A Gaussian radial/spherical decomposition gives the exact spherical mean and mixed moment; the three cases of a pair of root segments yield constants for identical, adjacent, and disjoint edges. The incidence count \(s=\sum_v\deg_T(v)\deg_S(v)\) and shared-edge count \(c\) give the claimed covariance after subtracting the product of means. For trees, \(s=3n-4+\sum_v(\deg_T(v)-1)(\deg_S(v)-1)\). Both nonconstant coefficients are strictly positive, making the two equality conditions necessary as well as sufficient. An explicit seed and attachments achieve them for every order. Chi-radius asymptotics prove the stated strictly negative limiting infimum.

Exact Prüfer enumeration examines every one of the 1,695,497 ordered tree pairs of orders four, five and six. Direct support-function and Gaussian-sphere experiments provide separate diagnostic checks. The latter do not prove the arbitrary-order theorem; the proof is analytic.

## Originality: PASS (qualified)

The closest previously published mathematical record, *Sharp width-variance extremizers among tree graphical zonotopes*, proves the same bivariate absolute-Gaussian segment kernel and the path/star extrema for one-tree width variance. Those ingredients are prior mathematics, expressly not novelty claims. Unlike that result, the present theorem solves a two-tree optimization with a precise edge-disjoint/nonleaf-disjoint equality class, and a nonzero negative limiting covariance. The full published record was inspected. Padrol–Pilaud–Poullot and Grujić supply the graphical-zonotope construction and cubical tree setting; their accessible full texts do not state this covariance minimum. The remaining bibliographic risk is that prior mixed-zonotope or Gaussian graph-variation literature contains the same coupled extremum under another formulation. A literature search cannot prove uniqueness.

## Mathematical value: PASS

The theorem resolves a motivated two-polytope geometric invariant: the smallest covariance of widths under a shared uniformly random Euclidean direction, over all pairs of canonical tree zonotopes on a common labelled set. Every individual tree zonotope is cubical with the same Euclidean intrinsic volume and mean width, yet the pair covariance has a negative sharp infimum persisting as the order grows. The equality class gives structural geometric information not contained in the one-body variance extrema.

## Scope and limitations

The classification covers all unweighted labelled spanning-tree pairs and common spherical directions. It does not classify Pearson correlations, stochastic ordering or arbitrarily weighted zonotopes. The novel conclusion relies on, and explicitly credits, known bivariate Gaussian angular identities. No independent mathematical audit has taken place.

Self-review: passed. Independent audit: not yet performed.
