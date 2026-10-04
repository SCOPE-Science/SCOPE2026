# Fiberwise barycentric calibration on the neutral May–Leonard simplex
## Finding
Consider the classical May–Leonard competition system
\[
\dot x=x(1-x-\alpha y-\beta z),
\]
\[
\dot y=y(1-\beta x-y-\alpha z),
\]
\[
\dot z=z(1-\alpha x-\beta y-z),
\]
with
\[
\alpha>0,\qquad
\beta>0,\qquad
\alpha+\beta=2,\qquad
\alpha\ne1.
\]

Let \(\mu\) be a compactly supported invariant Borel probability measure whose support lies in the strictly positive octant.

Then
\[
\boxed{x+y+z=1}
\]
holds \(\mu\)-almost surely.

More strongly, every own-species abundance determines the conditional mean of each competitor:
\[
\boxed{
\mathbb E_\mu[y\mid x]
=
\mathbb E_\mu[z\mid x]
=
\frac{1-x}{2}
},
\]
\[
\boxed{
\mathbb E_\mu[z\mid y]
=
\mathbb E_\mu[x\mid y]
=
\frac{1-y}{2}
},
\]
and
\[
\boxed{
\mathbb E_\mu[x\mid z]
=
\mathbb E_\mu[y\mid z]
=
\frac{1-z}{2}
}.
\]

Thus the two competitors are conditionally barycentric on every abundance fiber, despite their unequal cyclic interaction coefficients whenever
\[
\alpha\ne\beta.
\]

In particular,
\[
\mathbb E_\mu[x]
=
\mathbb E_\mu[y]
=
\mathbb E_\mu[z]
=
\frac13.
\]

There is also an exact fluctuation law. On the invariant simplex,
\[
\frac{\dot x}{x}
=
(\alpha-1)(z-y),
\]
\[
\frac{\dot y}{y}
=
(\alpha-1)(x-z),
\]
and
\[
\frac{\dot z}{z}
=
(\alpha-1)(y-x).
\]
Therefore
\[
\boxed{
\mathbb E_\mu
\left[
\left(\frac{\dot x}{x}\right)^2
+
\left(\frac{\dot y}{y}\right)^2
+
\left(\frac{\dot z}{z}\right)^2
\right]
=
3(\alpha-1)^2
\left[
\operatorname{Var}_\mu(x)
+
\operatorname{Var}_\mu(y)
+
\operatorname{Var}_\mu(z)
\right]
}.
\]

The simplex reduction and global mean values are treated as prior phenomena. The finding assessed here is the fiberwise conditional calibration and the exact distribution-level fluctuation identity.

## Assumptions and scope
The measure \(\mu\) is invariant under the autonomous May–Leonard flow and has compact support contained in
\[
(0,\infty)^3.
\]
Compactness inside the open positive octant gives positive lower bounds on \(x\), \(y\), and \(z\), so logarithmic test functions are legitimate.

The parameter relation
\[
\alpha+\beta=2
\]
is the classical neutral May–Leonard case. Published treatments describe periodic motion on the plane
\[
x+y+z=1
\]
in this regime. The degenerate point
\[
\alpha=\beta=1
\]
is excluded because every positive point on that simplex is an equilibrium and the two unequal cyclic interaction directions collapse into one.

The foundational May–Leonard article was published in September 1975. Mathematical bibliographic metadata for that article lists MSC \(34C15\), \(34C25\), and \(34C60\), together with biological-dynamics classifications. The present result is classified under \(34C15\).

## Proof
Write
\[
N=x+y+z.
\]
Summing the three equations and using
\[
\alpha+\beta=2
\]
gives
\[
\dot N
=
N-N^2
=
N(1-N).
\]

Because the support is compactly contained in the positive octant,
\[
N>0
\]
on the support. Stationarity of
\[
\log N
\]
gives
\[
0
=
\mathbb E_\mu\!\left[\frac{\dot N}{N}\right]
=
1-\mathbb E_\mu[N].
\]
Hence
\[
\mathbb E_\mu[N]=1.
\]
Stationarity of \(N\) itself gives
\[
0
=
\mathbb E_\mu[N-N^2],
\]
so
\[
\mathbb E_\mu[N^2]=1.
\]
Therefore
\[
\operatorname{Var}_\mu(N)=0,
\]
and consequently
\[
N=1
\]
almost surely.

