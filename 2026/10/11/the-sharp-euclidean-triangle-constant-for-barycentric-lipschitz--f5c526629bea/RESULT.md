# The sharp Euclidean triangle constant for barycentric Lipschitz-free \(p\)-interpolation

## Finding
Let \(T\subset\mathbb R^2\) be a nondegenerate closed Euclidean triangle with distinct vertices \(v_0,v_1,v_2\), and let \(V=\{v_0,v_1,v_2\}\) carry the induced Euclidean distances. Fix any basepoint in \(V\). Write \(\lambda_j(x)\) for the barycentric coordinates of \(x\in T\), and define \(R_p(x)=\sum_{j=0}^2\lambda_j(x)\delta_V(v_j)\) with values in the real Lipschitz-free \(p\)-space \(\mathcal F_p(V)\).

For every \(0<p\le1\), if \(\theta_{\max}\in[\pi/3,\pi)\) is the largest of the three interior angles, then
\[
\boxed{\operatorname{Lip}(R_p)=2^{1/p-1}\sec(\theta_{\max}/2).}
\]
The maximum is realized as the ratio of the images of two distinct points in \(T\) lying on a segment that starts at any largest-angle vertex and points along the internal angle bisector. This gives the exact equilateral-triangle constant \(2^{1/p}/\sqrt3\), and the classical Banach case \(\operatorname{Lip}(R_1)=\sec(\theta_{\max}/2)\).

## Assumptions and scope
All scalars are real. The domain carries its Euclidean distance. There is no restriction on the side lengths beyond strict triangle inequalities, and the exponent is any real \(0<p\le1\). The codomain is the free \(p\)-space **of the three vertex metric points**, not the free space of the entire triangle. The map is affine, uniquely determined by its values \(\delta_V(v_j)\), and independent of the chosen base vertex up to the canonical isometric change of basepoint. Lipschitz constants use the ordinary quotient of the target quasi-norm by Euclidean distance.

For a zero-sum molecule \(m=\sum_{v\in V}m_v\delta_v\), define the transportation \(p\)-norm by
\[
\|m\|_p^p=\inf\left\{\sum_{i<j}d(v_i,v_j)^p|f_{ij}|^p:\ \sum_{j}f_{ij}-\sum_{j}f_{ji}=m_{v_i}\right\}.
\]
Here the three variables \(f_{ij}\) denote signed flows along arbitrarily oriented edges of the complete three-vertex graph, and the sign convention is immaterial. This is the finite-metric realization of the usual Lipschitz-free \(p\)-norm; aggregating parallel representations cannot increase the cost when \(0<p\le1\). For \(p=1\) it is the usual Arens–Eells transportation norm.

## Proof
**1. The three-edge reduction.** For any given molecule, the solutions of the flow constraints form a one-dimensional affine line. Parameterize them by one cycle variable \(t\). The transportation \(p\)-cost becomes
\[
F(t)=w_1^p|t-a_1|^p+w_2^p|t-a_2|^p+w_3^p|t-a_3|^p,
\]
where each \(w_j>0\) is an edge length. On each interval avoiding the three breakpoints \(a_j\), every summand is concave for \(0<p\le1\). Therefore a minimum on that interval occurs at one of its endpoints. Since \(F(t)\to\infty\) as \(|t|\to\infty\), a global minimum occurs at a breakpoint: *some edge flow vanishes*. Thus a three-point molecule is optimally represented on one of the three spanning trees. This also applies to \(p=1\) by piecewise linearity.

**2. Universal comparison with \(p=1\).** Any nonzero zero-sum real molecule on three vertices has one sign occurring at exactly one vertex. If it has one source and two sinks, the direct two-edge star from the source to the sinks minimizes the \(p=1\) transportation cost by the metric triangle inequality; reverse signs for the one-sink case. If the two nonnegative weighted edge costs are \(A,B\), then
\[
\|m\|_1=A+B,\qquad
\|m\|_p\le(A^p+B^p)^{1/p}
\le2^{1/p-1}(A+B).
\]
The last inequality follows from concavity of the power function on \([0,\infty)\). Consequently
\[
\operatorname{Lip}(R_p)\le2^{1/p-1}\operatorname{Lip}(R_1).
\]
This inequality is independent of side lengths and remains valid for all molecule differences \(R_p(x)-R_p(y)\).

**3. Exact Banach interpolation norm.** The dual space of \(\mathcal F_1(V)\) is the real space of Lipschitz potentials on \(V\) modulo constants, with norm \(\max_{i\ne j}|f(v_i)-f(v_j)|/d(v_i,v_j)\). Since \(T\) is nondegenerate, the three strict triangle inequalities imply that this unit ball is a centrally symmetric hexagon. Its six extreme potentials, modulo constants, are the three distance functions \(f_i(v)=d(v_i,v)\) and their negatives. Thus the operator norm of the affine map into \(\mathcal F_1(V)\) equals the largest Euclidean gradient norm among the affine interpolants of these six potentials.

