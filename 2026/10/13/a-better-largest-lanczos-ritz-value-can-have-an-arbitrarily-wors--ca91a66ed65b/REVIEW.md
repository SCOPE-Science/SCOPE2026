# Self-review

## Correctness
PASS. The first Rayleigh quotient and residual are computed exactly. A basis
\[
u_\varepsilon=(1,1,\varepsilon)^{\mathsf T},
\qquad
w_\varepsilon=(-1,0,1-\varepsilon)^{\mathsf T}
\]
represents the two-dimensional Krylov space without becoming singular as
\[
\varepsilon\downarrow0.
\]
The resulting symmetric definite generalized Ritz pencil converges to one with simple top eigenvalue
\[
5/3
\]
and physical Ritz vector
\[
(-1,1,2)^{\mathsf T}/\sqrt6.
\]
Its residual has norm
\[
\sqrt2/3.
\]
Together with the exact first-residual asymptotic, this yields
\[
\|r^{(2)}_\varepsilon\|_2/\|r^{(1)}_\varepsilon\|_2
\sim
2\sqrt6/(9\varepsilon).
\]

Variational maximality proves strict improvement of the largest Ritz value, and the two-dimensional full-space alternative proves minimal dimension three. The packaged checker replays the exact pencil identities and a high-precision finite witness.

## Originality
PASS with stated residual risks. Classical Rayleigh--Ritz and Lanczos extraction, residual bounds, finite-precision near-breakdown concerns, and generic residual distortion under spectral filtering are prior work.

The closest full Rayleigh--Ritz source was inspected through its convergence, residual, and refined-Ritz sections. A primary Lanczos source was inspected through its exact recurrence and Ritz-residual setup. Neither contains the fixed-condition-number family, the divergent consecutive largest-Ritz residual ratio, the simultaneous strict Ritz-value improvement, or the dimension-three minimality statement.

Focused published-record and literature searches found no implication-equivalent theorem. Older near-breakdown literature remains the main originality risk.

## Value
PASS. Hermitian eigensolvers commonly monitor both an extremal Ritz value and its residual. The example shows that variational progress of the Ritz value does not even qualitatively force stepwise progress of the residual: at condition number two the residual ratio can be arbitrarily large. The exact near-breakdown mechanism and minimal dimension provide a compact diagnostic for interpreting sudden residual changes.

## Closest literature and limitations
The closest inspected sources are Jia--Stewart's Rayleigh--Ritz convergence report and Paige--Panayotov's Lanczos Ritz-vector analysis. A nearby published spectral-filter theorem gives a broad residual-distortion law for prescribed filters, but does not determine the adaptive filter selected by the largest Ritz extraction.

The result is exact arithmetic, concerns only the transition from Krylov dimensions one to two, and gives an unbounded relative rather than absolute residual spike. It is not a typical-case statement.

Self-review: passed. Independent audit: not yet performed.
