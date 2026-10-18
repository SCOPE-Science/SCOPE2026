# Scientific review

## Correctness — PASS

Every connected simple cubic graph on six vertices is isomorphic to either \(K_{3,3}\) or the triangular prism, because the complement is a simple 2-regular graph with six vertices, hence either one 6-cycle or two 3-cycles. Exhaustive enumeration of all \(512\) edge states for each graph and all six roots supplies exact integer counts for each rooted cluster size. Two independent connectivity implementations agree in all \(6144\) rooted states. The ensuing polynomial identities establish the three strictly positive tail differences, the mean difference and the degree-12 variance factor. Transforming the latter by \(t=p/(1-p)\) yields 13 coefficients with exactly one sign change, so Descartes' rule together with its opposite endpoint signs proves a unique variance crossing in \(0<p<1\). The complete labeled six-vertex cubic census independently confirms the two possible isomorphism classes.

The proof is exhaustive only for this finite graph class. The one-crossing statement for the continuous transmissibility parameter is proved algebraically, not inferred from a numerical grid. Exact rational evaluations bracket the root and check a representative reversal.

## Originality — PASS (best-knowledge assessment)

The closest identified full-text source, Miller's 2008 open preprint *Spread of infectious diseases through clustered populations* (arXiv:0806.2888), investigates clustered epidemic networks and their growth, probability and size, without the specific six-vertex two-graph exact rooted component comparisons or variance polynomial. Newman's 2003 random clustered-network model addresses giant-component and epidemic-size behavior, not the six-vertex exact stochastic order. Gleeson, Melnik and Hackett's 2009 preprint considers bond-percolation thresholds in clustered random networks. House, Ross and Sirl study methods for outbreak final-size calculations but the accessible abstract does not establish this sharp comparison. Previously published three-point-connectivity covariance formulas concern whole-network component and triangle statistics, not this rooted outbreak variance reversal.

The novel mathematical assertion assessed here is the **joint** complete first-possible cubic contact-class classification, strict all-parameter first-order stochastic dominance, and the unique opposite variance ordering at high transmissibility. A general recipe for enumerating component probabilities is not asserted as new. Related literature available only in abstract form creates residual bibliographic uncertainty; independent verification remains warranted.

## Mathematical value — PASS

The theorem isolates clustering while matching all degrees and edges, settles the complete smallest nontrivial cubic contact-network class, and demonstrates a nontrivial limitation of using mean outbreak burden as a surrogate for outbreak uncertainty: the graph with uniformly smaller outbreak-size distribution can have **larger variance** above a unique transmissibility threshold. The exact crossover has an all-parameter proof and a reproducible complete finite census rather than an arbitrary point estimate. This structural boundary is motivated by clustered-contact epidemic modeling and tests a meaningful comparison of entire outbreak laws.

## Closest sources and limitations

Miller (2008/2009, arXiv:0806.2888), Newman (2003, doi:10.1103/PhysRevE.68.026121), Gleeson–Melnik–Hackett (2009/2010, arXiv:0912.4204), and House–Ross–Sirl (2012/2013, doi:10.1098/rspa.2012.0436) provide context. Some were inspected only through abstracts, so equivalence elsewhere is not ruled out conclusively. The modeled six-person network is idealized, without heterogeneous transmission or dependent edge outcomes.

Self-review: passed. Independent audit: not yet performed.
