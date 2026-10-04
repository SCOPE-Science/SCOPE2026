# Same-model review

## Correctness
PASS. Arbitrary one-variable generator tests give
\[
\mathbb E[x\mid z]=0
\]
and
\[
y\bigl(\mathbb E[x^2\mid y]-1\bigr)=0.
\]
The exact identities for \(L(z^2)\), \(L(x^2)\), and \(Ly\) imply
\[
\mathbb E[y]=\mathbb E[x^2].
\]
The invariant negative-y region is incompatible with that nonnegative mean-square identity. The invariant plane \(y=0\) is an anti-stable linear system whose only bounded complete trajectory is the origin, giving the exact origin-mass formula. The unit-cylinder equality case is also incompatible with compact invariance because \(z'=\mu x\ne0\) there. The packaged checker verifies the polynomial algebra and invariant-plane characteristic polynomial.

Risk: the support arguments use standard invariance of the support of a compactly supported invariant probability measure and the elementary spectral classification of a two-dimensional linear system.

## Originality
PASS. The inspected full primary source gives the exact equations, unique equilibrium, Lyapunov calculations, parameter-driven toroidal behavior, and sensitive dependence of coexisting attractors. It contains no invariant-measure, stationary-average, or moment formulation, and its final remarks explicitly call for further analytical treatment. Exact-object semantic searches for conditional, unit-amplitude, half-space, and periodic-crossing formulations found no same-object coverage.

Risk: a differently phrased or poorly indexed later statement could have escaped the targeted searches.

## Value
PASS. The source's main phenomenon is coexistence of distinct attractors under the same parameters. The theorem identifies structure common to every compact recurrent statistical state: no stationary mass can lie below \(y=0\), every positive-y slice has unit conditional mean-square \(x\), and every non-origin component has exact mean \(y\) and mean-square \(x\) equal to one. The forced crossing of \(|x|=1\) supplies a geometric consequence for every nonconstant recurrent component.

Same-model review: passed. Independent audit: not yet performed.
