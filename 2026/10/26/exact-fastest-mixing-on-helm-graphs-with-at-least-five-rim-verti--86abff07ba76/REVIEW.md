# Scientific review of the helm-graph fastest-mixing theorem

## Correctness: PASS
The lower bound is a Rayleigh quotient on the first nonconstant Fourier mode of the dihedral average of any feasible symmetric Markov kernel. The test vector removes the unknown leaf-edge weight and uses the hub and rim row budgets. The explicitly proposed weights attain the bound: direct multiplication proves the top-mode eigenvalue identity; a universal trigonometric bound establishes positive feasibility for every integer \(n\ge5\); a lower-semidefinite bound controls all negative Fourier eigenvalues; and the exact radial quadratic controls both remaining eigenvalues. Dihedral averaging extends invariant optimality to the unrestricted symmetric problem. The strict equality conditions uniquely identify the invariant optimizer, not every optimizer. The companion executable independently checks the critical symbolic identities, dense spectra and finite competitors, without substituting those tests for the infinite proof.

## Originality: PASS, with residual risk
The 2007 full arXiv paper of Boyd, Diaconis, Parrilo and Xiao (arXiv:0709.0955v1, §§1–2 and 5.3.3) develops symmetry reduction and solves the wheel graph, but its wheel has no pendant leaves and has a radial block of size two rather than three. Its wheel formula cannot be applied to the helm graph by renaming a parameter. The full accessible 2020 Jafarizadeh text studies clique lifts and separate path, star, windmill and symmetric-tree constructions; these do not encompass a wheel with a private leaf attached to each rim vertex. A targeted literature search for helm fastest-mixing weights revealed no all-size formula, while the named graph structure agrees with MathWorld. Available mathematical-record searches gave no stronger or equivalent helm-SLEM theorem. Similarities to earlier fastest-mixing methods and the possibility of unindexed equivalent work are explicitly recognized. A failed search is not proof of worldwide priority.

## Value: PASS
The helm family is a standard wheel augmentation with leaves, introducing a third transition orbit and a leaf--rim bottleneck. Its optimum is not the wheel answer or a trivial uniform weighting: the leaf probability is a nonlinear trigonometric function of graph size, and both hub and rim self-loops saturate exactly at zero. The complete infinite-family SLEM and invariant-weight classification quantifies a concrete asymptotic improvement of about 30.9% in spectral gap over maximum-degree weighting. This supplies exact calibration for a natural high-symmetry network family rather than an arbitrary finite parameter slice.

## Closest literature and limitations
- S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004): general convex formulation; no helm-specific formula identified in accessible source material.
- S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1: exact wheel formula, Fourier symmetry machinery; not a pendant-wheel theorem.
- S. Jafarizadeh, *Fastest Mixing Reversible Markov Chain: Clique Lifted Graphs & Subgraphs*, DOI:10.1109/TSIPN.2020.2964211: different families and reductions, with no inspected helm instance.
- No global uniqueness assertion for noninvariant optimizers; no result for helm sizes three or four; no certification of novelty against inaccessible or unindexed literature.

Self-review: passed. Independent audit: not yet performed.
