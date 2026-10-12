# An explicit empty-Wolfe-step example for an admissible inexact Moreau oracle
## Finding

Consider Algorithm 1 of the recent Wolfe-type spectral conjugate-gradient method and its admissible inexact Moreau oracle. The paper requires an approximate minimizer \(p^a(x,\varepsilon)\) satisfying
\[
f(p^a)+\frac{1}{2\lambda}\lVert p^a-x\rVert^2\le F(x)+\varepsilon,
\]
and then defines \(F^a\) and \(g^a\) from that selected point.

Even for the one-dimensional smooth strongly convex quadratic
\[
f(z)=\frac12 z^2,
\]
the paper's two Wolfe-type inequalities can have no common positive step.

Take
\[
\lambda=1,\qquad x_0=\frac1{10},\qquad \varepsilon_0=\frac14,\qquad \varepsilon_1=\frac15,
\]
and Wolfe parameters
\[
\delta=\frac14,\qquad \sigma=\frac12.
\]
For this quadratic,
\[
F(x)=\frac{x^2}{4},
\]
and the inner objective has the exact decomposition
\[
\frac12 z^2+\frac12(z-x)^2
=
\frac{x^2}{4}+\left(z-\frac{x}{2}\right)^2.
\]
Thus every selection
\[
p^a(x,\varepsilon)=\frac{x}{2}+e,
\qquad e^2\le\varepsilon,
\]
is admissible under the source condition, with
\[
F^a(x,\varepsilon)=\frac{x^2}{4}+e^2,
\qquad
g^a(x,\varepsilon)=\frac{x}{2}-e.
\]

At the initial point choose
\[
e_0=-\frac9{20}.
\]
Then
\[
\widetilde g_0=\frac12,
\qquad
d_0=-\frac12,
\qquad
F^a(x_0,\varepsilon_0)=\frac{41}{200}.
\]
At tolerance \(\varepsilon_1\), define the admissible oracle selection by
\[
e(x)=
\begin{cases}
-\frac25,&x>-\frac15,\\
\frac25,&x\le-\frac15.
\end{cases}
\]
The choice is admissible everywhere because
\[
\left(\frac25\right)^2=\frac4{25}<\frac15.
\]

Along the source trial ray
\[
x(\alpha)=x_0+\alpha d_0=\frac1{10}-\frac\alpha2,
\]
the switch occurs exactly at \(\alpha=3/5\).

For
\[
0<\alpha<\frac35,
\]
we have
\[
g^a(x(\alpha),\varepsilon_1)=\frac9{20}-\frac\alpha4>\frac3{10}>\frac14.
\]
Because \(d_0=-1/2\), the source curvature inequality is equivalent to
\[
g^a(x(\alpha),\varepsilon_1)\le \sigma\widetilde g_0=\frac14,
\]
so curvature fails throughout this interval.

For
\[
\alpha\ge\frac35,
\]
the sufficient-decrease inequality reduces exactly to
\[
25\alpha^2+15\alpha-17\le0.
\]
Its positive root is
\[
\alpha_\star=\frac{\sqrt{77}-3}{10}<\frac35.
\]
Therefore sufficient decrease fails throughout the second branch.

Hence there is no positive \(\alpha\) satisfying both Wolfe-type conditions. Algorithm 1 can therefore be undefined at its first line search under an oracle that satisfies the paper's stated inexactness rule.

## Assumptions and scope

The objective \(f(z)=\tfrac12 z^2\) is finite-valued, smooth, locally Lipschitz, convex, and strongly convex. Its Moreau envelope is coercive and bounded below, so the example does not rely on an unbounded level set or a nonsmooth pathology.

The construction targets only well-definedness of the paper's Wolfe-type Step 2 under the admissible oracle model. It does not assert failure when the approximate minimizer is selected by a continuous deterministic inner solver, nor does it assess later iterations under a repaired selection rule.

The initial approximate gradient is nonzero, so any stopping tolerance strictly below \(1/2\) reaches the line-search step.

## Proof

For \(f(z)=z^2/2\) and \(\lambda=1\), completing the square gives
\[
\frac12 z^2+\frac12(z-x)^2
=
\frac{x^2}{4}+\left(z-\frac{x}{2}\right)^2.
\]
The exact proximal point is \(x/2\) and the exact Moreau envelope is \(F(x)=x^2/4\). Therefore, if
\[
p^a(x,\varepsilon)=\frac{x}{2}+e,
\]
then the source admissibility condition is precisely \(e^2\le\varepsilon\), and the source surrogate quantities are
\[
F^a(x,\varepsilon)=\frac{x^2}{4}+e^2,
\qquad
g^a(x,\varepsilon)=\frac{x}{2}-e.
\]

