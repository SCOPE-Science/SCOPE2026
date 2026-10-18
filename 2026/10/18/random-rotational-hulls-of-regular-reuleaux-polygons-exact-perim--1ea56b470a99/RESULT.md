# Random rotational hulls of regular Reuleaux polygons: exact perimeter and Gumbel covering

## Finding
Fix any odd integer \(n\ge3\), width \(w>0\), and integer \(m\ge1\). Let \(R_n(w)\) be the regular planar Reuleaux \(n\)-gon, centered at its dihedral center, and let \(U_1,\dots,U_m\) be independent uniform rotations about that center. Define the random convex body
\[
H_{n,m}=\operatorname{conv}\left(\bigcup_{j=1}^m U_jR_n(w)\right),\qquad
\alpha=\frac{\pi}{2n},\quad q=\frac{2\pi}{n}=4\alpha,\quad
R=\frac{w}{2\cos\alpha}.
\]
The exact expected perimeter for **every** admissible \(n,m,w\) is
\[
\boxed{\mathbb E\operatorname{Per}(H_{n,m})
=2\pi R\left\{1-\int_0^\alpha\!
\sin t\left[\left(\frac{t}{2\alpha}\right)^m+
\left(1-\frac{t}{2\alpha}\right)^m\right]dt\right\}.}
\tag{1}
\]
It is strictly increasing in \(m\), starts at \(\pi w\), and approaches \(2\pi R=\pi w\sec\alpha\). In particular,
\[
\mathbb E\operatorname{Per}(H_{n,2})=
\frac{\pi w}{2}+\frac{\pi w(1-\cos\alpha)}{\alpha^2\cos\alpha}.
\tag{2}
\]
The approach to the circumdisk has two sharply different geometric scales. For each fixed odd \(n\),
\[
\boxed{2\pi R-\mathbb E\operatorname{Per}(H_{n,m})
\sim \frac{8\pi R\alpha^2}{m^2}\quad (m\to\infty).}
\tag{3}
\]
For a fixed unit direction \(u\) and an independent unit exponential \(E\),
\[
m^2\bigl(R-h_{H_{n,m}}(u)\bigr)
\ \Longrightarrow\ 2R\alpha^2E^2.
\tag{4}
\]
By contrast, put \(\Delta_m=d_H(H_{n,m},RB_2)\), with \(B_2\) the Euclidean unit disk. Then
\[
\boxed{\frac{2m}{q}\arccos\left(1-\frac{\Delta_m}{R}\right)-\log m
\ \Longrightarrow\ \mathcal G,}
\tag{5}
\]
where \(\Pr(\mathcal G\le x)=\exp(-e^{-x})\) is the standard Gumbel distribution. Equivalently,
\[
\frac{8m^2\Delta_m}{Rq^2(\log m)^2}\ \longrightarrow\ 1
\quad\text{in probability}.\tag{6}
\]
For fixed \(m\), as odd \(n\to\infty\), the complementary exact curvature-scale expansion is
\[
\mathbb E\operatorname{Per}(H_{n,m})=
\pi w\left[1+\left(\frac12-\frac{4-2^{1-m}}{(m+1)(m+2)}\right)
\frac{\pi^2}{4n^2}+O_m(n^{-4})\right].\tag{7}
\]
Thus average perimeter error is of order \(m^{-2}\), but maximal directional support error is of order \(m^{-2}(\log m)^2\), with the full limiting extreme-value law in (5).

## Assumptions and scope
The Reuleaux polygon is the compact convex region bounded by the \(n\) radius-\(w\) arcs of the standard regular odd-sided construction. Its vertices are the vertices of the corresponding regular \(n\)-gon of circumradius \(R\), all rotations preserve their common center, and the rotations are independent with Haar-uniform angles on the full circle. The number of copies \(m\) is a positive integer and the number of arcs \(n\) is odd and at least three. No random translations are permitted. Perimeter is ordinary Euclidean boundary length. The Hausdorff metric is the Euclidean metric on compact planar sets. Statements (3)--(6) take \(n,w\) fixed as \(m\to\infty\); statement (7) takes \(m,w\) fixed while odd \(n\to\infty\). These limits are not asserted uniformly under simultaneous growth.

