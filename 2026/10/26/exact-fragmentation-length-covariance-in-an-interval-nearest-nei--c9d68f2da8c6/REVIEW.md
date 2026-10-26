# Self-review

## Correctness — PASS

The statement specifies the uniform sample law and undirected edge counting. Removing exactly the strictly local-maximum interior gaps gives the component count and edge length. Normalized independent exponentials yield the correct joint gap law, and the independent exponential sum permits covariance transfer. Independent rank calculations give on-site 11/27, adjacent -11/54, and distance-two 139/5400. Their finite-range sum gives the rational formula at all sample sizes, including \(n=2,3,4\). Exact rational computations using a standalone verifier reproduce the two-apart moment 413/1800 and the graph-covariance values for \(n=2\) through \(n=9\). Computation alone would not prove the infinite-family claim; the local-dependence argument does.

## Originality — PASS, subject to historical-priority risk

Penrose–Wade (2006, arXiv:math/0603561v1), notably Theorem 2.3 and Sections 4.2 and 5, analyze directed nearest-neighbor graph total length and use Dirichlet spacings, but do not give a closed exact finite-sample covariance between undirected distinct-edge length and connected-component count. Baryshnikov–Yukich (2004) develop limiting covariance functionals for geometric graph scores without evaluating this particular mixed moment. The accessible abstract of Sadasiv–Meng (2001) addresses nearest-neighbor cluster sizes, but the full text was inaccessible; that priority risk remains. Published general techniques are essential background, not themselves the present evaluated cross-covariance. Search noncoverage does not establish uniqueness.

## Mathematical value — PASS

Total distinct-edge length measures geometric network cost, while component count measures failure of global connectivity. Their explicit covariance gives a quantitative tradeoff invisible to the separate first moments. The strictly negative dependence holds for all \(n\ge4\) and persists on an order-one scale as n grows. The nonzero limiting constant and exact small-sample boundary distinguish the result from a routine expectation calculation. Unlike directed-length statistics, the undirected graph's total length must account for mutual selections only once.

## Limitations and closest sources

This result applies only to the one-dimensional uniform, undirected, distinct-edge model. The full text of the closely relevant 2001 cluster-size paper could not be inspected, so independent priority assessment remains necessary. The exact rational checks cover only \(n\le9\). Relevant primary sources are Penrose–Wade (arXiv:math/0603561v1), Baryshnikov–Yukich (2004), and Sadasiv–Meng (doi:10.1103/PhysRevE.63.027101).

Self-review: passed. Independent audit: not yet performed.
