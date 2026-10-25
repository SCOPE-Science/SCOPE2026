# One-threshold reconstruction and the identifiability boundary for random ellipsoid sections

## Finding
Let \(E\subset\mathbb R^3\) be a centered ellipsoid with ordered semiaxes \(a\ge b\ge c>0\). Choose an unoriented plane through its center using rotation-invariant probability measure on the Grassmannian of two-planes, and write \(R\) for the maximum Euclidean norm of a point in that section (one-half its diameter). The following identifies exactly when the **one-dimensional, unlabeled distribution of \(R\)** determines all three semiaxes.

**Reconstruction theorem.** If \(a>b\), the essential support of \(R\) is exactly \([b,a]\). These two support endpoints determine \(a,b\), and **any single value** \(\Pr\{R\le r\}\), at an arbitrarily chosen \(b<r<a\), uniquely determines \(c\) within \((0,b]\). This remains true when \(b=c\).

For every \(b<r<a\), set
\[
\alpha=r^{-2}-a^{-2},\quad \beta=b^{-2}-r^{-2},\quad
\gamma=c^{-2}-r^{-2},\quad z=\frac{\alpha}{\alpha+\beta}.
\]
Here \(\alpha,\beta,\gamma>0\), and \(0<z<1\). An exact formula and **sharp complete range over the unknown smallest axis** are
\[
\Pr\{R\le r\}=1-\frac2\pi\int_0^{\pi/2}
\sqrt{\frac{\alpha(\cos^2\phi/\beta+\sin^2\phi/\gamma)}
{1+\alpha(\cos^2\phi/\beta+\sin^2\phi/\gamma)}}\,d\phi,
\]
\[
1-\sqrt z\ \le\ \Pr\{R\le r\}\ <\ 1-\frac2\pi\arcsin\sqrt z.
\]
The lower bound is attained **if and only if** \(c=b\); the upper bound is the best possible, but is not attained by a nondegenerate ellipsoid (it is approached as \(c\downarrow0\)). The cumulative probability is strictly decreasing and continuous as \(c\) increases through \((0,b]\), with \(a,b,r\) fixed. Therefore every value in this half-open interval corresponds to exactly one \(c\).

A second, independent reconstruction statistic is the upper-endpoint square-root coefficient. For \(a>b\), define
\[
L=\lim_{r\uparrow a}\frac{\Pr\{R>r\}}{\sqrt{a-r}},\qquad
\Delta=b^{-2}-a^{-2},\qquad
k^2=1-\frac{\Delta}{c^{-2}-a^{-2}}.
\]
Writing \(\mathsf E(k)=\int_0^{\pi/2}\sqrt{1-k^2\sin^2t}\,dt\) for the complete elliptic integral of the second kind, we obtain
\[
L=\frac2\pi\sqrt{\frac{2}{a^3\Delta}}\,\mathsf E(k),\qquad
\frac2\pi\sqrt{\frac{2}{a^3\Delta}}<L\le\sqrt{\frac{2}{a^3\Delta}}.
\]
Equality at the right occurs exactly when \(c=b\); the left endpoint is a sharp unattained limit as \(c\downarrow0\). Because \(\mathsf E\) decreases strictly on \([0,1)\), \(L\) uniquely determines \(c\), including the case \(b=c\).

**Sharp failure of identifiability.** If \(a=b\), then \(R=a\) almost surely for **every** \(c\in(0,a]\). Thus the smallest semiaxis cannot be identified from the section-diameter distribution when the two largest semiaxes coincide. The full distribution determines the unordered semiaxes precisely in the strict-top-axis regime \(a>b\), with this exact degeneracy on its boundary.

## Assumptions and scope
All semiaxes are strictly positive. Plane orientations have Haar probability measure, not an affine-invariant or offset-conditioned plane measure. Sections pass through the center. The observable is the maximal semiaxis of the planar elliptical section, or equivalently half of its Euclidean diameter, **without recording the section orientation or the smaller section semiaxis**. The orientation distribution is continuous and normalized to total mass one. The exact one-threshold result assumes known support endpoints obtained from the full idealized probability law, not from finitely many measurements.

