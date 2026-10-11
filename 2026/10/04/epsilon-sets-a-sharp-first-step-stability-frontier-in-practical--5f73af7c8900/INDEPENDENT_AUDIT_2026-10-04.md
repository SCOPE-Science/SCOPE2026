# Independent mathematical audit

## correctness

PASS

Direct substitution into Algorithm 1 gives \(s_{1,i}=\gamma h_i x_i\), \(\nu_{1,i}=\gamma h_i^2x_i^2\), and multiplier \(1-q_i\) with \(q_i=c\gamma h_i/(\gamma^{1/3}h_i^{2/3}|x_i|^{2/3}+\varepsilon)\). Since the quadratic is diagonal, objective nonincrease is equivalent coordinatewise to \(0\le q_i\le2\). The supremum of \(q_i\) occurs as \(x_i\to0\), yielding exactly \(c\gamma L\le2\varepsilon\); solving \(q=2\) gives the spike radius, and convex endpoint optimization of \((1-q)^2\) gives the exact supremal factor. Equality at the frontier still gives strict decrease for every finite nonzero active coordinate because its denominator is strictly larger than \(\varepsilon\).

## originality

PASS

The defining paper supplies the exact practical recurrence and explains that its convergence proof uses a different denominator containing an additional gradient-bound term. It does not state the sharp practical first-step quadratic stability threshold, spike radius, or supremal amplification. The fresh Resultary search returned other one-step optimizer frontiers but no covering MADGRAD result.

## value

PASS

The result isolates a practically relevant mechanism hidden by the adaptive notation: near a zero gradient the cube-root accumulator contributes no startup scale, so epsilon alone controls first-step stability. A necessary-and-sufficient frontier, exact spike basin, and exact worst amplification give a concrete calibration diagnostic for a widely used optimizer and are not a generic numerical check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
