# Universal radial distribution law and sharp mean–variance disk for the Ikeda map
## Finding
Consider the generalized Ikeda plane-wave map
\[
F(z)=c+u e^{i\Theta(|z|^2)}z,
\]
where
\[
c\in\mathbb C\setminus\{0\},\qquad 0<u<1,
\]
and \(\Theta:[0,\infty)\to\mathbb R\) is continuous.

Every invariant Borel probability measure \(\mu\) is automatically supported in
\[
|z|\le \frac{|c|}{1-u}.
\]
No compact-support assumption has to be imposed separately.

The full stationary radial distribution satisfies the exact identity
\[
(|z-c|)_*\mu=(u|z|)_*\mu.
\]
Equivalently, for every bounded Borel function \(\phi\),
\[
\mathbb E_\mu[\phi(|z-c|)]
=
\mathbb E_\mu[\phi(u|z|)].
\]
Thus every radial quantile and every finite radial moment about the pump point \(c\) is obtained from the corresponding origin-centered quantity by multiplication by \(u\).

Define
\[
d=\frac{c}{1-u^2},
\qquad
\rho=\frac{u|c|}{1-u^2}.
\]
Then every invariant probability measure obeys the universal RMS-circle identity
\[
\mathbb E_\mu[|z-d|^2]=\rho^2.
\]
Writing
\[
m=\mathbb E_\mu[z],
\qquad
V=\mathbb E_\mu[|z-m|^2],
\]
one obtains the sharp mean–variance disk
\[
\boxed{
V+|m-d|^2=\rho^2
}.
\]
Hence
\[
|m-d|\le\rho.
\]
Boundary equality holds exactly for fixed-point atoms. Every invariant probability measure that is not a fixed-point atom satisfies
\[
|m-d|<\rho
\]
and has strictly positive variance.

For the standard choice
\[
c=1,
\qquad
u=\frac9{10},
\]
where \(u=\nu\), the support bound and mean–variance law become
\[
|z|\le10
\]
and
\[
V+
\left|m-\frac{100}{19}\right|^2
=
\left(\frac{90}{19}\right)^2.
\]
These identities are independent of the nonlinear phase parameters inside \(\Theta\).

## Assumptions and scope
The theorem applies to the plane-wave Ikeda family
\[
F(z)=c+u e^{i\Theta(|z|^2)}z
\]
with \(0<u<1\). The standard optical model has a nonlinear phase of the form
\[
\Theta(r)=\beta-\frac{\alpha}{1+r},
\]
but the proof uses only that the phase factor has unit modulus.

The first verified public source located for the plane-wave map is the conference paper “Global Dynamics of Ikeda's Plane-Wave Map,” presented at the International Quantum Electronics Conference held 18–21 June 1984. The first day, 18 June 1984, is therefore used as the verified public-source date.

The original optical-cavity work of Ikeda predates this map formulation and motivates the physical model, but the accepted statement is attached to the later plane-wave map itself.

The primary classification is \(37D45\), supported by same-object Ikeda-map chaos literature classified under strange attractors and chaotic dynamics.

## Proof
First note the pointwise estimate
\[
|F(z)|
\le
|c|+u|z|.
\]
Set
\[
R=\frac{|c|}{1-u}.
\]
For \(\varepsilon>0\), let
\[
A_\varepsilon=\{|z|>R+\varepsilon\}.
\]
If \(F(z)\in A_\varepsilon\), then
\[
R+\varepsilon
<|F(z)|
\le
(1-u)R+u|z|,
\]
so
\[
|z|>R+\frac{\varepsilon}{u}.
\]
Hence
\[
F^{-1}(A_\varepsilon)
\subset
A_{\varepsilon/u}.
\]
For an invariant probability measure,
\[
\mu(A_\varepsilon)
=
\mu(F^{-1}(A_\varepsilon))
\le
\mu(A_{\varepsilon/u}).
\]
Iterating gives
\[
\mu(A_\varepsilon)
\le
\mu(A_{\varepsilon/u^n}).
\]
The sets on the right decrease to the empty set as \(n\to\infty\), so continuity from above gives
\[
\mu(A_\varepsilon)=0.
\]
Thus every invariant probability measure is supported in \(|z|\le R\).

Now use the exact pointwise identity
\[
|F(z)-c|=u|z|.
\]
If \(Z\) has law \(\mu\), invariance means \(F(Z)\) also has law \(\mu\). Therefore
\[
|F(Z)-c|
\stackrel{d}{=}
|Z-c|,
\]
while the pointwise identity gives
\[
|F(Z)-c|=u|Z|.
\]
Consequently
\[
|Z-c|
\stackrel{d}{=}
u|Z|,
\]
with the same attenuation parameter, proving
\[
(|z-c|)_*\mu=(u|z|)_*\mu.
\]

Taking squares gives
\[
\mathbb E[|Z-c|^2]
=
u^2\mathbb E[|Z|^2].
\]
Expanding and returning to the symbol \(u\),
\[
(1-u^2)\mathbb E[|Z|^2]
-2\operatorname{Re}(\overline c\,m)
+|c|^2
=0.
\]
Divide by \(1-u^2\) and complete the square about
\[
d=\frac{c}{1-u^2}.
\]
This yields
\[
\mathbb E[|Z-d|^2]
=
\frac{u^2|c|^2}{(1-u^2)^2}
=\rho^2.
\]

