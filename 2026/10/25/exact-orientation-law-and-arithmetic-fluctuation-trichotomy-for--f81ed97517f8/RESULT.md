# Exact orientation law and arithmetic fluctuation trichotomy for bounding boxes of regular polygons

## Finding
For every integer \(n\ge3\) and circumradius \(R>0\), let \(P_n\) be a regular Euclidean \(n\)-gon and rotate it through a uniformly distributed angle \(\Phi\in[0,2\pi)\). Let \(B_n\) be the area of its smallest rectangle whose sides are parallel to two fixed perpendicular axes (equivalently, its axis-aligned bounding box after rotation). Put \(a=\pi/n\) and define \((C_n,D_n,b_n)\) by
\[
(C_n,D_n,b_n)=\begin{cases}
(2R^2,1,2a),&n\equiv0\pmod4,\\
(2R^2,\cos a,a),&n\equiv2\pmod4,\\
(2R^2\cos^2(a/2),\cos(a/2),a/2),&n\text{ odd}.
\end{cases}
\]
Then the **entire** orientation-induced area law is
\[
\boxed{B_n\ \stackrel{\mathrm d}=\ C_n\bigl(D_n+\cos T_n\bigr),\qquad
T_n\sim\operatorname{Unif}[-b_n,b_n].}
\tag{1}
\]
In particular, with \(L_n=C_n(D_n+\cos b_n)\) and \(U_n=C_n(D_n+1)\), the exact cumulative distribution function is
\[
\Pr(B_n\le z)=\begin{cases}
0,&z\le L_n,\\
1-b_n^{-1}\arccos(z/C_n-D_n),&L_n<z<U_n,\\
1,&z\ge U_n.
\end{cases}
\tag{2}
\]
The endpoints carry zero probability. The first two moments are exactly
\[
\boxed{\mathbb E B_n=C_n\left(D_n+\frac{\sin b_n}{b_n}\right),\qquad
\operatorname{Var}(B_n)=C_n^2\left(\frac12+\frac{\sin(2b_n)}{4b_n}-\left(\frac{\sin b_n}{b_n}\right)^2\right).}
\tag{3}
\]
There is a striking three-class high-order fluctuation law for fixed \(R\):
\[
\boxed{\lim_{\substack{n\to\infty\\ n\equiv r\ (\mathrm{mod}\,4)}}\frac{n^4}{R^4}\operatorname{Var}(B_n)=
\begin{cases}
64\pi^4/45,&r=0,\\4\pi^4/45,&r=2,\\\pi^4/180,&r=1,3.
\end{cases}}
\tag{4}
\]
Thus the leading fluctuation variances for the three types have ratios **\(256:16:1\)** even though their means all satisfy
\[
\mathbb E B_n=4R^2-\frac{4\pi^2R^2}{3n^2}+O(R^2n^{-4}).
\tag{5}
\]
Finally, the normalized *orientation loss* \(X_n=(U_n-B_n)/(U_n-L_n)\in[0,1]\) has the universal exact CDF
\[
\boxed{\Pr(X_n\le x)=\frac{2}{b_n}\arcsin\!\left(\sin(b_n/2)\sqrt{x}\right),\quad 0\le x\le1.}
\tag{6}
\]
Consequently \(X_n\Rightarrow\operatorname{Beta}(1/2,1)\) in every residue class, with the **sharp** Kolmogorov-distance correction
\[
\boxed{\sup_{0\le x\le1}\left|\Pr(X_n\le x)-\sqrt{x}\right|=\frac{b_n^2}{36\sqrt3}+O(b_n^4).}
\tag{7}
\]
The area law, the complete CDF, and the three-residue variance and sharp distributional-rate statements form one coherent result about sensitivity of bounding-box area to an unknown orientation.

## Assumptions and scope
The polygon is fixed and regular, \(n\ge3\), with genuine vertices and circumradius \(R>0\); only its rotation angle is random, with normalized Haar measure on the planar rotation circle. The bounding rectangle has sides parallel to the chosen fixed Cartesian axes; no optimization over orientations is performed **after** the random rotation. The quantity \(B_n\) is the product of the polygon's horizontal and vertical widths. This is a probability distribution on an explicit compact interval, not an assertion of independence of the two widths. \(n\to\infty\) in (4) is taken separately along the indicated congruence classes. All statements allow \(n=3\) and \(n=4\). Whenever a range endpoint is discussed, its exact value is included in (2), but it has no atom.

