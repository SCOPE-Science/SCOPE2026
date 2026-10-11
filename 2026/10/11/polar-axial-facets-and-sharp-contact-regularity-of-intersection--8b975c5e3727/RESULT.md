# Polar axial facets and sharp contact regularity of intersection bodies of smooth prisms

## Finding

Let \(n\geq3\), let \(B\subset\mathbb R^{n-1}\) be an origin-symmetric convex body with a \(C^\infty\) boundary of strictly positive Gauss curvature, let \(h>0\), and put \(K=B\times[-h,h]\). Define its intersection body \(I K\) by
\[\rho_{I K}(u)=\operatorname{Vol}_{n-1}(K\cap u^\perp),\qquad u\in S^{n-1}.\]
Write \(V=\operatorname{Vol}_{n-1}(B)\), \(H(v)=\max_{x\in B}\langle x,v\rangle\) for \(v\in S^{n-2}\), and \(B^\circ=\{y:\langle x,y\rangle\leq1\text{ for every }x\in B\}\). Then the intersections of \(I K\) with its two horizontal supporting hyperplanes are **exactly**
\[I K\cap\{z=\pm V\}=\{(y,\pm V):y\in hV B^\circ\}.\]
In particular, the two axial exposed facets are precisely scaled copies of the **polar** of the original base, not generally copies of the base itself.

For each \(v\in S^{n-2}\), let \(x(v)\in\partial B\) be the unique point with outer unit normal \(v\), and let \(\mathcal K(v)>0\) be its Gauss curvature. Set \(r_0(v)=hV/H(v)\). In the meridional half-plane \(\{(rv,z):r\geq0\}\), the part of the upper boundary immediately outside the axial facet has a single-valued graph \(z=z_v(r)\) with
\[
\boxed{V-z_v(r)=C(v)\bigl(r-r_0(v)\bigr)^{n/2}\bigl(1+o(1)\bigr),\quad r\downarrow r_0(v),\ r>r_0(v),}
\]
where the strictly positive and explicit constant is
\[
\boxed{C(v)=\frac{2^{n/2+1}\kappa_{n-2}}{n\sqrt{\mathcal K(v)}}\left(\frac{H(v)^2}{hV}\right)^{n/2},\qquad
\kappa_j=\frac{\pi^{j/2}}{\Gamma(1+j/2)}.}
\]
This has an optimal *global boundary regularity* consequence. Let \(k=\lceil n/2\rceil-1\) and \(\alpha=n/2-k\), so \(0<\alpha\leq1\). The embedded hypersurface \(\partial(IK)\) is \(C^{k,\alpha}\), but it is not \(C^{k,\beta}\) for any \(\beta>\alpha\) when \(\alpha<1\), nor \(C^{k+1}\) when \(\alpha=1\). Thus in dimension \(3\) the rim is sharply \(C^{1,1/2}\), in dimension \(4\) it is \(C^{1,1}\) but not \(C^2\), and the optimal smoothness rises in successive half-integer steps as the dimension grows.

## Assumptions and scope

The ambient Euclidean space has dimension \(n\geq3\). The base has dimension \(n-1\), contains the origin in its interior, is centrally symmetric, and has \(C^\infty\) boundary with every principal curvature strictly positive. No rotational symmetry of \(B\) is assumed. \(\mathcal K(v)\) denotes the product of those \(n-2\) principal curvatures at the support point with normal \(v\). The intersection body uses unnormalized Euclidean central-section volume. Convexity of \(I K\) follows from the classical intersection-body theorem for symmetric convex bodies; the proof below identifies its axial facets and their precise tangency order. The \(C^{k,\alpha}\) statement is about local hypersurface graphs, including every point of the facet rims, not merely about radial data along one chosen direction.

## Proof

**1. Exact section/strip identity.** Use coordinates \((x,z)\in\mathbb R^{n-1}\times\mathbb R\). For \(0\leq\theta<\pi/2\) and \(v\in S^{n-2}\), the central hyperplane orthogonal to \(u=(\sin\theta\,v,\cos\theta)\) is \(z=-\tan\theta\langle x,v\rangle\). Its Jacobian over the \(x\)-coordinates is \(\sec\theta\). Consequently
\[
\rho_{I K}(\theta,v)=\sec\theta\,S\bigl(v,h\cot\theta\bigr),\qquad
S(v,t)=\operatorname{Vol}_{n-1}\{x\in B:|\langle x,v\rangle|\leq t\},
\]
where at \(\theta=0\) the strip is interpreted as the entire base. Central symmetry gives \(S(v,t)=V-2A_v(H(v)-t)\) for \(0\leq t\leq H(v)\), where \(A_v(s)\) is the volume of the cap \(\{x\in B:\langle x,v\rangle>H(v)-s\}\); also \(S(v,t)=V\) for \(t\geq H(v)\).

**2. Exact polar facets.** The upper height of the radial boundary point is \(\rho_{I K}(\theta,v)\cos\theta=S(v,h\cot\theta)\leq V\). Equality holds exactly when \(h\cot\theta\geq H(v)\), since positive curvature and nonempty interior make every positive-height cap have positive volume. The corresponding horizontal radial coordinate is \(r=V\tan\theta\), so equality holds precisely for \(0\leq r\leq hV/H(v)\). The identity \(\rho_{B^\circ}(v)=1/H(v)\) therefore identifies the entire top facet as \(hV B^\circ\times\{V\}\). Central symmetry yields the bottom facet.

