# Exact stationary RMS law and a sharp recurrence boundary for the Jafari–Sprott NE6 flow
## Finding
Consider the one-parameter NE6 flow
\[
\dot x=y,\qquad
\dot y=z,\qquad
\dot z=-y-xz-yz-a,
\]
where
\[
a\in\mathbb R.
\]

Every compactly supported invariant probability measure \(\mu\) satisfies
\[
\mathbb E_\mu[y\mid x]=0,
\qquad
\mathbb E_\mu[z\mid y]=0,
\]
together with
\[
\mathbb E_\mu[y]
=
\mathbb E_\mu[z]
=
\mathbb E_\mu[xy]
=
\mathbb E_\mu[yz]
=
0.
\]
Its central stationary balance is
\[
\boxed{\mathbb E_\mu[y^2]=a}
\]
and simultaneously
\[
\boxed{\mathbb E_\mu[xz]=-a}.
\]

These identities give a sharp parameter trichotomy for compact stationary recurrence.

If
\[
a<0,
\]
there is no compactly supported invariant probability measure.

If
\[
a=0,
\]
the compactly supported invariant probability measures are exactly the compactly supported probability measures on the equilibrium line
\[
\{(x,0,0):x\in\mathbb R\}.
\]

If
\[
a>0,
\]
then every compactly supported invariant probability measure, whenever one exists, has
\[
\operatorname{Var}_\mu(y)=a,
\qquad
\operatorname{Cov}_\mu(x,z)=-a,
\]
and
\[
\operatorname{Var}_\mu(x)\operatorname{Var}_\mu(z)\ge a^2.
\]
It also gives positive mass to both
\[
y>0
\qquad\text{and}\qquad
y<0.
\]

For the source value
\[
a=\frac34,
\]
the stationary \(y\)-amplitude is fixed exactly:
\[
\sqrt{\mathbb E_\mu[y^2]}
=
\frac{\sqrt3}{2}.
\]

## Assumptions and scope
The measure \(\mu\) is a Borel probability measure invariant under the polynomial flow and supported on a compact subset of \(\mathbb R^3\). Compact support guarantees integrability of all coordinate and polynomial test functions used in the proof.

The equations are Case NE6 in the original catalog of elementary quadratic chaotic flows without equilibria. The source value is
\[
a=\frac34,
\]
for which the original paper reports a dissipative strange attractor, a positive largest Lyapunov exponent, and a period-doubling route to chaos.

The parameter \(a\) is retained as the natural constant forcing in the source family. The theorem does not assert existence of a compact invariant measure for every positive value of \(a\); its positive-\(a\) conclusions are necessary identities for any such measure.

The earliest verified public source date is 16 January 2013, when the foundational article became available online.

## Proof
Let \(L\) be the generator of the flow.

For any continuous function \(\phi\) on the compact \(x\)-range, choose an antiderivative \(H\) with
\[
H'(x)=\phi(x).
\]
Then
\[
LH=\phi(x)y.
\]
Invariance gives
\[
\mathbb E_\mu[\phi(x)y]=0
\]
for every such \(\phi\), hence
\[
\mathbb E_\mu[y\mid x]=0.
\]
In particular,
\[
\mathbb E_\mu[y]=0
\]
and
\[
\mathbb E_\mu[xy]=0.
\]

Similarly, for any continuous function \(\psi\) on the compact \(y\)-range, choose an antiderivative \(K\) with
\[
K'(y)=\psi(y).
\]
Since
\[
LK=\psi(y)z,
\]
stationarity gives
\[
\mathbb E_\mu[z\mid y]=0.
\]
Consequently,
\[
\mathbb E_\mu[z]=0
\]
and
\[
\mathbb E_\mu[yz]=0.
\]

Now
\[
L(xy)
=
y^2+xz.
\]
Therefore
\[
\mathbb E_\mu[y^2]
+
\mathbb E_\mu[xz]
=
0.
\]

Stationarity of the coordinate \(z\) gives
\[
0
=
-\mathbb E_\mu[y]
-\mathbb E_\mu[xz]
-\mathbb E_\mu[yz]
-a.
\]
Using the already established zero moments yields
\[
\mathbb E_\mu[xz]=-a.
\]
Substitution into the \(xy\) balance gives
\[
\mathbb E_\mu[y^2]=a.
\]

If
\[
a<0,
\]
this contradicts the nonnegativity of \(y^2\), so no compact invariant probability measure exists.

Suppose
\[
a=0.
\]
Then
\[
\mathbb E_\mu[y^2]=0,
\]
so \(y=0\) almost surely and the invariant support lies in the plane \(y=0\). Invariance of the support requires tangency to that plane:
\[
0=\dot y=z.
\]
Hence the support lies in
\[
y=z=0.
\]
For \(a=0\), every point
\[
(x,0,0)
\]
is an equilibrium. Thus every invariant measure is supported on this equilibrium line, and conversely every compactly supported probability measure on that line is invariant.

