# Sharp intact-section probabilities for convex cylinders with fixed base perimeter

## Finding
Let \(B\subset\mathbb R^2\) be any compact convex body with nonempty interior, perimeter \(2\pi r\), and let \(C=B\times[-H/2,H/2]\subset\mathbb R^3\), where \(H,r>0\). Choose an unoriented affine plane by Euclidean-motion-invariant plane measure, conditioned on intersecting \(C\). An **intact section** is a section that equals the whole section of the infinite cylinder \(B\times\mathbb R\) by the same plane; thus neither horizontal end cap truncates it. Let \(p(B,H)\) be the probability of an intact section.

The following interval is sharp and complete:
\[
\boxed{\frac{H-2r\arctan(H/(2r))}{H+\pi r}\ \le\ p(B,H)\ <\ \frac{\sqrt{H^2+\pi^2r^2}-\pi r}{H+\pi r}.}
\]
**Lower equality holds exactly for planar convex bodies of constant width \(2r\)**, including disks and noncircular Reuleaux bodies. The upper endpoint is not attained by a body with nonempty interior, but is approached by rectangles degenerating to a segment while their perimeter remains \(2\pi r\). Every probability between the two endpoints, including the lower endpoint and excluding the upper endpoint, occurs for some such convex base.

The probability depends only on the entire directional width function of \(B\), not on its nonsymmetric component. Define \(w_B(v)=\max_{x\in B}\langle v,x\rangle-\min_{x\in B}\langle v,x\rangle\) for \(v\in S^1\) and \(F_H(x)=H/2-x\arctan(H/(2x))\) for \(x>0\) (continuously \(F_H(0)=H/2\)). Then
\[
\boxed{p(B,H)=\frac{2}{H+\pi r}\frac1{2\pi}\int_0^{2\pi}F_H\bigl(w_B((\cos\phi,\sin\phi))/2\bigr)\,d\phi.}
\]
The lower bound has a quantitative rigidity refinement:
\[
\boxed{p(B,H)-\frac{H-2r\arctan(H/(2r))}{H+\pi r}
\ \ge\ \frac{4H^3}{(H+\pi r)(H^2+\pi^2r^2)^2}
\frac1{2\pi}\int_0^{2\pi}\bigl(w_B((\cos\phi,\sin\phi))/2-r\bigr)^2\,d\phi.}
\]
The displayed rigidity coefficient is valid for every base and height; optimality of that coefficient is not claimed.

For a disk base of radius \(r\), intact sections are ellipses almost surely. Put \(\kappa=H/(2r)\) and let \(E\) be the usual Euclidean eccentricity of a section, conditional on being intact. Its exact distribution is
\[
\boxed{\mathbb P(E\le x\mid\text{intact})=
\frac{\kappa x^2-\arcsin x+x\sqrt{1-x^2}}{\kappa-\arctan\kappa},\qquad
0\le x\le\frac{\kappa}{\sqrt{1+\kappa^2}}.}
\]
The conditional law of \(E/\kappa\) tends to \(\operatorname{Beta}(2,2)\) as \(\kappa\downarrow0\), while \(E\) tends to \(\operatorname{Beta}(2,1)\) as \(\kappa\to\infty\). Consequently the narrow-height decay exponents of the sharp lower and upper envelope differ:
\[
\frac{H-2r\arctan(H/(2r))}{H+\pi r}\sim\frac{H^3}{12\pi r^3},\qquad
\frac{\sqrt{H^2+\pi^2r^2}-\pi r}{H+\pi r}\sim\frac{H^2}{2\pi^2r^2}
\quad(H/r\downarrow0).
\]

## Assumptions and scope
All base bodies are compact, convex, and have nonempty planar interior. Heights are strictly positive. The base can be asymmetric and need not have differentiable boundary. Perimeter is the usual Euclidean perimeter. The finite cylinder is the Cartesian product with the vertical interval; no skew, taper or curved lateral walls are assumed. Random planes have **joint invariant measure**, not a uniform orientation followed by an independently normalized offset: the probability density on a normal \(n\in S^2_+\) and signed offset \(t\) is proportional to \(\mathbf1\{\{x:\langle n,x\rangle=t\}\cap C\ne\varnothing\}\,d\sigma(n)\,dt\). Tangent and vertical planes have zero measure and do not affect the formulas.

The parameter \(r\) is the radius of a disk with the **same perimeter** as \(B\); it is not an inradius or an area radius. The constant-width equality family is determined by \(w_B(v)\equiv2r\). Equality at the upper endpoint is excluded only because the base is required to have nonempty interior.

