# Scientific review

## Correctness

PASS. The explicit rim/spoke parametrization proves that each feasible vertex-parity fibre has exactly \(2^m\) orientations. Every directed cycle in a wheel is either the consistently oriented rim or contains a directed triangle, as proved by following the spoke-direction switch along a directed hub-to-hub rim path. The four-state transfer entries implement exactly those triangle exclusions, and the correction removes precisely the two possible directed-rim cases when the prescribed parity vector is constant. The separate parity cases supply acyclic constructions, while source/sink parity rules exclude exactly the two constant signatures for odd rim size. A separately implemented direct-graph enumerator tests all cases for rim sizes 3 through 8. Finite checks are secondary evidence, not an infinite proof.

## Originality

PASS on the accessible comparisons, with a remaining priority risk. The strongest nearby source by Gravier, Petiteau and Sivignon (arXiv:2603.09475, March 2026) studies feasibility and necessary parity/source/sink constraints and provides constructions for grids, cylinders and tori; its inspected principal claims and searchable full text do not give the wheel fibre enumerator. Mühlherr and Poullot (arXiv:2609.02249, September 2026) study edge-disagreement acyclic polynomials and wheel Hamiltonicity, not prescribed indegree parity. Stanley's classical chromatic-polynomial evaluation gives the sum of all fibre counts, but not their individual multiplicities. Searches of mathematical records and available research claims found no dominating formula. An unindexed equivalence remains possible; independent priority determination has not occurred.

## Value

PASS. The result computes the **entire labelled parity-fibre profile**, rather than only the existence of an acyclic orientation or the unrefined total number of acyclic orientations. The size-four transfer is uniform over infinitely many wheels, with a linear number of arithmetic operations per signature. The exact parity-dependent existence obstruction and the two-realization boundary cases give structural information that is not obtainable from the total count alone. This is a natural refinement of a contemporary orientation-feasibility problem, not an arbitrarily selected finite statistic.

## Scientific scope and residual risk

The proof treats all simple wheels with at least three rim vertices. Its time bound is in arithmetic operations. Existing parity-obstruction theory may subsume the existence part of the theorem but not the verified multiplicity formula; further unindexed literature may affect priority. Independent mathematical audit and independent bibliographic determination remain unperformed.

Self-review: passed. Independent audit: not yet performed.
