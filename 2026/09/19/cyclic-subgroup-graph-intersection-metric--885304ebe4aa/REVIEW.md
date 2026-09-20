# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The distance proof was checked at the edge-local and global levels. If X<Y is an edge, Y is cyclic and |Y:X| is prime. The quotient map H∩Y -> Y/X has kernel H∩X, so the intersection rank can increase by only zero or one prime factor. Hence the stated potential changes by exactly one on every edge. Saturated chains from H∩K to H and K supply the matching upper bound. The concatenated chain is induced because nonconsecutive vertices on one chain have an intermediate subgroup and vertices strictly above H∩K on opposite chains are incomparable.

The C4×C2 counterexample was checked explicitly: its cyclic-subgroup graph has six vertices and five edges, is a tree of diameter three, and therefore cannot contain the length-four induced path asserted by Proposition 2.5(2) for n=4.

For the cycle correction, Γ(C_n) is the Cartesian product of paths indexed by the prime exponents. Prime powers give a path. The p^a q case with a>1 gives a ladder, in which an induced cycle can only be a single square. The positive cases are realized by a rectangle boundary for two thick coordinates, by C4 for pq, and by opposite coordinate-order saturated paths when at least three distinct primes occur.

## Originality

PASS, to the best of our knowledge.

The current full text of arXiv:2409.13796v2 was inspected at Proposition 2.5, the cyclic product-of-paths result, and Theorem 2.11. It states the two induced-subgraph claims corrected here and gives only general diameter bounds, not the exact intersection distance formula. Its special proof for the upper diameter bound on C_n×C_n uses a related potential for one selected pair, which is treated as prior art rather than novelty.

The accessible text of arXiv:2503.12184v1 / the 2025 line-graph paper was checked; its focus is forbidden induced subgraphs and line-graph classification. Tărnăuceanu's edge-count paper and the open-access 2025 subgroup-graph degree paper were also checked for scope. Searches using exact and synonymous formulations of cyclic-subgroup-graph distance, diameter, intersections, shortest paths, Proposition 2.5, corrections and errata did not locate the formula or the corrections above.

Residual risk remains because the distance argument is elementary and could be implicit in general Hasse-diagram or ranked meet-semilattice folklore under different terminology. No novelty is claimed for that abstract lemma. The current cyclic-subgroup-graph application, exact formula, and corrections are the originality claim.

## Value

PASS.

The result replaces a general two-sided diameter estimate by an exact pairwise metric, gives an exact diameter maximization formula, and simultaneously identifies why the current induced-path argument fails when equal-order cyclic subgroups intersect. It also supplies explicit counterexamples to both parts of a current proposition and a sharp cyclic-group criterion for the claimed long induced cycle.

## Limitations

The results are for finite groups. The long-cycle criterion classifies the subgraph arising from a cyclic subgroup C_n; in a larger ambient group, failure of that criterion does not exclude a same-length induced cycle built elsewhere. Same-model review is not independent validation, formal verification, or peer review.
