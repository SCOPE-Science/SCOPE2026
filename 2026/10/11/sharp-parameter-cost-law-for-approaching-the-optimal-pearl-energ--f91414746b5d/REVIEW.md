# Review of Sharp parameter-cost law for approaching the optimal Pearl energy coefficient

## Correctness

PASS. Subtracting the source limit from its exact optimized coefficient and setting
\[
x=1/A
\]
reduces the gap to an elementary combination of
\[
-\log(1-x).
\]
Its convergent power series gives the first coefficient
\[
c_*=\frac13+\log\frac34
\]
and, for every order \(n\ge2\), the exact coefficient
\[
\frac{4n-7}{3n(n-1)}.
\]
These coefficients are positive, which independently proves strict monotonicity and yields a two-sided remainder bound.

The admissible-cost law uses only the verified inequality
\[
C(A,B)\ge C_*(A),
\]
density of odd-rational-square parameters, and continuity of \(C\). The expansion of \(B_{\min}\) follows from the exact trigonometric identity for \(\Phi_0\).

## Originality

PASS. The fresh primary source proves that the optimized coefficient decreases to
\[
(1-\log3)/2
\]
and uses density to obtain an arbitrarily small prescribed gap. It does not state a first correction, an all-order positive gap series, or a sharp asymptotic for the admissible \(A\)-cost of a prescribed tolerance.

The earlier Diamond paper supplies a fixed quasioptimal coefficient rather than a parameter family converging to the Pearl limit. It therefore does not imply a convergence-rate or admissible-cost statement.

Searches under the exact source, optimized coefficient, limiting value, first-correction, and parameter-efficiency formulations produced no covering result. A residual risk remains because the expansion is algebraically short once the fresh optimized formula is available.

## Value

PASS. The main existence theorem of the Pearl paper is explicitly tolerance-based: for every positive \(\varepsilon\), it selects admissible geometric parameters whose linear energy coefficient lies within \(\varepsilon\) of the limiting value.

The accepted result turns that qualitative statement into a sharp resource law. It identifies the exact leading constant governing how the polar parameter must diverge, proves that the arithmetic restrictions do not change this scale, and exposes the different square-root relaxation scale of the optimized tropical parameter. These quantities describe the geometric cost of approaching the best coefficient available in the new construction.

Same-model review: passed. Independent audit: not yet performed.
