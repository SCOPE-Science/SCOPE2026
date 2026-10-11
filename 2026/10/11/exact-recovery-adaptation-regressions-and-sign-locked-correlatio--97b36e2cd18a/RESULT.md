# Exact recovery–adaptation regressions and sign-locked correlations in Hindmarsh–Rose bursting
## Finding
Consider the three-dimensional Hindmarsh–Rose neuron model
\[
\dot x
=
y-a x^3+b x^2-z+I,
\]
\[
\dot y
=
c-dx^2-y,
\]
\[
\dot z
=
r\left[s(x-x_R)-z\right],
\]
with
\[
a>0,\qquad d>0,\qquad r>0,\qquad s>0,
\]
and arbitrary real
\[
b,\qquad c,\qquad I,\qquad x_R.
\]

Let \(\mu\) be any compactly supported invariant Borel probability measure.

Then all three coordinates satisfy exact stationary regressions:
\[
\boxed{
\mathbb E_\mu[y-z\mid x]
=
a x^3-bx^2-I
},
\]
\[
\boxed{
\mathbb E_\mu[x^2\mid y]
=
\frac{c-y}{d}
},
\]
and
\[
\boxed{
\mathbb E_\mu[x\mid z]
=
x_R+\frac{z}{s}
}.
\]

The corresponding regression residuals are precisely the three coordinate speeds. Therefore
\[
\boxed{
\operatorname{Var}_\mu(y-z)
-
\operatorname{Var}_\mu(a x^3-bx^2-I)
=
\mathbb E_\mu[\dot x^2]
},
\]
\[
\boxed{
d^2\operatorname{Var}_\mu(x^2)
-
\operatorname{Var}_\mu(y)
=
\mathbb E_\mu[\dot y^2]
},
\]
and
\[
\boxed{
s^2\operatorname{Var}_\mu(x)
-
\operatorname{Var}_\mu(z)
=
\frac{1}{r^2}\mathbb E_\mu[\dot z^2]
}.
\]

The fast recovery and slow adaptation variables have exact sign-locked stationary covariances:
\[
\boxed{
\operatorname{Cov}_\mu(x^2,y)
=
-\frac{1}{d}\operatorname{Var}_\mu(y)
}
\]
and
\[
\boxed{
\operatorname{Cov}_\mu(x,z)
=
\frac{1}{s}\operatorname{Var}_\mu(z)
}.
\]

The second regression also forces
\[
\boxed{
\operatorname{supp}\mu\subseteq\{y\le c\}
}.
\]

Each of the three variance defects vanishes exactly when \(\mu\) is supported on equilibria.

Hence every compact stationary state that is not equilibrium-supported has strict defects. In particular,
\[
-1
<
\operatorname{Corr}_\mu(x^2,y)
<
0
<
\operatorname{Corr}_\mu(x,z)
<
1.
\]
More precisely,
\[
\operatorname{Corr}_\mu(x^2,y)
=
-
\sqrt{
1-
\frac{
\mathbb E_\mu[\dot y^2]
}{
d^2\operatorname{Var}_\mu(x^2)
}
},
\]
and
\[
\operatorname{Corr}_\mu(x,z)
=
\sqrt{
1-
\frac{
\mathbb E_\mu[\dot z^2]
}{
r^2s^2\operatorname{Var}_\mu(x)
}
}.
\]

Thus the observed recovery anticorrelation and adaptation correlation are not merely qualitative features of a chosen bursting orbit: for every compact recurrent statistical state, their signs and magnitudes are tied exactly to unresolved coordinate-speed energy.

## Assumptions and scope
The theorem concerns the autonomous three-dimensional Hindmarsh–Rose flow on \(\mathbb R^3\). Compact support guarantees integrability of the polynomial observables and arbitrary one-variable antiderivative tests used below.

The parameter assumptions
\[
a,d,r,s>0
\]
match the standard neuronal interpretation: the cubic voltage term is dissipative at large positive and negative voltage, \(d\) couples voltage square into fast recovery, \(r\) sets the slow timescale, and \(s\) couples voltage into adaptation.

The model was introduced by Hindmarsh and Rose in 1984. The verified publication date of the three-variable bursting article is 22 March 1984.

A same-object mathematical article classifies the autonomous Hindmarsh–Rose system under primary MSC \(34C23\), with additional codes \(34C25\), \(34C60\), and \(34D10\). The present statement is classified under \(34C23\).

No ergodicity assumption is needed. The formulas apply to periodic-orbit measures, invariant measures on chaotic compact sets, equilibrium atoms, and convex mixtures of compact invariant measures.

## Proof
Let \(L\) denote the generator of the Hindmarsh–Rose flow.

