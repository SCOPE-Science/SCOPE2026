# First spherical-cap overlap law for type-\(D\) root-polytope widths

## Finding
For every integer \(n\ge3\), consider the type-\(D_n\) root polytope
\[
K_n=\operatorname{conv}\{\pm e_i\pm e_j:1\le i<j\le n\}\subset\mathbb R^n.
\]
Let \(U\) be uniform on the unit sphere \(S^{n-1}\) and let \(W_n=h_{K_n}(U)+h_{K_n}(-U)\) be its directional width. For \(w\in[\sqrt6,2\sqrt2]\), its entire upper-tail law is
\[
\Pr(W_n>w)=n(n-1)I_{1-w^2/8}\!\left(\frac{n-1}{2},\frac12\right),
\tag{1}
\]
where \(I_x(a,b)\) is the regularized incomplete beta function. The threshold \(\sqrt6\) is sharp: for \(w<\sqrt6\) sufficiently close to it, the right-hand side of (1) strictly overcounts the actual upper-tail probability. More precisely, as \(w\uparrow\sqrt6\) from below,
\[
\boxed{\Pr(W_n\le w)=1-n(n-1)I_{1-w^2/8}\!\left(\frac{n-1}{2},\frac12\right)
+C_n(\sqrt6-w)^{n/2}+o((\sqrt6-w)^{n/2})},
\tag{2}
\]
with the explicit positive coefficient
\[
C_n=\frac{4\sqrt3(n-1)(n-2)}{\pi}\left(\frac23\right)^{n/4}.
\tag{3}
\]
Thus the first failure of the disjoint spherical-cap approximation has a dimension-dependent onset exponent \(n/2\), with its exact multiplicity and leading constant.

For \(n=3\), \(K_3\) is a regular cuboctahedron, scaled to have vertices \((\pm1,\pm1,0)\) and permutations. In this dimension the *entire* distribution is elementary, with two additional interior regimes. Put \(t=w/2\), \(d=\arctan\sqrt2\), and for \(1\le t\le\sqrt{3/2}\) define
\[
\alpha(t)=\arccos\!\left(\frac{t}{\sqrt{3(2-t^2)}}\right),\quad
a(t)=d-\alpha(t),\quad b(t)=d+\alpha(t),\quad
Q(\phi)=\arcsin\!\left(\frac{\sqrt3}{2}\sin(\phi-d)\right).
\]
Then the cumulative distribution \(F_3(w)=\Pr(W_3\le w)\) is
\[
F_3(2t)=
\begin{cases}
0,&t\le1,\\
\frac{12}{\pi}\left[\frac{t}{\sqrt2}a(t)-Q(a(t))-\frac\pi4\right],&1<t\le\frac2{\sqrt3},\\
\frac{12}{\pi}\left[\frac{t}{\sqrt2}\big(\frac\pi2-2\alpha(t)\big)-Q(a(t))+Q(b(t))-\frac{5\pi}{12}\right],&\frac2{\sqrt3}<t\le\sqrt{\frac32},\\
3\sqrt2t-5,&\sqrt{\frac32}<t<\sqrt2,\\
1,&t\ge\sqrt2.
\end{cases}
\tag{4}
\]
In particular, the cuboctahedral width density is exactly constant, \(3/\sqrt2\), throughout its upper interval \(\sqrt6<w<2\sqrt2\), while its lower portion has distinct analytic branches meeting at \(4/\sqrt3\) and \(\sqrt6\). Equations (1)--(4) constitute one dimensional-family law with the cuboctahedron as its complete low-dimensional instance.

## Assumptions and scope
The polytope is the stated full-dimensional, centrally symmetric convex hull; all \(4\binom n2=2n(n-1)\) signed two-coordinate vectors occur. Width uses unit Euclidean normals, with the *unoriented* normal distributed by Haar surface measure (equivalently choose \(U\) uniformly on \(S^{n-1}\)). The strict \(>\) convention in (1) is immaterial because the width distribution has no atoms. Formula (2) holds for each fixed integer \(n\ge3\) as \(w\uparrow\sqrt6\), not uniformly in growing \(n\). The function \(I_x(a,b)=B_x(a,b)/B(a,b)\) uses standard beta normalization. The arctrigonometric branches in (4) are principal real branches. Formula (4) gives all thresholds exactly, including endpoints by continuity.