The complex bias–variance identity gives
\[
\mathbb E[|Z-d|^2]
=
\mathbb E[|Z-m|^2]+|m-d|^2,
\]
so
\[
V+|m-d|^2=\rho^2.
\]

If \(|m-d|=\rho\), then \(V=0\). Therefore \(Z=m\) almost surely, so \(\mu=\delta_m\). Invariance then forces
\[
F(m)=m,
\]
so \(m\) is a fixed point. Conversely, any fixed-point atom is invariant and the displayed radial identity gives
\[
|m-c|=u|m|,
\]
which is exactly the Apollonius circle
\[
|m-d|=\rho.
\]
Thus the boundary of the mean disk is attained precisely by fixed-point atoms.

## Verification
The accompanying checker uses exact sparse-polynomial and rational arithmetic.

Writing
\[
X=c+u(xC-yS),
\qquad
Y=u(xS+yC),
\]
with
\[
C^2+S^2=1,
\]
it verifies algebraically that
\[
(X-c)^2+Y^2
=
u^2(x^2+y^2),
\]
with the same attenuation parameter.

For
\[
c=1,
\qquad
u=\frac9{10},
\]
it verifies exactly
\[
R=10,
\qquad
d=\frac{100}{19},
\qquad
\rho=\frac{90}{19},
\]
and checks coefficient-by-coefficient that the second-moment balance is equivalent to
\[
\mathbb E\left[
\left|Z-\frac{100}{19}\right|^2
\right]
=
\left(\frac{90}{19}\right)^2.
\]

The stored output is `VERIFY_OK`.

The support argument, distributional pushforward identity, and boundary classification are analytic proofs and are not inferred from finite simulation.

## Relationship to prior work
The 1984 conference paper “Global Dynamics of Ikeda's Plane-Wave Map” and the 1985 article by Hammel, Jones, and Moloney develop the global bifurcation and attractor geometry of the optical ring-cavity map. The accessible 1985 material emphasizes fixed points, bifurcations, attractors, basin boundaries, and the area contraction of the map.

A 2000 study constructs an approximate generating partition for the Ikeda–Hammel–Jones–Moloney map from unstable periodic orbits. A 2005 topological-horseshoe study gives computer-verifiable chaotic dynamics for the Ikeda map and is classified under \(37D45\).

A 2012 full article uses the Ikeda map as an application of a planar horseshoe-detection algorithm, including the standard attenuation value near \(0.9\). Targeted full-text searches did not locate invariant-measure or stationary-moment formulations.

A 2019 full article is the closest implication-level comparison because it explicitly approximates invariant measures and metric entropy for the Ikeda map using symbolic images and stationary graph flows. It does not state a radial pushforward law, mean–variance circle, or fixed-point boundary classification in its Ikeda example.

The accepted result is independent of the detailed nonlinear phase. It extracts a distribution-level invariant from the map's translation-plus-rotation-plus-attenuation structure and then converts it into a sharp two-dimensional mean–variance constraint.

## Limitations
The theorem uses \(0<u<1\). The conservative case \(u=1\) and expansive cases \(u>1\) require different arguments and do not have the same finite center \(d\).

The result constrains radial distributions, means, and variances. It does not determine angular distributions, entropy, Lyapunov exponents, or uniqueness of a physical measure.

The 1985 article was available through substantial publisher-preview material rather than a complete readable article in the inspected source, so no whole-document noncoverage claim is made for it.

Because the radial identity follows from a simple geometric feature of the map, an equivalent observation may exist under optical-power or cavity-energy terminology in literature not indexed by the searches performed.

## References
1. J. V. Moloney, S. Hammel, and C. Jones, “Global Dynamics of Ikeda's Plane-Wave Map,” International Quantum Electronics Conference, paper WEE5 (1984).
2. S. M. Hammel, C. K. R. T. Jones, and J. V. Moloney, “Global dynamical behavior of the optical field in a ring cavity,” Journal of the Optical Society of America B 2, 552–564 (1985), DOI 10.1364/JOSAB.2.000552.
3. S. Isaeva, V. S. Afraimovich, and R. V. Puzikov, “Constructing a generating partition for the Ikeda map,” Physical Review E 61, 1353–1359 (2000), DOI 10.1103/PhysRevE.61.1353.
4. X.-S. Yang, H. Li, and Y. Huang, “A planar topological horseshoe theory with applications to computer verifications of chaos,” Journal of Physics A 38 (2005), DOI 10.1088/0305-4470/38/19/008.
5. Q. Li et al., “An Algorithm to Automatically Detect the Smale Horseshoes,” International Journal of Bifurcation and Chaos / open application article (2012), DOI 10.1155/2012/283179.
6. N. Ampilova and I. Soloviev, “On a method of applied symbolic dynamics for investigation of dynamical systems,” Vibroengineering Procedia 25 (2019), DOI 10.21595/vp.2019.20698.
