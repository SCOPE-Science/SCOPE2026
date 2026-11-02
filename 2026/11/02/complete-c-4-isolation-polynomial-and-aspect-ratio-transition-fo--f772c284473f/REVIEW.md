# Mathematical assessment

## Correctness — PASS

The theorem is quantified over every integer \(2\le m\le n\). Four-cycles are non-induced. The residual-rectangle lemma is an if-and-only-if: the selected cells remove exactly their occupied rows and columns, and a surviving rectangle has a four-cycle precisely when both dimensions are at least two, or one dimension is one and the other is at least four. The occupancy polynomial uses two-level inclusion-exclusion, counting each set by its unique occupied row and column sets. The lower bound uses the number of surviving rows and columns; the five exact optimizer counts follow from explicit disjoint cases, with the square-board overlap subtracted once. The standalone verifier directly reconstructs four-cycles from adjacency rather than assuming the structural lemma. Exhaustive checks cover all subsets of the 13 specified boards through \(4\times5\), and algebraic comparisons of the five cases cover \(2\le m\le8\). Those finite tests are supporting evidence, not an infinite proof.

## Originality — PASS, with residual risk

The October 2023 square-isolation papers of Bartolo–Borg–Scicluna and Wei–Zhang–Zhao establish sharp universal *upper bounds* based on order and size, respectively, with equality families. They do not count all \(C_4\)-isolating subsets or classify minimum subsets in two-factor rook graphs. A full-text inspection of the former's definitions, main theorem, proof context and problems section, plus the latter's HTML introduction, theorem, proof and text searches, found no statement implying the row-column occupancy enumerator. Targeted searches for rook, lattice, Cartesian-product and line-graph equivalents found no matching result. Other known rook-graph results concern different parameters. In particular, a star-isolation spectrum based only on residual maximum degree cannot specialize to square isolation, because \(R_{1,3}\) and \(R_{2,2}\) both have maximum degree \(2\) but opposite four-cycle status. Reusing row-column occupancy machinery is not a claim that these different predicates are equivalent. An unindexed equivalent enumeration or unpublished manuscript is an unresolved priority risk; the review does not claim exhaustive novelty.

## Mathematical value — PASS

Square isolation is a motivated cycle-elimination invariant studied in the cited 2023 literature. The rook graph is a canonical structured but highly four-cycle-rich family. The result gives every cardinality coefficient, not merely a special case of a general order bound, and resolves a parameter-sensitive optimum counting question. The threshold at \(n=m+3\), the exceptional second family at equality, and the symmetry overlap on square boards explain how the geometry of four-cycle removal changes across aspect ratios. The exact optimizer counts are distinct natural combinatorial quantities, not arbitrary finite table entries.

## Limitations and closest sources

See arXiv:2310.09128 and arXiv:2310.17337. The result does not cover induced-cycle isolation, more than two product factors, or arbitrary graph families. Originality remains conditional on discoverable literature and independently checkable priority.

Self-review: passed. Independent audit: not yet performed.
