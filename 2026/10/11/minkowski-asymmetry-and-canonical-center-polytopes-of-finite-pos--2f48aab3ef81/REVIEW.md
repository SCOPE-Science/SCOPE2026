# Scientific review: Minkowski centers of order polytopes

## Correctness

PASS. The exact reflection-containment criterion follows from the upper-set vertices of an order polytope and gives coordinate lower/upper bounds and unit separation at every cover. The longest-chain inequality forces a dilation factor at least the height, while the longest-chain-ending rank function attains it. The center polytope is a network difference-constraint polytope with an integral vertex description. A weighted-longest-path perturbation establishes that only elements lying on longest chains have forced center coordinates. Exact-rational tests corroborate the center-dimensional formula for 1,219 poset presentations without being used as an infinite proof.

## Originality

PASS, with an equivalence risk. The relevant literature provides order-polytope facet and vertex descriptions, codegree interior labelings, and poset-polytope triangulations. Haase–Kohl–Tsuchiya (arXiv:1805.02967), the closest result, already treats the strict-labeling hull and should receive full credit for that object; it does not in the inspected sections identify that hull with the complete set of Minkowski centers or compute their affine dimension from longest-chain membership. Chappell–Friedl–Sanyal (arXiv:1606.04938) study double poset polytopes and comparability-graph chain polytopes, not this center classification. Von Bell et al. (arXiv:2102.11306) analyze triangulations, circuits and volume rather than asymmetry. A general difference-constraints or Hibi-ring formulation might already imply the theorem, so an earlier equivalent statement cannot be ruled out solely by phrase searches.

## Value

PASS. This is a natural, complete convex-geometric classification for every finite poset, not a numerical special case: it identifies the minimizing dilation, the entire optimizing locus, its exact lattice-geometric realization, and a combinatorial criterion for its dimension and uniqueness. The last criterion differs from purity of a poset: two disjoint three-element chains with a cover from the first point of one to the last point of the other have an additional short maximal chain but still a unique Minkowski center. The connection of the optimizing locus to the canonical degree interior hull is potentially useful in geometric and poset-theoretic work; no downstream theorem is asserted.

## Evidence and limitations

The proof is in RESULT.md; the standard-library program verify.py and its reproduced output provide bounded exact computation. The strongest related published result is arXiv:1805.02967, especially §§6 and 8. The 2021 geometry-source paper arXiv:2102.11306 is dated by its first arXiv posting, not its revision or journal appearance. The stable-set realization of comparability-graph chain polytopes is a known construction, but the order/chain transfer is not affine; thus no general chain-polytope metric conclusion transfers automatically to order polytopes. The independent audit has not been performed.

Same-model review: passed. Independent audit: not yet performed.
