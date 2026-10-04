# Same-model review

## Correctness
PASS. Arbitrary antiderivative tests in the two recovery coordinates give
\[
\mathbb E[x^2\mid y]=\frac{c-y}{d},
\qquad
\mathbb E[x\mid z]=x_R+\frac{z}{s}.
\]
Their conditional residuals are exactly \(-\dot y/d\) and \(\dot z/(rs)\), yielding
\[
d^2\operatorname{Var}(x^2)-\operatorname{Var}(y)=\mathbb E[\dot y^2]
\]
and
\[
s^2\operatorname{Var}(x)-\operatorname{Var}(z)=r^{-2}\mathbb E[\dot z^2].
\]
Invariant-support rigidity proves the stated equality cases. The packaged checker verifies the polynomial identities exactly.

Risk: the equality classification uses standard invariance of the support and bounded completeness.

## Originality
PASS. The foundational article, a full same-object energy paper, and a modern mathematical treatment were compared. The energy paper's global long-run balance does not imply conditional identities against arbitrary functions of the recovery variables. Direct and alias searches found no same-object theorem stating the conditional laws or the derivative-energy variance defects.

Risk: because the identities are short, an incidental differently worded observation in unindexed neuroscience or control literature may remain.

## Value
PASS. The result resolves stationary voltage statistics along the two natural recovery coordinates and turns the remaining variance into an exact dynamical activity measure. Equality distinguishes equilibrium-supported states from genuinely active recurrence, providing a reusable analytic and numerical consistency test for a canonical bursting-neuron model.

Same-model review: passed. Independent audit: not yet performed.
