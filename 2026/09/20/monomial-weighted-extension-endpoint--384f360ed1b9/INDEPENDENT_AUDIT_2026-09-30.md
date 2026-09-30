# Independent audit — Endpoint weighted extension for monomial finite-type curves

## Scope
Independent review of `2026/09/20/monomial-weighted-extension-endpoint--384f360ed1b9` for task `d78192f91c71d25955327c261d13fec3`. The assigned source tree `1931cdc86f9f8670c20861767683606e60de658d` matches the tree on repository `main` at commit `eff2c6312cec5b0dee5115e5f42211a853092dfb`. Audit date: 2026-09-30 UTC.

## Correctness
**PASS.**

- Squaring the extension operator and applying Plancherel in the linear graph coordinate correctly reduces the endpoint L4 norm to one-dimensional quadratic forms in the two-point phase.
- The critical spatial weight has a positive Laplace-mixture Fourier kernel with small-frequency behavior |xi|^(-1/k) and |xi|^(-2) decay. At k>2 the quadratic collision singularity is locally integrable.
- The flat regime s<=R^(-1/k) scales to a uniformly integrable power singularity and gives the inverse terminal cutoff. In the curved regime the phase difference is comparable to s^(k-2)|x^2-y^2|; scaling h=(R s^(k-2))^(-1/2) and the bound J(A)<=C/(1+A) produce the exact normal-gap-plus-terminal-cutoff denominator.
- Symmetric Schur, the change of variables s=t+v, and the normal-parameter comparison then yield the stated energy. Translation, real noninteger k>=3, the symmetric stationary point, and bounded-to-L2 truncation introduce no missing endpoint loss.

## Originality
**PASS_NARROW.**

- Vergara's arXiv:2609.20643 was freshly checked on 2026-09-30; it was submitted September 17 and last updated September 18, and its monomial endpoint iota=(k-1)/k is still described as open in the indexed source/open-problem material.
- Targeted current searches did not locate a contemporaneous theorem closing this exact normal-direction-energy endpoint. Related square-function and phase-space weighted-extension papers concern different inequalities or frameworks.
- The conclusion is deliberately restricted to the monomial model; it does not claim the general finite-type endpoint.

## Scientific value
**PASS.**

- The theorem closes an explicit endpoint gap in a very recent direct theorem, turning the monomial threshold into the exact closed condition iota>=(k-1)/k and identifying a positive-kernel mechanism that avoids the critical logarithmic divergence of annular summation.

## Literature checked
- [Normal-Direction Energy and Fourier Restriction for Convex Planar Curves](https://arxiv.org/abs/2609.20643)
- [Reverse square function estimates for degenerate curves and its applications](https://arxiv.org/abs/2602.03167)
- [Generalized square function estimates for curves and their conical extensions](https://arxiv.org/abs/2408.07248)
- [A phase-space approach to weighted Fourier extension inequalities](https://doi.org/10.1017/fms.2025.10127)

## Limitations
- The proof is specific to the monomial graph and explicit two-point power geometry; no general finite-type endpoint theorem follows.
- Because the motivating source is only days old, unindexed contemporaneous overlap remains a meaningful but currently unsupported originality risk.

## Conclusion
The record **passes** the independent three-axis audit on the stated, literature-bounded claim. No substantive research-file correction is required. This audit does not convert a targeted literature search into an exhaustive priority guarantee.
