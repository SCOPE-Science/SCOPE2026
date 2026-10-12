# Scientific assessment: thermal attenuation of optical single-rail qubits

## Correctness — PASS

The Gaussian-channel characteristic-function calculation determines the Wigner polynomial and its exact negative disk, including the positivity boundary. Every fixed-excitation mixed input is a nontrivial convex combination of two pure inputs with opposite coherences, and their displaced negative disks force strict Jensen inequality. A radial Gaussian intersection argument proves the strict energy-volume bound and uniqueness of the one-photon global maximizer. The disk-centered polar integral and elementary Fock specialization agree numerically with independent phase-space quadrature. Boundary cases \(p=0\), \(p=1\), \(A=2\eta\), \(\eta=0\) are treated.

## Originality — PASS, with residual priority risk

The lossless single-photon negative volume is explicitly reported by Kenfack and Życzkowski (arXiv:quant-ph/0406015). Earlier optical-scissors studies derive single-rail Wigner profiles (arXiv:quant-ph/0107048), and Miranowicz et al. explicitly plot negative volume for pure qudit coherent-state families (arXiv:1307.6950), including the qubit case. Miranowicz et al. (arXiv:1502.04523) solve different nonclassicality orderings and depth thresholds for mixed single-rail states. None of their materially inspected results gives the strict mixed-input fixed-population Wigner-negative-volume optimum after arbitrary thermal attenuation and the evaluated universal capacity. The new theorem does not re-claim the already-known noiseless Fock number or pure-state profile. Residual risk: an unlocated general convex ordering theorem, or another thermal-channel Wigner-volume study, could already imply it; independent publication-priority audit is outstanding.

## Value — PASS

For an experimentally meaningful optical-qubit family, the theorem solves the exact constrained optimization over **every** density matrix, not merely a selected pure-state curve: it distinguishes pure and mixed inputs at fixed mean excitation, determines the sharp resource capacity under ambient thermal noise, and proves a strict photon-population upper bound. This directly informs non-Gaussian optical state preparation when thermal attenuation is unavoidable. It requires no downstream application to qualify as a natural closed classification.

## Limitations and reproducibility

Numerical quadrature cannot prove all-parameter extremality; the analytic strict-convexity and radial-rearrangement arguments provide that proof. The theorem does not address higher Fock levels, non-phase-insensitive channels, success probabilities, or independent novelty verification. Run `python verify.py` with `requirements.txt`.

Self-review: passed. Independent audit: not yet performed.
