# The exact John ellipsoid of a one-step generalized Steiner ball, with a singular dimension crossover

## Finding

For every integer \(n\ge2\) and \(0\le\lambda\le1/2\), apply one \(\lambda\)-Steiner symmetrization in any direction to the Euclidean unit ball \(B_2^n\). The resulting body \(K_{n,\lambda}\) has **exactly** the John ellipsoid
\[
E_{n,\lambda}=\left\{(x,z)\in\mathbb R^{n-1}\times\mathbb R:\frac{\|x\|_2^2}{a^2}+\frac{(z-c)^2}{b^2}\le1\right\},
\]
where, writing \(\alpha=2(1-\lambda)\), \(\beta=2\lambda\) and \(D=\sqrt{(n-1)^2\beta^2+4n\alpha^2}\),
\[
 b=\frac12\left(\beta+\frac{D}{n+1}\right),\qquad
 c=b-\beta,\qquad
 a^2=\frac{(n+1)b^2-n\beta b}{\alpha^2}.
\]
The ellipsoid is unique. Its normalized volume ratio, denoted \(\eta_n(\lambda)=\operatorname{vol}_n(E_{n,\lambda})/\operatorname{vol}_n(K_{n,\lambda})\), equals \(a^{n-1}b\). At the shaking endpoint,
\[
\eta_n(0)=\frac{2}{\sqrt{n+1}}\left(\frac{n}{n+1}\right)^{n/2}\sim\frac{2e^{-1/2}}{\sqrt n},
\]
whereas for every fixed \(0<\lambda\le1/2\),
\[\lim_{n\to\infty}\eta_n(\lambda)=2\lambda.\]
The exact transition scale is \(\lambda=t/\sqrt n\): for each fixed \(t\ge0\),
\[
\boxed{\displaystyle \lim_{n\to\infty}\sqrt n\,\eta_n(t/\sqrt n)
=\left(t+\sqrt{t^2+4}\right)\exp\left[-\frac{\left(\sqrt{t^2+4}-t\right)^2}{8}\right].}
\]
Here \(t/\sqrt n\le1/2\) is understood for sufficiently large \(n\).

## Assumptions and scope

Fix \(n\ge2\), Euclidean coordinates \((x,z)\in\mathbb R^{n-1}\times\mathbb R\), and \(0\le\lambda\le1/2\). The symmetrization moves each vertical chord of \(B_2^n\), preserving length, to have lower and upper endpoints \(-2\lambda\sqrt{1-\|x\|_2^2}\) and \(2(1-\lambda)\sqrt{1-\|x\|_2^2}\). Thus
\[
 K_{n,\lambda}=\{(x,z):\|x\|_2\le1,\ -\beta\sqrt{1-\|x\|_2^2}\le z\le\alpha\sqrt{1-\|x\|_2^2}\}.
\]
This is a convex body, the union along a common equatorial disk of the upper half of the ellipsoid \(\|x\|_2^2+z^2/\alpha^2\le1\) and, for \(\beta>0\), the lower half of \(\|x\|_2^2+z^2/\beta^2\le1\). At \(\beta=0\), the lower half is the flat equatorial disk. The volume of this body is \(\kappa_n(\alpha+\beta)/2=\kappa_n\), where \(\kappa_n\) denotes the unit-ball volume. No regularity beyond convexity is imposed.

## Proof

**1. Parameters and an upper inclusion certificate.** For \(\alpha\ge\beta\ge0\), the stated value \(b\) is the positive solution of
\[
 b^2-\beta b=\frac{n(\alpha^2-\beta^2)}{(n+1)^2}.
\]
Consequently \(b\ge\beta\), \(c=b-\beta\ge0\), and \(a^2=(n+1)b^2/\alpha^2-n\beta b/\alpha^2>0\). Parameterize the candidate ellipsoid by \(x=a\sqrt{1-s^2}\,\omega\), \(z=c+bs\), with \(-1\le s\le1\) and \(\omega\in S^{n-2}\). Using the quadratic identity above and the definition of \(a\), direct expansion gives the exact certificate
\[
 a^2(1-s^2)+\frac{(c+bs)^2}{\alpha^2}
=1-\frac{nb(b-\beta)}{\alpha^2}\left(s-\frac1n\right)^2\le1.
\]
The same inequality holds for every point in the interior by convexity of the upper ellipsoid, so \(E_{n,\lambda}\) lies inside the complete upper ellipsoid \(\|x\|_2^2+z^2/\alpha^2\le1\). In particular, setting \(s=0\) shows \(a^2\le1\).

**2. The lower inclusion certificate.** If \(\beta=0\), the lowest ordinate of \(E_{n,0}\) is \(c-b=0\); the preceding upper inclusion suffices. Suppose \(\beta>0\). A point on the ellipsoid boundary lies below the equator precisely for \(-1\le s\le s_0\), where \(s_0=-c/b\in[-1,0]\). On this interval define
\[
 F_\beta(s)=a^2(1-s^2)+\frac{(c+bs)^2}{\beta^2}.
\]
Its quadratic coefficient is \(b^2/\beta^2-a^2\ge0\), since \(b\ge\beta\) and \(a\le1\). Thus \(F_\beta\) is convex. At the interval endpoints, \(F_\beta(-1)=1\) and \(F_\beta(s_0)=a^2(1-s_0^2)\le1\); hence \(F_\beta(s)\le1\) throughout. All lower boundary points of \(E_{n,\lambda}\) belong to the lower ellipsoid. The interior follows by convexity, proving \(E_{n,\lambda}\subseteq K_{n,\lambda}\).

