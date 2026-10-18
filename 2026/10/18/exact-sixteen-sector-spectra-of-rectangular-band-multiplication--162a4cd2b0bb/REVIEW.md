# Review of the rectangular-band spectral classification

## Correctness (PASS)

The exact adjacency identity follows from inclusion–exclusion on three equality relations, with the two-fold first/second intersection and triple intersection both equal to the identity. Tensor decomposition into constant and zero-sum coordinate spaces supplies all eigenvalues with their true dimensions, rather than merely a list of candidate eigenvalues. Connectedness follows by explicit paths inside first-coordinate and second-coordinate fibers. For the four-element rectangular band, an explicit five-generator Cayley presentation establishes the folded-cube and common-neighbor claims. The attached standard-library verifier checks every eigenvector identity in an integral basis for sixteen finite configurations; no extrapolation from finite checks is needed for the general proof. Limits: the result is restricted to rectangular bands and undirected exactly-one-coordinate adjacency.

## Originality (PASS, subject to bibliographic limits)

The nearest literature is Sorouhesh–Golriz–Panbehkar arXiv:2511.23190, whose v1 Proposition 5.3 and v2 Proposition 5.3 establish **regularity** for rectangular bands. V2 Lemma 5.4 suggests a qualitative block description, but no multiplicity-resolved rectangular-band eigenvalue formula appears in Sections 5–6 or Appendices A–B. V2 Section 6's explicit spectral computation concerns **null semigroups**, not rectangular bands. The matrix formula here describes all cross-fiber edges and proves connectedness in the two-sided nontrivial regime. Searches on exact graph names, factor parameters, folded-cube equivalence, semigroup-band spectra and published mathematical-record summaries found no equivalent. An unindexed or differently named graph representation could still subsume the result; no bibliographic uniqueness is certified.

## Value (PASS)

The exact spectrum simultaneously gives the graph energy and spanning-tree number for an unbounded two-parameter semigroup family. It distinguishes the connected regime from disjoint clique boundaries, connects the four-element rectangular band with the Clebsch graph, and clarifies that a fixed-left-coordinate block partition cannot disconnect the nontrivial rectangular-band graph. This addresses an explicit graph-family spectral problem beyond the existing regularity-only theorem. The degree-based reconstruction of factor sizes is credited as an elementary consequence of earlier methods rather than advertised as independent novelty.

Self-review: passed. Independent audit: not yet performed.
