# Heightwise wave-feedback calibration and stationary moment geometry in the Lorenz–Stenflo flow
## Finding
Consider the Lorenz–Stenflo system
\[
\dot x=\sigma(y-x)+s w,
\qquad
\dot y=x(r-z)-y,
\]
\[
\dot z=xy-bz,
\qquad
\dot w=-x-\sigma w,
\]
with
\[
\sigma>0,\qquad b>0,\qquad r>0,\qquad s>0.
\]

Let \(\mu\) be any compactly supported invariant Borel probability measure.

The quadratic wave-feedback product is calibrated exactly on every height fiber:
\[
\boxed{
\mathbb E_\mu[xy\mid z]=bz
}.
\]

Thus the nonlinear input \(xy\) in the height equation is not merely balanced after global averaging. Its conditional mean is exactly linear in the instantaneous height coordinate for every compact stationary state.

Write
\[
m=\int z\,d\mu.
\]
Then two exact global moment laws hold:
\[
\boxed{
\mathbb E_\mu[x^2]
+
s\mathbb E_\mu[w^2]
=
bm
}
\]
and
\[
\boxed{
\mathbb E_\mu[y^2]
+
b\operatorname{Var}_\mu(z)
=
bm(r-m)
}.
\]

Consequently
\[
0\le m<r.
\]
Moreover,
\[
m=0
\]
occurs exactly for the origin atom. Hence every non-origin compact stationary state satisfies
\[
\boxed{
0<m<r
}.
\]

The heightwise calibration also has an exact speed-defect form. Since
\[
xy=bz+\dot z,
\]
and the conditional residual has zero mean on every \(z\)-fiber,
\[
\boxed{
\operatorname{Var}_\mu(xy)
=
b^2\operatorname{Var}_\mu(z)
+
\mathbb E_\mu[\dot z^2]
}
\]
and
\[
\boxed{
\operatorname{Cov}_\mu(z,xy)
=
b\operatorname{Var}_\mu(z)
}.
\]

Whenever
\[
\operatorname{Var}_\mu(z)>0,
\]
the correlation is therefore
\[
\boxed{
\operatorname{Corr}_\mu(z,xy)
=
\left(
1+
\frac{
\mathbb E_\mu[\dot z^2]
}{
b^2\operatorname{Var}_\mu(z)
}
\right)^{-1/2}
}.
\]

At the frequently used hyperchaotic parameters
\[
\sigma=1,\qquad b=\frac7{10},\qquad r=26,\qquad s=\frac32,
\]
every non-origin compact stationary state obeys
\[
0<m<26,
\]
\[
\mathbb E[x^2]+\frac32\mathbb E[w^2]=\frac7{10}m,
\]
and
\[
\mathbb E[y^2]
+
\frac7{10}\operatorname{Var}(z)
=
\frac7{10}m(26-m).
\]

Known fixed-point, bifurcation, boundedness, and Lyapunov-region results for the Lorenz–Stenflo system are prior. The finding assessed here is the all-invariant-measures heightwise calibration and the stationary moment geometry that follows from it.

## Assumptions and scope
The vector field is the four-dimensional Lorenz–Stenflo model for acoustic-gravity-wave dynamics,
\[
\dot x=\sigma(y-x)+s w,
\quad
\dot y=x(r-z)-y,
\quad
\dot z=xy-bz,
\quad
\dot w=-x-\sigma w.
\]

Compact support guarantees the integrability of the polynomial observables and one-coordinate antiderivative tests used below.

The model goes back to Stenflo's 1996 generalized Lorenz equations for acoustic-gravity waves in the atmosphere. The historically earlier 1996 and 2010 sources were verified without a day-resolved public publication date in the checked records. The structured full-date field therefore uses 24 August 2013, the earliest checked day-resolved same-object publication, rather than inventing a day for an earlier source.

A mathematical treatment of generalized Lorenz equations for acoustic-gravity waves lists primary MSC \(37L30\). The present result is classified under that dynamical-systems code.

