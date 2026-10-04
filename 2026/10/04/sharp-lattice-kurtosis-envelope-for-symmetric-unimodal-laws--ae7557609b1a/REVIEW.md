# Review

## Correctness

PASS. The proof reconstructs every symmetric unimodal lattice law as an
explicit probability mixture of centered discrete uniforms, with
\[
\lambda_m=(2m+1)(p_m-p_{m+1}).
\]
The discrete-uniform second and fourth moments are evaluated exactly, and the
moment points lie on the strictly convex parabola
\[
q=\frac{9v^2-v}{5}.
\]
For a target variance between two consecutive grid variances, the secant
through those adjacent points lies below every other grid point, so averaging
gives the exact fourth-moment lower envelope. Equality forces support of the
mixing index on those two adjacent uniforms. The phase asymptotic is an exact
algebraic consequence of the finite formula.

## Originality

PASS, with a residual older-literature risk. The full Navard--Seaman--Young
paper was inspected at its definition of discrete unimodality, convexity
characterization, and variance-bound sections. It develops the relevant
lattice shape class but does not optimize fourth moments at fixed variance.

The continuous symmetric-unimodal kurtosis literature gives the sharp lower
value \(9/5\), attained by the continuous uniform distribution. The present
discrete result is not a specialization because centered discrete uniforms
fall below \(9/5\), and the sharp lattice envelope has an order-\(1/v\) phase
oscillation.

The closest prior lattice-tail result for the same distribution class was
compared by implication. It solves a threshold-dependent tail maximization;
it does not determine the minimum fourth moment at fixed variance or the
adjacent-uniform equality classification.

Targeted semantic and web searches for discrete symmetric unimodal kurtosis,
fourth-moment envelopes, centered-uniform mixtures, and lattice corrections
did not return an equivalent formula.

## Value

PASS. Kurtosis is the canonical standardized fourth-moment shape functional.
The theorem gives a complete finite-variance lattice correction to the
classical symmetric-unimodal \(9/5\) benchmark, identifies every exact
extremizer, and shows that discretization produces a persistent phase effect
at the first correction order. This is a structural moment classification,
not a finite table or a routine recomputation.

Same-model review: passed. Independent audit: not yet performed.


Exact-rational replay: `VERIFY_OK moment_checks=1503 chord_checks=80000 equality_checks=5250 random_mix_checks=20000 phase_checks=5269`.