## Proof
Write \(q_1=a^{-2}\le q_2=b^{-2}\le q_3=c^{-2}\) and \(Q=\operatorname{diag}(q_1,q_2,q_3)\). For a plane \(n^\perp\) with unit normal \(n\), the section radius is
\[
R(n)=\left(\min_{v\perp n,\ |v|=1}v^\mathsf TQv\right)^{-1/2}.
\]
If \(a>b\), the Courant--Fischer interlacing inequalities imply \(q_1\le R(n)^{-2}\le q_2\), so \(b\le R(n)\le a\). With \(n=e_1\) and \(n=e_3\), these endpoint values are attained. Continuity of the minimum Rayleigh quotient and positive Haar measure of every open spherical neighborhood show that the essential support is all of \([b,a]\).

Fix \(b<r<a\) and put \(t=r^{-2}\). The strict sublevel cone of \(Q\) relative to \(t\) is
\[
\big\{v:\ \beta v_2^2+\gamma v_3^2<\alpha v_1^2\big\}.
\]
The section has \(R(n)>r\) precisely when \(n^\perp\) meets this cone nontrivially. Setting \(v_1=1\), this amounts to minimizing \(\beta v_2^2+\gamma v_3^2\) subject to \(n_2v_2+n_3v_3=-n_1\). Weighted Cauchy--Schwarz gives minimum \(n_1^2/(n_2^2/\beta+n_3^2/\gamma)\), so (outside probability-zero boundary cases)
\[
R(n)\le r\quad\Longleftrightarrow\quad
n_1^2\ge\alpha\left(\frac{n_2^2}{\beta}+\frac{n_3^2}{\gamma}\right).
\]
For a uniformly random normal, \(|n_1|\) is uniform on \([0,1]\) and independent of the azimuthal angle \(\phi\) of \((n_2,n_3)\), modulo the symmetries of squares. Writing \(H(\phi)=\cos^2\phi/\beta+\sin^2\phi/\gamma\), the last criterion becomes \(|n_1|\ge\sqrt{\alpha H/(1+\alpha H)}\). Integrating its conditional probability proves the exact formula.

For fixed \(a,b,r\), increasing \(c\) strictly decreases \(\gamma\) and strictly increases \(H(\phi)\) for every \(\phi\in(0,\pi/2)\). The square-root integrand is strictly increasing in \(H\); hence the cumulative probability decreases strictly. Continuity is immediate from bounded convergence. At \(c=b\), \(\gamma=\beta\), and the integral reduces to \(\sqrt{\alpha/(\alpha+\beta)}=\sqrt z\). As \(c\downarrow0\), \(\gamma\to\infty\), and the integrand becomes \(\sqrt{\alpha\cos^2\phi/(\beta+\alpha\cos^2\phi)}\). Substitution \(u=\sin\phi\) evaluates its mean to \((2/\pi)\arcsin\sqrt z\). For finite \(c\) the integrand is strictly larger on a set of positive measure, so the upper envelope is unattained. Strict monotonicity gives the claimed one-point inverse correspondence.

Next let \(r\uparrow a\). Since \(\alpha=r^{-2}-a^{-2}=2(a-r)/a^3+O((a-r)^2)\), bounded dominated convergence yields
\[
L=\frac2\pi\sqrt{\frac2{a^3}}\int_0^{\pi/2}
\sqrt{\frac{\cos^2\phi}{q_2-q_1}+
\frac{\sin^2\phi}{q_3-q_1}}\,d\phi.
\]
Factoring \(\Delta^{-1/2}\), this is the stated complete elliptic integral. As \(c\) increases, the integrand increases strictly except at isolated angles; hence \(L\) is strictly increasing, with \(\mathsf E(1)=1\) and \(\mathsf E(0)=\pi/2\) yielding the sharp limits. The value of \(k\), and hence \(c=(q_1+\Delta/(1-k^2))^{-1/2}\), is uniquely recovered.

