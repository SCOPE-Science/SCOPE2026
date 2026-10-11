# Mutual mean-independence and exact zero covariance in the classical Lotka–Volterra flow
## Finding
Consider the classical predator–prey equations
\[
\dot x
=
x(\alpha-\beta y),
\qquad
\dot y
=
y(-\gamma+\delta x),
\]
with
\[
\alpha>0,\qquad
\beta>0,\qquad
\gamma>0,\qquad
\delta>0.
\]

Let \(\mu\) be any compactly supported invariant Borel probability measure whose support lies in the strictly positive quadrant
\[
(0,\infty)^2.
\]
Define the coexistence-equilibrium coordinates
\[
x_*=\frac{\gamma}{\delta},
\qquad
y_*=\frac{\alpha}{\beta}.
\]

Then the two species obey exact reciprocal regression laws:
\[
\boxed{
\mathbb E_\mu[y\mid x]=y_*
}
\]
and
\[
\boxed{
\mathbb E_\mu[x\mid y]=x_*
}.
\]

Equivalently, for every bounded Borel function \(f\) of \(x\) and every bounded Borel function \(g\) of \(y\),
\[
\boxed{
\mathbb E_\mu[f(x)(y-y_*)]=0
}
\]
and
\[
\boxed{
\mathbb E_\mu[g(y)(x-x_*)]=0
}.
\]
Thus each species is mean-independent of the other.

In particular,
\[
\boxed{
\mathbb E_\mu[x]=x_*,
\qquad
\mathbb E_\mu[y]=y_*
}
\]
and the prey and predator populations have exactly zero stationary covariance:
\[
\boxed{
\operatorname{Cov}_\mu(x,y)=0
}.
\]

The regression residuals are precisely the two per-capita growth rates:
\[
y-y_*
=
-\frac1\beta\frac{\dot x}{x},
\qquad
x-x_*
=
\frac1\delta\frac{\dot y}{y}.
\]
Consequently,
\[
\boxed{
\operatorname{Var}_\mu(y)
=
\frac1{\beta^2}
\mathbb E_\mu
\left[
\left(
\frac{\dot x}{x}
\right)^2
\right]
}
\]
and
\[
\boxed{
\operatorname{Var}_\mu(x)
=
\frac1{\delta^2}
\mathbb E_\mu
\left[
\left(
\frac{\dot y}{y}
\right)^2
\right]
}.
\]

Either variance vanishes if and only if
\[
\mu
=
\delta_{(x_*,y_*)}.
\]
Therefore every other compact stationary state in the positive quadrant has
\[
\operatorname{Var}_\mu(x)>0,
\qquad
\operatorname{Var}_\mu(y)>0,
\]
but nevertheless
\[
\boxed{
\operatorname{Corr}_\mu(x,y)=0
}.
\]

For a nonconstant periodic orbit, its normalized time measure is such a non-equilibrium invariant measure. Hence over every full least period
\[
\boxed{
\langle xy\rangle
=
\langle x\rangle\langle y\rangle
=
x_*y_*
}
\]
even though \(x(t)\) and \(y(t)\) are nonlinearly coupled along a closed orbit.

Moreover the exact means imply that every nonconstant periodic orbit takes values on both sides of each equilibrium nullcline:
\[
x=x_*,
\qquad
y=y_*.
\]
By continuity and periodicity, each coordinate crosses its equilibrium level at least twice per least period.

## Assumptions and scope
The result concerns the classical two-species Lotka–Volterra system in the strictly positive quadrant. Compactness of the invariant support ensures that both coordinates are bounded away from zero, which makes the logarithmic generator tests used below regular on a neighborhood of the support.

No ergodicity assumption is required. The theorem applies to the coexistence equilibrium, every periodic-orbit measure, and compact invariant mixtures of positive recurrent states.

