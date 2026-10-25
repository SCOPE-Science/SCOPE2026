# The logarithmic perimeter singularity of random central triaxial-ellipsoid sections

## Finding

Let \(a>b>c>0\), and let \(E=\{(x,y,z):x^2/a^2+y^2/b^2+z^2/c^2\le1\}\). Pick \(U\) uniformly from the unit sphere, and write \(L(U)\) for the Euclidean perimeter of the *central planar section* \(E\cap U^\perp\), not for its orthogonal projection. Define the ellipse-perimeter function

\[
\mathcal P(r,s)=4\int_0^{\pi/2}\sqrt{r^2\cos^2t+s^2\sin^2t}\,dt,\qquad r,s>0.
\]

The distribution of \(L\) is supported on the interval from \(\ell_-=\mathcal P(b,c)\) to \(\ell_+=\mathcal P(a,b)\). Its unique interior critical value is \(\ell_*=\mathcal P(a,c)\). It has a density \(f_L\), smooth away from those three values, and a *two-sided logarithmic singularity*

\[
f_L(s)=\frac1{\pi\sqrt{\mu\nu}}\log\!\frac{\ell_*}{|s-\ell_*|}+O(1),\qquad s\longrightarrow\ell_*\quad(s\ne\ell_*),
\]

where \(\mathcal P_1,\mathcal P_2\) denote ordinary partial derivatives and

\[
\mu=\frac{a(a^2-b^2)}{b^2}\mathcal P_1(a,c)>0,\qquad
\nu=\frac{c(b^2-c^2)}{b^2}\mathcal P_2(a,c)>0.
\]

In addition, define the four positive quantities

\[
\begin{aligned}
\alpha_1&=\frac{b(a^2-b^2)}{a^2}\mathcal P_1(b,c),&
\alpha_2&=\frac{c(a^2-c^2)}{a^2}\mathcal P_2(b,c),\\
\beta_1&=\frac{a(a^2-c^2)}{c^2}\mathcal P_1(a,b),&
\beta_2&=\frac{b(b^2-c^2)}{c^2}\mathcal P_2(a,b).
\end{aligned}
\]

The endpoint densities are finite, strictly positive, and exact:

\[
\lim_{s\downarrow\ell_-}f_L(s)=\frac1{\sqrt{\alpha_1\alpha_2}},\qquad
\lim_{s\uparrow\ell_+}f_L(s)=\frac1{\sqrt{\beta_1\beta_2}}.
\]

Thus the random central-section *perimeter alone* has one precisely located unbounded interior density peak, at the perimeter of the ellipse formed by the longest and shortest principal semiaxes; the extremes have only finite density limits.

## Assumptions and scope

The statement is for a fixed full-dimensional **strictly triaxial** ellipsoid with three pairwise distinct positive semiaxes, a Haar-uniform **unoriented central plane**, and Euclidean section perimeter. Sampling \(U\) uniformly on the sphere induces the same plane law because \(U\) and \(-U\) define the same plane. The random variable is neither the projected perimeter nor the normalized isoperimetric filamentarity of a randomly *offset* slice. The error \(O(1)\) is a bounded two-sided remainder for fixed \(a,b,c\), not a uniform estimate as two semiaxes coalesce.

## Proof

**1. Section perimeter is a smooth spectral function.** Put \(Q=\operatorname{diag}(a^{-2},b^{-2},c^{-2})\). On the plane \(u^\perp\), the restricted quadratic form \(Q_u=Q|_{u^\perp}\) has positive eigenvalues \(\sigma_1,\sigma_2\). The section semiaxes are \(\sigma_1^{-1/2},\sigma_2^{-1/2}\). Cauchy's planar support-function formula gives

\[
L(u)=\int_0^{2\pi}\sqrt{\frac{\cos^2t}{\sigma_1}+\frac{\sin^2t}{\sigma_2}}\,dt.
\]

This is smooth as a function of the positive quadratic form \(Q_u\), including at repeated restricted eigenvalues. Each derivative with respect to either restricted eigenvalue is strictly negative, directly from differentiation beneath the integral.

**2. There are exactly six critical normals.** At a fixed normal \(u\), choose an orthonormal eigenbasis \(v_1,v_2\) of \(Q_u\). For any tangent perturbation \(w=w_1v_1+w_2v_2\), choose an orthonormal plane frame transported with derivative \(v_i'=-w_i u\). Differentiating the restricted matrix yields diagonal entries \((Q_u)'_{ii}=-2w_i\langle Qu,v_i\rangle\). With \(\Psi_i<0\) denoting the derivative of the spectral perimeter function in the \(i\)-th eigenvalue, the derivative of the perimeter is

\[
D L(u)[w]=-2\sum_{i=1}^2 \Psi_i\,w_i\langle Qu,v_i\rangle.
\]

The same calculation holds for repeated eigenvalues since the matrix derivative there is scalar. Because both \(\Psi_i\) are nonzero, stationarity in all tangent directions is equivalent to \(Qu\parallel u\). The three eigenvalues of \(Q\) are distinct, hence \(u\) must be one of \(\pm e_1,\pm e_2,\pm e_3\). Their perimeters are \(\mathcal P(b,c),\mathcal P(a,c),\mathcal P(a,b)\), strictly ordered because \(\mathcal P\) increases strictly in each argument. There are no other critical points or critical values. In particular, the coarea formula gives a smooth density between critical values and no atoms.

**3. The three local quadratic forms.** At \(u=e_2\), use local sphere coordinates \(u=(x,\sqrt{1-x^2-z^2},z)\). Reflection symmetry kills the mixed quadratic term. If \(z=0\), one section semiaxis remains \(c\), while the other is \(a[1+(a^2/b^2-1)x^2]^{-1/2}\). If \(x=0\), one remains \(a\), while the other is \(c[1-(1-c^2/b^2)z^2]^{-1/2}\). Taylor expansion therefore yields

