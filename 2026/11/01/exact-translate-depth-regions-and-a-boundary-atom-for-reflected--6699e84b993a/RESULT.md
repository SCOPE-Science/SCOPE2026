# Exact translate-depth regions and a boundary atom for reflected triangular tests

## Finding
Let \(S\) be any nondegenerate triangle in the Euclidean plane, let \(g\) be its centroid, and let \(\mu\) be normalized area measure on \(S\). Use the test body \(K=-S\), which has the opposite orientation from \(S\). Define the *translate depth* of any \(y\in\mathbb R^2\) by
\[
 d_K(y;\mu)=1-\sup_{z\in\mathbb R^2:\ y\notin z+K}\mu(z+K).
\]
Denote the three affine barycentric-coordinate functions by \(\lambda_i\), so that \(\sum_{i=0}^2\lambda_i(y)=1\), and write
\[
 L(y)=\max_{0\le i\le2}\lambda_i(y),\qquad t(y)=\min\{L(y),\tfrac23\}.
\]
For **every** \(y\in\mathbb R^2\), including exterior points, the depth is exactly
\[
 \boxed{d_K(y;\mu)=1-2t(y)+\tfrac32 t(y)^2.}
\]
It has global minimum \(1/3\) and unique maximum \(1/2\), attained at the centroid \(g\).

For every level \(1/3<\alpha\le1/2\), set
\[
 u_\alpha=\frac{2-\sqrt{6\alpha-2}}3,\qquad r_\alpha=3u_\alpha-1.
\]
The exact depth region is a **reversed homothetic triangle**:
\[
 \boxed{D_\alpha:=\{y:d_K(y;\mu)\ge\alpha\}
 =\{y:\lambda_i(y)\le u_\alpha\ (i=0,1,2)\}=g-r_\alpha(S-g).}
\]
For \(0<\alpha\le1/3\), one has \(D_\alpha=\mathbb R^2\); for \(\alpha>1/2\), it is empty. The compact nonbaseline region lies inside the original triangle exactly when \(\alpha\ge3/8\). Hence the support-contact threshold is sharp at \(3/8\).

If \(X\sim\mu\) and \(Q(\alpha)=\Pr\{d_K(X;\mu)\ge\alpha\}\), then
\[
 \boxed{Q(\alpha)=
 \begin{cases}
 1-3(1-u_\alpha)^2,&1/3<\alpha\le3/8,\\
 (3u_\alpha-1)^2,&3/8\le\alpha\le1/2.
 \end{cases}}
\]
Also \(Q(\alpha)=1\) for \(\alpha\le1/3\), \(Q(\alpha)=0\) for \(\alpha>1/2\), and
\[
 \boxed{\Pr\{d_K(X;\mu)=1/3\}=\tfrac13.}
\]
In particular, \(Q(1/3+)=2/3\) despite \(Q(1/3)=1\). The conclusions hold without assuming that \(S\) is equilateral.

## Assumptions and scope
The triangle has positive area; there are no regularity, symmetry, or aspect-ratio restrictions. \(\mu\) is normalized **two-dimensional** Lebesgue measure on \(S\), not boundary-arc-length measure. The testing family comprises precisely all translates of \(-S\), with no rotations or independent dilations. The query point ranges over the full plane, including points outside \(S\). The supremum uses translates **excluding** the query point, rather than those that merely omit its interior; continuity of the overlap mass makes their suprema equal.

## Proof
**1. Parametrizing every reversed translate.** In the barycentric plane, a translate \(T=z-S\) is precisely
\[
 T_b=\{x:\lambda_i(x)\le b_i\ (i=0,1,2)\},\qquad b_0+b_1+b_2=2.
\]
Indeed, for \(x=z-w\), \(w\in S\), affineness gives \(\lambda_i(x)=\lambda_i(z)+\lambda_i(0)-\lambda_i(w)\); thus \(b_i=\lambda_i(z)+\lambda_i(0)\). Conversely, every triple summing to two arises from a unique translation since \(b_i-\lambda_i(0)\) sum to one. Therefore the overlap function is \(f(b)=\mu(S\cap T_b)\) on this affine parameter plane.