At \(x_0=1/10\), \(\varepsilon_0=1/4\), and \(e_0=-9/20\), admissibility holds since \(81/400<1/4\). Direct substitution gives
\[
\widetilde g_0=\frac12,
\qquad d_0=-\frac12,
\qquad F^a(x_0,\varepsilon_0)=\frac{41}{200}.
\]

At \(\varepsilon_1=1/5\), both branch errors \(e=\pm2/5\) are admissible. Along \(x(\alpha)=1/10-\alpha/2\), the threshold \(x=-1/5\) is reached at \(\alpha=3/5\).

On the first branch,
\[
g^a=\frac9{20}-\frac\alpha4.
\]
The source curvature condition is
\[
g^a d_0\ge\sigma\widetilde g_0d_0,
\]
which, because \(d_0<0\), is equivalent to \(g^a\le1/4\). But for \(0<\alpha<3/5\),
\[
g^a>\frac3{10}>\frac14.
\]
Thus curvature fails.

On the second branch,
\[
F^a(x(\alpha),\varepsilon_1)-F^a(x_0,\varepsilon_0)
=
\frac{\alpha^2}{16}-\frac{\alpha}{40}-\frac{17}{400}.
\]
The source sufficient-decrease right side is
\[
\delta\alpha\widetilde g_0d_0=-\frac{\alpha}{16}.
\]
Hence sufficient decrease is equivalent to
\[
25\alpha^2+15\alpha-17\le0.
\]
The polynomial is increasing for \(\alpha>0\), and at \(\alpha=3/5\) it equals \(1\). Equivalently, its positive root is \((\sqrt{77}-3)/10<3/5\). Thus sufficient decrease fails for every \(\alpha\ge3/5\).

The two branches cover all positive steps, proving that the Wolfe-type line-search set is empty.

## Verification

The bundled script `artifacts/verify_wolfe_empty.py` uses exact rational arithmetic. It checks the initial surrogate quantities, oracle admissibility, a dense rational replay of the trial ray, and the exact branch inequalities. It returns `VERIFY_OK`.

The script is supporting evidence. The proof of emptiness is the exact two-branch argument above.

## Relationship to prior work

The primary paper states the inexact minimizer condition, defines \(F^a\) and \(g^a\), and then instructs Algorithm 1 to choose a positive step satisfying the two Wolfe-type inequalities. Its manuscript does not prove existence of such a step for the arbitrary admissible selection \(p^a(x,\varepsilon)\).

A public machine review of the same manuscript independently identified this missing existence argument as load-bearing and suggested trying a discontinuous admissible oracle on a one-dimensional example. That review did not provide an explicit counterexample. The construction here supplies one and strengthens the concern by using a smooth strongly convex quadratic rather than a nonsmooth function.

Classical Wolfe line-search theory, including Hager--Zhang's smooth setting, works with a fixed differentiable objective and its genuine gradient. Those existence mechanisms do not imply existence for a surrogate assembled from an arbitrary discontinuous approximate minimizer selection.

Targeted searches using the paper identifier, inexact Moreau oracle terminology, Wolfe-step existence, discontinuous oracle aliases, and strongly convex quadratic counterexamples did not locate an earlier explicit witness equivalent to this one.

## Limitations

The result exploits the full freedom allowed by the paper's condition on the approximate minimizer. A concrete continuous inner algorithm could impose additional regularity that rules out this selection.

The finding does not determine the weakest extra oracle regularity sufficient for Wolfe-step existence. Natural repairs include requiring a suitably continuous selection, using the exact Moreau envelope in the line search, or proving termination for a concrete inner-solver/line-search coupling.

The result does not reassess claims unrelated to the line-search existence issue.

## References

1. Jauny, G. Kumar, *A Wolfe-Type Spectral Conjugate Gradient Method for Nonsmooth Convex Optimization Problems*, arXiv:2608.11689v1, 2026.
2. W. W. Hager, H. Zhang, *A New Conjugate Gradient Method with Guaranteed Descent and an Efficient Line Search*, SIAM Journal on Optimization 16(1), 170--192, DOI: 10.1137/030601880.
3. Pith, *Review of A Wolfe-Type Spectral Conjugate Gradient Method for Nonsmooth Convex Optimization Problems*, record KOJKEG3V, 2026.