## Proof
**1. Offset interval and invariant normalization.** Write a normal (apart from a null set) as \(n=(\sin\theta\,v,\cos\theta)\), where \(0\le\theta\le\pi/2\) and \(v=(\cos\phi,\sin\phi)\). The projection of \(C\) onto \(n\) has interval length
\[
L_{\mathrm{hit}}(\theta,v)=H\cos\theta+w_B(v)\sin\theta.
\]
The plane \(\langle n,(x,z)\rangle=t\) contains the entire infinite-cylinder affine section precisely when the heights \(z=(t-\sin\theta\langle v,x\rangle)/\cos\theta\) lie in \([-H/2,H/2]\) for every \(x\in B\). The admissible interval of \(t\) therefore has length
\[
L_{\mathrm{intact}}(\theta,v)=\bigl[H\cos\theta-w_B(v)\sin\theta\bigr]_+.
\]
The normalized spherical area element on the upper normal hemisphere is \(\sin\theta\,d\theta\,d\phi/(2\pi)\). Cauchy's planar perimeter formula yields \((2\pi)^{-1}\int_0^{2\pi}w_B(v)\,d\phi=2r\), so the total hitting measure after this harmless angular normalization is \(H/2+\pi r/2\). Direct integration, with \(q=w_B(v)/2>0\), gives
\[
\int_0^{\pi/2}\bigl[H\cos\theta-2q\sin\theta\bigr]_+\sin\theta\,d\theta
=\frac H2-q\arctan\frac H{2q}=F_H(q).
\]
Division gives the claimed exact probability and shows invariance under replacing the base by its central symmetral \((B+(-B))/2\).

**2. Strict lower bound and constant-width equality.** Differentiating twice gives
\[
F_H''(x)=\frac{4H^3}{(H^2+4x^2)^2}>0.
\]
Since \(q(v)=w_B(v)/2\) has angular mean \(r\), strict Jensen gives \(\langle F_H(q)\rangle\ge F_H(r)\), with equality if and only if \(q\) is constant. By continuity of widths this means \(w_B\equiv2r\). There are genuinely noncircular equality bodies: the smooth support function \(h(\phi)=r+\varepsilon\cos(3\phi)\), with \(0<|\varepsilon|<r/8\), has positive radius of curvature \(h(\phi)+h''(\phi)=r-8\varepsilon\cos(3\phi)>0\) and constant width \(2r\). Substitution gives the stated lower envelope.

**3. Sharp upper bound over all convex bases.** The central symmetral \(K=(B+(-B))/2\) has support function \(h_K(v)=q(v)\) and perimeter \(2\pi r\). Every centrally symmetric planar convex body is a zonoid, because centrally symmetric polygons are sums of segments and approximate it in Hausdorff distance. Consequently there exists a probability measure \(\nu\) on unoriented angles \(\alpha\in[0,\pi)\) such that
\[
q((\cos\phi,\sin\phi))=a\int_0^\pi|\cos(\phi-\alpha)|\,d\nu(\alpha),\qquad a=\frac{\pi r}2.
\]
The value of \(a\) follows by angular averaging: \(\langle|\cos|\rangle=2/\pi\). Applying Jensen in \(\nu\) and integrating over \(\phi\) yields
\[
\langle F_H(q)\rangle\le\frac2\pi\int_0^{\pi/2}F_H(a\cos t)\,dt.
\]
Write \(\eta=H/(2a)=H/(\pi r)\). The elementary integral \(J(\eta)=\int_0^{\pi/2}\cos t\arctan(\eta/\cos t)\,dt\) obeys
\[
J'(\eta)=\frac\pi2\left(1-\frac\eta{\sqrt{1+\eta^2}}\right),\qquad J(0)=0,
\]
whence \(J(\eta)=\frac\pi2(1+\eta-\sqrt{1+\eta^2})\). It follows that the upper numerator is \((\sqrt{H^2+\pi^2r^2}-\pi r)/2\), proving the upper envelope.

For a full-dimensional \(K\), the representing direction law \(\nu\) is not a point mass. For any two nonparallel segment directions, their absolute cosine supports differ at almost every \(\phi\). Strict convexity of \(F_H\) therefore makes the upper Jensen inequality strict on a set of positive angular measure. If \(K\) is a segment, equality holds, but it has no interior. Rectangles of fixed perimeter that collapse onto this segment converge in the support metric and approach the upper bound. Finally, the full-dimensional family \(B_s=(1-s)r\mathbb B_2+s[-a,a]e\), \(0\le s<1\), has constant perimeter \(2\pi r\). Its expected transformed support is strictly convex in \(s\), has derivative zero at \(s=0\), and thus increases continuously and strictly from the lower value to the upper value as \(s\uparrow1\). Hence the asserted probability interval is exact.

