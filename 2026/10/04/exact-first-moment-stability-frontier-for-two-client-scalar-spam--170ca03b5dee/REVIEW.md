# Review

## Correctness

PASS. The SPAM update was specialized directly to the scalar quadratic proximal map, producing a \(3\times3\) random linear state recursion. Independence of the current client from the past justifies averaging the transition matrix before propagating first moments. The characteristic polynomial factors into the refresh root \(1-p\) and one quadratic. The Jury inequalities reduce exactly to \((2-p)\rho^2t^2<(1+t)^2\). Boundary cases \(p=1\), \(\rho=0\), and \(\rho=1\) agree with the formula. The standalone checker reconstructs the matrix rather than merely evaluating the final formula.

Risk: the result is only first-moment stability. This restriction is stated in the finding, proof, slogan, and metadata.

## Originality

PASS. The SPAM source gives a general sufficient nonconvex convergence bound and reports the large-stepsize empirical sensitivity to \(p\), but inspection of its algorithm, theorem, and experimental discussion did not reveal an exact first-moment phase boundary for the two-client scalar quadratic specialization. The closest proximal-momentum analyses inspected use direct Polyak momentum on the iterate or a sketch-and-project stochastic proximal-point equivalence; neither has SPAM's momentum-variance-reduced estimator plus shifted client proximal map.

Targeted searches using the algorithm name, scalar quadratics, first moments, Schur stability, and the derived threshold found related stochastic-curvature and splitting stability results but no statement implying this claim. A residual literature risk remains because an equivalent analysis could exist under different terminology.

## Value

PASS. The source paper explicitly reports a qualitative stability change when \(p\) is raised from \(0.1\) to \(0.9\) at a very large exact-proximal stepsize. The exact scalar phase boundary isolates a mechanism by which refresh probability can control the first moment and places the displayed pair on opposite sides of a sharp threshold when \(\rho=1\) and \(t=20\). This supplies a compact diagnostic model for separating first-moment stabilization from stronger convergence guarantees and identifies where higher-moment analysis is genuinely necessary.

Same-model review: passed. Independent audit: not yet performed.
