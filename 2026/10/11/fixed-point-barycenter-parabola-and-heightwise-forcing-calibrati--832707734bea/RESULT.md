# Fixed-point barycenter parabola and heightwise forcing calibration in the Genesio flow
## Finding
Consider the Genesio system
\[
\dot x=y,
\qquad
\dot y=z,
\qquad
\dot z=x^2-cx-by-az,
\]
with
\[
a>0,\qquad b>0,\qquad c>0.
\]

Let \(\mu\) be any compactly supported invariant Borel probability measure.

The three coordinate layers satisfy exact stationary regressions:
\[
\boxed{
\mathbb E_\mu[y\mid x]=0
},
\]
\[
\boxed{
\mathbb E_\mu[z\mid y]=0
},
\]
and
\[
\boxed{
\mathbb E_\mu[x^2-cx-by\mid z]=az
}.
\]

Write
\[
m=\int x\,d\mu.
\]
The first two regressions give
\[
\mathbb E_\mu[y]=0,
\qquad
\mathbb E_\mu[z]=0.
\]
Averaging the third then yields
\[
\mathbb E_\mu[x^2]=cm.
\]
Therefore
\[
\boxed{
\operatorname{Var}_\mu(x)=m(c-m)
}.
\]

Hence every invariant barycenter lies on the segment joining the two equilibria
\[
p_0=(0,0,0),
\qquad
p_c=(c,0,0):
\]
\[
\boxed{
\int(x,y,z)\,d\mu=(m,0,0),
\qquad
0\le m\le c
}.
\]

The variance parabola gives the sharp parameter-only envelope
\[
\boxed{
\operatorname{Var}_\mu(x)\le\frac{c^2}{4}
}.
\]
Equality is attained by the invariant measure
\[
\frac12\delta_{p_0}+\frac12\delta_{p_c}.
\]

More generally, the unique two-equilibrium mixture with barycenter
\[
(m,0,0)
\]
has exactly the same \(x\)-variance as \(\mu\).

The endpoint cases are rigid:
\[
m=0
\]
occurs exactly for
\[
\mu=\delta_{p_0},
\]
and
\[
m=c
\]
occurs exactly for
\[
\mu=\delta_{p_c}.
\]

There is also a fiberwise speed-coherence law. Define the nonlinear forcing predictor
\[
Q=x^2-cx-by.
\]
Then
\[
\mathbb E_\mu[Q\mid z]=az
\]
and
\[
Q-az=\dot z.
\]
Thus
\[
\boxed{
\operatorname{Var}_\mu(Q)
=
a^2\operatorname{Var}_\mu(z)
+
\mathbb E_\mu[\dot z^2]
}
\]
and
\[
\boxed{
\operatorname{Cov}_\mu(z,Q)
=
a\operatorname{Var}_\mu(z)
}.
\]

The speed defect vanishes exactly for invariant measures supported on
\[
\{p_0,p_c\}.
\]
Consequently every compact stationary state not supported on those equilibria has
\[
\operatorname{Var}_\mu(z)>0,
\qquad
\mathbb E_\mu[\dot z^2]>0,
\]
and
\[
\boxed{
0<
\operatorname{Corr}_\mu(z,Q)
<
1
}.
\]
More precisely,
\[
\boxed{
\operatorname{Corr}_\mu(z,Q)
=
\left(
1+
\frac{
\mathbb E_\mu[\dot z^2]
}{
a^2\operatorname{Var}_\mu(z)
}
\right)^{-1/2}
}.
\]

For the standard chaotic parameter set
\[
a=1.2,\qquad b=2.92,\qquad c=6,
\]
the barycenter is confined to the fixed-point segment
\[
0\le m\le6,
\]
the sharp variance envelope is
\[
\operatorname{Var}_\mu(x)\le9,
\]
and the heightwise predictor is
\[
Q=x^2-6x-2.92y,
\qquad
\mathbb E[Q\mid z]=1.2z.
\]

A previously published Genesio recurrence balance,
\[
\mathbb E[z^2]=b\mathbb E[y^2],
\]
is prior coverage and is not part of the originality claim assessed here.