**4. Quantitative width rigidity.** The representation in Step 3 implies \(0\le q(v)\le a=\pi r/2\). Over this interval, \(F_H''\ge m=4H^3/(H^2+\pi^2r^2)^2\). The strong-convexity form of Jensen states \(\langle F_H(q)\rangle-F_H(r)\ge(m/2)\langle(q-r)^2\rangle\). Division by \((H+\pi r)/2\) proves the displayed stability estimate, with no additional regularity assumption.

**5. Disk ellipticity law.** For a disk, \(w_B\equiv2r\). An intact oblique section is an ellipse with semiaxes \(r\) and \(r/\cos\theta\), hence eccentricity \(E=\sin\theta\). The intact offset interval contributes weight \(2r[\kappa\cos\theta-\sin\theta]_+\), and \(\theta\le\arctan\kappa\). Changing variables \(x=\sin\theta\), the unnormalized eccentricity density is \(2r x(\kappa-x/\sqrt{1-x^2})\); its integral is \(r(\kappa-\arctan\kappa)\). Integrating and normalizing gives the stated CDF. Taylor expansion at \(\kappa=0\) yields the limit \(3y^2-2y^3\) for \(E/\kappa\), and dividing numerator and denominator by \(\kappa\) gives the limit \(y^2\) at infinity. Taylor expansion of the two envelopes proves the thin-height orders.

## Verification
Run `python verify_sections.py` with Python 3, NumPy, SciPy and SymPy installed. The script symbolically verifies the curvature identity and both thin-height coefficients, independently integrates the angle/offset formula for square, slender rectangle and asymmetric triangle bases at four heights, checks perimeter-normalized inequalities, the segment supremum, the width-variance lower gap, the complete disk eccentricity CDF and beta limit, and a direct rejection simulation of Euclidean-invariant joint plane-normal/offset measure on three base shapes. The final output is `ALL_CHECKS_PASSED`. The proof above, rather than finite numerical checks, establishes the unrestricted statements.

## Relationship to prior work
Van der Jagt, Jongbloed and Vittorietti (arXiv:2305.02864, first public version 4 May 2023) define the precise invariant sampling model for hyperplane sections and investigate absolute continuity and estimation of **section-area** laws, not intactness of a cylinder section or the fixed-perimeter extremal probability. Dirksen (arXiv:1602.07854, first public version 25 February 2016) studies **central cylinder sections** and maximal section area, including the elliptic-versus-truncated geometry; his results do not give the invariant-affine-plane intact-section event or the complete base-shape optimization. Jongbloed, McGarrity and Sietsma (DOI:10.1007/s11749-020-00729-9, first published 14 August 2020) analyze **vertical, fixed-orientation** plane cuts of a cylinder ensemble and size estimation, not the present isotropic orientation law. Cauchy's perimeter identity, the planar zonoid representation, and Jensen's inequality are standard mathematical ingredients and are not claimed as new. Historical priority for the combined probability and sharp extremizers remains provisional.

## Limitations
The theorem concerns Euclidean-motion-invariant affine planes conditional on hitting the cylinder, not uniform unoriented normals with independently sampled, shape-normalized offsets. It does not address skew cylinders, tapered frusta, spatially nonuniform planes or curved cylinder walls. The entire section is deemed intact only when neither end cap truncates the corresponding infinite-cylinder section. The stability coefficient need not be best possible. The conditional ellipse eccentricity law concerns a circular base only. No claim is made that finite computations prove any continuum statement, or that external literature searches establish global historical uniqueness.

## References
1. T. van der Jagt, G. Jongbloed and M. Vittorietti, *Existence and approximation of densities of chord length- and cross section area distributions*, arXiv:2305.02864 (first public version 2023-05-04), https://arxiv.org/abs/2305.02864; *Image Analysis & Stereology* 42 (2023), 171–184, DOI:10.5566/ias.2923.
2. H. Dirksen, *Hyperplane Sections of Cylinders*, arXiv:1602.07854 (first public version 2016-02-25), https://arxiv.org/abs/1602.07854.
3. G. Jongbloed, K. S. McGarrity and J. Sietsma, *Smooth estimation of size distributions in an oriented cylinder model*, *TEST* 30 (2021), 505–526; first online 2020-08-14, DOI:10.1007/s11749-020-00729-9.
4. R. Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, 2nd ed., Cambridge University Press, 2014, for support functions, Cauchy's perimeter formula and planar zonoids (background only).