Now fix a continuous function \(\phi\) on the compact \(x\)-range. Since \(x\) is bounded away from zero, choose a continuously differentiable function \(H\) satisfying
\[
H'(x)=\frac{\phi(x)}{x}.
\]
The generator gives
\[
LH
=
\phi(x)
\bigl(
1-x-\alpha y-\beta z
\bigr).
\]
Invariance implies
\[
\mathbb E_\mu[
\phi(x)
(
1-x-\alpha y-\beta z
)
]
=
0
\]
for every such \(\phi\). Thus
\[
\mathbb E_\mu[
\alpha y+\beta z
\mid x
]
=
1-x.
\]

But
\[
y+z=1-x
\]
holds pointwise on the invariant simplex. Therefore
\[
\alpha\mathbb E_\mu[y\mid x]
+
\beta\mathbb E_\mu[z\mid x]
=
\mathbb E_\mu[y+z\mid x].
\]
Subtracting and using
\[
\beta=2-\alpha
\]
gives
\[
(\alpha-1)
\left(
\mathbb E_\mu[y\mid x]
-
\mathbb E_\mu[z\mid x]
\right)
=
0.
\]
Since
\[
\alpha\ne1,
\]
we obtain
\[
\mathbb E_\mu[y\mid x]
=
\mathbb E_\mu[z\mid x].
\]
Their sum is
\[
1-x,
\]
so each is
\[
\frac{1-x}{2}.
\]

The two cyclic laws follow identically.

Taking expectations in
\[
\mathbb E_\mu[y\mid x]
=
\frac{1-x}{2}
\]
gives
\[
\mathbb E_\mu[y]
=
\frac{1-\mathbb E_\mu[x]}{2}.
\]
The cyclic analogues form a nonsingular three-equation system whose unique solution is
\[
\mathbb E_\mu[x]
=
\mathbb E_\mu[y]
=
\mathbb E_\mu[z]
=
\frac13.
\]

For the fluctuation identity, use
\[
x+y+z=1
\]
and
\[
\beta=2-\alpha.
\]
Then
\[
\begin{aligned}
\frac{\dot x}{x}
&=
1-x-\alpha y-(2-\alpha)z\\
&=
y+z-\alpha y-(2-\alpha)z\\
&=
(\alpha-1)(z-y).
\end{aligned}
\]
Cyclically,
\[
\frac{\dot y}{y}
=
(\alpha-1)(x-z),
\]
and
\[
\frac{\dot z}{z}
=
(\alpha-1)(y-x).
\]

Hence
\[
\sum_{\rm cyc}
\left(
\frac{\dot x}{x}
\right)^2
=
(\alpha-1)^2
\left[
(x-y)^2+(y-z)^2+(z-x)^2
\right].
\]

The elementary identity
\[
(x-y)^2+(y-z)^2+(z-x)^2
=
3(x^2+y^2+z^2)-(x+y+z)^2
\]
and
\[
x+y+z=1
\]
give
\[
\mathbb E_\mu
\left[
(x-y)^2+(y-z)^2+(z-x)^2
\right]
=
3\mathbb E_\mu[x^2+y^2+z^2]-1.
\]
Since each mean is \(1/3\),
\[
3\mathbb E_\mu[x^2+y^2+z^2]-1
=
3
\left[
\operatorname{Var}_\mu(x)
+
\operatorname{Var}_\mu(y)
+
\operatorname{Var}_\mu(z)
\right].
\]
Substitution proves the displayed fluctuation identity.

## Verification
The accompanying checker uses exact sparse-polynomial arithmetic and rational symbolic reductions.

It verifies that, under
\[
\alpha+\beta=2,
\]
the total population satisfies
\[
\dot N=N-N^2.
\]

It verifies the pointwise reductions
\[
\frac{\dot x}{x}
=
(\alpha-1)(z-y),
\]
\[
\frac{\dot y}{y}
=
(\alpha-1)(x-z),
\]
and
\[
\frac{\dot z}{z}
=
(\alpha-1)(y-x)
\]
after imposing
\[
x+y+z=1.
\]

