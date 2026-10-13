# Self-review

## Correctness

PASS. The affine witness is exact. At \(x=0\), only \(f_1(x)=x\) is active. The source max-model has its unique minimizer at \(v=-1\) with \(\theta=-1/2\), and the robust directional derivative equals \(-1\). The inactive scenario has gradient \(-M\), so its product with the same direction is \(M>0\). Hence the all-scenario maximum is positive and cannot satisfy the negative bound in Assumption 4.1(15).

The replacement is also exact. Writing the source model as \(\Psi_x(v)=\max_j\Phi_j^*(x,v)\), first-order optimality gives \(-v\in\partial\Psi_x(v)\). Convexity and \(\Psi_x(0)=0\) yield \(\Psi_x(v)\le-\|v\|^2\), from which
\[
\Phi_j^*(x,v)\le-|\theta|
\]
and
\[
\|v\|^2\le2|\theta|
\]
follow. Active scenario offsets vanish, so every active gradient product is strictly negative.

## Originality

PASS. The primary full proof, the monotone predecessor, the later global-convergence analysis, and a related non-monotone Newton method were compared statement-by-statement. The inspected sources do not state the affine inactive-scenario obstruction or the exact pair of automatic steepest-model inequalities. Targeted searches by article identifier, assumption number, active/inactive scenario language, and model-decrement terminology found no equivalent published result or correction.

A residual risk is a later or poorly indexed erratum. None was located.

## Value

PASS. The finding isolates a structural mismatch between worst-case active-set descent and a condition imposed on all uncertainty scenarios. It also supplies exact intrinsic inequalities from the same subproblem, providing a concrete route toward removing the extraneous inactive-scenario restriction rather than merely identifying a notation issue.

Self-review: passed. Independent audit: not yet performed.