## Proof
**Step 1: complete angular support law.** Write the vertices as \(v_j=R(\cos(2\pi j/n),\sin(2\pi j/n))\). Each arc has radius \(w\) and is centered at the vertex opposite its pair of consecutive endpoints. For a chosen circle center, the two center-to-endpoint chords make angles \(\pi-\alpha\) and \(\pi+\alpha\) with its radial axis; this follows by taking the arguments of the chords of the regular underlying \(n\)-gon. The resulting arc-normal interval has length \(2\alpha=\pi/n\), centered opposite its circle center. Dually, the normals of the two arcs incident to a vertex bound an outward-normal cone of length \(2\alpha\), centered on that vertex's radial direction. The vertex and arc intervals alternate and together partition the full circle, except for their common boundary normals. On a vertex interval, at signed angle \(t\) from its center, the support is \(R\cos t\). On an arc interval, the supporting point is the arc-circle center plus \(w\) times the outward unit normal, and the support is \(w-R\cos t\). At either endpoint the two formulas agree at \(w/2=R\cos\alpha\).

Consequently the support \(X=h_{R_n(w)}(V)\) for a uniform random unit direction \(V\) has the law
\[
X\ \stackrel{\rm law}=\begin{cases}
R\cos T,&\text{probability }1/2,\\
w-R\cos T,&\text{probability }1/2,
\end{cases}
\qquad T\sim\operatorname{Uniform}[0,\alpha],
\tag{8}
\]
with mixture choice independent of \(T\). The full cumulative distribution is
\[
F(x)=\begin{cases}
0,&x<w-R,\\
\displaystyle\frac{\arccos((w-x)/R)}{2\alpha},&w-R\le x\le w/2,\\
\displaystyle 1-\frac{\arccos(x/R)}{2\alpha},&w/2\le x\le R,\\
1,&x>R.
\end{cases}\tag{9}
\]
In particular \(F\) is continuous and nondegenerate, and \(R\) is its exact upper endpoint.

**Step 2: exact mean perimeter.** For every unit \(u\), support functions turn convex hulls into pointwise maxima:
\[
h_{H_{n,m}}(u)=\max_{1\le j\le m}h_{R_n(w)}(U_j^{-1}u).
\]
The terms are independent with distribution \(F\), so their maximum \(M_m\) satisfies \(\Pr(M_m\le x)=F(x)^m\). The support-function form of Cauchy's perimeter formula, \(\operatorname{Per}(K)=\int_0^{2\pi}h_K(u_\theta)\,d\theta\), implies rotationally
\(\mathbb E\operatorname{Per}(H_{n,m})=2\pi\mathbb EM_m\). Because \(M_m\in[w-R,R]\), the survival integral gives \(\mathbb EM_m=R-\int_{w-R}^{R}F(x)^m dx\). Substitute \(x=w-R\cos t\) on the lower branch of (9), and \(x=R\cos t\) in reverse orientation on the upper branch. This proves (1) without approximations. For \(m=1\), the bracketed powers sum to one and the result is \(2\pi R\cos\alpha=\pi w\), agreeing with Barbier's perimeter theorem. For \(m=2\), direct integration of the quadratic bracket gives (2). Since \(F\) lies strictly between zero and one on an interval, \(F^{m+1}<F^m\) there; thus the expectation increases strictly with \(m\). Dominated convergence gives the limit \(2\pi R\).

**Step 3: perimeter and fixed-direction scales.** For fixed \(\alpha>0\), the first integral term \(\int_0^\alpha\sin t(t/(2\alpha))^m dt\) is exponentially small in \(m\). In the second integral let \(t=2\alpha s/m\). The inequalities \(\sin t\le t\) and \((1-s/m)^m\le e^{-s}\), together with dominated convergence, give
\[
\lim_{m\to\infty}m^2\int_0^\alpha
\sin t\left(1-\frac{t}{2\alpha}\right)^m dt
=4\alpha^2\int_0^\infty se^{-s}ds=4\alpha^2.
\]
Multiplication by \(2\pi R\) proves (3). Furthermore, from the upper branch in (9), for each fixed \(y\ge0\),
\[
\Pr\{m^2(R-M_m)>y\}
=\left[1-\frac{\arccos(1-y/(Rm^2))}{2\alpha}\right]^m
\longrightarrow\exp\left(-\sqrt{\frac{y}{2R\alpha^2}}\right).
\]
The right side is the survival function of \(2R\alpha^2E^2\), proving (4); at \(y=0\) continuity gives the same conclusion.

