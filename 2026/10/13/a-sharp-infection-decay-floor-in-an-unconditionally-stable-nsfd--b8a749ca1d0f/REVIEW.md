# Self-review

## Correctness

PASS. Direct linearization gives continuous infected decay rate
\[
c(1-\mathcal R_0).
\]
Direct differentiation of the printed NSFD map gives
\[
\lambda(\phi)
=
\frac{1+c\mathcal R_0\phi}{1+c\phi}
=
\mathcal R_0+\frac{1-\mathcal R_0}{1+c\phi}.
\]
The strict floor and the sharp crossover
\[
h_*=
\frac{-\log\mathcal R_0}{c(1-\mathcal R_0)}
\]
follow exactly. Symbolic replay verifies the rate limits and the exact witness.

## Originality

PASS. Elementary stability and qualitative dynamic consistency are established NSFD concepts. The accepted contribution is the source-specific floor, crossover, and physical-time rate asymptotic. Source, broader-literature, published-finding, and same-slot ledger comparisons did not locate an equivalent implication.

## Value

PASS. The result distinguishes stability preservation from physical-time fidelity in a scheme promoted for arbitrary step sizes. Beyond an explicit threshold, exact infection-decay matching is impossible within the source update architecture, and its chosen denominator makes the large-step per-unit-time decay rate collapse to zero.

## Closest literature and limitations

Later SIR NSFD literature defines elementary stability qualitatively by preservation of equilibria and their linear stability properties. That does not cover decay-rate matching.

The finding is local to the disease-free infected mode. It does not invalidate the source's positivity or qualitative stability results and does not give a nonlinear transient-error theorem.

Self-review: passed. Independent audit: not yet performed.