**3. Optimality and uniqueness through \(n+1\) contacts.** Normalize the candidate ellipsoid to \(B_2^n\) with \((x,z)=(ay,c+bw)\). Its bottom pole \((0,-1)\) corresponds to the point \((0,-\beta)\in\partial K_{n,\lambda}\). By the upper certificate, every point of the latitude \(w=1/n\) on the normalized sphere also maps to \(\partial K_{n,\lambda}\). Choose \(n\) directions \(\omega_1,\ldots,\omega_n\) forming the vertices of a regular \((n-1)\)-simplex on \(S^{n-2}\). Then the \(n+1\) normalized contact vectors
\[
 u_0=-e_n,\qquad u_i=\left(\sqrt{1-n^{-2}}\,\omega_i,n^{-1}\right),\quad1\le i\le n,
\]
form a regular \(n\)-simplex: \(\sum_{i=0}^n u_i=0\) and \(\sum_{i=0}^n u_iu_i^\mathsf T=(n+1)I_n/n\). The positive contact weights \(n/(n+1)\) therefore satisfy both John moment identities \(\sum_i [n/(n+1)]u_i=0\) and \(\sum_i [n/(n+1)]u_iu_i^\mathsf T=I_n\). The sufficient part of John's contact characterization implies that the normalized unit ball is the unique maximum-volume inscribed ellipsoid. Undoing the affine change yields precisely \(E_{n,\lambda}\).

**4. Exact volume and singular dimension transition.** The splitting into two half ellipsoids gives \(\operatorname{vol}_n K_{n,\lambda}=\kappa_n\), whereas \(\operatorname{vol}_n E_{n,\lambda}=\kappa_n a^{n-1}b\). If \(\lambda=0\), the parameter equations reduce to \(a^2=n/(n+1)\) and \(b=2\sqrt n/(n+1)\), giving the stated exact endpoint ratio. For fixed \(\lambda>0\) let \(r=\beta/\alpha>0\), and \(B=b/\alpha\). The formulas become
\[
 B=\tfrac12\left(r+\frac{\sqrt{(n-1)^2r^2+4n}}{n+1}\right),\qquad
 a^2=\frac{n}{n+1}(1-r^2)+rB.
\]
Expansion at fixed \(r>0\) gives \(B=r+(1-r^2)/(r(n+1))+O_r(n^{-2})\), whence \(b\to\beta\) and \(a^2=1+O_r(n^{-2})\). Consequently \(a^{n-1}\to1\) and \(\eta_n(\lambda)\to\beta=2\lambda\). The endpoint \(\lambda=1/2\) is exactly the unit ball and is immediate.

Finally set \(\lambda=t/\sqrt n\) with fixed \(t\ge0\), and \(s=\sqrt{t^2+4}\). Expanding the explicit radical directly yields
\[
 \sqrt n\,b\longrightarrow t+s,\qquad
 n(1-a^2)\longrightarrow\frac{(s-t)^2}{4}.
\]
Thus \(a^{n-1}=(a^2)^{(n-1)/2}\to\exp[-(s-t)^2/8]\). Multiplication proves the boxed crossover formula, including \(t=0\).

## Verification

Run `python3 verify_john.py` using only the Python standard library. The checker evaluates the quadratic parameter identity, exact contact geometry, simplex moment conditions, axial inclusion envelopes at dense deterministic sample points, and independently compares high-dimensional evaluations with the displayed crossover function. Successful finite checks support, but do not replace, the algebraic certificates and John's theorem above. The provided script passes 14,526 high-precision diagnostic checks.

## Relationship to prior work

Kipp and Sagmeister introduce \(\lambda\)-Steiner symmetrization and prove qualitative random-iteration convergence/divergence results [1]. Their work uses John normalization in the rigidity argument but does not give a maximum-volume ellipsoid or normalized-volume profile for the image of a ball under one step. The contact criterion itself is classical, with a self-contained treatment in Ball [2]. The classical half-ellipsoid case corresponds to the single endpoint \(\lambda=0\); it does not supply the interpolation formula or the \(n^{-1/2}\)-scale crossover. Güler and Gürtuna [4] explicitly determine John ellipsoids of slabs (intersections of one ellipsoid with two parallel halfspaces); those bodies obey a single quadratic constraint and planar cuts, unlike the present two-branch quadratic boundary. Their statement does not imply the joined-half-ellipsoid formula. Related exact ellipsoids of unrelated polytopes and cones likewise have different constraints.

## Limitations

The classification applies to one generalized Steiner step starting from a Euclidean ball, not arbitrary initial convex bodies or repeated random iterations. The parameter is restricted to the standard range \(0\le\lambda\le1/2\), and dimension limits are pointwise in fixed \(\lambda>0\) or fixed crossover parameter \(t\). This is a self-review mathematical proof/check and has not received independent validation. The possibility of an equivalent older formula under different terminology remains a historical-priority risk.

## References

[1] C. Kipp and Á. Sagmeister, *Random convergence of generalized Steiner processes*, arXiv:2610.05113v1, first publicly submitted 2026-10-04. https://arxiv.org/html/2610.05113v1

[2] K. Ball, *Ellipsoids of maximal volume in convex bodies*, arXiv:math/9201217v1, 1990 preprint; *Geometriae Dedicata* 41 (1992), 241–250. https://arxiv.org/html/math/9201217v1

[3] F. John, *Extremum problems with inequalities as subsidiary conditions*, in *Studies and Essays Presented to R. Courant* (1948), 187–204. Standard contact characterization; historical source not independently reread for this result.

[4] O. Güler and F. Gürtuna, *Symmetry of convex sets and its applications to the extremal ellipsoids of convex bodies*, Optimization Methods and Software 27 (2012), DOI: 10.1080/10556788.2011.626037. Sections 4 and 6 treat the slab geometry. https://doi.org/10.1080/10556788.2011.626037
