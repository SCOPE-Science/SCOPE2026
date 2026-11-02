# Sharp dimension-free stability of metric-graph linear spline projection

## Finding

Let \(G\) be any finite connected simple graph with at least one edge. Realize every edge \(e\) as an interval of length \(\ell_e>0\), carrying the measure \(\rho_e\,ds\) with a constant density \(\rho_e>0\). Let \(S_G\) be the space of globally continuous real functions affine on each edge and let \(P_G\) be the orthogonal projector from real \(L^2(G)\) onto \(S_G\). Then the endpoint operator norm satisfies the **strict universal estimate**

\[
1\leq \|P_G\|_{L^\infty(G)\to L^\infty(G)}<3.
\]

The universal constant is **sharp**, even if all edges have unit length and density and the underlying graph has no vertices of degree one. Specifically, for the metric hypercube \(Q_d\), \(d\geq1\),

\[
0<3-\|P_{Q_d}\|\leq\frac{6}{d+2},\qquad
0\leq\frac{6}{d+2}-(3-\|P_{Q_d}\|)
\leq\frac{6(3d+2)}{d(d+2)(d+4)}.
\]

Consequently \(3-\|P_{Q_d}\|=6/d+O(d^{-2})\) as \(d\to\infty\), and \(\sup_G\|P_G\|=3\), with the supremum not attained by any finite connected graph of the stated kind. The norm on each fixed graph is attained by an \(L^\infty\) sign-of-kernel datum. 

There is also an **exact rational formula in every hypercube dimension**. Define the unique positive rational sequence \(a_0,\ldots,a_d\) by

\[
2d a_k-k a_{k-1}-(d-k)a_{k+1}=\mathbf 1_{\{k=0\}}
\quad(0\leq k\leq d),
\]

omitting terms with indices outside \(\{0,\ldots,d\}\). Then

\[
\boxed{\|P_{Q_d}\|=
3\sum_{k=0}^{d-1}\binom dk(d-k)
\frac{a_k^2+a_{k+1}^2}{a_k+a_{k+1}}.}
\]

For \(d=1,2,3,4\), the values are respectively \(5/3\), \(17/9\), \(24877/12075\), and \(7397/3381\).

## Assumptions and scope

Graphs are finite, loopless, undirected, connected, and simple. Each edge is a separate interval and carries a strictly positive **constant** arclength density. Continuity is imposed at common graph vertices; no derivative or Kirchhoff constraint is imposed on functions of \(S_G\). There is one affine finite element per original edge and no interior interpolation knot. Operator norms use the essential supremum for measurable input functions and the continuous supremum for the resulting projected spline. All measures are real and positive. The dimension of the cube is the number of binary coordinates, so \(Q_d\) has \(2^d\) vertices of degree \(d\).

## Proof

**1. Exact graph mass matrix.** For each vertex \(v\) let \(\phi_v\) be its nodal hat: on an edge \(uv\) parametrized by \(0\leq t\leq1\), its values are \(1-t\) at the \(u\) end, \(t\) at the \(v\) end, and zero for all other nodal hats. Let \(m_e=\rho_e\ell_e>0\), let \(W\) be the symmetric weighted adjacency matrix with \(W_{uv}=m_{uv}\) on edges and zero otherwise, and set \(D=\operatorname{diag}(\sum_vW_{uv})\). Direct edge integrations give

\[
\langle\phi_u,\phi_v\rangle_{L^2(G)}
=\tfrac16(2D+W)_{uv}.
\]

Thus the positive-definite Gram matrix is \(M=(2D+W)/6\). With \(B=(2D+W)^{-1}\), the integral kernel for vertex evaluation at \(o\) is, on edge \(uv\),

\[
K_o(uv,t)=6\bigl((1-t)B_{ou}+tB_{ov}\bigr).
\]

For a point interior to an edge the evaluation kernel is the corresponding convex combination of endpoint kernels. By convexity of its \(L^1\) norm, a norming evaluation can always be chosen at a graph vertex. The \(L^\infty\)-operator norm equals \(\max_o\int_G|K_o|\,d\mu\), attained for a norming vertex by \(f=\operatorname{sgn}K_o\) almost everywhere.

