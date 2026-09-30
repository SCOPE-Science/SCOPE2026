# Independent audit — 2026-09-29

Record: `2026/09/19/algebraically-independent-skeletons-euclidean-nonembeddability--1c2547e992d7`  
Assigned and audited source tree: `05077ba5c32c609e9c40770a6656b411c36639fb`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `ddccf6ca9e19f0abb4b27ce2fc836039f2b133b7`  
Disposition: **passed**

## Correctness

**independently_supported**. The three mathematical steps check. For a finite set of skeleton edges and a nonzero rational polynomial, the nonvanishing condition is open, while density follows by moving the induced finite metric into the open strict-metric cone, avoiding the polynomial hypersurface there, and applying Ishiki's exact metric interpolation theorem on the finite closed subset. Countability plus the Baire property of Met(X) gives the dense G_delta skeleton theorem. Fixed-dimensional Euclidean embeddability is closed because every fixed finite Gram matrix retains positivity and rank at most m under uniform metric limits; it is nowhere dense because an arbitrarily small finite perturbation on m+2 points can make the Cayley-Menger determinant nonzero and then be extended globally. Finally, a polynomial dependence among squared Euclidean edge lengths would remain a nonzero rational polynomial after substituting X_e=T_e^2, contradicting algebraic independence of the raw skeleton distances. The complete k-point dimension and planar (2,3)-sparsity consequences follow.

## Originality

**qualified_structural_extension**. Ishiki's September 2026 preprint proves density of full algebraic independence under strong zero-dimensionality and a G_delta statement for the full property on sigma-compact spaces. The inspected statement does not give algebraic independence on a prescribed countable skeleton for arbitrary metrizable topology, nor the rigidity-matroid transfer. Ishiki's earlier interpolation and Baire theorems supply most of the machinery, so the contribution is best characterized as a clean new consequence/synthesis rather than a new perturbation method. Targeted current searches did not locate the same skeleton theorem or finite-Euclidean-stratum statement.

## Scientific value

**meaningful_generic_geometry_result**. The result isolates a strong algebraic-generic phenomenon that survives on connected and positive-dimensional spaces, and translates it into exact Euclidean nonembeddability and rigidity-matroid obstructions. Its value is structural and broadly applicable, though the proof is short once the interpolation/Baire framework is available.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/19/algebraically-independent-skeletons-euclidean-nonembeddability--1c2547e992d7
- https://arxiv.org/abs/2609.19773
- https://arxiv.org/abs/2003.13227
- https://arxiv.org/abs/2402.04565
- https://doi.org/10.1137/21M1437986
- https://arxiv.org/abs/1003.5087
## Limitations

- Only a fixed countable skeleton is controlled; full algebraic independence on arbitrary positive-dimensional spaces is not proved.
- The Euclidean conclusions concern exact isometric embeddings, not approximate, bi-Lipschitz, coarse, or quasi-isometric embeddings.
- Rigidity-matroid independence is necessary, not sufficient, for Euclidean realizability.
- The main novelty is a consequence of existing interpolation/Baire machinery, and the motivating preprint is extremely recent.
