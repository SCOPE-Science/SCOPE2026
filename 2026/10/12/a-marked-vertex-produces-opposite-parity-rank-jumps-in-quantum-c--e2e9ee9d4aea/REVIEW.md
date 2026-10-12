# Review: marked-cycle average-mixing rank

## Correctness — PASS
The theorem is quantified over every integer \(n\ge3\) and every real \(\tau\). The spectral decomposition and simple-spectrum Gram reduction are reconstructed explicitly. For a nonzero marking, the reflection-even Jacobi restriction has simple eigenvalues, and its secular determinant excludes every untouched reflection-odd eigenvalue. All squared eigenvectors are consequently reflection invariant, giving an upper bound of \(\lfloor n/2\rfloor+1\). Diagonal closed-walk moments at lengths \(1,3,\ldots,2\lfloor n/2\rfloor-1\) form a triangular distance-shell witness with determinant exactly \((-1)^{\lfloor n/2\rfloor}\tau^{\lfloor n/2\rfloor}\), reaching the bound. Known explicit unmarked cycle formulas supply the separate zero-potential ranks. Exact integer checks and independent spectral checks replay from `verify.py` and corroborate the analytical proof; finite experiments are not used as infinite proof.

## Originality — PASS, residual risk stated
Godsil [1, Lemma 6.1] **already computes the unmarked-cycle mixing matrices**; these cases are properly attributed rather than claimed anew. The general squared-eigenvector rank framework appears in [2] and is a method rather than a finite marked-cycle classification. The integral-Hamiltonian analysis in [3] and the open-problems review [5] do not state a rank law for a continuously adjustable diagonal site potential. The directly relevant defect article [4] concerns an infinite line and scattering/localization, not the finite-ring Cesàro rank. Searched aliases included one-site impurity, diagonal rank-one perturbation, marked cycle, spectral projector Gram rank, onsite potential and long-time quantum walk mixing; published database results encountered did not imply the theorem. Although no direct coverage was found among these primary sources, an unlocated more general theorem about rank-one Jacobi perturbations and reflection-orbit mixing could imply this special case; the comparison is not a universal novelty certificate.

## Value — PASS
A one-site impurity is a natural localized perturbation of a finite quantum ring. The theorem gives an all-size, all-real-strength classification and finds a parity-sensitive *opposite direction* of rank change under arbitrarily weak nonzero detuning. The exact triangular odd-moment witness explains why the invariant is robust for every nonzero strength and connects quantum mixing ranks to shortest marked closed walks. This is structural information beyond the base Fourier cycle calculation and a usable diagnostic for finite-ring transport models.

## Scope and external review
The conclusion is restricted to one onsite diagonal mark and infinite-time averaging; no finite-time convergence or multiple-site statement is asserted. Independent external verification is outstanding.

Self-review: passed. Independent audit: not yet performed.
