# Self-review

## Correctness — PASS

The exact formula is reconstructed from the central transposition spectrum, the normalized class-character expansion, Frobenius reciprocity and the decomposition of the standard representation as an induced permutation representation minus the trivial representation. The coefficient of the subtraction term is checked directly. The classical Lindblad multiplier follows from commuting central Hamiltonian and jump dynamics and the standard transposition character ratio. The asymptotic step invokes the established *conditional* Kerov transition-measure law, deduced from Plancherel shape concentration and continuity of the transition map; bounded transforms justify the expectation of squares. A separate full-permutation-space matrix-exponential program matches thirty finite cases and performs twenty-nine further checks. Finite checks do not establish the infinite limit on their own.

## Originality — PASS, with residual risk

He–Hutsalyuk–Mussardo–Stampiggi's slow-mode Kronecker sum and variance scale, Kerov's transition-measure semicircle law, and Gerhardt–Watrous's symmetric-group quantum-walk character methods are prior results. The new implication is the *standard-mode* branching identity and explicit oscillatory Bessel-square scaling profile, not the known ingredients. The thesis chapter containing the recent paper's technical account was read, including its exact formula and slow-mode subsection. No equivalent result was found in targeted record/literature searches. The associated original full preprint could not be inspected; previously implicit or unindexed coverage remains possible and no priority guarantee is made.

## Value — PASS

The leading standard Fourier mode is singled out as the slowest classical mode in the motivating model. A variance lower bound identifies a scale but does not tell whether the mode has an oscillatory, Gaussian or monotone universal profile, nor reveal its first asymptotic zero. The theorem supplies the precise shape and incorporates a competing dissipative timescale, answering a model-motivated analytical question without claiming a full mixing-time solution.

## Boundary and reproducibility

For each fixed time-scale parameter the limit holds, including the continuous normalization at zero. Other Fourier components can dominate; the result does not establish a total-variation cutoff. The full original preprint is a residual source-inspection risk; comparisons with the accessible author thesis, older coherent quantum-walk paper and classical transition-measure theorem are documented separately in `AUDIT.json`. The included verifier uses NumPy and SciPy; the infinite proof is analytic and no independent assessment has occurred.

Self-review: passed. Independent audit: not yet performed.