\[
L(u)=\ell_*-\tfrac12\mu x^2+\tfrac12\nu z^2+O((x^2+z^2)^2).
\]

The same saddle occurs at \(-e_2\). At \(\pm e_1\), the corresponding local expansion is \(\ell_-+(\alpha_1 y^2+\alpha_2 z^2)/2+O(\|(y,z)\|^4)\); at \(\pm e_3\), it is \(\ell_+-(\beta_1 x^2+\beta_2 y^2)/2+O(\|(x,y)\|^4)\). These follow from the analogous two-axis tilt formulas. All six critical points are nondegenerate.

**4. Exact logarithmic coefficient.** The spherical density in the local orthogonal coordinates is \((4\pi)^{-1}(1+O(x^2+z^2))\). The smooth Morse lemma permits a local change of coordinates taking the saddle exactly to \(t=(\nu z^2-\mu x^2)/2\); its Jacobian at the origin is one. Let \(p=\sqrt{\nu/2}\,z+\sqrt{\mu/2}\,x\) and \(q=\sqrt{\nu/2}\,z-\sqrt{\mu/2}\,x\). Then \(t=pq\) and \(dx\,dz=dp\,dq/\sqrt{\mu\nu}\). The model delta integral has singular part

\[
\int_{|p|,|q|<R}\!\delta(t-pq)\,dp\,dq
=2\log\frac{R^2}{|t|},
\]

for sufficiently small nonzero \(t\). A smooth Jacobian perturbation contributes only \(O(1)\). Each saddle contributes \((2\pi\sqrt{\mu\nu})^{-1}\log(1/|t|)\); there are two antipodal saddles. Smooth coarea contributions away from their neighborhoods remain bounded, proving the asserted full-density coefficient and two-sided remainder.

**5. The finite endpoint limits.** A positive definite quadratic minimum \((\alpha_1 y^2+\alpha_2 z^2)/2\) has a delta-integral density \(2\pi/\sqrt{\alpha_1\alpha_2}\) immediately above its minimum. Multiplying by \(1/(4\pi)\) and summing its two antipodal neighborhoods gives \(1/\sqrt{\alpha_1\alpha_2}\). The analogous negative definite maximum gives \(1/\sqrt{\beta_1\beta_2}\). There are no further contributions near the endpoints because the critical points are isolated and global extremizers. This completes the proof.

## Verification

The standalone file `ellipsoid_section_perimeter_checker.py` computes section perimeters two independent ways (from the two spectral invariants and from an explicit orthonormal plane basis). For each of three triaxial axis triples it checks 500 general normals for agreement, 1,500 normal directions for the exact support bounds, and both analytic principal-axis Hessian coefficients by finite differences. For \((a,b,c)=(3,2,1)\), the predicted saddle is \(\ell_*\approx13.364893221\) and the logarithmic density coefficient is \(0.0673016391598\). An independent twelve-million-orientation direct sampler gave fitted interscale logarithmic slopes approximately \(0.064\)–\(0.068\) near the critical value. This is corroboration, not an infinite proof or an independent audit.

Reproduce with Python 3 and NumPy/SciPy: `python ellipsoid_section_perimeter_checker.py`. All statements needed for the exact coefficients are derived analytically above; no numerical certificate is used as a logical premise.

## Relationship to prior work

Gendzwill and Stauffer (1981) give deterministic formulas for ellipsoid sections and their principal axes (especially pp. 143–146), but not a probability density for random central-section circumference. Makarenko, Fletcher and Shukurov (first public arXiv version 15 July 2014) study a distribution of the **dimensionless filamentarity** based jointly on area and perimeter of random, generally *offset* sections of randomly oriented triaxial ellipsoids; their reported modal cusp is a related motivation, not an exact density law or coefficient for the unnormalized perimeter of a Haar-uniform central section. Hinrichs et al. (arXiv 1901.06639, 2019) study high-dimensional random-section circumradii and probability bounds; those are not perimeter distributions. The logarithm from a nondegenerate saddle is a standard analytic mechanism; the new claim is its globally exhaustive location and explicit geometric coefficient for this perimeter observable, together with both exact endpoint limits.

## Limitations

The result excludes axisymmetric and spherical degeneracies (two equal semiaxes); the prefactor becomes singular as an axis gap closes and a different scaling then arises. No full closed-form density away from the critical values, no stability or finite-sample parameter estimation theorem, and no claim about random offset planes is made. Literature overlap cannot be ruled out absolutely, especially in older stereological tables or treatments of pushforwards of smooth spectral statistics. The scientific verification here is not independent.

## References

1. D. J. Gendzwill and M. R. Stauffer, *Analysis of Triaxial Ellipsoids: Their Shapes, Plane Sections, and Plane Projections*, Mathematical Geology **13** (1981), 135–153. Available full text: https://www.researchgate.net/publication/225869829_Analysis_of_triaxial_ellipsoids_Their_shapes_plane_sections_and_plane_projections .
2. I. Makarenko, A. Fletcher and A. Shukurov, *3D morphology of a random field from its 2D cross-section*, arXiv:1407.4048v1, publicly submitted 15 July 2014. https://arxiv.org/abs/1407.4048 .
3. A. Hinrichs, D. Krieg, E. Novak, J. Prochno and M. Ullrich, *Random sections of ellipsoids and the power of random information*, arXiv:1901.06639v1, publicly submitted 20 January 2019. https://arxiv.org/abs/1901.06639 .