The exact time-average identities
\[
\langle x\rangle=x_*,
\qquad
\langle y\rangle=y_*
\]
are classical consequences of averaging the logarithmic growth equations and are not claimed as the new part. The finding is the stronger pair of conditional laws, their mutual mean-independence consequence, exact zero covariance, and the per-capita-growth variance identities.

Lotka's foundational article was published in the 15 July 1920 issue of the Proceedings of the National Academy of Sciences and writes the same predator–prey equations in its original notation. A mathematical study devoted to periods of the same Volterra–Lotka system is classified under MSC \(34C25\); that classification is used here.

## Proof
Because
\[
\operatorname{supp}\mu
\subset
(0,\infty)^2
\]
is compact, there is a positive lower bound for both coordinates on the support.

Let \(\phi\) be any continuous function on the compact \(x\)-projection of the support. Choose a continuously differentiable function \(H\) near that projection satisfying
\[
H'(x)=\frac{\phi(x)}{x}.
\]
For the flow generator \(L\),
\[
LH
=
H'(x)\dot x
=
\phi(x)(\alpha-\beta y).
\]
Invariance gives
\[
0
=
\int LH\,d\mu
=
\mathbb E_\mu[
\phi(x)(\alpha-\beta y)
].
\]
Since this holds for every continuous \(\phi\),
\[
\mathbb E_\mu[\alpha-\beta y\mid x]=0.
\]
Therefore
\[
\mathbb E_\mu[y\mid x]
=
\frac{\alpha}{\beta}
=
y_*.
\]

The same argument in the \(y\)-coordinate, using
\[
K'(y)=\frac{\psi(y)}{y},
\]
gives
\[
0
=
\mathbb E_\mu[
\psi(y)(-\gamma+\delta x)
]
\]
for every continuous \(\psi\), hence
\[
\mathbb E_\mu[x\mid y]
=
\frac{\gamma}{\delta}
=
x_*.
\]

Taking expectations yields
\[
\mathbb E[x]=x_*,
\qquad
\mathbb E[y]=y_*.
\]

Now choose
\[
\phi(x)=x.
\]
The first conditional law gives
\[
\mathbb E[xy]
=
y_*\mathbb E[x]
=
x_*y_*.
\]
Therefore
\[
\operatorname{Cov}(x,y)
=
\mathbb E[xy]
-
\mathbb E[x]\mathbb E[y]
=
0.
\]

More generally, conditional expectation gives
\[
\mathbb E[f(x)(y-y_*)]=0
\]
for every bounded \(f\), and symmetrically
\[
\mathbb E[g(y)(x-x_*)]=0
\]
for every bounded \(g\). This is exactly mutual mean-independence.

The differential equations give the pointwise residual identities
\[
\frac{\dot x}{x}
=
\alpha-\beta y
=
-\beta(y-y_*),
\]
and
\[
\frac{\dot y}{y}
=
-\gamma+\delta x
=
\delta(x-x_*).
\]
Squaring and integrating proves
\[
\operatorname{Var}(y)
=
\frac1{\beta^2}
\mathbb E
\left[
\left(
\frac{\dot x}{x}
\right)^2
\right]
\]
and
\[
\operatorname{Var}(x)
=
\frac1{\delta^2}
\mathbb E
\left[
\left(
\frac{\dot y}{y}
\right)^2
\right].
\]

Suppose
\[
\operatorname{Var}(y)=0.
\]
Then
\[
y=y_*
\]
on the support. The support of an invariant probability measure is invariant under the flow, so the vector field must be tangent to the line
\[
y=y_*
\]
at every support point. Along that line,
\[
\dot y
=
y_*\delta(x-x_*).
\]
Since
\[
y_*>0,
\]
tangency forces
\[
x=x_*.
\]
Thus the support is the single coexistence equilibrium. The converse is immediate.

The same argument applies when
\[
\operatorname{Var}(x)=0.
\]
Hence every non-equilibrium compact stationary state has both variances positive, while its covariance remains zero, proving the zero-correlation statement.