**2. The universal upper bound.** Write \(C=(2D-W)^{-1}\) and \(T=D^{-1}W\). The matrix \(T\) is row-stochastic. The absolutely convergent Neumann expansions

\[
B=\tfrac12\sum_{j=0}^\infty(-T/2)^jD^{-1},\qquad
C=\tfrac12\sum_{j=0}^\infty(T/2)^jD^{-1}
\]

show that \(|B_{ou}|\leq C_{ou}\) entrywise. Every entry of \(C\) is strictly positive because the graph is connected. Moreover \((2D-W)\mathbf1=D\mathbf1\), whence \(\sum_u D_{uu}C_{ou}=1\). Using the two nonnegative hat functions on every edge,

\[
\begin{aligned}
\int_G|K_o|\,d\mu
&\leq 3\sum_{uv\in E}m_{uv}(|B_{ou}|+|B_{ov}|)\\
&=3\sum_uD_{uu}|B_{ou}|\\
&\leq3\sum_uD_{uu}C_{ou}=3.
\end{aligned}
\]

The inequality is strict for every fixed connected graph. If the graph is bipartite, \(B_{ou}\) and \(B_{ov}\) are nonzero and have opposite signs on every edge \(uv\), so the edgewise triangle inequality is strict. If the graph is not bipartite, an odd closed walk from \(o\) contributes to the negative terms of the Neumann series for \(B_{oo}\) while the even (including length-zero) terms are positive, giving \(|B_{oo}|<C_{oo}\) and therefore strictness in the last displayed bound. Finally \(P_G\mathbf1=\mathbf1\), so the norm is at least one.

**3. Cubical Green functions and the exact formula.** On the unweighted hypercube \(Q_d\), \(D=dI\) and \(W=A\), the adjacency matrix. Fix a vertex \(o\). The matrix \(C=(2dI-A)^{-1}\) is positive and invariant under automorphisms fixing \(o\). Its entries \(C_{ov}\) therefore equal positive rational numbers \(a_k\), where \(k\) is the Hamming distance of \(v\) from \(o\). The equation \((2dI-A)C=I\) is exactly the stated recurrence. Bipartiteness gives \(B_{ov}=(-1)^k a_k\). An edge from shell \(k\) to shell \(k+1\) contributes

\[
\int_0^1 6\left|a_k(1-t)-a_{k+1}t\right|dt
=3\frac{a_k^2+a_{k+1}^2}{a_k+a_{k+1}}.
\]

There are \(\binom dk(d-k)\) such edges. All vertices are symmetry-equivalent, yielding the exact expression and its attainment by the sign of the corresponding vertex kernel.

**4. Quantitative approach to the sharp universal constant.** Since each row sum of \(C\) equals \(1/d\), summing the endpoint masses of edges shows

\[
\sum_{k=0}^{d-1}\binom dk(d-k)(a_k+a_{k+1})=1.
\]

Using \((a^2+b^2)/(a+b)=a+b-2ab/(a+b)\), the exact deficit is

\[
\Delta_d:=3-\|P_{Q_d}\|
=6\sum_{k=0}^{d-1}\binom dk(d-k)
\frac{a_ka_{k+1}}{a_k+a_{k+1}}.
\]

Let \(S_j=\sum_{k=0}^d k^j\binom dk a_k\) for \(j=0,1,2\). Summing the resolvent equation over the vertices, and then weighting by Hamming distance and its square, gives

\[
S_0=\frac1d,\qquad
S_1=\frac1{d+2},\qquad
S_2=\frac{3d+2}{(d+2)(d+4)}.
\]

For clarity, these identities use the neighbor-distance sums \(\sum_{v\sim u} k(v)=(d-2)k(u)+d\) and \(\sum_{v\sim u} k(v)^2=(d-4)k(u)^2+2dk(u)+d\). In particular,

