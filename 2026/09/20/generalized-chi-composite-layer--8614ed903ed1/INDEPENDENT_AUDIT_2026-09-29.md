# Independent audit — 2026-09-29 UTC

Record: `2026/09/20/generalized-chi-composite-layer--8614ed903ed1`  
Assigned source tree: `76bc4836297abe7fd33fb16ce4d52c3e6967a8e4`  
Audited current source tree: `76bc4836297abe7fd33fb16ce4d52c3e6967a8e4`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `45b5ed411db78e6653b00dd091702af395d5a741`  
Disposition: **passed**

## Correctness

**independently_supported**. The structural conjugacies are exact. The permutation i->i+v decomposes Z/nZ into d=gcd(n,v) cycles of length ell=n/d, and reindexing along each cycle turns F_{n,v} into the ordinary chi_ell rule with no cross-block variables. For the second family, direct expansion over F_2 verifies that the involution T(z)_t=z_{-t}+1 satisfies T chi_ell T(z)_t=z_t+z_{t-2}z_{t-1}+z_{t-1}. The source permutation condition 2^k|v makes ell odd; v nonzero modulo n gives ell>=3. Known ordinary-chi inverse degree and composite-chi restriction-weight/spectrum formulas then give the stated inverse degree, differential uniformity and product spectra. A direct product has maximum differential probability 1/4 because one block can be active and the remaining blocks inactive, so Delta=2^(n-2). Iteration, order and the gcd-based conjugacy classification follow immediately from the same block conjugacy.

## Originality

**qualified_supported_structural_identification**. Feng--Wang--Yu--Zhang introduce the skip-step families and characterize when the shift-invariant quadratic maps are permutations; their argument already uses coordinate cycles. Mella--Mehrdad--Daemen and Schoone--Daemen provide the ordinary/composite chi cryptanalytic and inverse algebraic machinery. The checked sources do not state that the new skip-step permutations themselves are direct products of ordinary chi blocks, nor the reversal-complement affine conjugacy of the second family. Targeted searches found no equivalent identification. Novelty is therefore narrow and source-specific, with material concurrency/folklore risk because the decomposition is short once the cycles are noticed.

## Scientific value

**meaningful_cryptanalytic_classification**. The classification shows that every valid even-dimensional named map is an imprimitive parallel nonlinear layer and transfers complete existing composite-chi spectra and inverse-degree information immediately. It materially changes how the new layer should be interpreted, while correctly not asserting insecurity of a full primitive with external linear mixing.

## Independent checks

- Exhaustively verified T chi T=B for all inputs at ell=3,5,7.
- Re-derived the cycle decomposition and the direct-product differential-uniformity argument.
- Compared the claim against the current generalized-chi and composite-chi literature.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/20/generalized-chi-composite-layer--8614ed903ed1
- https://arxiv.org/abs/2609.19548
- https://doi.org/10.1007/s12095-023-00639-1
- https://doi.org/10.1007/s10623-024-01395-w
- https://doi.org/10.1007/s10623-026-01830-0
- https://doi.org/10.46586/tosc.v2025.i3.800-826

## Limitations

- The theorem applies to the source's characterized quadratic shift-invariant family, not unrelated ChiChi or higher-degree variants.
- No claim is made that block decomposition of one nonlinear layer breaks a full primitive with intervening mixing.
- The ordinary-chi inverse and composite spectrum theory are prior art.
- The motivating preprint is extremely recent, so near-simultaneous observation risk is substantial.