Finally suppose
\[
a>0.
\]
Because
\[
\mathbb E[y]=\mathbb E[z]=0,
\]
the exact balances give
\[
\operatorname{Var}(y)=a,
\qquad
\operatorname{Cov}(x,z)=\mathbb E[xz]=-a.
\]
Cauchy–Schwarz gives
\[
a^2
=
\operatorname{Cov}(x,z)^2
\le
\operatorname{Var}(x)\operatorname{Var}(z).
\]

Since
\[
\mathbb E[y]=0
\qquad\text{and}\qquad
\mathbb E[y^2]=a>0,
\]
the measure cannot be supported in either closed half-space \(y\ge0\) or \(y\le0\) without being concentrated on \(y=0\). Therefore
\[
\mu\{y>0\}>0
\qquad\text{and}\qquad
\mu\{y<0\}>0.
\]

## Verification
The accompanying checker uses exact sparse-polynomial arithmetic over rational coefficients.

It verifies
\[
Lx=y,
\qquad
Ly=z,
\]
\[
L\left(\frac{x^2}{2}\right)=xy,
\qquad
L\left(\frac{y^2}{2}\right)=yz,
\]
and
\[
L(xy)=y^2+xz.
\]

It also replays the stationary algebra
\[
\mathbb E[y]=
\mathbb E[z]=
\mathbb E[xy]=
\mathbb E[yz]=0
\]
to recover
\[
\mathbb E[xz]=-a,
\qquad
\mathbb E[y^2]=a,
\]
and verifies the source specialization
\[
a=\frac34,
\qquad
\sqrt{\mathbb E[y^2]}=\frac{\sqrt3}{2}.
\]

The stored checker output is `VERIFY_OK`.

The conditional laws use arbitrary one-variable antiderivative test functions, and the \(a=0\) classification uses invariance of the compact support. Those analytic steps are not finite experiments.

## Relationship to prior work
Jafari, Sprott, and Hashemi Golpayegani introduced NE6 in their 2013 catalog of seventeen elementary three-dimensional quadratic chaotic flows without equilibria. Their Table 1 gives exactly
\[
\dot x=y,\qquad
\dot y=z,\qquad
\dot z=-y-xz-yz-a
\]
with
\[
a=\frac34.
\]
They report a positive largest Lyapunov exponent and show a period-doubling route to chaos as \(a\) varies. The full article was inspected directly. Searches within it for invariant measures, averages, moments, variance, and mean-square relations did not locate a stationary-statistics theorem.

Cafagna and Grassi later singled out NE6 as the integer-order starting point for an elegant fractional-order system without equilibria. Their analysis concerns Caputo fractional dynamics, predictor-corrector simulation, Lyapunov calculations, the \(0\)-\(1\) chaos test, and fractional circuit elements. It does not provide the integer-order invariant-measure balance above.

A later mathematical study of chaotic mechanisms in jerk systems cites the Jafari–Sprott catalog in its jerk-system literature and is classified under MSC \(34C28\), among related ordinary-differential-equation classifications. Its stated results concern local bifurcations and mechanisms of chaotic motion rather than stationary invariant-measure identities.

Targeted searches for the exact RMS law, the covariance law, the conditional formulations, and the \(a=0\) recurrence boundary did not locate a same-object statement implying the theorem.

## Limitations
The positive-\(a\) theorem is conditional on existence of a compactly supported invariant probability measure. It does not prove existence of a strange attractor or periodic orbit for every
\[
a>0.
\]

The source's chaotic attractor at
\[
a=\frac34
\]
is reported numerically; the present proof does not turn that numerical observation into an independent existence proof.

The theorem fixes selected stationary moments and conditional means but not the complete invariant distribution.

The fractional-order follow-up is dynamically different from the integer-order flow and is used only for literature comparison. A short stationary identity could occur in unindexed or differently phrased later literature; this remains a residual originality risk.

## References
1. S. Jafari, J. C. Sprott, and S. M. R. Hashemi Golpayegani, “Elementary quadratic chaotic flows with no equilibria,” Physics Letters A 377, 699–702 (2013), DOI 10.1016/j.physleta.2013.01.009.
2. D. Cafagna and G. Grassi, “Elegant Chaos in Fractional-Order System without Equilibria,” Mathematical Problems in Engineering 2013, 380436, DOI 10.1155/2013/380436.
3. X. Hu, B. Sang, and N. Wang, “The chaotic mechanisms in some jerk systems,” AIMS Mathematics 7, 15714–15740 (2022), DOI 10.3934/math.2022861.
