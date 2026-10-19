# Self-review

## Correctness — PASS
Walsh diagonalization gives a two-column Gram matrix at each energy. Its interior determinant is strictly positive for nonantipodal sinks because both parity-overlap signs occur for every weight; for antipodal sinks its columns are proportional in every weight. The bright/dark decomposition reduces the non-Hermitian generator; the sink form excludes undamped eigenvectors in the bright block, proving long-time convergence even for defective blocks. Direct inversion of the Gram matrix gives all-site probabilities; taking its trace proves mean probabilities. A standalone checker reports 739 finite comparisons, including dynamics with unequal loss rates; they are corroboration, not a general proof.

## Originality — PASS (self-review)
Le et al., arXiv:1707.07482, establish the dark-state spectral principle, which is used rather than rediscovered here. Thiel et al., arXiv:1906.08112 and arXiv:1909.02114, study discrete projective first detection, including single-detector examples. The reviewed full text did not state the two independently absorbing hypercube sites' rank dichotomy or this two-point Krawtchouk probability law. Searches against published research records and accessible earlier findings returned related hypercube spectra, Fourier restriction, and whole-Hamming-shell absorption, but no implication covering the two-point theorem. Search absence cannot certify uniqueness; an implicit stronger controllability or strong-cospectrality result remains a significant literature risk.

## Value — PASS
The hypercube is a natural transport network, and detecting whether placement of a second sink increases eventual transport is a motivated architectural question. The answer is an exact, all-dimensional classification: every nonantipodal placement has the same average bright fraction, whereas antipodal placement is spectrally redundant. The full Krawtchouk law supplies exact location-dependent absorption values without simulating the open evolution. These are structural and quantitative facts beyond mere restatement of the generic dark-subspace criterion.

## Scientific limits and sources
The conclusion concerns ideal continuous-time hopping and asymptotic absorption with strictly positive rates. It does not cover speed of absorption, additional traps, decoherence, or arbitrary onsite potentials. Closest inspected sources: arXiv:1707.07482; arXiv:1906.08112; arXiv:1909.02114. Related comparison was also made with a different prior first-Hamming-shell quantum-hypercube absorption result and a discrete-time percolated Grover absorption model.

Self-review: passed. Independent audit: not yet performed.
