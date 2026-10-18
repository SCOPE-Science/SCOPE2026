# Scientific review of the double-star curvature-distortion profile

## Correctness: PASS

The statement covers all integers \(1\le a\le b\) and real \(0\le k\le2/(a+b+1)\), with infeasibility above that endpoint. The proof derives the weighted tree edge-curvature identity from the cut form of Wasserstein distance, uses the exact sum of tree-edge curvatures to prove the endpoint, and obtains a scalar lower bound from **arbitrary**, not merely symmetric, weights. Its scalar function is strictly increasing. The explicit two-branch solution attains the bound with properly normalized positive weights; equality forces the stated unique optimizer. Differentiation on both sides of the interior threshold proves a strict derivative jump when \(a<b\).

The accompanying verifier checked 726 candidate/root/curvature combinations, 180 independently optimized orbit-constant problems, 300 exact rational endpoint parameter pairs, and 180 independent optimal-transport LP comparisons. These finite checks support, but do not replace, the unrestricted argument.

## Originality: PASS, with limited priority uncertainty

The closest source, Qing Xia's *Prescribed Lin--Lu--Yau Curvature Lower Bounds* (Zenodo DOI 10.5281/zenodo.22757916, made public September 15, 2026; later arXiv:2610.21454), establishes general finite-tree feasibility, implicit fixed-point solutions, uniqueness and monotonicity. Its examples cover \(P_4\) and the maximum-target \(D_{1,2}\), but not the complete two-leaf-class phase diagram or its interior nondifferentiability. Xia's earlier *Nonnegative Lin--Lu--Yau Curvature* (arXiv:2609.12125, Section 4.1) already has \(\mathrm{DN}^{0}_{\mathrm{LLY}}(D_{a,b})=\sqrt{ab}\). These known statements are not separately claimed as new.

Bai--Cheng--Hua (arXiv:2604.22449) and Cheng (arXiv:2605.20862) characterize constant-curvature Einstein weightings and their spectral sign, rather than the full prescribed-floor minimum-distortion profile. Relevant mathematical-research records on spider trees and pineapple graphs involve a different parameter range or different graph families. No direct covering closed-form profile or asymmetry-triggered curvature kink was found in the completed comparisons. The September Zenodo PDF itself was not materially read; a distinct earlier algebraic presentation cannot be entirely excluded.

## Value: PASS

This solves an explicit, natural two-parameter family for an optimization invariant whose general theory is implicit. The sharp leaf-activation threshold and derivative discontinuity give a structural phenomenon absent from the general continuity theorem: asymmetric double stars exhibit a genuine interior change of active constraints, while balanced double stars have no such interior transition. The result includes a certificate of global optimality against all nonuniform leaf weights and a complete optimizer classification. It is more than a zero-curvature substitution or a check of a single small tree.

## Limitations and residual risks

The metric uses fixed combinatorial distances, the leaf classes are positive, and the prescribed target is nonnegative. Neither the general optimal weighting for all trees nor the Einstein endpoint is claimed as newly established. No independent mathematical audit or definitive bibliographic priority assessment has taken place. A general published implicit fixed-point theorem already entails computability of every tree case; the specific new content is its explicit two-branch reduction and non-differentiable family-level phase law. The September preprint PDF and uncatalogued equivalent results leave modest priority uncertainty.

Self-review: passed. Independent audit: not yet performed.
