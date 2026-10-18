# Damping-driven relocation of an optimal actuator on two-hub trees

## Finding

**Theorem.** For every integer \(m\ge2\), consider the unit-conductance tree \(T_m\) with a degree-three junction \(c\), one private leaf \(e\) attached to \(c\), and two additional neighbors \(a,b\), each of which has exactly \(m\) private leaves. The tree has \(2m+4\) vertices. For every damping parameter \(\alpha>0\), let \(L\) denote its combinatorial Laplacian and let \(A_\alpha=-(L+\alpha I)\). Exactly one unit-coordinate actuator may be installed at a vertex \(v\). Choose \(v\) to maximize the trace of the infinite-horizon controllability Gramian
\[
 W_v=\int_0^\infty e^{tA_\alpha}e_ve_v^{\mathsf T}e^{tA_\alpha}\,dt.
\]

No junction or hub can be optimal. For \(m=2\), precisely the four private leaves of the two hubs are optimal for every \(\alpha>0\). For every \(m\ge3\), define the sharp threshold
\[
\alpha_*(m)=\frac{\sqrt{(m+2)^2+8/(m-2)}-(m+2)}{2}.
\]
If \(0<\alpha<\alpha_*(m)\), precisely the \(2m\) hub-attached leaves are optimal. At \(\alpha=\alpha_*(m)\), all \(2m+1\) leaves tie. If \(\alpha>\alpha_*(m)\), the junction's private leaf \(e\) is uniquely optimal. Moreover,
\[
\lim_{m\to\infty}m^2\alpha_*(m)=2.
\]
For \(m=3\), the transition occurs at \(\alpha_*(3)=(\sqrt{33}-5)/2\).

The following exact all-parameter difference specifies the margin between the junction leaf and any hub leaf. Write \(G=(L+\alpha I)^{-1}\); then
\[
G_{ee}-G_{oo}=\frac{(m-2)\alpha^2+(m^2-4)\alpha-2}{(\alpha+1)[\alpha^2+(m+2)\alpha+1][\alpha^3+(m+6)\alpha^2+(4m+9)\alpha+2m+4]},
\]
where \(o\) is any hub-attached private leaf. The corresponding Gramian-trace difference is one half this quantity.

## Assumptions and scope

All edges have conductance one, \(m\) is an integer at least two, \(\alpha\) is strictly positive, and inputs are standard coordinate columns of Euclidean norm one. The state-space norm in the Gramian trace is the standard Euclidean norm. The actuator is selected at exactly one vertex without any gain, price, or controllability-rank constraint. A site is optimal if it maximizes the indicated trace, even when the single-input pair is not fully controllable. The result concerns infinite-horizon stable diffusive dynamics, not minimum actuation energy to reach every state and not finite-horizon Gramians.

## Proof

**1. The objective is a resolvent diagonal.** Since \(L\) is real symmetric positive semidefinite, \(M=L+\alpha I\) is positive definite. Cyclicity of trace and symmetry yield
\[
\operatorname{tr}W_v=\int_0^\infty e_v^{\mathsf T}e^{-2tM}e_v\,dt=\tfrac12(M^{-1})_{vv}.
\]
Thus every comparison is a comparison of diagonal entries of \(G=M^{-1}\).

**2. An internal vertex adjacent to a pendant leaf is strictly inferior.** Let \(\ell\) be a leaf adjacent to \(u\). Delete their common edge but retain all vertices. The resulting matrix before restoring the edge is a direct sum of \([\alpha]\) and \(B=L_{T-\ell}+\alpha I\). Put \(p=1/\alpha\) and \(q=(B^{-1})_{uu}\). The restored edge is the rank-one positive-semidefinite update \((e_\ell-e_u)(e_\ell-e_u)^{\mathsf T}\). Sherman–Morrison gives
\[
G_{\ell\ell}-G_{uu}=\frac{p-q}{1+p+q}.
\]
The remaining tree is connected and contains more than one vertex; hence \(B^{-1}\preceq\alpha^{-1}I\), with strict inequality on the \(u\)-diagonal. Indeed, \(L_{T-\ell}\) has one-dimensional kernel spanned by the constant vector, while \(e_u\) is not constant. Consequently \(0<q<p\) and the difference is positive. Every nonleaf of \(T_m\) (namely \(c,a,b\)) has a pendant neighbor, so no nonleaf maximizes the objective.