Finally, if \(a=b\), every two-plane intersects the two-dimensional top-eigenspace \(\operatorname{span}(e_1,e_2)\) in a nonzero direction. The section contains a radial segment of length \(a\) in that direction, and no section radius exceeds \(a\). Thus \(R=a\) for every plane, independent of \(c\). This also includes spheres.

## Verification
The standard-library checker `check_triaxial.py` constructs an orthonormal basis of each sampled plane and directly diagonalizes the corresponding \(2\times2\) quadratic-form restriction. For 90,000 independently generated Haar normals it separately checks the quadratic cone criterion at five thresholds, compares empirical probabilities against deterministic Simpson quadrature of the exact formula, verifies strict ordering in the smallest axis and both sharp endpoint envelopes, and tests the elliptic-integral square-root asymptotic. The checker reports `TRIAXIAL_SECTION_CHECK_OK orientations=90000 thresholds=5 upper_coefficient=0.306288274762`. The exact symbolic proof above, not Monte Carlo or quadrature, establishes the universal assertions.

For example, the axes \((a,b,c)=(4,2,1)\) give \(\Pr\{R\le3\}=0.609526908472756\ldots\), between the two sharp bounds. Their upper-endpoint coefficient is \(L=0.306288274761508\ldots\).

## Relationship to prior work
Guedon, Litvak, Tatarko and Vritsiou, arXiv:2609.24131 (first publicly available September 21, 2026), investigate diameters of random sections of general convex bodies, including \(p\)-ellipsoids, and develop sharp probability bounds in high-dimensional regimes. The present work asks a distinct finite-dimensional **inverse** question: which axes are determined by an *unlabeled scalar diameter distribution*, and what is the best possible one-threshold range?

The entire **forward joint eigenvalue law** of Haar-orthogonal compressions of a fixed-spectrum symmetric matrix is classical: see Cuenca, arXiv:1807.06134, Section 1.2--1.3 and its attribution to the earlier Rayleigh-triangle formulas. The forward marginal distribution by itself is **not claimed as novel**. The claimed contribution here is the complete sharp one-threshold inverse/reconstruction criterion, its optimal envelopes and a precise top-axis degeneracy, obtained by an elementary cone formulation rather than by republishing that joint density. Prior work reconstructing ellipsoid axes from inverse moments of random central-section **volumes** concerns a different measured statistic and does not immediately imply the present diameter-only conclusion.

## Limitations
The reconstruction assumes the full ideal probability law, whose support endpoints cannot in general be exactly determined from a finite noisy sample. Neither finite-sample stability rates nor robust estimation bounds are proved. The exact forward integral itself is a specialization of classical random compression laws, and historical priority for the stronger inverse and sharp-range conclusions has not been independently certified. All results are restricted to three-dimensional ellipsoids and center-passing Haar-random planes; random offset planes or higher-dimensional sections obey different laws. Although the one-point dependence on \(c\) is strictly monotone, its inverse can be poorly conditioned near singular axis limits.

## References
1. O. Guedon, A. E. Litvak, K. Tatarko, B.-H. Vritsiou, *On random diameters of convex bodies*, arXiv:2609.24131, September 21, 2026. https://arxiv.org/abs/2609.24131
2. C. Cuenca, *Universal behavior of the corners of orbital beta processes*, arXiv:1807.06134, 2018; especially Section 1.2--1.3 on Haar-orthogonal random matrix compressions and Rayleigh-triangle densities. https://arxiv.org/html/1807.06134v2
3. A. A. Makarenko, A. Fletcher and A. Shukurov, *3D morphology of a random field from its 2D cross-section*, arXiv:1407.4048, 2014. https://arxiv.org/abs/1407.4048
