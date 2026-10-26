# Review of the equicorrelated-block Kaczmarz sampling theorem

## Correctness

PASS. The normalized-row Gram matrix is positive definite on the stated open parameter domain. The proof reduces unrestricted row probabilities by concavity and permutation averaging, decomposes the weighted Gram spectrum into repeated-row contrasts and a two-dimensional coupled block, proves a global upper bound for the latter by an exact determinant square, identifies the crossover algebraically, and establishes uniqueness for arbitrary asymmetric laws by a bottom-eigenvector kernel argument. The `verify.py` calculation was executed from the actual package source and agrees with the claim. Finite tests are supplementary, not a proof.

## Originality

PASS on the inspected evidence, with residual specialized-literature risk. Strohmer–Vershynin give the norm-proportional method and its bound; Dai–Soltanalian–Pelckmans give the general SDP but no explicit two-coherence family solution or active-eigenmode threshold; Agaskar–Wang–Lu optimize a distinct long-time exponent; Gower–Richtárik give a general projection-method framework. A published inverse-positive coordinate-sampling result has a hypothesis not satisfied by the positive equicorrelation block. A related pooled-row star geometry has a different Gram matrix. No inspected source states a theorem implying the complete branch formulas and arbitrary-law uniqueness; the generic SDP itself does not evaluate them.

## Mathematical value

PASS. Repeated correlated measurements and a single exceptional measurement form a natural two-coherence row model for projection-based linear solvers. The exact design yields a nontrivial parameter transition, explicitly identifies which spectral mode is rate-limiting, and quantifies improvements over uniform sampling (about 35% in the sharp one-step gain for a ten-row repeated block with a specified admissible coherence). The theorem covers every block size and every feasible positive correlation pair, not an arbitrary finite slice.

## Remaining limitations

The optimized quantity is the one-step worst-direction squared-error decrease, not the exact infinite-time mean-square exponent, and the correlation family is structured. Special-case overlap outside the retrieved literature cannot be excluded. Independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