**Step 4: exact Hausdorff reduction on a high-probability event.** Every circular arc point has the form \(v_j+w u\), where the normal \(u\) makes signed angle at most \(\alpha\) from \(-v_j/R\). Its squared distance to the center is \(R^2+w^2-2Rw\cos t\le R^2\), because \(2R\cos\alpha=w\). Thus \(R_n(w)\subset RB_2\), and hence \(H_{n,m}\subset RB_2\).

Reduce the \(m\) independent rotation angles modulo the fundamental period \(q=2\pi/n\). Their phases are independent uniform points on a circle of circumference \(q\). Let \(G_m\) denote their greatest cyclic gap. On the event \(G_m<q/2=2\alpha\), every normal direction lies within angular distance \(d(\theta)\le G_m/2<\alpha\) of a vertex of one of the rotated Reuleaux polygons. That vertex contributes support \(R\cos d(\theta)>R\cos\alpha=w/2\), whereas every circular-arc support contributes at most \(w/2\). Therefore the exact hull support is \(R\cos d(\theta)\). Its minimum occurs midway across a largest phase gap, so the support characterization of Hausdorff distance gives the **finite-configuration identity**
\[
\Delta_m=R\left(1-\cos\frac{G_m}{2}\right)
\quad\text{on }\{G_m<q/2\}.\tag{10}
\]
A gap at least \(q/2\) requires a sample phase with no other phase in its next half-circle. A union bound gives \(\Pr(G_m\ge q/2)\le m2^{-(m-1)}\to0\). Thus (10) holds with probability tending to one.

**Step 5: Gumbel extreme and scale separation.** Anchor the circular phase sample at any one of its sampled points. The \(m\) successive normalized gaps have Dirichlet\((1,\ldots,1)\) law, equivalently
\[
G_m\ \stackrel{\rm law}=\ q\frac{\max(E_1,\ldots,E_m)}{E_1+\cdots+E_m},
\tag{11}
\]
where the \(E_j\) are independent unit exponentials. The independent exponential maximum satisfies
\[
\Pr\left(\max_jE_j-\log m\le x\right)
=\left(1-\frac{e^{-x}}m\right)^m\longrightarrow e^{-e^{-x}},
\]
and the law of large numbers gives \((E_1+\cdots+E_m)/m\to1\). The ratio correction to the centered maximum is \(o_{\Pr}(1)\), since \(\max E_j=O_{\Pr}(\log m)\) and the relative sum fluctuation is \(O_{\Pr}(m^{-1/2})\). Hence \(mG_m/q-\log m\Rightarrow\mathcal G\). On the event in (10), \(2\arccos(1-\Delta_m/R)=G_m\), proving (5) by the vanishing exceptional probability. Since \(G_m\sim q\log m/m\) in probability and \(1-\cos z\sim z^2/2\), (6) follows. No assertion about independent Gumbel and pointwise Weibull limits is required or made.

**Step 6: large odd order at fixed copy count.** Set \(t=\alpha u\) in (1). Taylor expansion yields
\[
\int_0^\alpha\sin t\left[\left(\frac{t}{2\alpha}\right)^m+
\left(1-\frac{t}{2\alpha}\right)^m\right]dt
=\alpha^2 A_m+O_m(\alpha^4),
\]
with the exact beta integral
\[
A_m=\int_0^1u\left[(u/2)^m+(1-u/2)^m\right]du
=\frac{4-2^{1-m}}{(m+1)(m+2)}.
\]
Finally \(2\pi R=\pi w\sec\alpha\), \(\sec\alpha=1+\alpha^2/2+O(\alpha^4)\), and \(\alpha^2=\pi^2/(4n^2)\). This proves (7).

