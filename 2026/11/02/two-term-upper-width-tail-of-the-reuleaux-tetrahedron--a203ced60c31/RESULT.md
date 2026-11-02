# Two-term upper-width tail of the Reuleaux tetrahedron

## Finding
Let \(K\) be the intersection of the four closed unit balls centered at the vertices of a regular Euclidean tetrahedron with edge length one. For \(U\) uniformly distributed on the unit sphere, define its directional width \(W(U)=h_K(U)+h_K(-U)\), where \(h_K(u)=\max_{x\in K}\langle x,u\rangle\). Put
\[
W_*=\sqrt3-\frac1{\sqrt2},\qquad \Delta=\sqrt3-\sqrt2.
\]
Then, as the dimensionless deficit \(\varepsilon\downarrow0\),
\[
\boxed{\Pr\{W(U)>W_*-\varepsilon\}
=\frac{6}{\Delta}\varepsilon+
\frac{3\sqrt3}{2\Delta^3}\varepsilon^2+O(\varepsilon^3).}
\]
The previously known maximal width \(W_*\) is not claimed as new. The contribution is the sharp upper-tail law, including its second coefficient. The first two coefficients are respectively approximately \(18.8775862196518\) and \(80.9165807559226\).

## Assumptions and scope
The convex body has unit generating-ball radius and unit tetrahedral edge length; the probability is over uniformly oriented **unoriented** directions, equivalently uniform \(U\in S^2\) since \(W(U)=W(-U)\). Strict inequalities are immaterial at the probability-zero equality boundary. The result concerns width rather than the distribution of random chord lengths or section diameters. We use the classical sharp extremal-width fact that \(W_*\) is the maximum and that its maximizing lines are the three common perpendiculars of the three pairs of opposite tetrahedral edges (six oriented axial normals). The prior extremal value and opposite-edge geometry are stated in Finch (2013) and the historical sources cited there; the derivation below proves the local expansion and probability coefficients, not a new global width inequality.

## Proof
Choose the four tetrahedron centers
\[
V=\{(a,a,a),(a,-a,-a),(-a,a,-a),(-a,-a,a)\},
\quad a=\frac1{2\sqrt2}=\frac{\sqrt2}{4}.
\]
Their pairwise distances are one. Two unit spheres with center separation one intersect in a circle of radius \(r=\sqrt3/2\) centered at their centers' midpoint. In a sufficiently small open neighborhood of \(e_1=(1,0,0)\), the positive supporting point is on the common circular arc of the balls centered at \((-a,a,-a)\) and \((-a,-a,a)\). The negative supporting point lies on the opposite circular arc, where the balls centered at \((a,a,a)\) and \((a,-a,-a)\) meet. This follows from the strict slackness of the other two ball constraints at the axial arc midpoints and the strict positivity of both active normal-cone coefficients at those midpoints; both properties persist by continuity. In particular, this is an exact support description, not an approximation.

