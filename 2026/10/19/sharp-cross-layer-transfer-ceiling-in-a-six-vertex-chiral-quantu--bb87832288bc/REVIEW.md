# Scientific review of the internal-to-external chiral-router bound

## Correctness — PASS
The matrix model is explicitly specified, and Fourier diagonalization reduces it to the three exact \(2\times2\) sectors with core eigenvalues \(0,\pm\sqrt3\). Their analytic offdiagonal propagators combine to the displayed real-trigonometric cross-layer amplitude. The triangle inequality provides a universal upper bound, and the rational independence of \(1,\sqrt3,\sqrt7\) makes the associated three-frequency phase flow dense, proving the exact supremum for every target offset. Simultaneous sine equality at a finite time would force \(\sqrt7\) rational, proving nonattainment. An independent six-site numerical reconstruction and 4,563 amplitude instances corroborate the proof but are not its substitute.

## Originality — PASS (self-review)
The closest directly overlapping works are Bottarelli–Frigerio–Paris, arXiv:2302.08472 (full relevant Sec. III, Eq. (4) and Eqs. (6)–(14)), and Acuaviva et al., arXiv:2301.01473 (Sec. 5.1 including the spectral decomposition and Theorem 5.4). Both already contain the identical physical graph and spectral ingredients. The former studies external-to-external site routing and coherent superpositions; the latter proves pretty-good transfer among the non-pendant triangle vertices. Neither gives or logically states a maximal **internal-to-one-pendant** transition probability. The present exact global-in-time maximization, its numerical constant, and nonattainment require combining sector amplitudes with a separate arithmetic density argument. Search comparisons found no stronger directly covering statement; an equivalent unpublished or differently named optimization remains a residual possibility.

## Value — PASS
Source applications emphasize high-fidelity individual-site routing. It is nontrivial and operationally relevant to know that the *same device* imposes an unavoidable \(\approx29.8952\%\) failure probability for a localized internal-to-pendant conversion, regardless of waiting time. This sharp, pair-independent bottleneck distinguishes two physical uses of one concrete network and cannot be inferred from source assertions of near-perfect same-layer transport. It does not purport to be a general quantum-network speed limit.

## Closest coverage and remaining risks
The published Hamiltonian and eigenvectors suffice to reconstruct the formula, so independent scientific priority review should check whether an equivalent cross-channel optimization appeared in later studies or different notation. The mathematical statement is intentionally limited to fixed chirality, hopping and detuning; it is neither a claim about variable flux nor about state-transfer efficiency at experimentally bounded times. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
