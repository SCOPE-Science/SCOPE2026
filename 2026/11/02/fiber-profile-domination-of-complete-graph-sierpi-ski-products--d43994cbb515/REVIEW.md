# Review of fiber-profile domination in complete Sierpiński products

## Correctness — PASS

The central claim is the exact ordinary domination number for every specified map \(f:[m]\to[n]\), \(m,n\ge2\). For a chosen set of empty clique fibers, domination of every vertex in each empty fiber forces the image of the occupied fibers to cover all \(n\) colors. If \(C\) is the set of colors of empty fibers, the minimum number of selected vertices among occupied fibers of any one color is exactly the maximum of its occupied-fiber count and \(|C|\). This gives matching constructive lower and upper bounds, including nonsurjective maps and bijections. Minimizing over the empty-fiber colors proves the sorted-multiplicity formula, and its corollaries follow explicitly. A graph-level checker reproduced the formula for 82 finite multiplicity profiles, without being used as the infinite proof.

## Originality — PASS, subject to priority uncertainty

The 2019 original product paper [1] defines the product and studies connectivity, planarity and automorphisms; it does not state the map-specific domination formula. The 2023 Sierpiński domination paper [2] provides a general bound, an upper extremal criterion, a degree-based equality case, and cycle-factor results. Those results cover a boundary subfamily but do not imply the profile formula or the unbounded missing-cardinality interval. Targeted mathematical-record and literature queries did not locate a theorem of the same strength. This is not a claim that a failed search establishes global novelty; equivalent work under other terminology is the principal residual risk.

## Mathematical value — PASS

The generating question is how the connecting map affects domination in the foundational Sierpiński product. Rather than determining one isolated value, the theorem reduces the domination number for **every** complete-factor map to its fiber multiplicities, determines both lower and upper product extrema, and shows a sharp surjective/nonsurjective separation. The complete two-color spectrum \(\{2,3,4,m\}\) has an interval of prohibited values of unbounded length as \(m\) grows. These structural and extremal consequences are not routine rephrasings of the general degree bound.

## Closest literature and limitations

[1] Kovič et al., *The Sierpiński product of graphs*, arXiv:1904.04180v1, first public 2019-04-08, https://arxiv.org/abs/1904.04180 .

[2] Henning et al., *The Sierpiński Domination Number*, arXiv:2309.15409v1, first public 2023-09-27, https://arxiv.org/abs/2309.15409 . Theorem 2.2 covers the upper extremum; Proposition 2.3 covers the case of smaller first-factor degree.

The theorem is confined to ordinary domination of one-step complete-factor products. Finite computations do not establish generality or publication priority. Other literature may use a different terminology for the same clique-layer construction.

Self-review: passed. Independent audit: not yet performed.