No ergodicity, hyperchaos, or symmetry assumption is imposed. The theorem applies separately to equilibrium atoms, periodic-orbit measures, compact chaotic invariant measures, and convex mixtures.

## Proof
Let \(L\) denote the generator of the flow.

Take any continuous function \(\phi\) on the compact \(z\)-range of the support and choose a continuously differentiable antiderivative \(H\) satisfying
\[
H'(z)=\phi(z).
\]
Then
\[
LH
=
\phi(z)(xy-bz).
\]
Invariance gives
\[
\mathbb E_\mu[\phi(z)(xy-bz)]=0
\]
for every such \(\phi\). Therefore
\[
\mathbb E_\mu[xy\mid z]=bz.
\]

Taking expectations gives
\[
\mathbb E_\mu[xy]=bm.
\]

Next differentiate the quadratic observable
\[
x^2+s w^2.
\]
Using the first and fourth equations,
\[
\begin{aligned}
\frac12\frac{d}{dt}(x^2+s w^2)
&=
x\{\sigma(y-x)+s w\}
+
s w(-x-\sigma w)\\
&=
\sigma xy-\sigma x^2-\sigma s w^2.
\end{aligned}
\]
The cross terms cancel exactly. Stationarity yields
\[
\mathbb E[x^2]+s\mathbb E[w^2]
=
\mathbb E[xy]
=
bm.
\]

Now use the \(y\)- and \(z\)-squared balances. From
\[
\frac12\frac{d}{dt}y^2
=
rxy-xyz-y^2,
\]
stationarity gives
\[
r\mathbb E[xy]
-
\mathbb E[xyz]
-
\mathbb E[y^2]
=
0.
\]
From
\[
\frac12\frac{d}{dt}z^2
=
xyz-bz^2,
\]
stationarity gives
\[
\mathbb E[xyz]
=
b\mathbb E[z^2].
\]
Substituting
\[
\mathbb E[xy]=bm
\]
therefore yields
\[
\mathbb E[y^2]
+
b\mathbb E[z^2]
=
brm.
\]
Since
\[
\mathbb E[z^2]
=
\operatorname{Var}(z)+m^2,
\]
we obtain
\[
\mathbb E[y^2]
+
b\operatorname{Var}(z)
=
bm(r-m).
\]

The left-hand side is nonnegative, so
\[
m\in[0,r].
\]

If
\[
m=0,
\]
then
\[
\mathbb E[y^2]=0
\]
and
\[
\operatorname{Var}(z)=0.
\]
Thus \(y=0\) and \(z=0\) on the invariant support. The equation
\[
\dot y=rx
\]
then forces
\[
x=0,
\]
and
\[
\dot x=s w
\]
forces
\[
w=0.
\]
Hence
\[
\mu=\delta_{(0,0,0,0)}.
\]

If
\[
m=r,
\]
then the same identity forces \(y=0\) and \(z=r\) on the support. But then
\[
\dot z=xy-br=-br\ne0,
\]
contradicting invariance. Hence
\[
m<r.
\]

Finally, from the conditional law,
\[
xy=bz+\dot z
\]
with
\[
\mathbb E[\dot z\mid z]=0.
\]
Conditional orthogonality gives
\[
\operatorname{Var}(xy)
=
b^2\operatorname{Var}(z)
+
\mathbb E[\dot z^2]
\]
and
\[
\operatorname{Cov}(z,xy)
=
b\operatorname{Var}(z).
\]
The correlation formula follows immediately whenever
\[
\operatorname{Var}(z)>0.
\]

## Verification
The accompanying checker uses only the Python standard library and exact rational arithmetic.

It verifies the cancellation in
\[
\frac12\frac{d}{dt}(x^2+s w^2)
=
\sigma xy-\sigma x^2-\sigma s w^2,
\]
the elimination of the mixed third moment between the stationary \(y^2\)- and \(z^2\)-balances, and the factorization
\[
brm-bm^2
=
bm(r-m).
\]

It also verifies the abstract conditional-regression variance and covariance decomposition for
\[
xy=bz+\dot z
\]
under
\[
\mathbb E[\dot z\mid z]=0.
\]

