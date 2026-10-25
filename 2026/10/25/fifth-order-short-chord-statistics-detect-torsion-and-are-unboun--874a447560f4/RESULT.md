# Fifth-order short-chord statistics detect torsion and are unbounded under smooth \(C^2\) convergence

## Finding
Let \(\gamma:\mathbb R/L\mathbb Z\to\mathbb R^d\), \(d\ge2\), be an embedded \(C^7\) unit-speed closed curve of length \(L>0\), and let \(X,Y\) be independent points sampled uniformly by arclength on it. Write \(T=\gamma'\) and \(F(r)=\Pr(\|X-Y\|\le r)\). Then
\[
F(r)=\frac{2r}{L}+\frac{r^3}{12L^2}\int_0^L\|T'\|^2ds
+\frac{r^5}{2880L^2}\int_0^L(35\|T'\|^4-8\|T''\|^2)ds+O_\gamma(r^7).
\]
In \(\mathbb R^3\), provided \(\kappa=\|T'\|>0\) throughout, the quintic coefficient can be written
\[
c_5=\frac1{2880L^2}\int_0^L\bigl(27\kappa^4-8(\kappa')^2-8\kappa^2\tau^2\bigr)ds.
\]
If the full curvature profile is separately known, the observed coefficient identifies the nonnegative weighted torsion energy:
\[
\int_0^L\kappa^2\tau^2ds=\frac18\int_0^L\bigl(27\kappa^4-8(\kappa')^2\bigr)ds-360L^2c_5.
\]
This energy vanishes exactly when the connected curve lies in a plane. Additionally the \(C^2\)-convergent embedded family
\[\Gamma_m(t)=(\cos t,\sin t,m^{-5/2}\sin mt),\qquad 0\le t\le2\pi,\qquad m\in\mathbb N\]
has \(c_5(\Gamma_m)=-m/(1440\pi)+O(1)\). Hence the quintic coefficient is not even locally bounded for the \(C^2\) topology, despite smoothness of every individual curve.

## Assumptions and scope
All derivatives \(T',T''\) are with respect to arclength. Embedded means the periodic parametrization is injective on its parameter circle. The small-radius expansion is for any fixed embedded \(C^7\) curve, with an implicit constant that may depend on that curve. The torsion expression requires dimension exactly three and positive curvature at every point. It does not say that the probability distribution alone determines torsion or planarity; the curvature profile must also be supplied. The wavy-circle family is analyzed after taking the small-radius coefficient for each fixed integer \(m\), not by interchanging radius and frequency limits.

## Proof
**Localization.** Since \(\gamma\) is an embedding of a compact parameter circle, for every sufficiently small \(\delta>0\) there is a positive minimum Euclidean separation between \(\gamma(s_1)\) and \(\gamma(s_2)\) when their shorter circular parameter separation is at least \(\delta\). Locally the chord \(q(s,u)=\|\gamma(s+u/2)-\gamma(s-u/2)\|\) is uniformly strictly increasing in \(u>0\), with first derivative approaching one as \(u\downarrow0\). Consequently, for sufficiently small \(r>0\), the event \(\|X-Y\|\le r\) has precisely the parameter representation \(s\in[0,L),\ |u|\le u_r(s)\), where \(q(s,u_r(s))=r\). The midpoint change of variables \((s,u)\mapsto(s+u/2,s-u/2)\) has absolute Jacobian one. Therefore \(F(r)=2L^{-2}\int_0^Lu_r(s)ds\).

**Symmetric chord expansion.** Set \(a(s)=\|T'(s)\|^2\) and \(b(s)=\|T''(s)\|^2\). Symmetric Taylor expansion, uniform in \(s\), gives
\[
\gamma(s+u/2)-\gamma(s-u/2)=uT+\frac{u^3}{24}T''+\frac{u^5}{1920}T^{(4)}+O_\gamma(u^7).
\]
Unit speed implies \(T\cdot T''=-a\), while twice differentiating \(a\) and four times differentiating \(T\cdot T=1\) yield \(T\cdot T^{(4)}=b-2a''\). Thus
\[
q(s,u)^2=u^2\Bigl[1-\frac{a}{12}u^2+\bigl(\frac b{360}-\frac{a''}{480}\bigr)u^4+O_\gamma(u^6)\Bigr].
\]
Take the positive square root, then revert the odd power series to obtain
\[
u_r(s)=r+\frac a{24}r^3+\frac{35a^2-8b+6a''}{5760}r^5+O_\gamma(r^7).
\]
The remainder is uniform on the compact circle. Integrating, use \(\int_0^L a''ds=0\) by periodicity. Multiplication by \(2/L^2\) proves the stated probability expansion.

**Torsion.** Where \(\kappa>0\), the Frenet–Serret equation gives \(T''=-\kappa^2T+\kappa' N+\kappa\tau B\). Hence \(b=\kappa^4+(\kappa')^2+\kappa^2\tau^2\), which gives the second formula. If \(\int\kappa^2\tau^2=0\), continuity and positive curvature imply \(\tau\equiv0\), so the binormal is constant; the connected curve is planar. The converse is immediate.

**Instability.** For the displayed smooth embedded family, write \(v_m(t)=\|\Gamma_m'(t)\|=(1+m^{-3}\cos^2(mt))^{1/2}\). Then its length \(L_m=\int_0^{2\pi}v_mdt=2\pi+O(m^{-3})\). Standard arclength differentiation yields, uniformly in \(t\),
\[
T'_m=(-\cos t,-\sin t,-m^{-1/2}\sin mt)+O(m^{-2}),\qquad
T''_m=(\sin t,-\cos t,-m^{1/2}\cos mt)+O(m^{-1}).
\]
These error estimates are vector norm bounds. Thus \(\int\|T'_m\|^4ds=O(1)\) and
\[
\int_0^{L_m}\|T''_m\|^2ds=\pi m+O(1).
\]
Substitution into the exact quintic coefficient gives \(c_5(\Gamma_m)=-8\pi m/[2880(2\pi)^2]+O(1)=-m/(1440\pi)+O(1)\). Since the vertical coordinate and its first and second derivatives are respectively bounded by \(m^{-5/2},m^{-3/2},m^{-1/2}\), the curves converge in \(C^2\) to the unit circle.

## Verification
For a round unit circle, the exact formula \(F(r)=2\arcsin(r/2)/\pi\) has cubic and quintic coefficients \(1/(24\pi)\) and \(3/(640\pi)\), agreeing with the integral formula. The standalone script `space_curve_distance_check.py` independently verifies the fifth coefficient on a closed nonplanar four-dimensional two-frequency torus curve, using the exact chord formula and numerical root solving. It also computes the arclength curvature and derivative integrals for increasing frequencies of the wavy embedded circles. The nonplanar curve's numerical scaled remainder converges toward its derived quintic coefficient; the wavy family approaches the predicted linear divergence. These computations corroborate, but do not replace, the uniform Taylor, geometric localization, and periodic integration arguments above.

## Relationship to prior work
Classical Frenet–Serret identities and their higher-dimensional derivatives are background mathematics; in particular Gutkin (2010) systematizes the curvature invariants of regular Euclidean curves. Pottmann et al. (2009) develop integral invariants for planar and spatial curves and record local curvature Taylor expansions. Clarkson (2008) defines the correlation integral as the probability that two independently sampled manifold points have small ambient distance, in work concerned with random projections and covering bounds. Álvarez-Vizoso et al. (2018) develop manifold integral-invariant curvature descriptors. The present statement concerns the precise **fifth** scalar short-chord probability coefficient, the explicit curvature-weighted torsion deficit, and its unboundedness under smooth \(C^2\) convergence; these assertions are not implied by the identified lower-order, pointwise, covariance, or covering-bound statements. A complete bibliographic exclusion of all historical formulations is not claimed.

## Limitations
The estimate requires embeddedness and enough smoothness for uniform high-order Taylor remainders; self-intersections, endpoints, and merely \(C^2\) curves fall outside the expansion. The expansion's radius of validity and constants are not uniform under the wavy-circle perturbations. Higher-order terms and reconstruction from the scalar distribution without external curvature data remain unproved. Historical sources may contain equivalent implicit higher-order formulas, so independent literature verification is desirable.

## References
1. E. Gutkin, *The Curvatures of Regular Curves and Euclidean Invariants of their Derivatives*, arXiv:1007.2960 (first publicly posted 2010-07-17), https://arxiv.org/abs/1007.2960.
2. H. Pottmann, J. Wallner, Y.-L. Huang and Y.-L. Yang, *Integral Invariants for Robust Geometry Processing*, Computer Aided Geometric Design 26 (2009), https://www.yongliangyang.net/docs/iirgp_cagd2009.pdf.
3. K. Clarkson, *Tighter Bounds for Random Projections of Manifolds* (2008), especially discussion of the correlation integral in Section 2.4, https://kenclarkson.org/jl_manifold/p.pdf.
4. J. Álvarez-Vizoso, M. Kirby and C. Peterson, *Manifold Curvature Descriptors from Hypersurface Integral Invariants*, arXiv:1804.04808v1 (2018), https://arxiv.org/html/1804.04808v1.