Write \(u=(\sqrt{1-s^2-t^2},s,t)\) and \(q=s^2+t^2\). Orthogonally projecting \(u\) onto the respective arc planes \(y=z\) and \(y=-z\) yields the **exact** local formula
\[
 W(u)=-2a\sqrt{1-q}
 +r\left(\sqrt{1-q/2+st}+\sqrt{1-q/2-st}\right).
\]
Consequently \(W_*=2(r-a)\). Taylor expansion, uniform in polar angle for sufficiently small \(q\), gives
\[
 W_*-W(u)=\kappa q-\beta(\phi)q^2+O(q^3),
 \quad\kappa=\frac{\Delta}{4}>0,
\]
where \(s=\sqrt q\cos\phi\), \(t=\sqrt q\sin\phi\), and
\[
 \beta(\phi)=\frac a4-\frac r{16}-\frac r{16}\sin^2(2\phi),
 \qquad\frac1{2\pi}\int_0^{2\pi}\beta(\phi)\,d\phi
 =\frac a4-\frac{3r}{32}.
\]
For small positive \(\varepsilon\), the radial boundary of the axial superlevel component solves
\[
 q_\varepsilon(\phi)=\frac{\varepsilon}{\kappa}
 +\frac{\beta(\phi)}{\kappa^3}\varepsilon^2
 +O(\varepsilon^3)
\]
uniformly in \(\phi\), by the implicit-function theorem applied to the positive radial derivative. The spherical area form in these local coordinates is \(ds\,dt/\sqrt{1-q}\). One oriented axial component therefore has area
\[
 \int_0^{2\pi}\left[1-\sqrt{1-q_\varepsilon(\phi)}\right]d\phi.
\]
By the known sharp extremal-width classification, the six axial points exhaust the global maximizers. Compactness thus confines the entire upper-tail event to six disjoint such neighborhoods when \(\varepsilon\) is sufficiently small. Tetrahedral symmetry makes their areas equal. Division by \(4\pi\) and expansion of \(1-\sqrt{1-q}=q/2+q^2/8+O(q^3)\) yield
\[
 \Pr(W>W_*-\varepsilon)
 =\frac{3}{2\kappa}\varepsilon
 +\frac{3}{2\kappa^3}
  \left(\frac a4-\frac{3r}{32}+\frac\kappa4\right)
  \varepsilon^2+O(\varepsilon^3).
\]
The parenthesized factor simplifies exactly to \(r/32\), because \(\kappa=r/2-a\). Substituting \(r=\sqrt3/2\) and \(\kappa=\Delta/4\) proves the claimed two coefficients. The remainder is \(O(\varepsilon^3)\) because the support formula is analytic and the implicit inversion is uniform on the compact polar-angle circle.

## Verification
The standalone file `verify.py` enumerates support candidates on all four spheres, six pairwise circle intersections, and four vertices. It independently compares numerical support optimization against the derived local formula; evaluates a deterministic grid of global directions as a non-exhaustive diagnostic; and integrates the exact six-cap local superlevel areas with bisection and midpoint angular quadrature. For deficits \(0.001\), \(0.0005\), \(0.0001\), and \(0.00005\), the scaled third-order numerical remainders approach approximately \(1296\), consistent with the proved \(O(\varepsilon^3)\) error. The computational checks are corroboration, not a proof of global maximizer classification or of the asymptotic statement.

Run `python verify.py` from this directory using Python 3.9 or newer; the script requires only the standard library.

## Relationship to prior work
The maximal width \(W_*\), the opposite-curved-edge maximizing geometry, and the nonconstant width of the Reuleaux tetrahedron are classical. Finch's 2013 study computes the **mean** width and explicitly reports the maximum; it does not derive a small-deficit distribution. Harbourne's classical description and Hynd's 2023 preprint/2024 revision concern area, volume and curved-edge structure, not the probability of near-maximal widths. The exact sequence for the already known maximum appears separately in OEIS A395679 (2026) and provides no tail asymptotic. The new result requires the full second-order angular geometry and spherical superlevel integration; it is not the historical maximum value restated.

## Limitations
The result is specific to the equal-radius regular Reuleaux tetrahedron, not general unequal-radius ball intersections or Meissner constant-width modifications. The proof invokes the previously known global maximum/equality classification; the standalone checker cannot independently certify this global geometric input. Historical distribution calculations not found by the searches could affect priority. The analytic second-order expansion has not undergone independent expert audit.

## References
1. Steven R. Finch, *Mutually Equidistant Spheres that Intersect*, arXiv:1301.5515 (public January 23, 2013), https://arxiv.org/abs/1301.5515 ; section 3 discusses the Reuleaux tetrahedron, mean width and the classical maximal width.
2. Ryan Hynd, *The perimeter and volume of a Reuleaux polyhedron*, arXiv:2310.08709 (first public October 12, 2023), https://arxiv.org/html/2310.08709v2 ; sections 1 and 2 describe the ball-polyhedron faces and paired circular edges.
3. B. Harbourne, *Volume and Surface Area of the Spherical Tetrahedron (AKA Reuleaux Tetrahedron) by Geometrical Methods*, https://www.math.unl.edu/~bharbourne1/ST/sphericaltetrahedron.html ; accessible search record explicitly describes the extremal edge-to-edge width, although the full page was temporarily unavailable at inspection.
4. OEIS Foundation, sequence A395679 (2026), https://oeis.org/A395679 ; decimal expansion and closed form for the classical maximum only.
