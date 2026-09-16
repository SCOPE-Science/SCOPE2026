# No universal symmetric four-hyperplane volume-and-section equipartition in R^4

## Context
Mahler's conjecture for centrally symmetric convex bodies asks whether the volume product |K||K^circ| is minimized by the cube. An inductive strategy would equipartition a symmetric body K in R^4 by linear hyperplanes through the origin and simultaneously equipartition each central section, reducing the estimate to smaller pieces. In R^3 such a simultaneous volume-plus-section equipartition exists for every symmetric convex body (Iriyeh-Shibata; Fradelizi-Hubard-Meyer-Roldan-Pensado-Zvavitch: three planes through the origin give 8 equal volumes and quarter each section). The question here is whether the analogous statement holds in R^4: for every origin-symmetric convex body K, do there exist four linear hyperplanes through the origin with independent normals giving 16 equal 4-volumes and 8 equal 3-volumes in every section K cap H_i?

## Definitions
Let K subset R^4 be compact convex with nonempty interior and K = -K. A linear hyperplane is H_i = u_i^perp with u_i in S^3, all through the origin. Assume det[u_1 ... u_4] != 0 so the four hyperplanes are in general position. They cut R^4 into 16 open orthants C_sigma indexed by sign patterns sigma in {+-1}^4. For fixed i, the three planes H_j cap H_i are in general position in H_i ~= R^3 and cut the central section K cap H_i into 8 open pieces. Volumes are Lebesgue 4-volume |.| and 3-volume on each H_i.

## Result
Theorem: There exists a smooth, strictly convex, origin-symmetric convex body K subset R^4, arbitrarily C^2-close to the Euclidean unit ball B^4, for which no ordered quadruple of linear hyperplanes H_1,...,H_4 through the origin with linearly independent normals satisfies simultaneously (i) each of the 16 orthants meets K in 4-volume |K|/16, and (ii) for each i, the other three hyperplanes cut K cap H_i into 8 pieces of equal 3-volume |K cap H_i|/8. In particular the universal claim over all symmetric K is false; a comeager set of small even perturbations of the ball are counterexamples.

## Proof / Evidence
Frame manifold M = {(u_1,...,u_4) in (S^3)^4 : det != 0}, dim 12. By antipodal symmetry pair the 16 orthants into 8 pairs with pair-volume V_P = 2V_sigma; condition (i) is V_P = |K|/8 for all pairs, giving 7 independent defects e_P after the sum-zero relation. For each section i, antipodal pieces pair into 4 pairs with pair-volume W_{i,Q}; condition (ii) is W_{i,Q} = |K cap H_i|/8 per pair, giving 3 independent defects f_{i,Q} per i after sum-zero, 12 total. Joint defect map Phi_K : M -> R^19, Phi_K = (e_7, f_12); zeros are exactly admissible quadruples. For smooth strictly convex K the maps are C^1 by transverse first variation. Hence 12 degrees of freedom versus 19 equations: strictly overdetermined.

Perturb the ball radially by even h in C^2_even(S^3), K_h = {r theta : r <= rho_0(1+h)}. Set F(h,u) = Phi_{K_h}(u). First-variation formulas write each defect component as a fixed signed Borel measure applied to h-dot. Surjectivity lemma: D_h F(0,u) : C^2_even(S^3) -> R^19 is onto at every u. Construction: 16 section bumps supported near H_i inside one section piece-pair (even, disjoint from other H_k) whose f-effects span each section's 3-dim sum-zero subspace (block-diagonal); 8 interior bumps deep inside orthant pairs (disjoint from all H_j) with zero f-effect whose e-effects span the 7-dim sum-zero subspace. Back-substitution gives joint surjectivity: match section targets first, then correct volume residual with interior bumps. Abstract generator ranks (8x8 I-11^T/8 rank 7; 4x4 I-11^T/4 rank 3; joint 19x24 block matrix rank 19) verified by output/artifacts/rank_check.py (all pass).

Since D_h F is surjective at every zero, 0 is a regular value of F : H x M -> R^19. By the Abraham parametric transversality theorem, the set of h for which Phi_{K_h} is transverse to {0} is comeager. A map from a 12-manifold transverse to a point in R^19 has empty preimage (a 12->19 derivative is never onto). Hence comeager small even perturbations admit no zero: generic counterexamples near B^4. Symmetric bodies (balls, cubes, ellipsoids) do admit coordinate quadruples; the obstruction appears only after generic symmetry-breaking.

## Limitations
The counterexample is generic-existential via Baire-category transversality, not an explicit closed-form body with coordinates. It rules out exact simultaneous equipartition only, not approximate or relaxed-equality variants, and does not address general (non-symmetric) masses or affine hyperplanes beyond the symmetric linear setting. C^1 regularity of transverse cone/section volumes and openness of the support configuration are used.

## Reproducibility
Run python3 output/artifacts/rank_check.py: expects orthant rank 7, restricted 7, section rank 3, restricted 3, joint rank 19, then ALL RANK CHECKS PASSED. The analytic steps (antipodal pairing counts, projection independence lemma, bump localization, block-triangular solve, transversality dimension count) are self-contained in output/DRAFT-equivalent text above.

## References
- M. Fradelizi et al., Equipartitions and Mahler volumes of symmetric convex bodies, arXiv:1904.10765 (R^3 volume-plus-section positive result).
- P. Soberon, Four hyperplanes do not always equipartition a mass in R^4, arXiv:2608.23312 (affine general-mass 16-part failure, no symmetry/section conditions).
- L. Martinez-Sandoval, Counterexamples and symmetry for uneven orthogonal mass partitions, arXiv:2609.16757 (planar results; surveys above).
- Roldan-Pensado-Soberon mass-partition survey; Frick et al. transversal hyperplane equipartitions (broader background, <=2 hyperplanes).
