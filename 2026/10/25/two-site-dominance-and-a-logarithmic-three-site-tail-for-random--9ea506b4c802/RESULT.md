# Two-site dominance and a logarithmic three-site tail for random minimum enclosing disks

## Finding

Let three points be sampled independently and uniformly from the closed unit disk. Let \(R\) denote the radius of their minimum enclosing Euclidean disk and let \(S\in\{2,3\}\) count the points determining it. For \(\varepsilon\downarrow0\),
\[
\Pr\{R>1-\varepsilon,S=2\}=\frac{128\sqrt2}{5\pi}\varepsilon^{5/2}+O(\varepsilon^3),
\]
\[
\Pr\{R>1-\varepsilon,S=3\}=\frac{16}{\pi^2}\varepsilon^3\log(1/\varepsilon)+O(\varepsilon^3).
\]
Consequently,
\[
\Pr\{S=3\mid R>1-\varepsilon\}\sim\frac5{8\sqrt2\pi}\sqrt\varepsilon\log(1/\varepsilon).
\]
The novelty lies principally in the logarithmic three-contact law and its conditional comparison with two-contact circles. The longest-side near-diameter marginal used for the first coefficient is known from the distance distribution of two disk points.

## Assumptions and scope

The ambient disk is \(D=\{x\in\mathbb R^2:\|x\|\le1\}\), the three sample points are independent with normalized Lebesgue area measure \(\pi^{-1}dx\), and \(\varepsilon\in(0,1)\) tends to zero. Almost surely, the triangle is noncollinear and not right-angled. The minimal enclosing disk is unique. The support count is \(S=2\) precisely for an obtuse triangle (with its longest side a diameter); it is \(S=3\) precisely for an acute triangle (with the triangle circumcircle its smallest enclosing circle). Neither support count refers to tangencies with the ambient unit disk.

## Proof

**1. A nearly diametral pair.** For two independent uniform points of \(D\), set their distance to \(d\). The exact density is
\[
f(d)=\frac{2d}{\pi}\left[2\arccos(d/2)-d\sqrt{1-d^2/4}\right],\quad 0<d<2.
\]
(The bracket is the area of overlap of two unit disks separated by \(d\).) With \(t=2-d\), that overlap is \((4/3)t^{3/2}+O(t^{5/2})\). Integrating from \(2(1-\varepsilon)\) to \(2\) gives
\[
p_\varepsilon:=\Pr\{d>2(1-\varepsilon)\}=\frac{128\sqrt2}{15\pi}\varepsilon^{5/2}+O(\varepsilon^{7/2}).
\]
For a three-point sample, two different pairs both satisfying this inequality have probability \(O(\varepsilon^4)\): the shared vertex is in a boundary annulus of area \(O(\varepsilon)\), and each of the other vertices lies in an opposing cap of area \(O(\varepsilon^{3/2})\). If a pair has length greater than \(2(1-\varepsilon)\), its midpoint has norm at most \(\sqrt{2\varepsilon}\); its diametral disk has radius at least \(1-\varepsilon\). The part of the unit disk exterior to that diametral disk has area \(O(\sqrt\varepsilon)\), uniformly over such pairs. Thus the event that a long pair exists but the third point lies outside that diametral disk has probability \(O(\varepsilon^3)\). On the complement, the minimum enclosing disk is the pair's diametral disk. Inclusion-exclusion therefore gives \(3p_\varepsilon+O(\varepsilon^3)\), proving the two-contact formula.

**2. Exact acute-triple integral.** For a noncollinear ordered triple, use circumcenter \(z\), circumradius \(r\), and three circle directions \(u_j=(\cos\theta_j,\sin\theta_j)\), so \(x_j=z+ru_j\). The absolute six-dimensional Jacobian is
\[
r^3\left|\det(u_2-u_1,u_3-u_1)\right|\,dz\,dr\,d\theta_1d\theta_2d\theta_3.
\]
The triple is acute exactly when its directions are not contained in a semicircle. Put \(d=\|z\|\). When \(0\le d\le1-r\), every direction is permitted by \(x_j\in D\); when \(1-r<d<\sqrt{1-r^2}\), the allowed directions constitute an arc of angular length \(\pi+\eta\), where
\[
\eta=2\arcsin\!\left(\frac{1-r^2-d^2}{2rd}\right),\qquad 0<\eta<\pi.
\]
When \(d\ge\sqrt{1-r^2}\), an acute triple is impossible. The limiting full-arc case uses \(\eta=\pi\). Integrating the determinant Jacobian over the acute ordered triples in an arc of length \(\pi+\eta\) yields the **exact** angular function
\[
H(\eta)=6\left[\eta^2+\eta\sin\eta+\pi(\eta-\sin\eta)\right].
\]
Indeed, order the angles in their allowed arc, multiply by the six possible labels, and put the first-to-second and second-to-third angular gaps into the determinant \(\sin x+\sin(x-v)+\sin v\); direct integration gives
\[
H(\eta)=6\int_0^\eta(\eta-v)\int_v^\pi
\left[\sin x+\sin(x-v)+\sin v\right]dx\,dv.
\]
In particular \(H(\pi)=12\pi^2\) and \(H(\eta)=12\eta^2+O(\eta^3)\) as \(\eta\to0\). Writing \(H(\eta(r,d))\) also for the full-arc zone, radial integration in \(z\) gives the exact three-contact probability
\[
A(\varepsilon)=\frac{2}{\pi^2}\int_{1-\varepsilon}^1r^3
\int_0^{\sqrt{1-r^2}} d\,H(\eta(r,d))\,dd\,dr.
\]

