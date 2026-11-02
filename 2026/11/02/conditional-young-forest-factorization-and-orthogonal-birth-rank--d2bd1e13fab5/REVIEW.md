# Scientific review

## Correctness: PASS

For every label and size, conditioning on the exact younger forest leaves independent, uniform choices in the finite old-label set for each component root. The component-sum law follows without treating component sizes as independent. Taking its conditional expectation and using measurability of all later subtree sizes establishes one-way conditional mean independence and zero pairwise covariance. A separate two-color Pólya urn calculation establishes the beta-binomial marginals and their exact variances. Double counting ancestors and the diagonal covariance then proves the all-weight variance formula. Empty components, the deterministic root and terminal vertex, and the nonindependence example have been checked. Exact enumeration of 5,913 trees and 9,326 assertions is supporting finite evidence, not the infinite proof.

## Originality: PASS (qualified)

The first-public 2014 Holmgren–Janson preprint with primary MSC 60C05 studies aggregated fringe-subtree counts and asymptotic distributions, not the finite birth-ranked young-forest conditional generating function. Grübel–Michailow's 2014 boundary representation and Dobrow–Fill's 1999 path-length decomposition provide important background, but the material read does not state a conditional law against the *entire* younger forest or its all-weight orthogonal-variance consequence. Fuchs studies global subtree-size frequencies. Searches of published research records for labeled descendant orthogonality, younger-forest conditional laws, weighted path variances, and aliases found closest claims about root attachment/path length and root degree/leaves, rather than coverage. Earlier mathematical claim texts showed a different two-vertex fringe/path-length dependence formula but not this result. The classical unweighted total-path-length variance and ordinary urn moments are treated as known; they are not asserted novel. Historical priority outside these sources remains uncertain, especially implicit martingale or recursive-forest formulations.

## Mathematical value: PASS

The exact conditional polynomial factorization is stronger than marginal mean/variance identities: it describes the full distribution after observing the entire younger forest. It yields mean independence against any measurable statistic of the whole younger subtree-size vector, but also sharply distinguishes this from genuine independence. The resulting exact *diagonal covariance matrix* for all labels supplies variances for an arbitrary family of birth-weighted ancestor costs without mixed terms, a naturally motivated statistic in recursive-tree path analysis. This is an all-parameter structural dependence theorem, not a small numerical increment or a recomputation of only total path length.

## Closest literature and limitations

- Holmgren and Janson, arXiv:1406.6883, primary MSC 60C05, submitted 2014-06-26: complete available text, aggregated size/type fringe-count asymptotics.
- Grübel and Michailow, arXiv:1406.7614, submitted 2014-06-30: full available text, boundary theory and path-length/subtree-mass representation.
- Dobrow and Fill, DOI 10.1017/S0963548399003855: full legally accessible 17-page text, classical total path length and subtree rooted at 2; not a birth-weight conditional forest PGF.
- Fuchs, DOI 10.1017/S0963548308009243: author full text, global fringe-size count approximations.

Residual risk is implicit equivalence in older random recursive tree, urn or martingale literature. This work does not establish priority absolutely, independence of the subtree sizes, or validity beyond uniform parent selection. A separate independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