Take a continuously differentiable function \(H\) of \(x\), with derivative
\[
H'(x)=\phi(x)
\]
for an arbitrary continuous test function \(\phi\) on the compact \(x\)-range. Then
\[
LH
=
\phi(x)
\left[
y-a x^3+b x^2-z+I
\right].
\]
Invariance gives
\[
\mathbb E_\mu
\left[
\phi(x)
\left(
y-z-a x^3+b x^2+I
\right)
\right]
=
0
\]
for every \(\phi\). Hence
\[
\mathbb E_\mu[y-z\mid x]
=
a x^3-bx^2-I.
\]

The identical argument with arbitrary antiderivatives of \(y\) gives
\[
\mathbb E_\mu[c-dx^2-y\mid y]=0,
\]
so
\[
\mathbb E_\mu[x^2\mid y]
=
\frac{c-y}{d}.
\]

Likewise, antiderivative tests in \(z\) give
\[
\mathbb E_\mu[s(x-x_R)-z\mid z]=0,
\]
hence
\[
\mathbb E_\mu[x\mid z]
=
x_R+\frac{z}{s}.
\]

The variance identities are conditional-orthogonality decompositions.

For the \(x\)-equation set
\[
A=y-z,
\qquad
B=a x^3-bx^2-I.
\]
The regression says
\[
\mathbb E[A\mid x]=B,
\]
and
\[
A-B=\dot x.
\]
Therefore
\[
\operatorname{Var}(A)
=
\operatorname{Var}(B)
+
\mathbb E[\dot x^2].
\]

For the \(y\)-equation set
\[
A=c-dx^2,
\qquad
B=y.
\]
Then
\[
\mathbb E[A\mid y]=B,
\qquad
A-B=\dot y.
\]
Thus
\[
d^2\operatorname{Var}(x^2)
-
\operatorname{Var}(y)
=
\mathbb E[\dot y^2].
\]

For the \(z\)-equation set
\[
A=s(x-x_R),
\qquad
B=z.
\]
Then
\[
\mathbb E[A\mid z]=B,
\qquad
A-B=\frac{\dot z}{r}.
\]
Hence
\[
s^2\operatorname{Var}(x)
-
\operatorname{Var}(z)
=
\frac1{r^2}\mathbb E[\dot z^2].
\]

The two covariance identities follow directly from the same regressions. For recovery,
\[
\mathbb E[x^2y]
=
\frac1d
\mathbb E[y(c-y)].
\]
Since
\[
\mathbb E[x^2]
=
\frac{c-\mathbb E[y]}{d},
\]
subtraction gives
\[
\operatorname{Cov}(x^2,y)
=
-\frac{\operatorname{Var}(y)}{d}.
\]

For adaptation,
\[
\mathbb E[xz]
=
x_R\mathbb E[z]
+
\frac1s\mathbb E[z^2],
\]
while
\[
\mathbb E[x]
=
x_R+\frac1s\mathbb E[z].
\]
Therefore
\[
\operatorname{Cov}(x,z)
=
\frac{\operatorname{Var}(z)}{s}.
\]

Because
\[
x^2\ge0,
\]
the conditional law
\[
\mathbb E[x^2\mid y]
=
\frac{c-y}{d}
\]
implies
\[
y\le c
\]
almost surely. Since \(\{y\le c\}\) is closed, the invariant support lies in that half-space.

It remains to prove the equality classification.

If the first variance defect is zero, then
\[
\dot x=0
\]
on almost every invariant trajectory, so \(x\) is constant. With \(x\) fixed, the other two coordinates satisfy scalar stable linear equations
\[
\dot y=(c-dx^2)-y,
\qquad
\dot z=r(s(x-x_R)-z).
\]
A nonconstant solution of either equation is unbounded backward in time. Every trajectory in a compact invariant set is complete and bounded, so both \(y\) and \(z\) must be constant. The trajectory is an equilibrium.

If the second defect is zero, then \(y\) is constant and
\[
x^2=\frac{c-y}{d}
\]
is constant. Continuity forces \(x\) itself to be constant. Then the \(x\)-equation forces \(z\) constant, so the trajectory is an equilibrium.

If the third defect is zero, then \(z\) is constant and
\[
x=x_R+\frac{z}{s}
\]
is constant. The \(x\)-equation then forces \(y\) constant, again giving an equilibrium.

Conversely, every equilibrium-supported invariant measure makes all three defects vanish.

For a non-equilibrium compact stationary state, the \(y\)- and \(z\)-defects are therefore strictly positive, and neither relevant variance vanishes. Combining
\[
\operatorname{Cov}(x^2,y)
=
-\frac{\operatorname{Var}(y)}d
\]
with
\[
d^2\operatorname{Var}(x^2)
=
\operatorname{Var}(y)+\mathbb E[\dot y^2]
\]
gives the exact negative-correlation formula. The adaptation formula follows identically from
\[
\operatorname{Cov}(x,z)
=
\frac{\operatorname{Var}(z)}s
\]
and
\[
s^2\operatorname{Var}(x)
=
\operatorname{Var}(z)
+
\frac1{r^2}\mathbb E[\dot z^2].
\]