**3. Exact two-leaf comparison.** Set \(x=\alpha\), \(s=x+1\), and eliminate all \(2m+1\) leaves by Schur complementation. On the ordered internal vertices \((c,a,b)\), the reduced positive-definite matrix is
\[
S=\begin{pmatrix}C&-1&-1\\-1&H&0\\-1&0&H\end{pmatrix},\qquad
C=x+3-\frac1s,\quad H=x+m+1-\frac ms.
\]
Write \(D=C-2/H>0\). Direct block inversion gives
\[
(S^{-1})_{cc}=\frac1D,\qquad (S^{-1})_{aa}=\frac1H+\frac1{H^2D}.
\]
Undoing the leaf elimination, the two diagonal resolvents are
\[
G_{ee}=\frac1s+\frac1{s^2D},\qquad
G_{oo}=\frac1s+\frac1{s^2}\left(\frac1H+\frac1{H^2D}\right).
\]
The second expression applies to every hub leaf by graph automorphisms. Putting these two rational expressions over a common denominator and canceling common factors gives exactly the factored difference stated in the theorem. Every factor in its denominator is strictly positive when \(x>0\) and \(m\ge2\), so its sign is precisely that of
\[
Q_m(x)=(m-2)x^2+(m^2-4)x-2.
\]

**4. Sharp classification.** If \(m=2\), then \(Q_2(x)=-2<0\). For \(m\ge3\), the derivative \(Q_m'(x)=2(m-2)x+(m^2-4)\) is strictly positive for all \(x\ge0\), while \(Q_m(0)=-2\) and \(Q_m(x)\to\infty\). Its unique positive zero is the displayed \(\alpha_*(m)\), obtained from \(Q_m(x)=(m-2)[x^2+(m+2)x]-2\). The sign of the diagonal difference and the leaf exclusion in step 2 yield the exhaustive optimizer sets, including all tie cases.

**5. Asymptotic scaling.** Rationalizing the root gives
\[
\alpha_*(m)=\frac{4}{(m-2)[\sqrt{(m+2)^2+8/(m-2)}+(m+2)]}.
\]
Multiplying by \(m^2\), dividing the bracket by \(m\), and taking \(m\to\infty\) gives the limit \(2\). This uses no finite enumeration.

## Verification

The accompanying standalone `verify.py` (Python with SymPy) symbolically cancels the difference between the Schur-complement formula and the factored rational identity, checks the threshold root and limit, and reconstructs exact full weighted Laplacian inverses. Across integers \(2\le m\le11\) and five positive rational damping values, it checks the claimed resolvent diagonal formulas, domination of each internal vertex by an adjacent leaf, equalities within leaf orbits, and optimality signs. Its executed output was `PASS 406 symbolic, exact-matrix and structural assertions`. Finite matrix tests do not replace the unrestricted all-parameter proof above.

## Relationship to prior work

Summers and Lygeros, *Optimal Sensor and Actuator Placement in Complex Dynamical Networks* (first public arXiv version 11 June 2013), establish the modularity of trace-of-Gramian actuator-set objectives and motivate individual-site ranking. That theorem does not specify the ranking's dependence on damping for the present family. Kirkland, Neumann, and Shader, *Distances in Weighted Trees and Group Inverse of Laplacian Matrices* (1997), characterize extremal diagonal entries of the **group inverse** \(L^\#\), corresponding to a zero-damping finite part rather than \((L+\alpha I)^{-1}\) for \(\alpha>0\). The present statement is an explicit positive-damping actuator-location phase transition, not a new proof of their general results. The exact family and rank transitions were compared against available research records; unindexed equivalent specializations remain possible.

## Limitations

The result concerns this specific two-hub tree, unweighted edges, a uniform damping shift, a single input of fixed unit magnitude, and the trace Gramian metric. It does not assert full controllability, nonzero determinant of the Gramian, improved minimum-energy steering to arbitrary targets, or optimality under other metrics. No theorem is claimed for general trees or heterogeneous damping. The computations are corroborating tests, not a proof by enumeration. Independent scientific audit has not been performed.

## References

1. T. H. Summers and J. Lygeros, *Optimal Sensor and Actuator Placement in Complex Dynamical Networks*, arXiv:1306.2491, v1 11 June 2013, https://arxiv.org/abs/1306.2491.
2. S. J. Kirkland, M. Neumann, and B. L. Shader, *Distances in Weighted Trees and Group Inverse of Laplacian Matrices*, SIAM J. Matrix Anal. Appl. 18 (1997), 827–841, DOI:10.1137/S0895479896298713. Author-affiliated open-access full text: https://pdfs.semanticscholar.org/6c13/6f0da4d44678c5251fe9b5a461f6ddbe1164.pdf.