## Proof
Let \(h_n(\theta)=R\max_{0\le j<n}\cos(\theta-2\pi j/n)\) be the support function. If \(\delta(\theta)\) denotes the signed angular distance to the nearest vertex direction reduced to \([-a,a]\), then \(h_n(\theta)=R\cos\delta(\theta)\). The width in direction \(\theta\) is \(w_n(\theta)=h_n(\theta)+h_n(\theta+\pi)\), and the area of its Cartesian bounding box after angle \(\theta\) is exactly
\[
B_n(\theta)=w_n(\theta)w_n(\theta+\pi/2).
\tag{8}
\]
This identity can also be verified directly by taking maximum and minimum vertex-coordinate values.

If \(4\mid n\), the polygon is centrally symmetric and \(\pi/2\) is an integral multiple of the vertex-direction period \(2a\). Hence \(w_n(\theta)=w_n(\theta+\pi/2)=2R\cos\delta\) and
\[
B_n(\theta)=4R^2\cos^2\delta=2R^2(1+\cos(2\delta)).
\tag{9}
\]
For uniformly random \(\theta\), the reduced phase \(\delta\) is uniform on \([-a,a]\), so \(T_n=2\delta\) is uniform on \([-2a,2a]\).

If \(n\equiv2\pmod4\), the polygon is again centrally symmetric, but a quarter turn amounts to a half-period shift: the angular distance of the nearest polygon vertex to \(\theta+\pi/2\) is \(a-|\delta|\). Thus
\[
B_n(\theta)=4R^2\cos\delta\cos(a-|\delta|)
=2R^2\bigl(\cos a+\cos(2|\delta|-a)\bigr).
\tag{10}
\]
The variable \(|\delta|\) is uniform on \([0,a]\), hence \(T_n=2|\delta|-a\) is uniform on \([-a,a]\).

If \(n\) is odd, \(\pi\equiv a\pmod{2a}\) and the width function has the shorter period \(a\). Reducing \(\theta\) modulo \(a\) to \(s\in[0,a]\) gives
\[
w_n(s)=R\cos s+R\cos(a-s)=2R\cos(a/2)\cos(s-a/2).
\tag{11}
\]
Because \(\pi/2\equiv a/2\pmod a\), the perpendicular width is the same expression with a shift of \(a/2\) modulo \(a\). The product is invariant under \(s\mapsto a-s\). Therefore \(t=\min(s,a-s)\) is uniform on \([0,a/2]\), and the product-to-sum identity gives
\[
B_n=4R^2\cos^2(a/2)\cos(t-a/2)\cos t
=2R^2\cos^2(a/2)\bigl(\cos(a/2)+\cos(2t-a/2)\bigr).
\tag{12}
\]
Now \(T_n=2t-a/2\) is uniform on \([-a/2,a/2]\). This proves (1) simultaneously in all three classes, with no exceptional low-order polygons.

In all cases \(0<b_n\le\pi/2\), so \(\cos|T_n|\) decreases continuously as \(|T_n|\) increases. Since \(|T_n|\) is uniform on \([0,b_n]\), the distribution transformation gives (2). Direct integration yields \(\mathbb E\cos T_n=\sin(b_n)/b_n\) and \(\mathbb E\cos^2T_n=1/2+\sin(2b_n)/(4b_n)\), proving (3).

For (4), the elementary expansions (uniform along residue subsequences) are
\[
\operatorname{Var}(\cos T_n)=\frac{b_n^4}{45}+O(b_n^6),\qquad
C_n=2R^2+O(R^2a^2),\qquad b_n=\kappa_n\frac\pi n,
\]
where \(\kappa_n=2,1,1/2\), respectively. Thus \(n^4\operatorname{Var}(B_n)/R^4\to4\kappa_n^4\pi^4/45\), yielding all three coefficients and their ratio. Expanding (3) gives the common mean (5).