## Assumptions and scope
The theorem concerns the classical three-dimensional Genesio flow with positive parameters
\[
a,b,c.
\]
Compact support guarantees integrability of every polynomial observable and every one-coordinate antiderivative test used below.

The standard chaotic example has
\[
a=1.2,\qquad b=2.92,\qquad c=6.
\]

The original Genesio–Tesi harmonic-balance article was published on 1 May 1992. A modern mathematical treatment writes the same vector field and classifies it primarily under MSC \(34C23\), with additional dynamical-systems classifications.

No ergodicity assumption is needed. The theorem applies to periodic-orbit measures, compact chaotic invariant measures, equilibrium atoms, and convex mixtures.

## Proof
Let \(L\) denote the generator of the Genesio flow.

Choose any continuous function \(\phi\) on the compact \(x\)-range of the support and an antiderivative \(H\) satisfying
\[
H'(x)=\phi(x).
\]
Then
\[
LH
=
\phi(x)y.
\]
Invariance gives
\[
\mathbb E_\mu[\phi(x)y]=0
\]
for every \(\phi\), hence
\[
\mathbb E_\mu[y\mid x]=0.
\]

Likewise, arbitrary antiderivative tests in \(y\) give
\[
\mathbb E_\mu[\psi(y)z]=0
\]
for every continuous \(\psi\), so
\[
\mathbb E_\mu[z\mid y]=0.
\]

Finally, arbitrary antiderivative tests in \(z\) give
\[
\mathbb E_\mu[
\chi(z)
(x^2-cx-by-az)
]=0.
\]
Therefore
\[
\mathbb E_\mu[x^2-cx-by\mid z]=az.
\]

Taking expectations in the first two identities gives
\[
\mathbb E[y]=0,
\qquad
\mathbb E[z]=0.
\]
Taking expectations in the third gives
\[
\mathbb E[x^2]-c\mathbb E[x]-b\mathbb E[y]
=
a\mathbb E[z],
\]
hence
\[
\mathbb E[x^2]=cm.
\]
Subtracting \(m^2\) proves
\[
\operatorname{Var}(x)=m(c-m).
\]

Nonnegativity of variance forces
\[
m\in[0,c].
\]
The barycenter is
\[
(m,0,0),
\]
so it lies on the fixed-point segment.

The concave quadratic
\[
m(c-m)
\]
has maximum
\[
c^2/4
\]
at
\[
m=c/2.
\]
The equal mixture of the two equilibrium atoms has that barycenter and variance, proving sharpness.

If
\[
m=0
\]
or
\[
m=c,
\]
then
\[
\operatorname{Var}(x)=0.
\]
Thus \(x\) is constant on the invariant support. Along every support trajectory,
\[
\dot x=y
\]
forces
\[
y=0.
\]
Then
\[
\dot y=z
\]
forces
\[
z=0.
\]
Finally
\[
0=\dot z=x(x-c),
\]
so the support is the corresponding equilibrium. The converse is immediate.

For the speed law, write
\[
Q=x^2-cx-by.
\]
The third regression says
\[
\mathbb E[Q\mid z]=az.
\]
Since
\[
Q=az+\dot z
\]
and
\[
\mathbb E[\dot z\mid z]=0,
\]
conditional orthogonality gives
\[
\operatorname{Var}(Q)
=
a^2\operatorname{Var}(z)
+
\mathbb E[\dot z^2]
\]
and
\[
\operatorname{Cov}(z,Q)
=
a\operatorname{Var}(z).
\]

Suppose
\[
\mathbb E[\dot z^2]=0.
\]
Because the vector field is continuous, \(\dot z\) vanishes on the invariant support, so \(z\) is constant along every support trajectory. Bounded completeness and
\[
\dot y=z
\]
force
\[
z=0.
\]
Then \(y\) is constant, and bounded completeness with
\[
\dot x=y
\]
forces
\[
y=0.
\]
Finally
\[
0=\dot z=x(x-c),
\]
so every support point is one of the two equilibria.

Conversely, every measure supported on those equilibria has
\[
\dot z=0.
\]

If
\[
\operatorname{Var}(z)=0,
\]
the same constant-height argument forces equilibrium support. Therefore any non-equilibrium-supported invariant measure has positive \(z\)-variance and positive speed defect. Substituting the covariance and variance formulas into the Pearson correlation gives the displayed strict formula.