**2. Optimizing with one prescribed barycentric cap.** For any \(b,c\), convexity implies
\[
 (1-\theta)(S\cap T_b)+\theta(S\cap T_c)
 \subseteq S\cap T_{(1-\theta)b+\theta c},\qquad0\le\theta\le1.
\]
The planar Brunn–Minkowski inequality therefore makes \(f(b)^{1/2}\) concave (also at zero-volume limits). Fixing \(b_i=s\), permuting the other two barycentric coordinates preserves \(\mu\) and the class \(T_b\). Averaging a parameter triple with its transposition gives
\[
 \sup_{b_i=s,\ \sum b_j=2}f(b)
 =f\left(s,\frac{2-s}{2},\frac{2-s}{2}\right),
\]
where the coordinates on the right are ordered with the prescribed index first. This equality proves a *global* optimizing property, not merely stationarity.

For \(b_i\ge0\), the normalized overlap equals the elementary inclusion–exclusion expression
\[
 f(b)=\sum_{J\subseteq\{0,1,2\}}(-1)^{|J|}
 \left(1-\sum_{j\in J}b_j\right)_+^2,
\]
with \(x_+=\max\{x,0\}\); if any \(b_i<0\), the overlap is zero. The identity follows by identifying the set where \(\lambda_j>b_j\) for all indices in \(J\) with a shrunken barycentric simplex of linear scale \((1-\sum_{j\in J}b_j)_+\). Substitution of the optimal symmetric caps yields the exact one-variable bound
\[
 F(s)=\sup_{b_i=s}f(b)=
 \begin{cases}
 0,&s\le0,\\
 2s-\tfrac32s^2,&0\le s\le1,\\
 \tfrac12(2-s)^2,&1\le s\le2,\\
 0,&s\ge2.
 \end{cases}
\]
It is strictly increasing on \([0,2/3]\), attains its unique global maximum \(F(2/3)=2/3\), and decreases for \(2/3<s\le2\). In particular, the maximum mass of an oppositely oriented translated triangle is \(2/3\); this overlap value itself is an elementary known geometric benchmark, not the asserted novel contribution.

**3. Exact exclusion optimization and depth.** A translate \(T_b\) fails to contain \(y\) exactly when \(b_i<\lambda_i(y)\) for at least one index. Hence, writing \(M(y)\) for its largest allowable overlap,
\[
 M(y)=\max_i\sup_{s<\lambda_i(y)} F(s)
 =F\bigl(\min\{L(y),2/3\}\bigr).
\]
For the last equality, note \(L(y)\ge1/3\) because \(\sum\lambda_i(y)=1\), and use the strict increase of \(F\) up to \(2/3\). If the optimal cap touches \(y\), approach its value from below; continuity of \(f\) ensures the same supremum for the strict-exclusion rule. Evaluating the quadratic branch of \(F\) gives the claimed formula \(d_K=1-M\) throughout \(\mathbb R^2\). Equality \(d_K=1/2\) is equivalent to \(L=1/3\), which forces every \(\lambda_i=1/3\), i.e. \(y=g\).

**4. Depth regions and their support transition.** Since \(d_K\) decreases strictly with \(L\) on \([1/3,2/3]\), solving \(1-2u+3u^2/2=\alpha\) for its smaller root gives \(u=u_\alpha\). Therefore \(d_K(y)\ge\alpha\) is equivalent to the three conditions \(\lambda_i(y)\le u_\alpha\). Put \(r=3u_\alpha-1\). If \(r>0\), \(y=g-r(x-g)\) with \(x\in S\) is equivalent to \(\lambda_i(x)=(u_\alpha-\lambda_i(y))/r\ge0\) for each \(i\); at \(r=0\) both regions reduce to \(\{g\}\). This proves the reflected homothety. Since the other two barycentric coordinates never exceed \(u\), their sum implies \(\lambda_i\ge1-2u\) for all points of the level region. Hence it is contained in \(S\) exactly when \(u\le1/2\), equivalently \(\alpha\ge3/8\). Levels at or below the baseline are all of \(\mathbb R^2\) by the exact depth formula.