Finally the exact change of variables from \(|T_n|\) to \(X_n=(1-\cos T_n)/(1-\cos b_n)\) gives (6). Taylor's theorem for \(\sin\) and \(\arcsin\) supplies a remainder uniform over \(0\le x\le1\):
\[
\Pr(X_n\le x)=\sqrt{x}+\frac{b_n^2}{24}(x^{3/2}-\sqrt{x})+O(b_n^4).
\tag{13}
\]
Because \(\max_{0\le x\le1}(\sqrt{x}-x^{3/2})=2/(3\sqrt3)\), attained uniquely at \(x=1/3\), taking suprema yields (7). This also proves weak convergence to the distribution with CDF \(\sqrt{x}\), namely \(\operatorname{Beta}(1/2,1)\). No finite sample is used to prove any universal statement.

## Verification
The standalone `verify.py` computes bounding-box areas **independently from every vertex's Cartesian coordinates**, then compares them against the trigonometric law for \(25,186\) configurations covering all \(3\le n\le100\). It independently integrates the first two moments, compares empirical angular CDFs in all three regimes, and checks the sharp leading variance and Kolmogorov-distance constants. Execute it with `python3 verify.py` using only the Python standard library. Expected final marker: `ALL_REGULAR_POLYGON_BOUNDING_BOX_TESTS_OK`. Finite computations corroborate (1)--(7); the proof above supplies the all-\(n\) justification.

## Relationship to prior work
Freeman and Shapira's classical minimum enclosing-rectangle theorem and the rotating-calipers developments study **the least area over orientations**, not the probability distribution at Haar-uniform orientation. Their structural theorem is prior work. The original five-page Freeman--Shapira article was materially inspected in its publicly readable text, including its three theorems and optimization algorithm. A 2014 account of rotating calipers likewise treats optimizing orientation, not its full area law.

The published result *Exact minimum-area enclosing parallelograms for regular polygons* already gives the arithmetic three-branch **minimum** \(4R^2\cos^2(a)\), \(4R^2\cos a\), or \(4R^2\cos^3(a/2)\). These coincide with \(L_n\) and are not presented as original here. Its complete published `RESULT.md` proves optimization using an edge-contact reduction but does not compute any randomly oriented box-area law, variance, or distributional limit. Similarly, the full published *Exact translative convex-hull profile of every regular polygon* concerns the *radial-chord times transverse-width* invariant, not the product of perpendicular widths in (8); its all-direction constant cases do not imply constant bounding-box area. The two products have different definitions and, for instance, (4) establishes a strictly positive asymptotic variance in each residue class.

The contribution here is the complete push-forward of **perpendicular width products under uniformly random rotations** for every regular polygon, together with its arithmetic variance split and universal sharp normalized loss law. Targeted searches did not find an exact prior distribution, but absence in the searched sources is not a proof of absolute historical originality.

## Limitations
The result does not treat irregular polygons, nonuniform angular distributions, minimum-perimeter rectangles, other enclosing shapes, or dimensions greater than two. Known classical and published minimum-area endpoints are credited explicitly, so novelty is not claimed for those endpoint values. The result is derived from elementary support-geometry ingredients, and a historically unindexed analysis of random rectangle orientations could overlap with these formulas. The sharp Kolmogorov correction is for the stated normalization by each polygon's **own** extreme rectangle areas. The probabilistic limits concern random orientation of deterministic polygons, not random polygon vertices.

## References
1. H. Freeman and R. Shapira, *Determining the minimum-area encasing rectangle for an arbitrary closed curve*, Communications of the ACM 18 (1975), 409--413. DOI: 10.1145/360881.360919. Public readable primary text: https://www.researchgate.net/publication/234816003_Determining_the_minimum-area_encasing_rectangle_for_an_arbitrary_closed_curve.
2. G. Toussaint, *Solving geometric problems with the rotating calipers*, IEEE MELECON, 1983. Readable paper excerpt: https://gradebuddy.com/doc/2680203/solving-geometric-problems-with-the-rotating-calipers/.
3. D. Geidav, *Computing oriented minimum bounding boxes in 2D*, originally posted 23 January 2014, https://geidav.wordpress.com/2014/01/23/computing-oriented-minimum-bounding-boxes-in-2d/.
4. *Exact minimum-area enclosing parallelograms for regular polygons*, publicly available `RESULT.md`, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-exact-minimum-area-enclosing-parallelograms-for-regular-polygons--827c68cd7bad/RESULT.md.
5. *Exact translative convex-hull profile of every regular polygon*, publicly available `RESULT.md`, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-exact-translative-convex-hull-profile-of-every-regular-polygon--79b005afe9c0/RESULT.md.
