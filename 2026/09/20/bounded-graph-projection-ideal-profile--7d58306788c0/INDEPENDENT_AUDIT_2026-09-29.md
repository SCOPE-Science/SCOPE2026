# Independent audit — 2026-09-29 UTC

Record: `2026/09/20/bounded-graph-projection-ideal-profile--7d58306788c0`  
Assigned and audited source tree: `e8c58edcbc95d64e86509c523992c7537f9cf929`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `d3aaf38646c17336ae70b661418962943d658a7a`  
Disposition: **passed**

## Correctness

**independently_supported**. The exact modulus identity is correct. The graph and orthogonal-complement isometries J_T,V_T are unitary coordinates and give V_B^*J_A=D_B(A-B)C_A and V_A^*J_B=D_A(B-A)C_B. For Delta=P_A-P_B, the universal two-projection identity makes Delta^2 block diagonal relative to ran(P_A) plus ker(P_A), with blocks S_AB^*S_AB and S_BA S_BA^*. Positive functional calculus gives the displayed direct-sum formula for |Delta|. Independent random finite-dimensional calculations reproduced the complete singular-value multiset. Invertibility of C_T,D_T then gives exact rank doubling, Schatten equivalence and bounds, while direct sums in the Calkin algebra give the essential-norm formula. The compact-difference geodesic corollary follows because I+B^*A is a compact perturbation of the invertible I+A^*A and hence has Fredholm index zero.

## Originality

**qualified_classical_core_with_graph_specific_packaging**. The core two-projection spectral geometry is classical: Halmos/Davis-era two-subspace theory and later work relate the spectrum and singular values of P-Q to subspace angles, and Andruchow's 2015 graph-map paper already treats fixed-base Schatten restricted Grassmannians. Azizov-Behrndt-Jonas-Trunk 2009 also gives the qualitative finite-rank and compact equivalences for graph projections. What was not located in the checked sources is the exact graph-coordinate packaging |P_A-P_B| ~ |D_B(A-B)C_A| direct-sum |(D_A(B-A)C_B)^*| together with the stated two-directed norm and essential-norm consequences for arbitrary bounded A,B. The record's own best-of-knowledge qualification and exclusion of the fixed-base/qualitative results are therefore adequate, but no broad novelty is assigned to the underlying two-projection principle.

## Scientific value

**meaningful_coordinate_sharpening**. Even with a classical spectral core, the graph-coordinate identity is a useful compact formula: it turns qualitative graph perturbation statements into exact rank, Schatten and essential-norm information with explicit dependence on A-B, and it supplies a concise compact-difference geodesic consequence.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/20/bounded-graph-projection-ideal-profile--7d58306788c0
- https://doi.org/10.1007/s00020-008-1650-1
- https://doi.org/10.1016/j.laa.2014.10.029
- https://arxiv.org/abs/2608.30120
- https://doi.org/10.1090/S0002-9939-1987-0870792-X
- https://doi.org/10.1016/j.laa.2009.11.002
## Limitations

- The theorem is restricted to bounded operators between Hilbert spaces.
- The general two-projection spectral/angle mechanism is classical and is not independently novel.
- The originality claim is only for the explicit two-graph coordinate identity and packaged consequences.
- Older graph/subspace literature, including Chung 1993, was not exhaustively inspected in full.