## Proof
**1. Support and cap threshold.** For each unit normal \(u\), writing the ordered absolute coordinates as \(u_{(1)}\ge u_{(2)}\ge\cdots\ge0\), the support function is \(h_{K_n}(u)=u_{(1)}+u_{(2)}\). Central symmetry gives \(W_n=2(u_{(1)}+u_{(2)})=2\max_{v\in V_n}\langle u,v\rangle\), where \(V_n\) is the vertex/root set above. Normalizing \(q=v/\sqrt2\), the event \(W_n>w\) is the union of \(N=2n(n-1)\) spherical caps \(\{\langle U,q\rangle>w/(2\sqrt2)\}\). Two distinct centers have largest possible inner product \(1/2\), achieved exactly when the corresponding signed roots share one coordinate with the same sign. Their least angular separation is therefore \(\pi/3\). Caps with angular radius at most \(\pi/6\), equivalently \(w\ge\sqrt6\), have pairwise disjoint interiors. One cap occupies the fraction \(\frac12I_{1-w^2/8}((n-1)/2,1/2)\). Multiplying by \(N\) proves (1).

**2. Pair count and no competing simultaneous intersections.** Every root has precisely \(4(n-2)\) other roots at the minimal angular separation, giving \(E=N\,4(n-2)/2=4n(n-1)(n-2)\) unordered nearest-center pairs. After permuting coordinates and signs, any such pair has roots \(e_1+e_2,e_1+e_3\), with midpoint direction \(m=(2e_1+e_2+e_3)/\sqrt6\). Its scalar product with these two normalized roots is \(\sqrt3/2\); with every other normalized root it is at most \(1/\sqrt3\). Thus no third cap meets their single tangency point at angular radius \(\pi/6\). By finiteness and compactness, for all sufficiently small increments of the angular radius above \(\pi/6\), no non-neighboring pair overlaps and no triple intersection occurs. Inclusion-exclusion is then exact with only the \(E\) pair lenses.

**3. Local pair-lens coefficient.** Set \(w=\sqrt6-\Delta\), \(\varepsilon=\Delta/(2\sqrt2)\), \(c=\sqrt3/2\) and \(s=1/2\). Near the contact direction \(m\), take tangent coordinates \((x,y)\in\mathbb R\times\mathbb R^{n-2}\) with the two cap centers equal to \(cm\pm se_1\). The two cap inequalities become
\[
c\sqrt{1-x^2-|y|^2}-s|x|\ge c-\varepsilon.
\]
Uniformly on the shrinking lens, \(x=O(\varepsilon)\) and \(|y|=O(\sqrt\varepsilon)\); hence the leading domain is \(s|x|+(c/2)|y|^2\le\varepsilon\). The spherical-area Jacobian in these coordinates is \((1-x^2-|y|^2)^{-1/2}=1+o(1)\). For \(v_k=\pi^{k/2}/\Gamma(k/2+1)\) denoting unit \(k\)-ball volume, direct integration shows that the *unnormalized* lens area is
\[
\frac{8}{n}v_{n-2}\left(\frac4{\sqrt3}\right)^{(n-2)/2}\varepsilon^{n/2}+o(\varepsilon^{n/2}).
\]
The unit-sphere area is \(S_{n-1}=2\pi^{n/2}/\Gamma(n/2)\), so \(v_{n-2}/S_{n-1}=1/(2\pi)\). Multiplying by the exact pair count \(E\), replacing \(\varepsilon=\Delta/(2\sqrt2)\), and simplifying yields (3). The event \(W_n\le w\) is the complement of the cap union, so the pair-overlap amount contributes with a **positive** sign as in (2). Because the coefficient is positive, the threshold is sharp.