**5. Distribution under uniform sampling.** For \(X\sim\mu\), the vector \((\lambda_0(X),\lambda_1(X),\lambda_2(X))\) has the uniform Dirichlet law on the two-dimensional probability simplex. For \(1/3\le u\le2/3\), inclusion–exclusion for the three caps \(\lambda_i>u\) gives
\[
 \Pr\{L(X)\le u\}=1-3(1-u)^2+3(1-2u)_+^2.
\]
For \(u\le1/2\), the same expression equals \((3u-1)^2\), and for \(u\ge1/2\) it equals \(1-3(1-u)^2\). Substituting \(u=u_\alpha\) gives the two survival branches. Finally \(d_K(X)=1/3\) exactly when \(L(X)\ge2/3\), an event of probability \(3(1-2/3)^2=1/3\). This also proves the jump at the baseline.

## Verification
The standalone program `verify.py` contains finite checks separate from the proof. Its recorded execution passed **13,352** exact-rational and numerical comparisons, including an independently coded convex-polygon clipping integral, the cap inclusion–exclusion identity, excluded-translate upper bounds, approximating optimizing translates, and the level-set/survival formulas. The checks are reproducible by `python3 verify.py` using only the Python standard library. They do not certify universal statements; those are established by the argument above.

## Relationship to prior work
Molchanov and Nagy, *Depth based on translates of a convex body: geometry, floating bodies, and empirical theory* (first public arXiv version 2026-10-19), introduce the translate-depth definition, erosion representation, nonzero baseline, and general convexity properties. Their inspected treatment does not provide the exact reversed-triangle pointwise formula, sharp support-contact threshold, or atomic survival law. The literature on aligned or positively homothetic simplex intersections includes Soltan's characterization, based on intersections of positively homothetic simplices; it does not imply the reversed-body calculation. General floating-body work and polygon cross-covariogram methods provide context but do not by themselves determine this entire depth profile. Lertpinyowong, Wattanawanichkul and Lengrugsa studied maximal triangle-overlap configurations under translation and rotation in 2015; their publicly accessible English abstract singles out the star-like regime as challenging and does not give the exclusion-conditioned depth law. The classical maximal overlap \(2/3\) of opposite triangles is only one ingredient; the contribution is the all-query optimization together with complete level and distribution descriptions. No claim of definitive historical priority is made.

## Limitations
Only two-dimensional nondegenerate triangles, normalized area measure, and translates of the exactly reflected same-size triangle are treated. No formula is asserted for independent test scaling, rotations, arbitrary convex sampling domains, or higher dimensions. The sharp bound and phase diagram are analytic, but comprehensive historical priority remains to be checked against older triangle-overlap and mathematical-statistics literature. No independent mathematical audit has been performed.

## References
1. I. Molchanov and S. Nagy, *Depth based on translates of a convex body: geometry, floating bodies, and empirical theory*, arXiv:2610.26108, first posted 2026-10-19. https://arxiv.org/abs/2610.26108
2. V. Soltan, *A Characterization of Homothetic Simplices*, Discrete & Computational Geometry 22 (1999), 193–200. https://doi.org/10.1007/PL00009454
3. C. Schütt, E. M. Werner and D. Yalikun, *Floating bodies for ball-convex bodies*, Journal of the London Mathematical Society 112 (2025), e70387. https://doi.org/10.1112/jlms.70387
4. P. Lertpinyowong, N. Wattanawanichkul and K. Lengrugsa, *Study of Overlapped Triangles with the Maximal Overlapped Area under Translation and Rotation*, 2015 research project; publicly accessible English abstract, https://ploynawapan.github.io/files/mwitsproject.pdf