\[
\sum_{k=0}^{d-1}\binom dk(d-k)a_{k+1}=S_1.
\]

Set \(r_k=a_{k+1}/a_k\). The recurrence gives \(r_{d-1}=1/2\) and, backwards,

\[
r_k=\frac{k+1}{2d-(d-k-1)r_{k+1}}.
\]

Backward induction proves \(0<r_k\leq1\) and \(r_k\leq(k+1)/d\). Consequently

\[
0\leq 6S_1-\Delta_d
=6\sum_{k=0}^{d-1}\binom dk(d-k)a_{k+1}
\frac{r_k}{1+r_k}
\leq\frac6d S_2.
\]

Substituting the exact moments proves both asserted two-sided bounds. In particular \(d\Delta_d\to6\). The inequalities, rather than any finite extrapolation, establish sharpness of the dimension-free constant.

## Verification

The included standalone `verify_graph_spline.py` uses exact rational Gaussian elimination. It checks the radial resolvent and its first three moments for dimensions \(1\) through \(16\), independently assembles and inverts the full finite-element Gram matrices for the hypercubes of dimensions \(1\) through \(4\), and checks the exact integral norm against the radial formula. It also tests the strict universal bound on 60 deterministically generated connected positively weighted graphs. The run passed 3,093 exact-rational assertions. Computations check the stated formulas in finite cases only; the four analytic steps above establish the universal statements.

Reproduce with `python3 verify_graph_spline.py` from a directory containing the standalone file. Only the standard Python library is required.

## Relationship to prior work

The interval spline result of Oskolkov, summarized in Kayumov's 2004 open preprint, already establishes that the optimal mesh-independent endpoint constant for continuous linear splines on an interval is three. That theorem does not by its stated domain include genuine branching of a metric graph, nor does it provide the cubical Green-function formula or the degree-dependent sharp deficit. Arioli and Benzi's paper develops finite-element stiffness and mass matrices for quantum graphs; its matrix construction underlies compatible numerical discretizations, but its discussion of the mass matrix and conditioning does not state an \(L^\infty\) orthoprojector constant or the hypercube asymptotic. General finite-element projection-stability studies by Crouzeix–Thomée and Boman have different geometric hypotheses and norm estimates. Previously established exact norms on stars, balanced complete multipartite graphs, and windmill graphs concern proper special families, do not imply the full graph bound, and do not include the hypercube asymptotic. Prior art for equivalent mass-matrix arguments may exist, so an independent priority search remains advisable.

## Limitations

The constant three is a supremum across graph sizes and structures, not attained on any finite connected graph covered here. The hypercube asymptotic is about growing graph degree and size; it is not an estimate for arbitrary graph families. The proof requires continuous, one-element-per-edge affine splines and positive constant edge densities. It does not address weighted densities varying *within* an edge, higher polynomial degrees, derivative constraints at vertices, or nonorthogonal projection. The search of earlier literature is necessarily nonexhaustive, and a general theorem on graphs in a differently phrased finite-element source could affect publication priority.

## References

1. A. Kayumov, *Least-squares approximation by second-order L-splines*, arXiv:math/0408418, first arXiv submission 2004-08-30, https://arxiv.org/abs/math/0408418 (introduction and theorem discussion of the sharp interval constant).
2. M. Arioli and M. Benzi, *A finite element method for quantum graphs*, IMA Journal of Numerical Analysis 38 (2018), 1119–1163, DOI:10.1093/imanum/drx029 (Sections 4–5 and conclusion; metric-graph finite-element mass matrices).
3. M. Crouzeix and V. Thomée, *The stability in Lp and Wp1 of the L2-projection onto finite element function spaces*, Mathematics of Computation 48 (1987), 521–532, DOI:10.2307/2007825 (background; full text not verified in this comparison).
4. M. Boman, *Estimates for the L2-projection onto continuous finite element spaces in a weighted Lp-norm*, BIT Numerical Mathematics 46 (2006), 249–260, DOI:10.1007/s10543-006-0062-3 (background; abstract inspected).