## Verification
The packaged checker uses only the Python standard library and exact rational arithmetic.

It verifies the pointwise residual identity
\[
Q-az=\dot z,
\]
the mean–variance factorization
\[
cm-m^2=m(c-m),
\]
the sharp quadratic maximum
\[
m(c-m)\le c^2/4,
\]
and the abstract conditional-regression variance and covariance algebra.

For
\[
a=\frac65,\qquad
b=\frac{73}{25},\qquad
c=6,
\]
it verifies the sharp value
\[
c^2/4=9
\]
and the exact predictor coefficient
\[
a=\frac65.
\]

The stored checker output is `VERIFY_OK`.

No finite trajectory computation is used to prove an invariant-measure statement.

## Relationship to prior work
Genesio and Tesi introduced harmonic-balance methods for chaotic nonlinear feedback systems and the system now bearing their names. The checked publication record dates the Automatica article to 1 May 1992.

A complete open 2012 article studies the exact Genesio system with distributed-delay feedback. It develops equilibrium stability, characteristic equations, Hopf bifurcation, center-manifold reduction, and numerical chaos control. Full-document searches located no invariant-measure, moment, or variance theorem matching the accepted statement.

A complete 2013 same-object article recasts the Genesio flow as a jerk system, proves its Newtonian-jerk representation, studies equilibria and Hopf bifurcations, and numerically analyzes Lyapunov exponents and coexisting attractors. Its complete searchable text contains no occurrence of `variance`, `moment`, `average`, or `invariant measure`.

A modern mathematical treatment writes exactly
\[
\dot x=y,\qquad
\dot y=z,\qquad
\dot z=-cx-by-az+x^2
\]
and studies the global phase portrait at infinity, Hopf bifurcation, invariant algebraic surfaces, exponential factors, and integrability. Its accessible publication page lists primary MSC \(34C23\). The publisher full text was not accessible in the checked route, so this source is not used for blanket whole-document noncoverage.

Published semantic-index searches located an earlier Genesio result proving
\[
\mathbb E[z^2]=b\mathbb E[y^2]
\]
for compact recurrent states and a sharp period floor. That result is treated as prior coverage. It does not implication-wise determine
\[
\operatorname{Var}(x)=m(c-m)
\]
or the fiberwise law
\[
\mathbb E[x^2-cx-by\mid z]=az.
\]

The accepted theorem therefore concerns a different exact structure: the fixed-point barycenter parabola and the conditional nonlinear-forcing calibration with its vertical speed defect.

## Limitations
The theorem is conditional on compactly supported invariant probability measures. It does not establish existence of a strange attractor for arbitrary parameters.

The barycenter parabola determines only the first two moments of \(x\), not the full invariant distribution.

The fiberwise law determines the conditional mean of
\[
x^2-cx-by
\]
given \(z\), not its full conditional distribution.

The complete 1992 publisher article was not available in the checked route. The 2025 publisher page exposed the exact system, abstract, references, and MSC classification, while its full text required access.

The earlier published Genesio recurrence balance and period-floor result are excluded from the originality claim.

Because the generator proof is short, a differently phrased equivalent observation could remain in unindexed literature.

## References
1. R. Genesio and A. Tesi, “Harmonic balance methods for the analysis of chaotic dynamics in nonlinear systems,” Automatica 28, 531–548 (1992), DOI 10.1016/0005-1098(92)90177-H.
2. J. Guan, F. Chen, and G. Wang, “Chaos control and Hopf bifurcation analysis of the Genesio system with distributed delays feedback,” Advances in Difference Equations 2012, 166 (2012), DOI 10.1186/1687-1847-2012-166.
3. Ö. Umut and S. Yaşar, “A Simple Jerky Dynamics, Genesio System,” International Journal of Modern Nonlinear Theory and Application 2, 60–68 (2013), DOI 10.4236/ijmnta.2013.21007.
4. C. Valls, “Global dynamical aspects and integrability analysis of the Genesio system,” Discrete and Continuous Dynamical Systems B 30, 3206–3221 (2025), DOI 10.3934/dcdsb.2025016.
