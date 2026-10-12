# Self-review

## Correctness
PASS. The residual propagator admits the exact similarity representation
\[
I-AB=A^{1/2}(I-C)A^{-1/2}.
\]
The spectral-equivalence hypothesis gives
\[
\|I-C\|_2\le\delta,
\]
so the Euclidean residual factor is at most
\[
\delta\sqrt{\kappa_2(A)}.
\]
A \(2\times2\) SPD construction attains equality. The same algebra shows contraction by \(\delta\) in the \(A^{-1}\)-residual norm, so the result does not confuse Euclidean transient growth with spectral divergence.

## Originality
PASS with stated residual risks. Preconditioned Richardson, spectral equivalence, and energy-norm convergence are prior work.

The full archive-era preprint of Kressner, Steinlechner, and Vandereycken was inspected because it places preconditioned Richardson explicitly in an SPD energy framework and lists primary MSC \(65F10\). It does not state the sharp Euclidean residual factor found here. Targeted searches for aliases, residual monotonicity, spectral equivalence, and the exact square-root condition-number factor did not locate an implication-equivalent result.

The principal residual risk is older preconditioning literature expressing the same similarity estimate without the present stopping-criterion terminology.

## Value
PASS. Euclidean residuals are routinely monitored, while preconditioners are routinely judged through the spectrum of a symmetrically preconditioned SPD operator. The theorem gives the exact compatibility frontier between these two diagnostics and shows that a strong preconditioner in the standard spectral sense need not make the monitored Euclidean residual monotone.

## Closest literature and limitations
The closest inspected full source develops preconditioned Richardson in an SPD energy setting; an older preconditioned-Richardson source explicitly uses spectral-equivalence constants but was access-limited through the inspected route. The theorem concerns one fixed SPD correction in exact arithmetic. Varying or nonsymmetric preconditioners, Krylov acceleration, and finite-precision residual gaps are outside scope.

Self-review: passed. Independent audit: not yet performed.