At
\[
\sigma=1,\qquad b=\frac7{10},\qquad r=26,\qquad s=\frac32,
\]
the checker verifies the exact coefficient values in the displayed moment laws.

The stored checker output is `VERIFY_OK`.

No finite trajectory simulation is used to prove an invariant-measure statement.

## Relationship to prior work
Stenflo introduced the generalized Lorenz equations for acoustic-gravity waves in 1996.

Xavier and Rech study the Lorenz–Stenflo system through fixed-point stability, pitchfork and Hopf bifurcations, parameter-space plots, Lyapunov exponents, bifurcation diagrams, periodic windows, and chaotic attractors. Their accessible publisher-preview text writes the same four equations used here.

Wang, Li, and Hu derive ultimate bounds and positively invariant sets for the hyperchaotic Lorenz–Stenflo system. Later boundedness work uses quadratic Lyapunov functions whose derivatives exploit the cancellation structure of the vector field. Those results are prior and no novelty is claimed for boundedness, absorbing regions, or quadratic Lyapunov cancellation.

A complete open 2013 article treats the same hyperchaotic Lorenz–Stenflo equations, including the parameter set
\[
\sigma=1,\qquad b=0.7,\qquad r=26,\qquad s=1.5,
\]
and develops chaos control and generalized synchronization. Its full searchable text contains no matching conditional-expectation, invariant-measure, or variance theorem.

Published mathematical work on generalized Lorenz equations for acoustic-gravity waves studies attractor dimension, convergence, and homoclinic trajectories and supplies primary MSC \(37L30\).

The accepted statement is distinct from these orbitwise and bounding results. It gives an exact disintegration law,
\[
\mathbb E[xy\mid z]=bz,
\]
for every compact invariant probability measure and combines it with two stationary quadratic balances to obtain the mean-height moment geometry
\[
\mathbb E[y^2]+b\operatorname{Var}(z)=bm(r-m).
\]

## Limitations
The theorem is conditional on compactly supported invariant probability measures. It does not prove that a chaotic or hyperchaotic attractor exists for arbitrary parameters.

The conditional law determines the conditional mean of \(xy\) given \(z\), not the full conditional distribution.

The interval
\[
0<m<r
\]
for non-origin stationary states is a necessary condition, not a complete existence classification.

The historically earliest 1996 source was verified without a day-resolved public date in the checked records, so no artificial day was assigned.

The principal same-object full-text comparison is the complete open 2013 article. Some earlier publisher material was available only as previews or bibliographic records.

Because the invariant-measure generator argument is short, a differently phrased equivalent observation could remain in unindexed literature.

## References
1. L. Stenflo, “Generalized Lorenz equations for acoustic-gravity waves in the atmosphere,” Physica Scripta 53, 83–84 (1996), DOI 10.1088/0031-8949/53/1/015.
2. J. C. Xavier and P. C. Rech, “Regular and Chaotic Dynamics of the Lorenz–Stenflo System,” International Journal of Bifurcation and Chaos 20, 145–152 (2010), DOI 10.1142/S0218127410025466.
3. P. Wang, D. Li, and Q. Hu, “Bounds of the hyper-chaotic Lorenz–Stenflo system,” Communications in Nonlinear Science and Numerical Simulation 15, 2514–2520 (2010), DOI 10.1016/j.cnsns.2009.09.015.
4. Y. Li, Y. Zhao, and Z. A. Yao, “Chaotic control and generalized synchronization for a hyperchaotic Lorenz-Stenflo system,” Abstract and Applied Analysis 2013, 515106 (2013), DOI 10.1155/2013/515106.
5. G. A. Leonov, “Generalized Lorenz Equations for Acoustic-Gravity Waves in the Atmosphere. Attractors Dimension, Convergence and Homoclinic Trajectories,” Communications on Pure and Applied Analysis 16, 2253–2263 (2017), DOI 10.3934/cpaa.2017111.
6. F. Zhang and W. Zhang, “Complex Dynamical Behaviors of Lorenz-Stenflo Equations,” Mathematics 7, 513 (2019), DOI 10.3390/math7060513.
