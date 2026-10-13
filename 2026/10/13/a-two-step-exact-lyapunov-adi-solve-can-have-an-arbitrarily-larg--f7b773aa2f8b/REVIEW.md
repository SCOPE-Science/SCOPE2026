# Self-review

## Correctness
PASS. The low-rank ADI residual factor after a real shift is the Cayley action
\[
(A+\sigma I)(A-\sigma I)^{-1}.
\]
For the displayed Jordan family at \(\sigma=1\), that matrix is
\[
\begin{pmatrix}
0&-M/2\\
0&0
\end{pmatrix},
\]
so it has arbitrarily large norm but square zero. The first residual is therefore amplified by exactly \(M^2/4\), and the second residual is exactly zero. Direct solution of the Lyapunov equation and construction of the ADI columns also prove
\[
0\preceq P_1\preceq P_2=P.
\]
The scalar case is strictly contractive, so dimension two is minimal. The packaged checker replays the identities in exact arithmetic.

## Originality
PASS with explicit residual risks. General ADI convergence theory, the low-rank residual-factor formula, nonnormal Lyapunov phenomena, and generic Cayley overshoot are prior work and are not claimed as new.

The closest full ADI source was inspected through its residual theorem and recurrence; the closest Cayley strong-stability source was inspected in full. Neither states the combined construction with fixed spectrum, arbitrarily large first Lyapunov residual, exact termination on the next identical shift, monotone positive-semidefinite approximation, and dimension-two minimality. Targeted published-record searches did not expose an implication-equivalent statement.

A residual risk remains because a broad 2011 ADI convergence paper was accessible only through its publisher record rather than complete body text, and older control literature may contain the same nilpotent-Cayley example in different language.

## Value
PASS. Residual norm is a standard ADI stopping diagnostic. The result gives an exact minimal example in which that diagnostic is maximally misleading: it can spike by any prescribed factor while the approximate Gramian moves monotonically toward the exact solution and the next ADI step terminates exactly. The fixed spectrum shows that eigenvalue information alone cannot exclude the transient.

## Closest literature and limitations
The closest sources are the low-rank ADI residual-factor paper, general ADI/RKSM convergence theory, strong-stability theory for Cayley transforms, and work on nonnormal Lyapunov-solution singular values. The theorem is exact-arithmetic and two-dimensional; it does not bound residual growth under dissipativity, numerical-range, eigenvector-conditioning, or finite-precision restrictions.

Self-review: passed. Independent audit: not yet performed.
