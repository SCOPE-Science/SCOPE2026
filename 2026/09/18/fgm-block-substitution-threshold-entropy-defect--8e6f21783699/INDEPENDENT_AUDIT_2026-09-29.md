# Independent Audit — 2026/09/18/fgm-block-substitution-threshold-entropy-defect--8e6f21783699

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `deb1e6d0eeab18c7e56f5588b5240a25154b6ff2`
- Disposition: **PASSED**

## Correctness

**PASS** — All three main statements check. For U=prod_i x_i, the full mixed derivative of Phi_theta(U,v) is 1+theta(1-2^m U)(1-2v); its variable factor has exact range [-(2^m-1),2^m-1], proving the iff threshold |theta|<=1/(2^m-1). For a smooth outer density c, repeated product differentiation gives exactly (1+u d/du)^{m-1}c, so nonnegativity of this density plus the inherited copula boundary conditions is the correct criterion. For entropy, A_m=1-Y_1 W satisfies E[A_m|Y_1]=A_1. Strong convexity of (1+theta b a)log(1+theta b a), together with E[B^2]=1/3, E[Y_1^2]=4/3 and Var(W)=(4/3)^{m-1}-1, gives precisely the displayed lower bound 2 theta^2/[9(1+|theta|(2^m-1))] * ((4/3)^{m-1}-1). The m=2, theta=1/4 specialization equals 1/378.

## Originality

**PASS** — The general warning that naive nesting of multivariate copulas needs compatibility conditions is established prior art, and the source paper itself proposes the unrestricted operation that is being corrected. The sharp FGM/independence phase boundary, the explicit Euler-operator density criterion for a product block, and the quantitative entropy defect within the valid-copula region were not found in the located hierarchical-Kendall, linkage, vector-copula, or source-paper literature. The first public repository commit for this record predates the closely overlapping second SCOPE record audited in the same assignment.

## Scientific value

**PASS** — The result gives a sharp and elementary falsification of an unrestricted copula substitution rule, separates closure failure from entropy-additivity failure, and supplies an exact differential operator that can be used to test product-block substitutions. The quantitative entropy gap is useful because it persists strictly inside the admissible region rather than only at invalid examples.

## Sources

- Copula Operad and Copula Entropy (X. Lu): https://arxiv.org/abs/2609.20512 — Motivating unrestricted block-substitution and entropy-additivity claims.
- Hierarchical Kendall copulas: Properties and inference (E. C. Brechmann): https://doi.org/10.1002/cjs.11204 — Established multivariate-block aggregation using Kendall transforms rather than naive direct substitution.
- Linkages: A Tool for the Construction of Multivariate Distributions with Given Nonoverlapping Multivariate Marginals (H. Li; M. Scarsini; M. Shaked): https://doi.org/10.1006/jmva.1996.0002 — Classical alternative framework for coupling multivariate blocks.

## Limitations

- The sharp threshold is specific to an FGM outer copula and an independence product block.
- The Euler-operator criterion assumes sufficient smoothness and does not classify arbitrary multiblock substitutions.
- The entropy bound is not claimed to be optimal.

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was read only as evidence and no repository write was performed. Open-access/preprint sources were checked first; Oxford Download was not needed for this record.
