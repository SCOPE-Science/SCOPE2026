# Scientific assessment

## Correctness — PASS

For an unselected edge \(uv\), perfect edge domination is equivalent to \(\deg_F(u)+\deg_F(v)=1\). The degree trichotomy is exhaustive. Every yellow–yellow selected edge contradicts a coordinate square; every black–black selected edge forces all vertices black by square propagation and connectivity. Consequently each nontrivial PEDS alternates the yellow vertices with black/white vertices along the cube's parity partition. Each yellow vertex has exactly one black neighbor, forcing \(d\lvert B\rvert=2^{d-1}\), and hence \(d\) a power of two. The syndrome-code construction gives an exact converse, and counting each selected black–yellow edge from its yellow end fixes the minimum size. The standalone verifier checks all PEDS candidates in dimensions two and three and code configurations in dimension four, and constructs valid sets in dimensions two, four and eight. Finite tests do not substitute for the unrestricted square argument.

## Originality — PASS, with specified risks

The closest full-text primary source is Lin–Lozin–Moyano–Szwarcfiter (2017): its page-four black/yellow/white characterization applies to arbitrary graphs, but it does not supply the cube-specific parity rigidity or the divisibility condition and converse construction. The recent Grippo–Lin–Moyano–Vera (2026) paper studies extremal counting on trees, forests and chordal graphs and algorithms on generalized series-parallel and chordal graphs, not this cube-classification theorem in its accessible abstract. Do Forte–Hanafi–Lucena (2023) studies integer-programming formulations with possible finite hypercube computational comparisons; the restricted abstract does not establish the theorem. The 2022 neighborhood-star-free theory is triangle-based and does not cover triangle-free cubes. Dedicated record queries compared hypercube domination, efficient edge domination, codes and perfect edge domination, with no statement found that logically implies the power-of-two theorem. The full 2026 and 2023 manuscripts could not be inspected exhaustively, so a remaining priority risk is explicitly acknowledged, not concealed.

## Value — PASS

The existence of any nontrivial solution changes sharply at precisely the power-of-two dimensions. When existence fails, the only possible solution contains *every* edge; when it succeeds, the optimum abruptly drops to \(2^{d-1}\). The equivalence with one-sided perfect binary codes gives a structural characterization and a concrete construction, linking edge domination to coding theory on a natural, highly symmetric infinite graph family. It is neither a tiny finite-table increment nor a bare reformulation of the general three-coloring observation.

## Limits

The theorem does not enumerate all code solutions at high dimensions, and complete source-level priority is not certified where full text was inaccessible. Independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
