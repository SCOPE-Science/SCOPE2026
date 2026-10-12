# Review of Maximal double Roman domination of cocktail party graphs

## Correctness
PASS. In \(CP_n\), every vertex has exactly one nonneighbor, so any vertex set of size at least two dominates the graph. Thus maximality forces the zero set to have size at most one. A zero-free function of weight at most \(2n+1\) has only one possible label-\(2\) vertex and no label \(3\); its partner is then an undefended label-\(1\) vertex. With one zero, the positive baseline has weight \(2n-1\) and defending the zero costs at least two additional units, proving the lower bound \(2n+1\). Equality with one label \(3\) fails at the label-\(1\) partner of that vertex, so every optimum has exactly two label-\(2\) vertices, both outside the zero vertex's partner pair. The converse is immediate from the unique-nonneighbor structure. Exhaustive direct verification of \(1{,}118{,}464\) labelings for \(2\le n\le5\) matches the full optimizer family.

## Originality
PASS. The foundational maximal-double-Roman paper was inspected in searchable full text. It develops complexity, general bounds and relationships, trees, paths, and cycles; its special-graphs section states that scope explicitly, and targeted full-text searches found no cocktail-party or complete-multipartite occurrence. The 2023 double-Roman survey summarizes the same maximal-variant scope. Exact and semantic searches under cocktail-party, perfect-matching-deletion, and complete-multipartite aliases found no equivalent value or minimum-function classification. Nearby complete-multipartite results concern ordinary Roman, Roman \(\{2\}\), restrained Roman, and other non-equivalent variants.

## Value
PASS. Cocktail party graphs are a canonical dense symmetric family, simultaneously viewed as complete graphs minus a perfect matching and as complete multipartite graphs with all parts of size two. The result completely resolves both the parameter and every optimum. The proof isolates how the maximality requirement interacts with the unique-nonneighbor geometry: the zero set collapses to a singleton and exactly two defenders remain. The closed count \(2n(n-1)(2n-3)\) is structural information beyond a scalar formula.

Self-review: passed. Independent audit: not yet performed.
