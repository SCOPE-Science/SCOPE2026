# Scientific review: saturation polynomial of two-row perfect hash families

## Correctness — PASS

For each distinct column interpreted as an edge of the labeled complete bipartite grid, a failing triple is exactly a three-edge path. The absence of such paths is equivalent to being a star forest. The proof exhausts all inclusion-maximal star forests by identifying (a) those using every vertex, and (b) the two mirror-image cases with isolated vertices confined to one bipartition class and every vertex opposite an isolate attached to a center of degree at least two. The two-sort exponential formula counts (a); associated Stirling set-partition numbers count (b). A two-star construction supplies the maximum coefficient and a constructive realization of every intervening size. Direct forbidden-triple enumeration for alphabet sizes three to five, independent in method from the star-component recurrence through size eight, agrees with every coefficient. No finite enumeration is used as a proof of the theorem's infinite quantifier.

## Originality — PASS, with residual risk

Walker and Colbourn (2007) supply the primary perfect-hash-family definitions and constructions. Shangguan and Ge (2016, arXiv:1601.04807v1, Theorems 1.5 and 1.7) already establish the optimal **maximum** \(2q-2\) for two-row strength-three families; that maximum is expressly **not** presented as novel. Aoudia, Nguyen, Mahjoub and Aïder (2014) study star forests in general graphs and their polytope, not this labeled maximal-family cardinality polynomial. Comparisons across the hash-family and star-forest formulations found no previous explicit classification of *all inclusion-maximal* families or coefficient counts, although inaccessible or unindexed equivalent counts remain possible.

## Value — PASS

Inclusion-maximality models terminal outcomes of constructing a perfect hash family by successive legal column additions, without prescribing the insertion order. The all-alphabet enumerator gives the complete distribution of attainable terminal sizes, proves that no intermediate sizes are missing, and quantifies a sharp worst-case factor approaching one half of optimal capacity. The count at each cardinality, not merely the already-known optimum, is the mathematical contribution.

## Limits and closest works

The labeled enumeration does not count equivalence classes under row or alphabet permutations, and says nothing about probabilistic insertion order, stronger separation strengths or larger row counts. A very early equivalent graph enumeration not indexed under hash terminology could subsume the originality claim; no proof of global novelty or independent scientific validation is asserted. Closest inspected works: DOI 10.1515/JMC.2007.008; arXiv:1601.04807v1; DOI 10.1109/CoDIT.2014.6996904.

Self-review: passed. Independent audit: not yet performed.
