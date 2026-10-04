# Exact radial transport and a variance–barycenter circle for the dissipative Ikeda map
## Finding
Consider the dissipative complex Ikeda family
\[
T(z)=A+u e^{i\Theta(|z|^2)}z,
\]
where
\[
A>0,
\qquad
0<u<1,
\]
and
\[
\Theta:[0,\infty)\to\mathbb R
\]
is continuous.

This includes the familiar normal form of the Ikeda map, in which a constant injected field is followed by a nonlinear phase rotation and a dissipative round-trip factor.

Let \(\mu\) be any compactly supported \(T\)-invariant Borel probability measure. Then the entire radial distribution about the injection point is a scaled copy of the radial distribution about the origin:
\[
\boxed{
(|z-A|)_\#\mu=(u|z|)_\#\mu
}.
\]
Equivalently, for every bounded Borel function \(\phi:[0,\infty)\to\mathbb R\),
\[
\boxed{
\int \phi(|z-A|)\,d\mu(z)
=
\int \phi(u|z|)\,d\mu(z)
}.
\]

Thus every radial moment, quantile, and distribution function is constrained exactly, independently of the nonlinear phase law \(\Theta\).

The second moment gives a particularly geometric consequence. Define
\[
c=\frac{A}{1-u^2},
\qquad
R=\frac{Au}{1-u^2},
\qquad
m=\int z\,d\mu(z).
\]
Then
\[
\boxed{
\int |z-m|^2\,d\mu(z)
+
|m-c|^2
=
R^2
}.
\]

Hence the barycenter of every compact invariant measure lies in the closed disk
\[
|m-c|\le R.
\]
The distance of the barycenter from the boundary is not an inequality loss: it is exactly the complex variance
\[
\operatorname{Var}_{\mathbb C}(\mu)
=
\int |z-m|^2\,d\mu(z)
=
R^2-|m-c|^2.
\]

Therefore every invariant measure that is not a point mass has
\[
|m-c|<R.
\]
Equality
\[
|m-c|=R
\]
holds exactly for invariant point masses, which are precisely atoms at fixed points of \(T\).

For the customary normalization
\[
A=1,
\qquad
u=0.9,
\]
where \(\nu\) denotes the round-trip dissipation factor, the circle is
\[
\boxed{
\int |z-m|^2\,d\mu(z)
+
\left|m-\frac{100}{19}\right|^2
=
\left(\frac{90}{19}\right)^2
}.
\]

The parameter letter \(\nu\) is used in this numerical specialization only to avoid confusing the decimal value with the generic symbol \(u\); mathematically \(\nu=u\).

## Assumptions and scope
The theorem concerns the planar discrete-time map
\[
T(z)=A+u e^{i\Theta(|z|^2)}z
\]
with real \(A>0\), dissipative factor \(0<u<1\), and continuous real phase function \(\Theta\). The phase may be the standard saturating Ikeda phase or another intensity-dependent phase; the proof uses only that the multiplier has unit modulus before the factor \(u\).

The measure \(\mu\) is compactly supported and invariant:
\[
T_\#\mu=\mu.
\]
Compact support guarantees all radial moments used below are finite. The complete pushforward identity itself only requires that the displayed bounded test functions be integrable.

Ikeda's 1979 ring-cavity paper derives the underlying complex difference dynamics, iterates it numerically, and identifies a strange attractor. The widely used simplified planar Ikeda map was developed in the subsequent optical-turbulence literature. A same-object mathematical bifurcation study classifies the Ikeda map under primary MSC \(37G25\) and \(37M20\); the present finding is placed under \(37G25\).

The first verified public date for the foundational ring-cavity difference-map source is 1 August 1979. The primary PDF itself identifies the issue as August 1979; the day field is supplied by a bibliographic article record.

## Proof
The defining map has the pointwise metric identity
\[
|T(z)-A|
=
\left|u e^{i\Theta(|z|^2)}z\right|
=
u |z|,
\]
where here and below \(\nu=u\).

Let \(\phi\) be any bounded Borel function on \([0,\infty)\). Invariance gives
\[
\int \phi(|z-A|)\,d\mu(z)
=
\int \phi(|T(z)-A|)\,d\mu(z).
\]
Using the pointwise identity,
\[
\int \phi(|z-A|)\,d\mu(z)
=
\int \phi(\nu|z|)\,d\mu(z).
\]
This is exactly
\[
(|z-A|)_\#\mu=(\nu|z|)_\#\mu.
\]

Take
\[
\phi(r)=r^2.
\]
Then
\[
\mathbb E|Z-A|^2
=
\nu^2\mathbb E|Z|^2,
\]
where \(Z\) has law \(\mu\). Since \(A\) is real,
\[
(1-\nu^2)\mathbb E|Z|^2
-2A\operatorname{Re}\mathbb E Z
+A^2
=0.
\]

Define
\[
c=\frac{A}{1-\nu^2}.
\]
Completing the square gives
\[
(1-\nu^2)\mathbb E|Z-c|^2
=
\frac{A^2\nu^2}{1-\nu^2}.
\]
Therefore
\[
\mathbb E|Z-c|^2
=
\left(
\frac{A\nu}{1-\nu^2}
\right)^2
=R^2.
\]

