# Scientific review: folded-five-cube induced-forest topology

## Correctness — PASS

The graph is specified by sixteen vertices and five bitwise-XOR connections. Two independent cycle/forest predicates agree on all 65,536 vertex subsets, giving 13,839 valid faces. The explicit pivot matching has 6,908 pairs and its complete 77,632-incidence directed Hasse graph is acyclic. The only unmatched simplices in the augmented matching are nineteen five-cells and four six-cells. The exact signed gradient-path boundary matrix has a four-by-four minor of determinant 1, which proves a primitive rank-four boundary map. Removing the matched empty/vertex pair produces a CW complex with a single zero-cell, nineteen five-cells and four six-cells. The four primitive degree vectors may be canceled, yielding fifteen five-spheres integrally. Independently computed mod-two boundary ranks match the result. The equivariant Lefschetz trace is checked for every one of the 1,920 automorphisms against the sign-twisted augmentation character; the proposed five-plus-ten rational decomposition follows from translation eigenspaces and the two five-label permutation orbits.

The proof relies on finite exhaustive checks whose complete definitions and code are supplied, rather than on an unaudited output table alone. The matching-check and integer-boundary certificate are critical; merely computing field homology would not establish the claimed homotopy equivalence. No general statement about larger folded cubes is inferred.

## Originality — PASS, with qualified risk

The closest directly relevant foundational source is Taylan, arXiv:1501.06754 (2015), which defines general devoid complexes and works out other host graph families. Carnero Bravo, arXiv:2307.13271 (2023), explicitly treats induced-forest complexes but its published examples and general results do not include the Clebsch graph. The accessible PDF texts were inspected at their introductions, family-classification sections and relevant theorem statements, including terminology checks for Clebsch, cube and folded-cube aliases. The best-matching indexed published records establish Clebsch independence or neighborhood complexes, which have strictly different face conditions; they do not imply the present forest-complex homotopy or its complete rational character. The exact search classes also included folded-five-cube aliases, acyclic vertex subsets, forest filtration, stronger general graph-family theorems, and representation descriptions.

Residual risk: unindexed equivalent work, or results in inaccessible complete indexed documents, cannot be ruled out by unsuccessful searches. The degree-five Clebsch naming convention is essential because some sources use the name for its complement. These limits are not treated as independent originality certification.

## Value — PASS

The object is the induced-forest endpoint of a published graph-topology filtration and is motivated by feedback-vertex-set theory. The five-regular Clebsch graph is the smallest familiar folded odd cube beyond the trivial cases and a canonical strongly regular example with a large full automorphism group. A complete integral wedge classification of its nonpure eight-dimensional complex and identification of a nontrivial five-plus-ten rational representation provide structural data beyond the existing independence and neighborhood-complex calculations. The precise dimensions are not arbitrary truncation parameters, and their representation-theoretic meaning supplies a natural reason to determine this exact finite invariant.

## Closest literature and limits

Taylan (2015), Carnero Bravo (2023), and the indexed Clebsch independence/neighborhood results are the closest inspected comparisons. No theorem for arbitrary folded cubes or integral representation lattice is claimed. The full indexed repository files could not be inspected; relevant source descriptions were distinguished from complete full-text inspection. An independent audit has not occurred.

Self-review: passed. Independent audit: not yet performed.
