# Review: cyclomatic bounds and sharp matching-induced-matching gaps

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The general inequality reduces to two elementary statements that were checked separately.

First, for a fixed maximum matching `M`, the conflict graph `C_M` has one vertex per edge of `M`, with adjacency recording an edge of the original graph joining the two matching edges. An independent set in `C_M` is therefore an induced submatching. Deleting vertices outside `V(M)` and contracting all edges of `M` produces `C_M` after simplification, so its cyclomatic number cannot exceed that of the original graph.

Second, a graph on `q` vertices and cyclomatic number `r` has independence number at least `ceil((q-r)/2)`: after choosing a spanning forest, one endpoint from each of the `r` nonforest edges deletes all nonforest edges, leaving a forest on at least `q-r` vertices. Bipartition of that forest supplies the required independent set. Combining the two observations proves the cyclomatic bound.

The tree and unicyclic fixed-order bounds then follow from `nu(G)<=floor(n/2)`. Sharpness was checked algebraically from the whiskering identity `nu(W(H))=|V(H)|` and `nu_s(W(H))=alpha(H)`. The pendant-twin modification used for odd orders cannot increase the induced matching number because any induced matching using the new leaf edge can replace it by the pre-existing whisker edge at the same base vertex.

Finite verification independently checks all nonempty connected Graph Atlas graphs for the cyclomatic inequality, all nonisomorphic trees through order 14 for the tree extremum, and all nonisomorphic connected unicyclic graphs through order 11 for the unicyclic extremum. No discrepancy was found.

## Originality

PASS, to the best of our knowledge.

The closest checked literature falls into several adjacent lines:

- Fricke--Laskar (1992), Zito (1999, 2000), and Golumbic--Lewenstein (2000) concern maximum-induced-matching algorithms on trees or related graph classes. The full texts of all three older tree sources were not available for complete inspection; accessible descriptions emphasize algorithms rather than a comparison with ordinary matching number.
- Cameron--Walker (2005) characterizes the equality class `nu=nu_s`, rather than bounding their difference by cycle rank or fixed order.
- Kang--Kim--Kim--Law (2017) studies the number of `r`-matchings in an `n`-vertex tree and proves an extremal counting result for induced matchings; this is a different quantity from the maximum cardinality `nu_s` and its gap from `nu`.
- Choi--Furuya--Kim--Park (2020) explicitly treats matching number and induced matching number together, but in Ramsey-type induced-subgraph theorems. Its accessible arXiv text was checked for the relevant parameter comparison and cycle terminology; the theorem here was not located.
- Unicyclic edge-ideal literature uses induced matching number in regularity formulas, but the checked descriptions do not give the ordinary-matching gap or the cyclomatic inequality.
- Recent work comparing induced matching with edge open packing in trees concerns a different pair of parameters.

Direct searches were also made under the synonymous terms `strong matching`, `2-matching`, `matching number`, `induced matching number`, `forest`, `tree`, `unicyclic graph`, and `cyclomatic number`. No equivalent statement was located in the checked sources or the checked public archive.

The principal residual originality risk is an older theorem stated in strong-matching notation, especially in the incompletely inspected tree-algorithm literature, or an equivalent inequality embedded in edge-ideal literature. This risk is explicitly retained rather than treated as evidence of absence.

## Value

PASS.

The result provides a single sparse-structure parameter, cyclomatic number, that quantitatively controls the difference between two canonical matching invariants. It immediately yields exact fixed-order extrema for both trees and connected unicyclic graphs, with simple sharp constructions for every admissible order. The proof mechanism is reusable: a maximum matching is compressed to a conflict minor, converting induced-submatching selection into an independence problem whose excess edges are measured by cycle rank.

## Limitations

- Originality is to the best of our knowledge, not an exhaustive literature guarantee.
- Several older tree sources were inspected only through abstracts, bibliographic summaries, or secondary citations.
- The fixed-order theorems give exact maximum values but do not classify all extremal isomorphism classes.
- The finite computations are corroborative and are not used in place of the general proofs.
