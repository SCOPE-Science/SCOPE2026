# The seventh-order short-distance law and a curvature-gradient sign transition

## Finding

Let \(K\subset\mathbb R^2\) be a compact strictly convex body with \(C^6\) boundary of everywhere positive curvature. Write \(A=\operatorname{area}(K)\), \(L=\operatorname{length}(\partial K)\), and \(\kappa(s)>0\) for the curvature in arclength \(s\). For two independent points \(X,Y\) uniformly distributed by area on \(K\), define
\[
R_K=\sqrt{A/\pi},\qquad D_K(\rho)=\mathbb P\{\|X-Y\|<\rho R_K\}.
\]
Then, as \(\rho\downarrow0\),
\[
\boxed{\begin{aligned}
D_K(\rho)={}&\rho^2-\frac{2L}{3\pi^{3/2}\sqrt A}\rho^3
+\frac{\sqrt A}{60\pi^{5/2}}\left(\int_{\partial K}\kappa^2\,ds\right)\rho^5\\
&+\frac{A^{3/2}}{20160\pi^{7/2}}\left(\int_{\partial K}(9\kappa^4-8\kappa_s^2)\,ds\right)\rho^7+o(\rho^7).
\end{aligned}}
\tag{1}
\]
Here \(\kappa_s=d\kappa/ds\). In particular, the seventh-order coefficient, unlike the positive fifth-order coefficient, is not sign-definite among smooth strictly convex bodies.

For every integer \(k\ge2\) and \(0\le a<1\), let \(K_{k,a}\) have support function
\[
h_{k,a}(\theta)=1+\frac{a}{1-k^2}\cos(k\theta),\qquad
h_{k,a}+h_{k,a}''=1+a\cos(k\theta)>0.
\]
Then its seventh-order curvature invariant is exactly
\[
\boxed{\int_{\partial K_{k,a}}(9\kappa^4-8\kappa_s^2)\,ds
=\frac{\pi\,[18-(9+8k^2)a^2-(9+2k^2)a^4]}{(1-a^2)^{7/2}}.}
\tag{2}
\]
For each fixed \(k\ge2\), there is a unique \(a_k\in(0,1)\) at which this coefficient vanishes; explicitly,
\[
a_k^2=\frac{\sqrt{(9+8k^2)^2+72(9+2k^2)}-(9+8k^2)}{2(9+2k^2)}.
\]
The coefficient is positive below and negative above \(a_k\). At the explicit smooth example \(k=3\), \(a=1/2\), the invariant is \(-56\pi/(3\sqrt3)\) and the normalized seventh-order coefficient is \(-7\sqrt{21}/(61440\pi)<0\). For the unit disk the corresponding coefficient is \(1/(1120\pi)>0\).

## Assumptions and scope

The boundary of \(K\) is a single \(C^6\) closed embedded curve, strictly convex with a uniform positive lower curvature bound, and orientation is chosen so that \(\kappa\) is positive. All integrals and derivatives of curvature are with respect to Euclidean arclength. The parameter \(\rho\) is the distance divided by the equal-area disk radius, not unnormalized distance; the formula is invariant under translations, rotations, and positive dilations. The remainder is for each fixed body and is not claimed uniformly over arbitrary families of bodies. The harmonic support functions define genuine smooth strictly convex bodies for the entire stated parameter range because their curvature radii are strictly positive.

## Proof

**1. Reduction to endpoint chords.** Fix a unit direction \(u\) and use coordinates \((x,v)\), with \(x\) parallel to \(u\) and \(v\) perpendicular to \(u\). The intersection of \(K\) with the line at \(v\) is an interval of length \(\ell_u(v)\), possibly zero. The covariogram is therefore exactly
\[
g_K(tu)=|K\cap(K+tu)|=\int (\ell_u(v)-t)_+\,dv.
\]
Its projection width is \(w_K(u^\perp)\). Subtracting \(A-tw_K(u^\perp)\) and separating the two endpoints of the projection interval gives, for sufficiently small positive \(t\),
\[
g_K(tu)=A-tw_K(u^\perp)+\sum_{\sigma\in\{+,-\}}\int_0^t\delta_{\sigma,u}(q)\,dq.\tag{3}
\]
Here \(\delta_{\sigma,u}(q)\) is the perpendicular inward depth, measured from the corresponding extreme support line, at which the local chord has length \(q\). Strict convexity makes each local chord increasing in depth for sufficiently small depths. Compactness and the uniform curvature lower bound make these neighborhoods and the expansion errors uniform over \(u\).

