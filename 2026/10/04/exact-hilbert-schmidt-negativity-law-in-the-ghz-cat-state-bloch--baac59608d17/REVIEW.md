# Same-model review

## Correctness
**PASS.** The claim is reconstructed analytically from the logical cat-state density matrix. Partial transpose produces exactly one signed \(2\times2\) coherence block for every nontrivial bipartition, so the standard negativity is \(\sqrt{n_x^2+n_y^2}/2\). The Hilbert–Schmidt metric is a constant multiple of Euclidean metric in Bloch coordinates, and the probability law follows from exact spherical/cylindrical volume. The beta factorization, conditional mean, marginal moments, and tube expansion were each checked against the same normalization. The numerical verifier is supplementary rather than evidentiary for an infinite claim.

## Originality
**PASS.** The closest source, Zhou–Joynt, supplies the GHZ Bloch-ball geometry and the separable axis but no Hilbert–Schmidt distribution. Zhu–Hayashi–Chen gives broader pointwise links between \(l_1\)-coherence and negativity, so that pointwise identity is treated as prior-compatible rather than novel. Maziero reports sampled average \(l_1\)-coherence for random-state generators, and Zhang–Singh–Pati treat analytic averages of other coherence quantities; neither gives the exact beta law, the purity/angular independence, or the tube coefficient. Searches under GHZ, maximally-correlated, random-qubit, Hilbert–Schmidt, negativity-distribution, and \(l_1\)-coherence aliases did not locate a covering statement. A residual terminology risk remains because the derivation is elementary once the ensemble is specified.

## Value
**PASS.** Zhou–Joynt's motivating distinction is topological: in the GHZ cat-state ball the zero-negativity set is a lower-dimensional diameter. The exact CDF converts that statement into a sharp quantitative neighborhood law \(6\varepsilon^2+O(\varepsilon^4)\), while the independent purity/angular factorization gives a reusable conditional benchmark. The ensemble is the canonical volume induced by the Hilbert–Schmidt metric on the very affine state space under discussion, rather than an arbitrary parameter slice.

## Closest literature and limitations
The claim is restricted to Hilbert–Schmidt volume conditioned on the two-dimensional cat support. It does not cover full many-qubit Hilbert–Schmidt random states, Bures or other induced measures, or genuine multipartite entanglement measures. The later coherence-negativity literature can reproduce the pointwise relation, but the inspected sources do not supply the new probability law. The principal residual originality risk is an unretrieved exact random-qubit \(l_1\)-coherence distribution under different terminology.

Same-model review: passed. Independent audit: not yet performed.
