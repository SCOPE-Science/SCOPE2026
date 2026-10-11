# Scientific review

## Correctness — PASS

The edge-based Lipschitz norm is exactly twice the largest coordinate derivative. Walsh derivatives commute with frequency selection after deleting the derivative coordinate, giving the upper estimate from the \(\ell_\infty\)-norm of a Walsh convolution kernel. The sign of that kernel produces a Boolean-valued sharp witness of Lipschitz norm exactly two; therefore every coordinate-shadow upper bound is attained. Translation averaging preserves the Walsh subspace, fixes it pointwise and yields the unique equivariant projection, proving minimality rather than mere boundedness. The dual argument covers the corresponding projection of the finite Lipschitz-free space. The homogeneous Krawtchouk formula follows by elementary subset counting, and the quadratic expression follows by an exact symmetric-binomial moment identity. The standalone exact-arithmetic checker passed 585 spectral-family witness comparisons and 23 binomial moment identities. These finite checks corroborate, but do not replace, the proof.

## Originality — PASS, with residual risk

The closest result is Defant–Galicer–Mansilla–Mastyło–Muro, arXiv:2208.06467v1, Theorems 2.3.1 and 8.1.1, which exactly determine the projection constants of Walsh-supported subspaces of \(C(\{-1,1\}^n)\) with the **supremum** norm. Their companion arXiv:2302.00233, Theorems 3.1 and 4.1, provides those kernel identities and fixed-degree asymptotics, also in the supremum norm. The result here does not assert novelty for those known kernels, but proves a new exact reduction to coordinate shadows for the **Lipschitz** norm and its induced free-space norm. The key implication requires demonstrating that the arbitrary edge-gradient constraints admit a jointly Lipschitz extremizer for each shadow; the published \(C\)-norm formula alone does not establish that. Cúth–Doucha, arXiv:2104.11519, treats invariant orbit projections in Lipschitz-free spaces, not the full nontrivial spectral family or the displayed norm. The available full-text comparisons do not establish prior coverage. An unindexed or implicitly known seminorm transfer remains a meaningful originality risk.

## Mathematical value — PASS

Relative projection constants quantify how well a natural subspace is complemented and control approximation within that subspace. The result solves this invariant **simultaneously for every Walsh spectral family** on the finite Hamming cube, not merely for a selected small example. The sharp edge-gradient reduction connects projection theory on \(C\)-spaces to finite Lipschitz-free geometry, while the quadratic case shows that canonical homogeneous projections can have norms of order \(\sqrt n\) despite individual Walsh projections being contractive. This is a structural and quantitative conclusion of potential use in studying Fourier truncation and finite-dimensional decomposition constants, not a normalization check or a table recomputation.

## Limits and related literature

The conclusion is for unweighted Hamming distance; weighted edges may invalidate the sign-witness sharpness mechanism. The homogeneous Krawtchouk sums and their sup-norm asymptotics are credited to prior Walsh analysis. An independent scientific validation has not been performed.

Same-model review: passed. Independent audit: not yet performed.
