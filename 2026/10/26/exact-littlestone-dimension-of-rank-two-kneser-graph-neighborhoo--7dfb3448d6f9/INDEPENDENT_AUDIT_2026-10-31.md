# Independent mathematical audit

## correctness

PASS

For intersection labels (complement of disjointness) maintain marked S. False-disjoint predictions introduce a new true target element, at most twice; false-overlap predictions remove a marked non-target, also at most twice; hence universal mistake bound 4. Small n branch-size bound using C(n−2,2) disjoint target pairs rules out depth n−2. The pinned certificate gives full trees with 2,4,8,16 realized terminal paths for n4–7; independent memoized shattering-tree search recovered these depths and verifies small upper bounds. A depth4 tree on [7] embeds in every n>7.

## originality

PASS

Adler–Benediktsson–Macpherson 2020 determine nonadaptive VC bounds and VC density for Johnson/Hamming graphs; at rank2 Johnson adjacency is one-point intersection while Kneser adjacency is disjointness. Complementing a predicate does not equate VC and adaptive Littlestone dimension. Other general Littlestone literature explains the mistake-bound invariant without giving this exact all-n transition. No direct existing formula found via Resultary semantic search. A possibly unindexed online learning sparse-disjunction theorem may imply it and is retained as risk.

## value

PASS

The exact adaptive mistake bound for a natural finite graph neighborhood concept class is a meaningful online-learning invariant and demonstrably differs from merely tabulating ordinary VC-dimension; both the sharp finite n cutoff and explicit realizable full trees are provided.

The dated certificate retains the supplied scientific assessment, sources and limitations.