**4. Complete three-dimensional law.** In dimension three, consider the Voronoi cell of the root \((1,1,0)/\sqrt2\) on \(S^2\). In spherical polar coordinates about this root, choose tangent axes \((1,-1,0)/\sqrt2\) and \((0,0,1)\). Writing \(\phi\) for the azimuthal variable, its cell has radial ceiling
\[
\rho(\phi)=\arctan\!\left(\frac{1}{|\cos\phi|+\sqrt2|\sin\phi|}\right).
\]
This follows directly by requiring the first two positive coordinates of \(u\) to be at least the absolute third coordinate. There are twelve congruent cells of spherical area \(\pi/3\). With \(\theta=\arccos(t/\sqrt2)\), the event \(W_3\le2t\) within the chosen cell has area \(\int_0^{2\pi}\int_{\theta}^{\rho(\phi)}\sin r\,dr\,d\phi\), with negative intervals interpreted as empty. Fourfold azimuthal symmetry gives
\[
F_3(2t)=\frac{12}{\pi}\int_0^{\pi/2}\bigl[\cos\min\{\theta,\rho(\phi)\}-\cos\rho(\phi)\bigr]d\phi.
\tag{5}
\]
On \([0,\pi/2]\), write \(D(\phi)=\cos\phi+\sqrt2\sin\phi=\sqrt3\cos(\phi-d)\). Then \(\cos\rho=D/\sqrt{1+D^2}=Q'(\phi)\), and the threshold \(\rho(\phi)=\theta\) has roots \(a(t),b(t)\) whenever they are in the quadrant. At \(t=2/\sqrt3\) the second root enters at \(\pi/2\); at \(t=\sqrt{3/2}\) the roots merge. Evaluating (5) over the corresponding intervals yields exactly (4), including the cap-disjoint upper branch. The first positive widths appear at \(w=2\), and the maximal width is \(2\sqrt2\).

## Verification
Run `python verify_width.py` (Python 3 with `numpy`, `scipy` and `mpmath`). The standalone script (i) compares (4) with independent direct spherical-cell quadrature at several points in each branch, (ii) checks positivity, monotonicity, endpoint and transition continuity, (iii) checks the exact disjoint-cap formula, (iv) numerically verifies the predicted \(3/2\)-power onset against the **full** three-dimensional law, and (v) computes the four-dimensional lens area independently from the exact uniform-disk marginal, checking its \(\Delta^2\) constant against (3). Simulation is deliberately not substituted for the all-dimensional proof. The proof of the gap before triple intersections is analytic, based on a strict dot-product margin and finiteness.

## Relationship to prior work
Finch's 2011 width-distribution study works out mean and second-moment calculations for the tetrahedron and cube, not the type-\(D\) family. The 2009 root-polytope work of Mészáros concerns triangulations and algebraic structure, not random directional widths. Abas's 2026 framework states a general coarea formula and explicit three-dimensional densities for selected polytopes including the truncated octahedron, not the present all-dimensional \(D_n\) first-overlap constant; however its complete manuscript could not be inspected. Related published research records treat cube width transitions, an octahedral width law, and simplex-centered spherical-cap overlaps. Their bodies, center systems, contact multiplicities, or dimensions differ, and none of their retrieved statements supplies (3) for \(D_n\) or the explicit three-branch cuboctahedral expression (4). The individual cap formula and local lens technique are classical ingredients; novelty is claimed for their sharp type-\(D_n\) synthesis, not for the general technique or earlier benchmark results.

## Limitations
The exact full CDF is given only in dimension three; in higher dimensions (1) is restricted to the sharp upper interval and (2) is a one-sided local law. The asymptotic is at **fixed dimension**; uniformity in \(n\to\infty\) is not claimed. The comparison with the full Abas 2026 manuscript and with older broad stereological tables remains incomplete; mathematical priority is provisional pending independent literature review. No independent scientific audit has been performed. The work makes no claim about every section, brightness distribution, or random projection area.

## References
- Karola Mészáros, *Root polytopes, triangulations, and the subdivision algebra, II*, arXiv:0904.3339, first public version 2009-04-21. Supports the earlier root-system framework.
- Steven R. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671, first public version 2011-10-04. The accessible full-text rendering was checked.
- Omri Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability*, arXiv:2609.26202, first public version 2026-08-10. Abstract checked; complete manuscript not retrieved.
- Published mathematical-record comparison: *Exact directional-width law of the cube and its first spherical-cap transition*, published-finding corpus record `2026/10/11/SCOPE-exact-directional-width-law-of-the-cube-and-its-first-spherical--c1e6aa54ecb2` (summary checked).
- Published mathematical-record comparison: *Exact width distribution of the unit-edge regular octahedron*, published-finding corpus record `2026/10/11/SCOPE-exact-width-distribution-of-the-unit-edge-regular-octahedron--953206d3d8c4` (summary checked).
- Published mathematical-record comparison: *Exact third-order union formula at the first multiple-overlap threshold for simplex-centred spherical caps*, published-finding corpus record `2026/10/4/SCOPE-exact-third-order-union-formula-at-the-first-multiple-overlap-th--e4ea7f0caeb7` (summary checked).
