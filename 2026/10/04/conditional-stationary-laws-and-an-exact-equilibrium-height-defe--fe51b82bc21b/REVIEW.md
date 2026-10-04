# Same-model review

## Correctness
PASS. Arbitrary antiderivative test functions give
\[
\mathbb E[y\mid x]=x,
\qquad
\mathbb E[xy\mid z]=bz.
\]
With \(d=y-x\), exact differentiation gives
\[
L\left(
xd-\frac{c-a}{2a}x^2
\right)
=
a d^2+(2c-a-z)x^2.
\]
This proves the defect. Its equality case is reconstructed using support invariance and yields exactly the three equilibrium atoms. Strict defect forces positive mass above the equilibrium height, and zero mean plus positive variance of \(y-x\) forces both signs. The packaged checker verifies the algebra.

Risk: the equality classification uses the standard invariance of the support of an invariant probability measure under the complete flow restricted to that compact support.

## Originality
PASS. The full 2000 same-object analysis gives the equations, equilibria, bifurcation structure, periodic windows, and a Poincare section at \(z=2c-a\), but not the accepted invariant-measure identities. The 2003 abstract advertises a stronger-looking trajectory-crossing theorem, so possible overlap with the height-crossing corollary is retained as a risk. Its accessible statement does not imply the two conditional laws, exact weighted defect, or equality classification. Exact-object semantic searches returned no same-object coverage of those core statements.

Risk: the complete 2003 paper was unavailable for full-text comparison.

## Value
PASS. The established Chen-system literature already makes \(z=2c-a\) a meaningful equilibrium and Poincare height. The theorem turns that level into a universal recurrence barrier valid for every non-equilibrium compact invariant statistical state and supplies exact conditional stationary laws and a quantitative defect. For the classical attractor, this gives the concrete necessary excursion \(z>21\).

Same-model review: passed. Independent audit: not yet performed.