**3. Local cap coefficient.** Fix \(v\). At the support point \(x(v)\), use tangent coordinates \(w\in\mathbb R^{n-2}\) and inward normal depth \(s\). The boundary has the local expansion
\[s=\tfrac12\langle Q_v w,w\rangle+O(|w|^3),\quad Q_v>0,\quad\det Q_v=\mathcal K(v).\]
The smooth Morse lemma straightens this positive-definite height function into \(|w'|^2/2\), with Jacobian at the origin \(\mathcal K(v)^{-1/2}\). Integrating the thickness of the resulting cap and scaling \(w'=\sqrt\delta\,\xi\) shows, as \(\delta\downarrow0\),
\[
A_v(\delta)=\frac{2^{n/2}\kappa_{n-2}}{n\sqrt{\mathcal K(v)}}\delta^{n/2}\bigl(1+O(\delta)\bigr).
\]
The odd Taylor terms of the smooth Jacobian integrate to zero on the centered ball. The same argument yields a complete smooth one-sided factor after extracting \(\delta^{n/2}\), with derivative bounds; it is uniform over support normals by compactness and positive curvature. In particular, the leading coefficient is nonzero in every direction.

**4. Contact with the facet.** Write the upper boundary near the rim as \((rv,z_v(r))\). The exact identity in step 1 becomes
\[z_v(r)=V-2A_v\left(H(v)-\frac{h z_v(r)}r\right)\]
for \(r>r_0(v)\) close to \(r_0(v)\). The associated angular parametrization has \(r=V\tan\theta+O((\theta-\theta_0)^{n/2})\), with \(\theta_0(v)=\arctan(h/H(v))\). Hence \(r\) is a valid increasing boundary coordinate near the rim, and \(V-z_v(r)=O((r-r_0)^{n/2})\). It follows that
\[H(v)-h z_v(r)/r=\frac{H(v)}{r_0(v)}(r-r_0(v))+o(r-r_0(v)).\]
Insert this into the cap expansion in step 3, use \(H(v)/r_0(v)=H(v)^2/(hV)\), and obtain the stated exact coefficient \(C(v)\).

**5. Optimal smoothness.** In smooth local coordinates transverse to the polar-facet rim, the proof in steps 3–4 yields a smooth, nonvanishing factor multiplying the one-sided power \((s_+)^{n/2}\). All other boundary pieces are \(C^\infty\): on the facet this is clear; off its rim the strip boundaries cut the positively curved base transversely and the section-volume integral depends smoothly on its direction. For \(k=\lceil n/2\rceil-1\) and \(\alpha=n/2-k\), the one-sided power belongs to \(C^{k,\alpha}\). If \(n\) is odd, its \(k\)-th derivative has precisely the nonzero \(\alpha\)-Hölder leading term and no better exponent; if \(n\) is even, its \(n/2\)-th derivative has a nonzero one-sided jump. Since \(C(v)>0\) at every rim point, these failures cannot cancel. This proves the global optimal regularity assertions.

## Verification

The standalone script `verify.py` uses 65-digit arithmetic. It checks 266 instances, including two equivalent independently integrated slicing expressions for circular bases in dimensions \(3\) through \(12\), the sharp angular and facet-graph coefficients, an independent section-plane polar integral in dimension \(3\), and anisotropic elliptical bases with curvature computed directly from the ellipse. Its observed output is `VERIFY_OK cases=266 max_slicing_relative_error=3.816723e-65 max_cap_coefficient_relative_error=0.00015736394`. Small finite errors for the leading coefficients reflect testing at positive, rather than infinitesimal, distances. These tests do not prove an infinite-dimensional or global assertion; steps 1–5 provide the analytic proof.

## Relationship to prior work

Alfonseca and Kim [1] analyze quantitative convexity of intersection bodies of bodies of revolution, including the round cylinder. Their main local power-type results concern the **equator**; the polar axial facets and curvature-dependent rim contact for nonrotational smooth bases are different geometric data. Dirksen [2] supplies general central-section formulas and a three-dimensional piecewise formula for round cylinders and analyzes maximal sections, but does not state the anisotropic polar-facet identity, positive-curvature coefficient, or dimension-optimal rim regularity. Classical theory includes the Busemann convexity theorem and smooth-cap asymptotics; they are premises, not claimed as discoveries. A general microlocal treatment of Radon-transform singularities [3] is historically relevant and could overlap with the contact exponent; its exact specialization to facet geometry has not been independently established here.

## Limitations

The theorem requires central symmetry, a bounded positive-height product prism, and smooth strictly positive Gaussian curvature of the base to claim a universal sharp coefficient and global Hölder class. It makes no such regularity claim for polytopal bases, zero-curvature points, nonsymmetric bases, or non-product bodies. It identifies only the axial supporting facets; it does not classify all other exposed faces in arbitrary nonrotational examples. The cap coefficient is asymptotic rather than an exact finite-distance profile. The cited general singularity literature leaves a residual historical overlap risk, and independent expert validation has not been performed.

## References

[1] M. A. Alfonseca and J. Kim, *On the local convexity of intersection bodies of revolution*, arXiv:1304.3359v1 (first publicly available 2013-04-11), especially §§1–3 and the cylinder discussion in §4; https://arxiv.org/abs/1304.3359.

[2] H. Dirksen, *Hyperplane Sections of Cylinders*, arXiv:1602.07854v1 (first publicly available 2016-02-25), especially Lemma 2.1 and §§2–3; https://arxiv.org/abs/1602.07854.

[3] A. G. Ramm and A. I. Zaslavsky, *Singularities of the Radon transform*, Bull. Amer. Math. Soc. 28 (1993), 109–115, arXiv:math/9301215; https://arxiv.org/abs/math/9301215 (full-text comparison unresolved).
