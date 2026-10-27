# Self-review: Six-point rigidity of three-distance mutual visibility in rectangular grids

## Correctness — PASS

The proof addresses the same selected-pair diameter-three and internally unobstructed shortest-path definition as the original paper, not a weaker variant. A per-row/column occupancy bound yields at most six points in any rectangular grid. Equality rigidifies to one of exactly two translated, transposed templates. Each template has explicit unobstructed geodesics for all symmetry classes of pairs. A separate complete 3-by-3 corner/midpoint argument proves cardinality five and exactly four optimizers. `check_grid_mu3.py` independently tests the original condition on all distance-three cliques for thirteen finite test grids, recording 20,675 bounded-diameter subsets and exact optimizer sets. Finite tests corroborate, but do not establish, infinite claims.

## Originality — PASS

Cera López et al. (arXiv:2408.03976, DOI 10.1007/s40840-024-01811-3), §6, explicitly ask for k-distance mutual visibility on Cartesian products of paths; they do not provide the radius-three exact solution. Their general Theorem 2.1 is a lower bound, not a complete classification. Korže and Vesel (DOI 10.1007/s00025-024-02139-x) and Cicerone, Di Stefano and Klavžar (DOI 10.1016/j.amc.2022.127619) treat unrestricted visibility. A later mutual d-visibility article (DOI 10.1007/s00025-025-02450-1) exempts far-apart pairs rather than rejecting them. Fault-tolerant visibility is another variant. Published-record searches found a k=3 hypercube theorem and Cartesian high-girth connected mutual-visibility theorem, neither of which implies this grid statement. A copy of the original 2023 unrestricted-product full paper could not be read; a later unindexed equivalent remains possible.

## Value — PASS

The result resolves an explicitly motivated open family question at the first nontrivial radius beyond two. It completely determines all maximizers, not just their size, and gives an exact placement count across infinitely many grids. The constant optimum and two-template rigidity are structural features of the cutoff condition, not a routine substitution into the unrestricted parameter.

## Limitations and scientific sources

The theorem does not address general distance thresholds, products with more factors, cylindrical grids, thin grids, or variant visibility definitions. Main source: Cera López et al., arXiv:2408.03976, first public 2024-08-07, DOI 10.1007/s40840-024-01811-3. Closest related product results: DOI 10.1007/s00025-024-02139-x and DOI 10.1016/j.amc.2022.127619. Independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
