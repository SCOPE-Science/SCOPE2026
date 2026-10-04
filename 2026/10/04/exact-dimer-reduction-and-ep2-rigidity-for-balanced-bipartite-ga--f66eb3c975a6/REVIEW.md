# Review: Exact dimer reduction and EP2 rigidity for balanced bipartite gain-loss Hamiltonians

## Correctness
PASS. The SVD similarity is exact: if \(U=P\Sigma Q^T\), then \(\operatorname{diag}(P,Q)^T H_\gamma(U)\operatorname{diag}(P,Q)\) has diagonal off-block \(\Sigma\) and permutes to independent \(2\times2\) dimers. Each dimer squares to \((\sigma_j^2-\gamma^2)I_2\), giving the characteristic polynomial, axis confinement, and eigenvalue counts. At \(\sigma_j=\gamma>0\), the dimer is nonzero rank-one nilpotent of index two, hence exactly one \(J_2(0)\) block. Repeated threshold singular values remain a direct sum of EP2 blocks.

## Originality
PASS with a deliberately narrow originality scope. Standard Jordan-Wielandt theory already covers the zero-gain embedding, so that is not claimed as new. The inspected 2022/2024 bipartite-network paper gives the exact block form, states that the large random Hamiltonian is not analytically diagonalized, derives formulas for \(N=4\), and numerically maps real/imaginary fractions for larger \(N\); its inspected text contains no singular-value reduction. Targeted searches for the shifted singular-value formula, SVD treatment of that paper, and EP-order consequences did not locate prior coverage. The remaining risk is that an equivalent application exists under different terminology.

## Value
PASS. The reduction replaces a \(2m\)-dimensional non-Hermitian eigenvalue classification by a singular-value problem for \(U\), yields exact finite-sample real/imaginary fractions, identifies every transition point, and rules out higher-order Jordan blocks within the model. This directly sharpens the interpretation of numerical stability maps and isolates what changes between the symmetric and nonsymmetric coupling ensembles: their singular-value statistics rather than a different spectral algebra.

## Closest literature and limitations
Li et al., arXiv:1212.1676, provide an archive-era four-mode square-root PT transition. Moreno-Rodriguez et al., arXiv:2212.13642 / Chaos 34, 053116 (2024), are the closest model-specific source. Standard Jordan-Wielandt/Hermitian-dilation theory is the closest generic algebraic antecedent. The finding assumes equal bipartition, off-diagonal transpose coupling, and scalar balanced gain/loss; perturbing those hypotheses can destroy the dimer decomposition.

Same-model review: passed. Independent audit: not yet performed.