Finally, let
\[
(x(t),y(t))
\]
be a nonconstant periodic orbit of least period \(P\). Its time measure is invariant, so
\[
\frac1P\int_0^P x(t)\,dt=x_*,
\qquad
\frac1P\int_0^P y(t)\,dt=y_*.
\]
A continuous nonconstant periodic function with average equal to \(x_*\) cannot remain entirely above or entirely below \(x_*\); otherwise its average would be strictly displaced unless it were constant. Thus \(x(t)-x_*\) takes both signs. The same holds for \(y(t)-y_*\). Continuity and periodicity then force at least two zero crossings of each centered coordinate per least period.

## Verification
The accompanying checker uses only the Python standard library and exact rational arithmetic.

It verifies the coexistence coordinates, the two pointwise per-capita residual identities, the conversion of the conditional laws to
\[
\mathbb E[xy]=x_*y_*,
\]
and therefore the exact covariance cancellation.

It also verifies the two variance–speed identities at exact rational test parameters and checks that the coexistence point makes both vector-field components vanish.

The stored checker output is `VERIFY_OK`.

The conditional-expectation step and the invariant-support equality classification are analytic arguments. No finite orbit sampling is used as proof.

## Relationship to prior work
Lotka's 1920 article writes the two multiplicative predator–prey equations, identifies the positive equilibrium, and establishes undamped oscillatory behavior with closed trajectories in the positive quadrant. The complete article contains no covariance formulation; its discussion of an “average” is qualitative rather than the conditional regression theorem proved here.

Waldvogel studies the one-parameter family of periodic Volterra–Lotka solutions and their period. That work concerns period computation and asymptotics, not stationary covariance or conditional expectations.

Grozdanovski and Shepherd give a complete perturbative study of periodic solutions near the coexistence point. Their article writes the same equations, the exact first integral, and Poincaré–Lindstedt approximations. Full-document searches found no occurrence of `average`, `mean`, or `covariance`.

The familiar theorem that the time average of each species equals its coexistence-equilibrium value follows from integrating
\[
\frac{d}{dt}\log x
\quad\text{and}\quad
\frac{d}{dt}\log y.
\]
That scalar average theorem does not imply the stronger identities
\[
\mathbb E[y\mid x]=y_*,
\qquad
\mathbb E[x\mid y]=x_*,
\]
which encode all weighted relations
\[
\mathbb E[f(x)(y-y_*)]=0,
\qquad
\mathbb E[g(y)(x-x_*)]=0.
\]
The exact zero covariance and variance–growth identities are immediate structural consequences of these stronger fiberwise laws.

## Limitations
The theorem is restricted to invariant measures with compact support strictly inside the positive quadrant. Boundary invariant measures involving extinction states are excluded because the logarithmic generator tests become singular there.

The result does not determine the variances themselves, the orbit period, or the full joint distribution.

Zero covariance does not mean statistical independence. A nonconstant periodic-orbit measure is concentrated on a nonlinear closed curve and is strongly dependent even though its Pearson correlation vanishes.

The classical equality of time averages with equilibrium coordinates is prior knowledge and is not claimed as original.

Because the conditional-generator argument is short, an equivalent weighted-average identity could remain in unindexed literature.

## References
1. A. J. Lotka, “Analytical Note on Certain Rhythmic Relations in Organic Systems,” *Proceedings of the National Academy of Sciences* 6, 410–415 (1920), DOI 10.1073/pnas.6.7.410.
2. J. Waldvogel, “The Period in the Volterra–Lotka Predator-Prey Model,” *SIAM Journal on Numerical Analysis* 20, 1264–1272 (1983), DOI 10.1137/0720098.
3. T. Grozdanovski and J. J. Shepherd, “Approximating the periodic solutions of the Lotka–Volterra system,” *ANZIAM Journal* 49, C243–C257 (2008), DOI 10.21914/anziamj.v49i0.353.