**3. The logarithmic boundary layer.** Put \(s=1-r\) and \(q=1-r^2\). The portion \(0\le d\le s\) contributes \(O(s^2)\) to the inner integral. For \(s<d<\sqrt q\), set \(c=(q-d^2)/(2rd)\), so \(0\le c\le1\) and \(H(2\arcsin c)=48c^2+O(c^3)\) uniformly on this interval. Direct integration gives
\[
\int_s^{\sqrt q}48d c^2\,dd
=\frac{12}{r^2}\int_s^{\sqrt q}\frac{(q-d^2)^2}{d}\,dd
=24s^2\log(1/s)+O(s^2).
\]
The cubic remainder contributes \(O(s^2)\), because \(c\le C\min(1,s/d)\) and \(\int_s^{\sqrt q}d\min(1,(s/d)^3)dd=O(s^2)\). Hence the full inner integral is \(24s^2\log(1/s)+O(s^2)\), and therefore
\[
A(\varepsilon)=\frac2{\pi^2}\int_0^\varepsilon(1-s)^3\left[24s^2\log(1/s)+O(s^2)\right]ds
=\frac{16}{\pi^2}\varepsilon^3\log(1/\varepsilon)+O(\varepsilon^3).
\]
This is the three-contact law. Dividing by the two-contact-dominated total probability yields the stated conditional coefficient. The estimates refer to all sufficiently small positive \(\varepsilon\); no conclusion is made about finite-threshold exact ordering outside the asymptotic regime.

## Verification

The standalone `verify_mec_tail.py` is part of this package. It independently evaluates the six-by-six circumcircle-coordinate Jacobian on random nondegenerate configurations, numerically evaluates the angular integral \(H\), computes the exact one-pair and three-contact integrals by adaptive quadrature, and simulates 1,200,000 random disk triangles for a finite-threshold check. All tests executed successfully. Integration and simulation corroborate the proof; their finite precision and finite sample sizes are not infinite proofs.

## Relationship to prior work

Finch (2010) derives the one-side distance law of a random disk triangle, which already implies the basic long-pair term; this coefficient is not asserted as a new marginal distribution. Classical minimum-enclosing-ball work proves existence/uniqueness and characterization for deterministic point sets (Mordukhovich, Nam and Villalobos, 2011). Bull and collaborators (2024) use radius of the minimum enclosing circle of random triples in spatial correlation calculations, estimating the null law numerically by Monte Carlo rather than computing its support-marked sharp upper endpoint. The marked logarithmic three-support asymptotic and the precise vanishing conditional support fraction are not implied by the statements inspected in those sources. Similarities of terminology should not be mistaken for a proof of historical novelty.

## Limitations

The formulas concern exactly three independent **area-uniform** points inside a fixed unit disk and the near-maximal-radius regime. The law is not an exact distribution at general radii, and it does not treat other sampling densities, arbitrary convex domains, more than three sampled points, or higher dimensions. The second main term for the two-contact law is not resolved at \(\varepsilon^3\) accuracy. Numerical experiments do not certify the asymptotics. The literature comparison is evidence-based but cannot exclude unindexed or inaccessible earlier treatments, and no independent validation was performed.

## References

1. Steven R. Finch, *Perimeter Variance of Uniform Random Triangles*, arXiv:1007.0261v1, first public 2010-07-01, https://arxiv.org/html/1007.0261v1.
2. B. S. Mordukhovich, N. M. Nam and C. Villalobos, *The Smallest Enclosing Ball Problem and the Smallest Intersecting Ball Problem: Existence and Uniqueness of Solutions*, arXiv:1111.1280, first public 2011-11-05, https://arxiv.org/html/1111.1280v2.
3. Bull et al., *Extended correlation functions for spatial analysis of multiplex imaging data*, *Biological Imaging* (2024), section 2.3.4.2, https://www.cambridge.org/core/journals/biological-imaging/article/extended-correlation-functions-for-spatial-analysis-of-multiplex-imaging-data/FB677F0E100658E36725C5B4A3944EB7.