Let \(\theta_i\) be the angle at vertex \(v_i\), and let \(e_{ij},e_{ik}\) be the two unit edge vectors pointing out of \(v_i\). The affine interpolant \(\widetilde f_i\) of \(f_i\) satisfies \(\nabla\widetilde f_i\cdot e_{ij}=\nabla\widetilde f_i\cdot e_{ik}=1\). Solving these two equations gives a gradient in the angle-bisector direction of magnitude \(1/\cos(\theta_i/2)\). Therefore
\[
\operatorname{Lip}(R_1)=\max_i\|\nabla\widetilde f_i\|_2
=\max_i\sec(\theta_i/2)
=\sec(\theta_{\max}/2).
\]
The first equality uses ordinary Banach duality and the fact that the maximum of the norm of a linear functional of the potential occurs at a vertex of the compact Lipschitz polytope.

**4. Matching lower bound for every \(p\).** Let \(v_a\) have the largest angle, and write \(b=d(v_a,v_b)\), \(c=d(v_a,v_c)\), and \(a=d(v_b,v_c)\). Because \(a\) is the longest side, \(a\ge b,c\). Consider
\[
m=\frac{\delta(v_b)-\delta(v_a)}b+
  \frac{\delta(v_c)-\delta(v_a)}c.
\]
The direct-star transport uses two edges, each of weighted magnitude \(1\), giving \(p\)-cost \(2\). By step 1, it suffices to compare the other two spanning trees. Their respective \(p\)-costs are
\[
(1+b/c)^p+(a/c)^p\quad\hbox{and}\quad
(1+c/b)^p+(a/b)^p.
\]
Each is strictly larger than \(2\), since \(a\ge b,c\). Hence \(\|m\|_p=2^{1/p}\).

Let
\[
u=\frac{v_b-v_a}b+\frac{v_c-v_a}c.
\]
This is the sum of two Euclidean unit vectors enclosing angle \(\theta_{\max}\), so \(\|u\|_2=2\cos(\theta_{\max}/2)\). For any \(\varepsilon>0\) such that \(\varepsilon(1/b+1/c)\le1\), the point \(v_a+\varepsilon u\) lies in \(T\), and the affine definition gives
\[
R_p(v_a+\varepsilon u)-R_p(v_a)=\varepsilon m.
\]
Thus
\[
\operatorname{Lip}(R_p)\ge
\frac{2^{1/p}}{2\cos(\theta_{\max}/2)}
=2^{1/p-1}\sec(\theta_{\max}/2).
\]
Combining with steps 2–3 proves the equality for every indicated triangle and exponent. \(\square\)

## Verification
The proof covers the entire continuous exponent interval and all nondegenerate Euclidean triangles. Step 1 checks the only potentially nonstandard finite-metric lemma by a complete three-spanning-tree reduction; step 4 compares all three candidates and supplies explicit finite points realizing equality. A separately executable, standard-library-only numerical check samples many triangle shapes, four exponents, and Euclidean directions and agrees with the analytic constant to mesh accuracy; those samples do not replace the universal analytic argument. Reproduce with `python verify_triangle.py`.

## Relationship to prior work
Bíma's 2023 work studies coordinatewise affine canonical maps on unions of **axis-aligned cubes** equipped with the \(\ell_1\) metric and gives dimension-dependent upper and lower bounds; it does not state an exact Euclidean **simplex** interpolation law. Its source, Albiac–Ansorena–Cúth–Doucha (2020), likewise constructs multiaffine interpolation on cubical grids, in the \(\ell_\infty\) ambient metric. The present result instead gives the exact operator norm of the unique affine interpolation over a single Euclidean triangular cell, with a sharp dependence on its largest angle and on \(p\). The familiar \(p=1\) scalar affine-interpolant norm is identified explicitly; the simultaneous exact \(0<p<1\) free quasi-Banach norm is established using optimal transport across all spanning trees.

## Limitations
The result does **not** provide a bound for maps patched over arbitrary triangulations and does not claim extension optimality among all (possibly nonlinear) vertex-interpolating maps. For degenerating triangles the constant diverges as the largest angle tends to \(\pi\), and no uniform shape-independent estimate is claimed. No independent mathematical audit has been performed. Existence of equivalent formulas in less-indexed interpolation literature remains a prior-art risk; the value and scope of the theorem are limited to its stated canonical local interpolation operator.

## References
- Jan Bíma, *Lipschitz-free spaces and subsets of finite-dimensional spaces*, arXiv:2303.03265 (first version public 6 March 2023); *Proc. R. Soc. Edinburgh A* (2025), DOI 10.1017/prm.2023.109. Section 3 and Theorem 3.2 treat cubical interpolation.
- Fernando Albiac, José L. Ansorena, Marek Cúth, and Michal Doucha, *Structure of the Lipschitz free p-spaces \(\mathcal F_p(\mathbb Z^d)\) and \(\mathcal F_p(\mathbb R^d)\) for \(0<p\le1\)*, arXiv:2006.08018 (first version public 14 June 2020). Section 3, Theorem 3.5, treats coordinatewise affine cubical interpolation.
- Shayne Waldron, *The Error in Linear Interpolation at the Vertices of a Simplex*, *SIAM J. Numer. Anal.* 35 (1998), 1191–1200, DOI 10.1137/S0036142996313154. Different sharp pointwise scalar interpolation error problem; full text not examined.
