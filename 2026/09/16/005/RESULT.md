# No universal symmetric four-hyperplane volume-and-section equipartition in R^4

## Context

In dimension three, the equipartition used in proofs of the symmetric Mahler conjecture simultaneously divides a centrally symmetric body into equal-volume cones and divides each central section into equal-area pieces. The question considered here is the direct four-dimensional analogue with four linear hyperplanes through the origin.

## Definitions

Let K be a smooth, strictly convex, origin-symmetric body in R^4. Let H_i=u_i^perp for four linearly independent normals u_i. The hyperplanes cut R^4 into 16 cones. Inside each H_i, the other three hyperplanes cut K cap H_i into 8 pieces.

## Result

There exist smooth strictly convex origin-symmetric bodies K, arbitrarily C^2-close to the Euclidean ball, for which no ordered quadruple of linearly independent central hyperplanes simultaneously

1. gives all 16 four-dimensional cone pieces volume |K|/16, and
2. for every i gives all 8 pieces of K cap H_i three-dimensional volume |K cap H_i|/8.

Indeed such counterexamples form a comeager set among sufficiently small even C^2 radial perturbations of the ball.

## Proof / evidence

The frame space M={(u_1,...,u_4) in (S^3)^4: det[u_1 ... u_4] != 0} has dimension 12. Antipodal symmetry pairs the 16 cone pieces, so equal four-volume is equivalent to 7 independent defects. In each section H_i, antipodal symmetry pairs the 8 pieces, leaving 3 independent defects; four sections contribute 12 more. The joint defect map therefore takes values in R^19.

Write a nearby symmetric body as K_h={r theta: 0<=r<=rho_0(1+h(theta))} with h even and C^2-small, and let F(h,u) be the 19-component defect map. At any frame u the derivative in the h-direction is onto R^19. For each section H_i, four even bump pairs can be supported near points of H_i lying in the four antipodal section-cell pairs and away from all other H_j. Their section-volume first variations span the 3-dimensional sum-zero defect space for that section, without affecting the other three sections. Independently, eight even bump pairs can be supported strictly inside the eight antipodal four-dimensional cone pairs and away from every H_j; they affect no section defect and span the 7-dimensional sum-zero four-volume defect space. The resulting derivative is block-triangular and surjective.

Thus 0 is a regular value of the universal map F. Abraham's parametric transversality theorem gives a comeager set of small even perturbations h for which the partial map F_h:M->R^19 is transverse to 0. But a map from a 12-manifold cannot be transverse to a point of R^19 at a preimage, since surjectivity of its derivative would be required. Hence F_h^{-1}(0) is empty for generic h. Sufficiently small C^2 radial perturbations preserve smoothness and strict convexity.

The script `artifacts/rank_check.py` is only a finite-dimensional sanity check for the abstract sum-zero/block ranks (7, 3, and 19); the geometric bump-localization argument above is the substantive surjectivity proof.

## Limitations

The theorem is generic-existential, not an explicit coordinate body. It rules out exact simultaneous equipartition by one quadruple of central hyperplanes; it says nothing about approximate partitions, affine hyperplanes, A-dependent relaxations, or other approaches to Mahler's conjecture.

## Reproducibility

Run `python3 artifacts/rank_check.py` (NumPy). It checks the algebraic ranks used by the first-variation argument. The dimension count and bump-localization proof are analytic and are not certified by that script alone.

## References

- M. Fradelizi, A. Hubard, M. Meyer, E. Roldán-Pensado, A. Zvavitch, *Equipartitions and Mahler volumes of symmetric convex bodies*, arXiv:1904.10765.
- P. Soberón, *Four hyperplanes do not always equipartition a mass in R^4*, arXiv:2608.23312. This is a different nonsymmetric affine-mass problem and does not include the simultaneous central-section condition here.
- R. Abraham, *Transversality in manifolds of mappings*, Bull. Amer. Math. Soc. 69 (1963), 470–475.
