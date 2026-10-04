# Same-model review

## Correctness
PASS. On a diagonal positive-definite quadratic, the algorithm has the exact coordinate recurrence
\[
x_i^{n+1}=\left(1-\frac{\eta\lambda_i}{w_i^n}\right)x_i^n.
\]
The primary source proves both convergence of the smooth-convex iterates and square-summability of successive gradient differences. The latter gives a finite limit for every \(w_i^n\). If an active limit satisfied \(w_i^\infty\leq\eta\lambda_i/2\), every multiplier would have magnitude at least one, contradicting convergence of that nonzero coordinate to zero. The asymptotic ratio and finite-dimensional Q-linear conclusion then follow directly.

## Originality
PASS. The primary AdaGrad-Diff preprint was inspected at the algorithm, main convergence theorem, gradient-difference summability result and its appendix proof, experiments, and discussion. It gives a generic \(\mathcal O(1/n)\) ergodic rate and iterate convergence, but no diagonal-quadratic limiting stability threshold or last-iterate linear-rate statement was found. Focused database searches returned related stability frontiers for different algorithms rather than this claim.

The closest inspected literature uses gradient differences in a different local-curvature update (Malitsky--Mishchenko) or discusses gradient-difference accumulation as a way around a composite AdaGrad pathology. Neither inspected result implies the stated half-threshold for the cumulative AdaGrad-Diff metric.

Residual risk remains that an equivalent statement may exist under different terminology or in an unindexed preprint; the later composite-objective paper was available only through its abstract and a detailed accessible summary during this check.

## Value
PASS. AdaGrad-Diff is explicitly motivated by stability and reduced sensitivity to the base parameter \(\eta\). This result gives a concrete mechanism on the standard separable strongly convex quadratic test class: the cumulative gradient-difference metric must drive every active limiting effective step strictly inside the exact scalar gradient-descent stability interval, which in turn yields eventual last-iterate Q-linear convergence. This is a structural explanation of the method's central robustness claim, not a routine recomputation.

Same-model review: passed. Independent audit: not yet performed.
