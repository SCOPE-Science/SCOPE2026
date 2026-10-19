# Scientific review

## Correctness

PASS. In the eigenbasis of the symmetric drift, the exact forcing coefficient is the integral of the product of two decaying exponentials. Strict Cauchy–Schwarz and arithmetic–geometric mean inequalities give the exact entrywise ordering of exact, balanced, and symmetrized forcing. The common homogeneous propagator makes the inequality propagate to the full discrete trajectory and establishes the strict Frobenius comparison. The Taylor expansions and Riemann sums prove both sharp global second-order coefficients; the positive-definiteness threshold and strict monotonicity follow from the displayed determinant and logarithmic derivative. `verify.py` reproduces 18,692 finite checks and supports, but does not prove, the universal statements.

## Originality

PASS within the inspected literature, with residual bibliographic uncertainty. Shkeir and Grafke introduce the METD1 formula and commutator treatment, not this complete positivity frontier or the balanced forcing-error theorem. Bertram and Faßbender cover the Gramian integral and low-rank quadrature; Behr, Benner and Heiland cover general Sylvester spectral formulas. Such exact formulas already imply the Cauchy–Schwarz ingredients but do not explicitly supply the sharp symmetrized-METD1 failure boundary, the strict all-step balanced-versus-symmetrized comparison, and their universal four-to-one error constants. A full search of all publications is impossible and an equivalent specialized reformulation may exist; the 2024 version of the motivating paper was confirmed by its public submission record while the inspected complete text is a later open revision.

## Value

PASS. Differential Lyapunov equations propagate covariance and controllability Gramians, so positive-semidefinite output is a mathematical requirement rather than a cosmetic feature. The result simultaneously classifies a sharp failure regime—including rank-one noise at every step—and provides a simple rank-preserving, positivity-preserving second-order alternative whose error improvement is proved uniformly in step size. The spectral threshold can be used to assess a concrete solver without claiming general nonlinear integration properties or computational cost improvement.

## Closest literature and limitations

Sources: Shkeir–Grafke arXiv:2406.13761 (METD1 and Lyapunov examples); Bertram–Faßbender arXiv:1903.05383 (factorized Gramian quadrature); Behr–Benner–Heiland arXiv:1811.08327 (exact differential Lyapunov solutions). The claim is restricted to fixed real symmetric stable drift and constant PSD forcing in exact arithmetic. General quadrature algorithms already preserve PSD, and other methods can be cheaper or more accurate. An overlooked equivalent specialized calculation remains a literature-priority risk.

Self-review: passed. Independent audit: not yet performed.
