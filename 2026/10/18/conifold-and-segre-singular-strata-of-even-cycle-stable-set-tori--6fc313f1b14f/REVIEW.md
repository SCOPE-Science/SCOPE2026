# Scientific review: even-cycle stable-set normal fans

## Correctness — PASS

The all-parameter proof transforms the stable-set polytope of an even cycle into a circular-fence order polytope by an integral affine coordinate change. Primitive facet normals are a totally unimodular rooted incidence matrix. The minimal circuits in an active normal graph are either a four-edge rooted square (one for each centered triple) or the unrooted full cycle, and all nonsimplicial cones contain one such minimal cone. This exhausts the reduced singular support. Saturated lattice bases identify the square with the three-dimensional conifold cone and the full-cycle cone with the cone of rank-one \(m\times m\) matrices. Face intersections and their parity-dependent contacts with the diagonal segment are checked combinatorially. The standalone exact checker enumerates vertex normals and all component-subset intersections for \(n=4,6,8,10\), giving `VERIFY_OK`. The finite tests are not substitutes for the symbolic proof.

## Originality — PASS (qualified)

Stanley's order-polytope paper gives general facet and face methods. Lakshmibai–Mukherjee's Hibi work establishes a general affine toric singular-locus criterion, but the inspected statements do not explicitly give this projective normal-fan all-even-cycle stratification, generic transverse Segre matrix cone, multiplicities, or the complete independence-complex intersection arrangement. Stable-set toric-ring studies address different invariants. Relevant existing small-cycle and path cases were checked and excluded as claims of novelty. Searches for the even-cycle, crown-poset, circular-fence, normal-fan and determinantal formulations found no stronger all-parameter special classification. The residual risk is an equivalent specialized statement in unindexed or differently named literature; absence from search results does not prove uniqueness.

## Mathematical value — PASS

The result gives a full geometric classification of the reduced singular support of a natural infinite family, distinguishing \(2m\) large conifold strata from a single high-codimension determinantal line with growing transverse multiplicity \(\binom{2m-2}{m-1}\). The intersection nerve, exact parity-restricted intersection with the line, and smooth fixed-point cutoff give information not supplied by the basic polytope description. The claim makes no assertion about the nonreduced singular scheme, all germs at intersections or the two previously treated smallest even cycles.

## Relevant sources and limitations

R. P. Stanley, *Two Poset Polytopes* (1986), DOI:10.1007/BF02187680; V. Lakshmibai and H. Mukherjee, *Singular Loci of Hibi toric varieties* (2007), arXiv:0706.2686; K. Matsuda, H. Ohsugi, and K. Shibata, *Toric Rings and Ideals of Stable Set Polytopes* (2016), arXiv:1603.01850. Independent verification has not been performed.

Self-review: passed. Independent audit: not yet performed.