Now write
\[
m=\mathbb E Z.
\]
The Hilbert-space variance decomposition gives
\[
\mathbb E|Z-c|^2
=
\mathbb E|Z-m|^2
+
|m-c|^2.
\]
Thus
\[
\mathbb E|Z-m|^2+|m-c|^2=R^2.
\]

The variance term is nonnegative, so \(|m-c|\le R\). It vanishes exactly when \(Z=m\) almost surely, that is, when \(\mu=\delta_m\). Such a point mass is invariant exactly when
\[
T(m)=m.
\]
Hence equality in the barycenter-disk bound is equivalent to a fixed-point atom.

For
\[
A=1,
\qquad
\nu=\frac9{10},
\]
we have
\[
1-\nu^2=\frac{19}{100},
\qquad
c=\frac{100}{19},
\qquad
R=\frac{90}{19},
\]
which yields the stated specialization.

## Verification
The accompanying checker verifies the second-moment completion of the square and the standard-parameter specialization using exact rational arithmetic.

Starting from
\[
(1-u^2)\mathbb E|Z|^2
-2A\operatorname{Re}\mathbb E Z
+A^2=0,
\]
it checks algebraically that
\[
\mathbb E|Z-c|^2
=
\frac{A^2u^2}{(1-u^2)^2}
\]
with
\[
c=\frac{A}{1-u^2}.
\]

For
\[
A=1,
\qquad
u=\frac9{10},
\]
the checker verifies
\[
c=\frac{100}{19},
\qquad
R=\frac{90}{19}.
\]

The complete radial pushforward identity is a direct consequence of invariance and the pointwise equality \(|T(z)-A|=u|z|\); it is not inferred from numerical sampling of an attractor.

The stored checker output is `VERIFY_OK`.

## Relationship to prior work
Ikeda's 1979 paper derives complex difference equations for a nonlinear optical ring cavity, iterates them, and reports periodic windows and a strange attractor. The source is concerned with optical bistability, stability loss, and the appearance of chaotic transmitted-light dynamics.

Ikeda, Daido, and Akimoto's 1980 optical-turbulence work established the now-standard reduced-map viewpoint for chaotic ring-cavity dynamics. The present theorem does not claim the map, its attractor, or its period-doubling route as new.

Osinga and Rankin study boundary crises, homoclinic and heteroclinic tangencies, saddle-node bifurcations, and subduction channels in the Ikeda map. Their open article page identifies primary MSC \(37G25\) and \(37M20\). Those bifurcation results concern creation and destruction of attractors rather than exact statistics shared by every invariant measure.

Ampilova and Soloviev explicitly approximate invariant measures of the Ikeda map by symbolic-image stationary flows and compute metric entropy. Their complete open article contains an Ikeda-map invariant-measure example, but targeted searches do not reveal a mean, moment, or variance identity of the form proved here.

Recent Ikeda-map work continues to emphasize bifurcation diagrams, shrimp structures, Lyapunov exponents, multistability, and transitions between regular and chaotic phases. The accepted statement is orthogonal to that program: it gives a phase-independent radial transport law for every compact invariant probability measure and an exact relation between its barycenter and total variance.

## Limitations
The theorem exploits the affine-plus-rotated-copy form
\[
T(z)=A+u e^{i\Theta(|z|^2)}z.
\]
It does not apply unchanged to extensions with anisotropic gain, additive noise, multiple coupled cavities, or non-scalar loss.

The variance–barycenter circle does not determine the full invariant measure, metric entropy, Lyapunov spectrum, fractal dimension, or basin geometry.

The result is independent of the phase function, which is a strength for universality but means it does not distinguish among different phase-induced bifurcation scenarios.

The 1979 primary source is a more general ring-cavity difference model; the simple normal form is standard in subsequent Ikeda-map literature. A short radial-moment observation could remain in unindexed optical-chaos literature.

## References
1. K. Ikeda, “Multiple-valued stationary state and its instability of the transmitted light by a ring cavity system,” Optics Communications 30, 257–261 (1979), DOI 10.1016/0030-4018(79)90090-7.
2. K. Ikeda, H. Daido, and O. Akimoto, “Optical Turbulence: Chaotic Behavior of Transmitted Light from a Ring Cavity,” Physical Review Letters 45, 709–712 (1980), DOI 10.1103/PhysRevLett.45.709.
3. H. M. Osinga and J. Rankin, “Two-parameter locus of boundary crisis: Mind the gaps!,” AIMS Conference Publications 2011, 1148–1157 (2011), DOI 10.3934/proc.2011.2011.1148.
4. N. Ampilova and I. Soloviev, “On a method of applied symbolic dynamics for investigation of dynamical systems,” Vibroengineering PROCEDIA 25, 128–134 (2019), DOI 10.21595/vp.2019.20698.
5. D. F. M. Oliveira, “Mapping chaos: Bifurcation patterns and shrimp structures in the Ikeda map,” Chaos 34, 123137 (2024), DOI 10.1063/5.0238147.