## Verification
The accompanying checker uses only the Python standard library and exact rational arithmetic.

It verifies the three pointwise residual identities:
\[
(y-z)-(a x^3-bx^2-I)=\dot x,
\]
\[
(c-dx^2)-y=\dot y,
\]
and
\[
s(x-x_R)-z=\frac{\dot z}{r}.
\]

It checks the generic regression-variance algebra
\[
\operatorname{Var}(A)-\operatorname{Var}(B)
=
\mathbb E[(A-B)^2]
\]
under
\[
\mathbb E[A]=\mathbb E[B],
\qquad
\mathbb E[AB]=\mathbb E[B^2].
\]

It also verifies the covariance reductions from the recovery and adaptation regression moments.

The stored checker output is `VERIFY_OK`.

The conditional-expectation statements, support implication, and equilibrium-rigidity arguments are analytic and are not inferred from finite numerical trajectories.

## Relationship to prior work
Hindmarsh and Rose introduced the three-variable bursting model in 1984. The original article develops the fast subsystem, equilibria, separatrices, limit cycles, addition of the slow third equation, and periodic bursting under steady applied current.

Barrio and Shilnikov provide a complete open same-object computational study. They write the standard equations
\[
\dot x=y-a x^3+b x^2-z+I,
\qquad
\dot y=c-dx^2-y,
\qquad
\dot z=\varepsilon[s(x-x_0)-z],
\]
and analyze spike counts, interspike intervals, duty cycles, Lyapunov exponents, slow manifolds, homoclinic bifurcations, spike adding, multistability, periodic bursting, and chaotic regimes. Document-wide searches located no conditional-expectation, moment, covariance, or variance theorem matching the accepted statement.

Llibre and Valls study the same polynomial burster from Darboux-integrability theory, characterizing invariant algebraic surfaces, exponential factors, and integrable parameter cases. Those structural algebraic results do not imply the accepted stationary regressions for arbitrary compact invariant probability measures.

Musafirov studies admissible perturbations preserving reflecting functions for the autonomous Hindmarsh–Rose system and classifies that work under MSC \(34C23\), \(34C25\), \(34C60\), and \(34D10\). The paper's accessible scientific statement concerns reflecting functions, bifurcation diagrams, periodic attractors, and strange attractors rather than invariant-measure regression.

A modern controlled-Hindmarsh–Rose study treats Lyapunov stability, codimension-one bifurcations, periodic and chaotic attractors, energy, and Jacobi stability. Targeted accessible-text searches found no conditional, moment, covariance, or variance formulation matching the present result.

Published semantic-index searches used direct conditional-regression language together with moment, covariance, variance-defect, recovery-variable, and slow-adaptation aliases. The closest indexed statements concern conditional invariant-measure laws for different chaotic flows, not the Hindmarsh–Rose neuron.

## Limitations
The theorem assumes compact support. It does not by itself prove existence of a bursting attractor or global boundedness for every parameter set.

The support statement
\[
y\le c
\]
is necessary for compact stationary support; it is not a bifurcation criterion.

The exact correlations concern
\[
x^2
\]
versus \(y\), and \(x\) versus \(z\). They do not determine the full joint invariant density or the spike-count distribution.

The 1984 foundational article is used for provenance and verified date rather than a blanket whole-document novelty exclusion.

The 2023 perturbation article's retrieved web representation exposed the abstract, classification, references, and figures but not all body text. It is therefore not used as a whole-document noncoverage source.

Because the generator arguments are short, a differently phrased equivalent observation could remain in unindexed neuronal-dynamics literature.

## References
1. J. L. Hindmarsh and R. M. Rose, “A model of neuronal bursting using three coupled first order differential equations,” Proceedings of the Royal Society of London. Series B 221, 87–102 (1984), DOI 10.1098/rspb.1984.0024.
2. R. Barrio and A. Shilnikov, “Parameter-sweeping techniques for temporal dynamics of neuronal systems: case study of Hindmarsh-Rose model,” Journal of Mathematical Neuroscience 1, 6 (2011), DOI 10.1186/2190-8567-1-6.
3. J. Llibre and C. Valls, “On the Darboux Integrability of the Hindmarsh-Rose Burster,” Acta Mathematica Sinica, English Series 34, 947–958 (2018), DOI 10.1007/s10114-017-5661-1.
4. E. Musafirov, “Admissible perturbations of the three-dimensional Hindmarsh–Rose neuron model,” Journal of Applied Analysis & Computation 13, 1668–1678 (2023), DOI 10.11948/20210098.
5. Q. Yang and X. Lu, “Dynamics and Jacobi stability of the controlled 3D Hindmarsh-Rose neuron model,” Discrete and Continuous Dynamical Systems B 29, 2227–2256 (2024), DOI 10.3934/dcdsb.2023175.