**2. Local inverse-chord calculation.** At a tangency point, introduce tangent coordinate \(x\) and inward normal coordinate \(y\), with the boundary locally a graph \(y=f(x)\), \(f(0)=f'(0)=0\). Frenet differentiation gives
\[
f(x)=\frac\kappa2x^2+\frac{\kappa_s}{6}x^3
+\frac{\kappa_{ss}+3\kappa^3}{24}x^4+o(x^4).\tag{4}
\]
The two roots of \(f(x)=\delta\) differ by the chord length \(q\). Series inversion (including the cubic asymmetry of the graph) gives
\[
\delta(q)=\frac\kappa8q^2+
\frac{9\kappa^4+3\kappa\kappa_{ss}-5\kappa_s^2}{1152\kappa}\,q^4+o(q^4).\tag{5}
\]
For clarity, writing \(f(x)=b_2x^2+b_3x^3+b_4x^4+o(x^4)\), the coefficient of \(q^4\) is \(b_4/16-5b_3^2/(64b_2)\). Substituting \(b_2=\kappa/2\), \(b_3=\kappa_s/6\), and \(b_4=(\kappa_{ss}+3\kappa^3)/24\) yields (5). Formula (3) then becomes
\[
g_K(tu)=A-w_K(u^\perp)t+
\frac{\kappa_+(u)+\kappa_-(u)}{24}t^3
+\frac{t^5}{5760}\sum_{\sigma=\pm}
\left(9\kappa_\sigma^3+3\kappa_{ss,\sigma}-\frac{5\kappa_{s,\sigma}^2}{\kappa_\sigma}\right)+o(t^5).\tag{6}
\]
All curvatures in (6) are evaluated at the two tangencies for the chosen projection direction.

**3. Angular average and normalization.** Let \(d\theta\) be angular arclength on \(\mathbb S^1\). Cauchy's perimeter identity and the positive-curvature Gauss map \(d\theta=\kappa\,ds\) give
\[
\int_{\mathbb S^1}w_K(u^\perp)d\theta=2L,\qquad
\int_{\mathbb S^1}(\kappa_++\kappa_-)d\theta=2\int_{\partial K}\kappa^2ds.
\]
In the fifth-order covariogram coefficient the Gauss map yields twice the integral of \(9\kappa^4+3\kappa\kappa_{ss}-5\kappa_s^2\). Periodic integration by parts transforms this to twice \(\int(9\kappa^4-8\kappa_s^2)ds\). Hence
\[
\int_{\mathbb S^1}g_K(tu)d\theta
=2\pi A-2Lt+\frac{t^3}{12}\int\kappa^2ds
+\frac{t^5}{2880}\int(9\kappa^4-8\kappa_s^2)ds+o(t^5).\tag{7}
\]
The random displacement density is \(g_K(z)/A^2\). Integrating (7) radially with the polar Jacobian \(t\,dt\) gives, for \(r\downarrow0\),
\[
\frac1{A^2}\int_{|z|<r}g_K(z)dz
=\frac{\pi r^2}A-\frac{2Lr^3}{3A^2}
+\frac{r^5}{60A^2}\int\kappa^2ds
+\frac{r^7}{20160A^2}\int(9\kappa^4-8\kappa_s^2)ds+o(r^7).
\]
Setting \(r=\rho\sqrt{A/\pi}\) yields (1). There are no fourth or sixth powers: the local inverse-chord expansion contains only even powers through the order used.

**4. Exact sign transition.** A planar support function with \(h+h''=r(\theta)>0\) has \(ds=r\,d\theta\), \(\kappa=1/r\), and \(\kappa_s=-r'/r^3\). Therefore
\[
\int_{\partial K}(9\kappa^4-8\kappa_s^2)ds
=\int_0^{2\pi}\left(\frac9{r^3}-\frac{8(r')^2}{r^5}\right)d\theta.\tag{8}
\]
For \(r=1+a\cos(k\theta)\), reducing the integrals by elementary differentiation of \(\int_0^{2\pi}(1+a\cos\theta)^{-1}d\theta=2\pi/\sqrt{1-a^2}\) yields exactly (2). The numerator in (2), as a polynomial in \(a^2\), decreases strictly from \(18\) at \(a=0\) to \(-10k^2\) as \(a\uparrow1\). It has exactly one zero. For \(k=3\), \(a=1/2\), the numerator is \(-63/16\); the support-function area formula gives \(A=\pi[1-a^2/(2(k^2-1))]=63\pi/64\). Substitution proves the stated negative coefficient. The disk follows directly from constant \(\kappa=1\), \(A=\pi\), and \(\int9\kappa^4ds=18\pi\).

## Verification

Run `python3 verify.py` from the directory containing the accompanying standalone program; the expected output is `FINITE_GEOMETRIC_CHECKS_OK 33`. The standard-library program independently integrates the curvature invariant on four ellipses and checks it against the affine-image-of-disk covariogram calculation, evaluates sixteen support-function examples directly and via (2), checks the exact negative and positive limits, and compares low-radius covariogram expansions for the disk. These are finite numerical and exact-arithmetic corroborations, not a proof of the universal asymptotic theorem; (3)–(8) supply the analytic argument.

For a unit disk, (1) specializes to \(D_K(\rho)=\rho^2-4\rho^3/(3\pi)+\rho^5/(30\pi)+\rho^7/(1120\pi)+o(\rho^7)\), agreeing with its exact lens covariogram. The ellipse checks provide a second independent normalization control for the nontrivial seventh-order term.

## Relationship to prior work

Wang [1] introduces the equal-volume-radius normalized probability \(D_K\), expresses it as a covariogram radial integral, and gives the first correction in perimeter; these definitions and the first correction are not new here. Existing isotropic autocorrelation and curvature literature, including the limited accessible description of Brazke's thesis [2], addresses a third radial derivative and hence the \(\rho^5\) curvature-squared contribution. We do **not** claim priority for this lower-order term. The contribution asserted here is the universal next \(\rho^7\) term with its derivative-energy combination \(\int(9\kappa^4-8\kappa_s^2)ds\), and the explicit complete sign transition in an infinite smooth harmonic family. The published polygonal analysis [3] instead has an exact small-radius quartic formula and an angle-rigidity inequality: the different regularity class produces different powers, so neither claim covers the other. Prior covariogram studies [4] establish first-order brightness and do not state the seventh-order invariant in their inspected portions. Earlier distance-distribution methods [5] and [6] provide different representations, not the displayed curvature-gradient formula in the accessible descriptions.

## Limitations

Only fixed strictly convex planar bodies with \(C^6\) boundaries and curvature uniformly bounded below are covered. No extension is proved to nonsmooth boundaries, bodies with flat points, higher dimensions, or uniform remainders over varying bodies. The harmonic sign threshold concerns this curvature coefficient, not a sign change of the probability itself. Historical priority is provisional: the full text of a relevant older isotropic-autocorrelation thesis was inaccessible, and other older covariogram expansions could use equivalent terminology. The finite verifier is not an independent mathematical audit.

## References

[1] Sinan Wang, *A Brunn–Minkowski Theory for the Distribution of Random Pairs of Points in Convex Bodies*, arXiv:2610.01916v1, first public 1 October 2026. https://arxiv.org/html/2610.01916v1.

[2] Denis Brazke, doctoral thesis on nonlocal isoperimetric energies and isotropic autocorrelation, University of Heidelberg repository, https://archiv.ub.uni-heidelberg.de/volltextserver/35273/1/thesis_brazke.pdf (full text inaccessible at inspection; indexed mathematical description only).

[3] *Sharp uniform angular stability for the short-pair distance coefficient of convex polygons*, published mathematical result, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-uniform-angular-stability-for-the-short-pair-distance-coef--24e8bcd8655b.

[4] L. Langharst and collaborators, *General measure extensions of projection bodies*, Proceedings of the London Mathematical Society (2022), https://doi.org/10.1112/plms.12477.

[5] Takeshi Koshizuka, *Distance distribution in an arbitrary region*, Journal of the City Planning Institute of Japan 37 (2002), pp. 37–42, https://doi.org/10.11361/journalcpij.37.37.

[6] R. H. Aramyan and V. A. Mnatsakanyan, *Conditional moments of the distance distribution two random points in a convex domain in R2*, Proceedings of the YSU 54 (2020), pp. 3–8, https://doi.org/10.46991/PYSU:A/2020.54.1.003.
