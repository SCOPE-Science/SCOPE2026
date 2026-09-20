# Review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** The proof starts from the published GRL hull criterion and specializes it to the full evaluation set. Since `x^q-x` has derivative `-1`, all Lagrange coefficients are `-1`; choosing the normalization scalar `-1` makes the unscaled multipliers equal to `1` without taking any nontrivial `(p^ell+1)`-st roots. The root-count argument forces `g=-f^(p^ell)`. In the strict degree range, nonsingularity of the extension matrix kills the top `s` coefficients of `f`. At the sole possible degree boundary, the scalar choice `A_s=mu I_s` and `mu^(p^ell+1) != 1` kills the same coefficients. Scaled evaluation coordinates then force exactly `z=k-s-h` roots, leaving an `h`-dimensional polynomial space. The converse is explicit.

For `s=2`, the published distance criterion is independent of nonzero evaluation multipliers. In the strict range an `A_zeta` with `zeta` in the `(k-1)`-subset-sum set gives AMDS/NMDS distance. At the boundary, the required multiplicative subgroup has size `k-1` and sum zero, so the scalar extension matrix also satisfies the AMDS criterion. The published classical-to-EAQECC conversion applies to every Galois index.

The standalone verifier exhaustively checks all `8^3` codewords for representative GF(8) examples and all `27^3` codewords for representative GF(27) examples. It confirms both requested hull dimensions and the stated minimum distances. The GF(27) case has `ell=2`, `e=3`, so `ell` does not divide `e`.

## Originality

**PASS, to the best of our knowledge.** The motivating paper arXiv:2609.20453v1 explicitly assumes `2 ell | e` in its main construction regime and in its full-evaluation AMDS theorem. Its root-existence lemma explains why that hypothesis is used in the generic normalization. The present observation bypasses that lemma for the full evaluation set by making the normalized target identically `1`.

Searches covered the exact motivating title and arXiv identifier; generalized/Roth--Lempel hull terminology; `ell`-Galois and `e`-Galois formulations; arbitrary/all Galois indices; full evaluation; AMDS/NMDS parameters of length `q+2`; and nearby GRS/EGRS and Hermitian Roth--Lempel literature.

Relevant prior work was separated from the novelty claim. Wan--Zhu, arXiv:2412.05011, handles all Galois indices for GRS/EGRS MDS self-orthogonality and derives MDS hull families, so arbitrary-index Galois hulls in general are not claimed as new. Sok, arXiv:2207.07792, and Liu--Wu--Zhou, arXiv:2604.11350, address Hermitian Roth--Lempel/GRL hull or self-orthogonality phenomena. None of the located sources states the present arbitrary-index full-evaluation GRL theorem or its length-`q+2` AMDS/NMDS consequence.

The main residual risk is temporal: arXiv:2609.20453v1 was submitted on 17 September 2026, so a near-simultaneous note, an unindexed response, or a later revision could independently contain the same simplification. Older Galois-hull literature may also contain algebraically equivalent normalization ideas outside GRL terminology. This is why the originality verdict is explicitly qualified.

## Value

**PASS.** The result removes the field-divisibility restriction from a concrete, recent GRL hull family, not merely from an auxiliary lemma. It covers Galois indices with `ell` not even dividing `e`, preserves the entire hull range `0 <= h <= k-s`, yields length-`q+2` AMDS/NMDS codes with exact distance, and immediately supplies EAQECC families. The proof also identifies a simple structural mechanism: on the full field, the Lagrange vector is constant and can be normalized to the trivial power value `1`.

## Limitations

The argument is specific to the full evaluation set and does not extend every evaluation-set construction of the motivating paper. The maximal degree boundary requires a scalar extension matrix. The finite verifier is supporting evidence rather than the general proof. No independent review, formal proof assistant verification, or exhaustive literature guarantee is claimed.
