# Scientific review: exact retraction-product rank transfer

## Correctness

**PASS.** Every idempotent self-map fixes its image. Partitioning possible second-factor images by their size and their overlap with a specified first-factor image gives a disjoint count: an inclusion–exclusion occupancy number for the remaining image targets, multiplied by the number of unrestricted outside assignments. This proves every coefficient of the integer transition kernel, including the zero/empty boundary cases. Conditional on the composite's image, a fresh uniformly sampled idempotent has a rank distribution depending only on image cardinality, giving the exact Markov law for every product length. Strictly nested injectivity constraints force the transient diagonal eigenvalues to be distinct, with the rank-two eigenvalue dominant. A positive path from the initial rank to two supplies the matching lower bound, while the triangular spectral argument supplies the upper bound. Independent direct-function enumeration checks all transition coefficients through six points and all two-step product counts through four points. Tests do not substitute for the proof.

## Originality

**PASS relative to inspected sources, with residual risk.** Araújo–Bentz–Cameron (arXiv:1910.08335; introduction and Section 3) prove structural strong-factorization properties, rather than exact random-idempotent product-rank counts. Sarkar–Singh (arXiv:2106.08063; introduction and Section 3) establish unit-regularity conditions, not iterated rank probabilities. Bugay (DOI:10.12958/adm2223; Section 2, Proposition 3 and Theorem 4) studies quasi-idempotents, Green classes and generating ranks; its cited criterion for preservation of rank by a product is qualitative and does not imply the finite occupancy kernel. The product-factorization context and unrestricted random-map composition problem are prior mathematics, not claims here. An equivalent pre-existing rank transition kernel under occupancy, random-mapping, automata or Green-relation terminology cannot be ruled out from the available coverage.

## Value

**PASS.** The full transformation monoid is a foundational finite semigroup, and idempotent factors are central to its generation and factorization. The result gives an exact, all-length multiplication statistic rather than a single example: every product-image rank probability, the finite-time synchronization law, its sharp exponential tail and exact expected stopping time. It also identifies the first loss of symmetry between ordered factor-rank distributions at four points, a concrete manifestation of noncommutative multiplication. These are natural invariants of the idempotent-product process and are not a parameter-renaming or isolated unmotivated census.

## Closest sources and limits

The quantitative rank kernel is not stated in the inspected 2019, 2021 or 2024 sources. The result addresses independent uniform idempotent total maps only, fixes the ground-set size in the tail asymptotic, and counts image cardinality rather than output-map isomorphism classes. Older combinatorial probability treatments could contain an equivalent formula, so independent prior-art assessment remains important.

Self-review: passed. Independent audit: not yet performed.
