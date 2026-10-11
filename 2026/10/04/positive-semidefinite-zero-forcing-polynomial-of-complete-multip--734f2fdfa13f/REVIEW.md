# Independent mathematical audit

## correctness

PASS

The structural criterion follows exactly from the positive-semidefinite component rule. If all white vertices lie in one part, the white graph is independent and each white vertex is a singleton component, so forcing succeeds. If whites occupy at least two parts, the white graph is connected. A blue vertex in white-support part \(i\) has exactly \(|W|-w_i\) white neighbors, so an initial force exists precisely when all white vertices outside that part consist of one vertex and that part contains a blue vertex. Thus three or more white-support parts stall, while two parts succeed exactly under the displayed asymmetric one-white condition; one force then reduces to the one-part case. The generating polynomial counts these disjoint support cases with one inclusion-exclusion correction for the one-white/one-white overlap. Its least exponent is \(N-\max_i n_i\). The assigned verifier independently recomputes white components and exhausts every initial subset for all complete-multipartite types through order ten.

## originality

PASS

Peters proves only the scalar value \(Z_+(K_{n_1,\ldots,n_k})=n_2+\cdots+n_k\) for ordered part sizes and does not enumerate all positive-semidefinite zero-forcing sets. The audited result refines that number to an iff classification of every initial set and a complete size-generating polynomial. Current Resultary search surfaced ordinary zero-forcing polynomials and other complete-multipartite domination polynomials but no prior positive-semidefinite all-set polynomial.

## value

PASS

Positive-semidefinite zero forcing is an established minimum-rank invariant, and complete multipartite graphs are a canonical family. Classifying every forcing set and its cardinality distribution is a natural exact refinement of Peters's minimum theorem, useful for probabilistic and polynomial versions of forcing rather than a routine recomputation of the minimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