It also verifies
\[
(x-y)^2+(y-z)^2+(z-x)^2
=
3(x^2+y^2+z^2)-(x+y+z)^2.
\]

Finally, exact linear algebra confirms that the three cyclic conditional-mean consequences have the unique global mean
\[
\left(\frac13,\frac13,\frac13\right).
\]

The stored checker output is `VERIFY_OK`.

The conditional-expectation step itself follows from invariant-measure testing against arbitrary one-variable logarithmic antiderivatives; it is not inferred from finite simulation.

## Relationship to prior work
May and Leonard introduced the three-species competition system in 1975. Their foundational analysis identified a special class of periodic limit cycles and nonperiodic oscillatory behavior with increasing cycle time.

The neutral relation
\[
\alpha+\beta=2
\]
and the role of the plane
\[
x+y+z=1
\]
are established parts of the classical theory. A modern full treatment of stochastic May–Leonard models explicitly summarizes that the deterministic system converges to a periodic orbit in this plane when
\[
\alpha+\beta=2.
\]
No novelty is claimed for that invariant plane or for existence of the classical periodic family.

Redheffer later studied mean values for nonautonomous May–Leonard equations. Global time averages and partial-survival phenomena are therefore treated as prior context rather than the originality target here.

Leach and Miritzis analyze the classical May–Leonard system using singularity and symmetry methods to identify integrable parameter values. Their open article focuses on integrability and symmetry; targeted searches of the accessible full article page found no conditional-expectation or variance formulation matching the present result.

Blé, Castellanos, Llibre, and Quilantán-Ortega later study integrability and global dynamics of the May–Leonard model. That work addresses invariant structures and global phase portraits rather than the all-invariant-measures fiberwise barycentric law above.

A recent full deterministic/stochastic treatment writes the classical mean-field May–Leonard equations explicitly and discusses the
\[
\alpha+\beta=2
\]
periodic regime, heteroclinic cycling, and stochastic extinction. Its occurrences of conditional distributions concern stochastic extinction events, not the deterministic stationary conditional means proved here.

Published semantic searches targeted conditional means, own-species fibers, per-capita growth variance, stationary measures, and the neutral simplex. No same-object source was found that implies
\[
\mathbb E[y\mid x]
=
\mathbb E[z\mid x]
=
\frac{1-x}{2}
\]
for every compact positive invariant probability measure or the exact three-species fluctuation identity.

## Limitations
The theorem requires the invariant measure to be compactly supported inside the strictly positive octant. It does not apply directly to invariant measures supported on boundary heteroclinic networks.

The result is specific to the neutral parameter surface
\[
\alpha+\beta=2
\]
and excludes the degenerate point
\[
\alpha=\beta=1.
\]

The theorem determines conditional first moments and one exact aggregate fluctuation law. It does not determine the full invariant density, orbit period, first integral, or phase distribution along a periodic orbit.

The global mean values are not claimed as new. The originality claim is restricted to the fiberwise barycentric conditional law and its exact stationary fluctuation consequence.

Because the proof is short once the invariant simplex is used, an equivalent observation could remain in unindexed ecological-dynamics literature.

## References
1. R. M. May and W. J. Leonard, “Nonlinear Aspects of Competition Between Three Species,” SIAM Journal on Applied Mathematics 29, 243–253 (1975), DOI 10.1137/0129022.
2. R. Redheffer, “Mean values and the nonautonomous May–Leonard equations,” Nonlinear Analysis: Real World Applications 4, 301–306 (2003), DOI 10.1016/S1468-1218(02)00021-4.
3. P. G. L. Leach and J. Miritzis, “Analytic Behaviour of Competition among Three Species,” Journal of Nonlinear Mathematical Physics 13, 535–548 (2006), DOI 10.2991/jnmp.2006.13.4.8.
4. G. Blé, V. Castellanos, J. Llibre, and I. Quilantán-Ortega, “Integrability and global dynamics of the May–Leonard model,” Nonlinear Analysis: Real World Applications 14, 280–293 (2013), DOI 10.1016/j.nonrwa.2012.06.004.
5. N. W. Barendregt and P. J. Thomas, “Heteroclinic cycling and extinction in May–Leonard models with demographic stochasticity,” Journal of Mathematical Biology 86 (2023), DOI 10.1007/s00285-022-01859-4.