## Verification
Run the bundled standalone standard-library script `verify.py` with Python 3.9 or later. It independently maximizes the dot product over all original vertices and all actual boundary-circle arcs and matches the proposed piecewise support at 9,000 orientation/scale inputs; tests exact first- and second-copy perimeter formulas and finite expectations; compares a 130,000-sample rotational Monte Carlo estimate with the derived four-copy perimeter; checks large-copy and large-order coefficients; verifies 45 independent largest-gap midpoint support identities; and tests 2,200 normalized-exponential maxima against the predicted Gumbel distribution. The recorded successful output is `VERIFY_OK 9060`, `HAUSDORFF_OK 45`, and `GUMBEL_OK 2200`. Finite regressions diagnose geometry, constants, and implementations; the quantified theorem and weak limits follow from the analytical proof, not numerical sampling.

## Relationship to prior work
Falcó and Myroshnychenko identify the centered regular Reuleaux odd polygons as the area minimizers among planar constant-width bodies with prescribed odd cyclic symmetry. Their construction supplies the natural source of the family and the circumradius identity; their article studies area minimization, not random rotated convex hulls, perimeter order statistics, or maximal angular-gap laws.

A separately published study of the Reuleaux triangle's rotated Minkowski **arithmetic mean** computes an area profile depending on the relative angle of two copies; averaging sets by Minkowski addition is not taking their convex hull, and the deterministic area identity does not imply (1) or (5). A published random-rotation theorem for **intersections** of polygons circumscribed about a disk computes expected intersection areas; intersections with a common incircle, unlike our outer hulls, use nearest facet normals and a different integral. An outer-symmetry computation for regular Reuleaux polygons concerns the smallest centrally symmetric container and includes a specific deterministic opposite copy; it has no independent-rotation average.

The geometric theory of independent uniform circular spacings and the Gumbel law for exponential maxima is classical, as is the Cauchy support-perimeter identity. A separate polygonal random-inscription theorem derives a Gumbel limit for errors caused by independent arclength points on straight edges, with a different geometry and normalization. The present shape-specific result combines the exact Reuleaux support law (9), the full mean-perimeter profile (1), and an exact high-probability conversion from rotational gaps to Hausdorff error (10); none of these asserted combinations follows as a special case of the materially inspected prior theorems without a new object-specific geometric argument. The novelty claim concerns this combined family-level classification, not the classical underlying probability tools.

## Limitations
All results are planar and use regular odd-order Reuleaux polygons and common-center independent uniform rotations; no conclusions are claimed for arbitrary constant-width bodies or random translations. Equations (3)--(6) are fixed-order asymptotics; (7) is the distinct fixed-copy asymptotic. The exact finite-configuration Hausdorff reduction (10) requires its stated angular-gap event; no universal finite-copy formula outside that event is claimed. Random perimeter fluctuations, mean Hausdorff error constants, and joint limit independence are not determined. Older unindexed stochastic-geometry references might already imply the same classification; novelty is based on searched and materially inspected literature, not exhaustive historical certification. Verification is analytical plus reproducible same-study diagnostics, not independent audit.

## References
1. J. Falcó and S. Myroshnychenko, *Area Minimization Among Group-Invariant Planar Convex Bodies of Constant Width*, arXiv:2608.05125v1, first public 2026-08-05. https://arxiv.org/abs/2608.05125.
2. *Exact rotational Minkowski-average area profile of the Reuleaux triangle*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-rotational-minkowski-average-area-profile-of-the-reuleaux--53c190e0340e.
3. *Sharp random-rotation area order and exponential shape memory for tangential polygons*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-random-rotation-area-order-and-exponential-shape-memory-fo--9cc93a56f053.
4. *Exact Estermann measure of regular Reuleaux polygons*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-estermann-measure-of-regular-reuleaux-polygons--6e48f964d474.
5. *Gumbel transition and second-order Hausdorff error for randomly inscribed regular polygons*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-gumbel-transition-and-second-order-hausdorff-error-for-randomly--3fe000dbc9a1.
6. *Universal radial coverage by concentric regular-polygon unions*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-universal-radial-coverage-by-concentric-regular-polygon-unions--4705952c9b28.
7. E. Barbier, *Note sur le problème de l’aiguille et le jeu du joint couvert*, J. Math. Pures Appl. 5 (1860), 273--286 (classical constant-width perimeter identity).
