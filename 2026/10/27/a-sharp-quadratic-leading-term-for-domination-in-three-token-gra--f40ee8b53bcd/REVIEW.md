# Scientific assessment

## Correctness (PASS)

The claim has precise quantifiers \(n\ge4\), finite simple base graphs, closed-neighbourhood domination and a specific three-token adjacency convention. For any dominating set, every unselected layer-zero triple has a selected layer-one neighbour and therefore contains a pair in the projected family; selected layer-zero triples each add at most one pair. The complement of the projected family is triangle-free, so the proved Mantel bound gives the lower inequality. The explicit upper witness has exactly \(\binom n2-\lfloor n^2/4\rfloor+n-2\) members; all three token layers are covered by a separately checked adjacency argument. Direct finite verification agrees for \(4\le n\le18\). The limit follows by squeezing, not extrapolation from experiments.

## Originality (PASS, subject to historical priority)

The strongest close comparison is arXiv:2610.28936, Theorem 1.2, which supplies an order-\(n^2\) lower bound with leading constant \(1/12\) and order-\(n^3\) upper bound for this parameter family. The new statement supplies a common leading constant \(1/4\) and an explicit \(O(n)\) gap. The 2025 initiating source treats stars and complete graphs rather than the bipartite three-token instance; its Mantel argument for complete graphs is acknowledged. The earlier complete-bipartite token paper concerns automorphism groups. Literature and mathematical-research database searches did not uncover an equivalent or stronger statement, but absence from searches does not establish global novelty.

## Value (PASS)

The 2025--2026 token-domination literature leaves the higher-token complete-bipartite family with wide general-purpose bounds. Determining the sharp leading asymptotic coefficient on the first non-star bipartite subfamily replaces a cubic-order generic upper estimate with quadratic growth and improves the lower leading coefficient by a factor of three. The construction and combinatorial projection are reusable techniques; the remaining linear gap poses a concrete, naturally motivated next problem. This is more than substituting parameters into the cited inequalities.

## Closest literature and limitations

Primary comparisons: Fabila-Monroy--Gómez-Galicia, arXiv:2509.16448 (2025), sections 3--4; Chinman--Cortijo--Pedroni--Seong--Stenger, arXiv:2610.28936 (2026), sections 1, 2, and 5; Fabila-Monroy--Trujillo-Negrete, arXiv:2302.07914 (2023), sections 1 and 3. The theorem is an asymptotic law with an explicit additive window, not an all-\(n\) exact formula. Bibliographic priority and independent validation are unperformed.

Self-review: passed. Independent audit: not yet performed.
