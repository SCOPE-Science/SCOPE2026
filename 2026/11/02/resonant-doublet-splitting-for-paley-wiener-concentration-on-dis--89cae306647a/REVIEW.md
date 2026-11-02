# Scientific review: resonant two-window Paley–Wiener concentration

## Correctness — PASS

The stated object is the sinc-kernel concentration operator on two equal, disjoint intervals. The Fourier normalization fixes the sinc kernel as \(\sin(\pi u)/(\pi u)\). The one-interval top eigenvalue is simple with a strictly positive gap by classical prolate theory. The proof derives the exact commutator \((\lambda_0-K_a)(x\psi_a)=(c_a/\pi)\sin(\pi x)\), from which \(c_a\ne0\) and \(Q_a>0\) follow without numerical assumptions. The cross kernel has an operator-uniform expansion through degree two in inverse integer distance. The degenerate reduced-resolvent expansion gives the diagonal self-energy \(Q_a\) and off-diagonal coefficient \((-1)^m(C_a t-2Q_a)\). Diagonalization yields the theorem, with a uniform \(O_{a,T}(m^{-3})\) remainder even at the second-order cancellation point. The generic \(O_a(R^{-2})\) estimate follows from first-order compression and the fixed spectral gap. The proof does **not** interpret a finite numerical test as establishing an infinite claim.

The supplementary `CHECK.py` uses independent quadrature discretizations of the one-window and two-window sinc kernels and a residual check of the commutator. The executed checker returned `CHECK_OK 279`. Its role is to catch normalization, sign and branch errors; the proof supplies the universal quantifiers.

## Originality — PASS relative to checked sources

Zelent [1] (2026-10-01) studies quantitative global concentration stability relative to single intervals. Its operator-theoretic preliminaries include the prolate spectral gap, but the work does not calculate the far-separated equal-window doublet or the \(m^{-1}\) detuning resonance. Abreu–Speckbacher [2] (2026-07-21) proves global interval optimality and supplies an upper bound based on the total measure; that upper bound does not imply the oscillatory split or the explicit \(Q_a\) correction. Bonami–Jaming–Karoui [4] treats the one-interval spectrum, not the distant two-interval coupling. Widom [5] and Fahs–Krasovsky [6] analyze sine-kernel determinants under increasing interval/bandwidth scales; they do not address the fixed-width, distant-center top-two eigenvalue regime. A relevant published record on *exact detachment crossover* concerns a vanishing translated piece at a vanishing displacement, which neither covers the equal fixed-window regime nor implies the new spectral doublet formula.

No accessible inspected primary statement or indexed mathematical record was found that implies the full resonant law. This is a best-knowledge originality assessment, not a proof that no earlier equivalent result exists. Residual risk includes earlier unindexed two-window eigenvalue perturbation formulas and the incomplete inspection of older full texts.

## Value — PASS

A pair of disconnected observation windows has two almost identical concentration modes in the large-separation limit. Its highest spectral gap is the central measure of how weakly the two modes couple. The theorem identifies an oscillatory inverse-distance splitting, isolates the exceptional lattice separations, and determines a nontrivial \(m^{-1}\) tuning of the center distance that removes the entire second-order doublet gap. The positive exact coefficient \(Q_a\), obtained from a prolate commutator, is essential to the cancellation and is not a discretionary numerical slice. This gives a natural, complete leading-order description of the resonant separation window; it is useful for understanding the spectrum and near-extremizers of disconnected bandlimited concentration. The work does not claim a full spectrum, exact crossings or optimal remainder constants.

## Closest literature and limits

References [1]–[6] in `RESULT.md` provide the scientific context. The strongest direct comparisons are to [1] for arbitrary observation sets and to [4] for the one-interval spectral gap. The argument requires that external standard spectral fact; everything else needed for the stated coefficients and asymptotics is shown. The independence of the scientific review has not been established.

Self-review: passed. Independent audit: not yet performed.
