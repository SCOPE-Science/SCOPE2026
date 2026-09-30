# Independent audit — 2026-09-30 UTC

Record: `2026/09/21/fixed-point-free-automorphisms-finite-abelian-groups--88ac3f97afbf`  
Assigned and audited source tree: `266a7f03325bb0c726d5374395ae3acf66c7fd5b`  
Repository/branch: `SCOPE-Science/SCOPE2026` / `main`  
Current RESULT.md blob: `d5542015736ab14e4ab5773642bde2e7e1e47997`  
Disposition: **passed**

## Correctness

**independently_supported**. The product count is correct. In the Hillar–Rhea matrix model, reduction modulo p is block upper triangular by equal cyclic exponent, and the diagonal-block map from Aut(P) onto ∏GL_{m_r}(F_p) is surjective with equal-size fibers. For a finite group, φ is fixed-point-free exactly when φ-I is bijective, which here is equivalent to every diagonal block B_r-I being invertible. The count is therefore the total automorphism count times the product of finite-field derangement proportions. Möbius inversion on the subspace lattice gives the displayed D_m(p) formula. Multiplication over characteristic Sylow factors and the distinct-exponent specialization then follow.

## Originality

**qualified_supported**. Hillar–Rhea supply the matrix description and automorphism count, while Hayat–López-Aguayo–Abbas 2018 give the rank-two distinct-exponent fixed-point-free formula and pose the higher-rank theta-value problem. Gross gives the abelian 2-group existence criterion, and Senden studies which fixed-point cardinalities occur rather than how many automorphisms realize them. Targeted searches did not locate the product formula by exponent multiplicities or the all-rank d=1 specialization. Because the derivation is short once the standard matrix model is in hand, implicit older enumeration remains a residual priority risk.

## Scientific value

**meaningful_exact_enumeration**. The theorem gives a uniform closed count for every finite abelian group, resolves the fixed-point-free slice of an explicit higher-rank theta-value question, explains the exponent-multiplicity invariance of the proportion, and refines a classical existence criterion into an exact enumeration.

## Independent checks

- Reconstructed the block-reduction homomorphism and its surjectivity.
- Checked fixed-point-freeness via invertibility of φ-I on a finite group.
- Re-derived D_m(p) by subspace-lattice Möbius inversion.
- Verified the standard automorphism-order substitution and distinct-exponent exponent sum.
- Checked the p=2 existence consequence D_1(2)=0 and D_m(2)>0 for m≥2.

## Literature and evidence checked

- https://arxiv.org/abs/math/0605185
- https://doi.org/10.3390/sym10070238
- https://scholar.rose-hulman.edu/rhumj/vol11/iss2/3/
- https://doi.org/10.4153/CJM-1968-128-5
- https://doi.org/10.1017/S0013091523000500
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/21/fixed-point-free-automorphisms-finite-abelian-groups--88ac3f97afbf
## Limitations

- Only θ(A,1), the fixed-point-free stratum, is counted.
- The full θ(A,d) problem for d>1 remains open in the stated higher-rank setting.
- Classical automorphism-group and finite-field derangement machinery are prior inputs.
- An implicit or differently phrased older enumeration remains possible.
