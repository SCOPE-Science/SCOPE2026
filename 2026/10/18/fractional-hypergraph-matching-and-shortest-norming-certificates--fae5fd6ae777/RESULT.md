# Fractional hypergraph matching and shortest norming certificates for lattice bottlenecks

## Finding
Let \(n\ge1\), let \(\mathcal H\subseteq2^{[n]}\setminus\{\varnothing\}\) be a **nonempty, finite set** of hyperedges, and let \(1\le p<\infty\). The real free \(p\)-convex Banach lattice over \(\ell_1^n\) is denoted by \(X_p=\operatorname{FBL}^{(p)}[\ell_1^n(\mathbb R)]\). Write \(\delta_{e_i}\) for its canonical generators and take the following positive lattice polynomial:

\[
F_{\mathcal H}=\bigvee_{S\in\mathcal H}\ \bigwedge_{i\in S}|\delta_{e_i}|.
\]

Define the **fractional matching number** by the finite linear program

\[
\nu^*(\mathcal H)=\max\left\{\sum_{S\in\mathcal H}w_S:\ w_S\ge0,\quad\sum_{S\ni i}w_S\le1\quad(1\le i\le n)\right\}.
\]

The exact norm and the optimal finite-test complexity are

\[
\boxed{\ \|F_{\mathcal H}\|_{X_p}^{p}=\nu^*(\mathcal H),\qquad
\sigma(F_{\mathcal H})=\min\{|\operatorname{supp}w|:\ w\text{ is an optimal fractional matching}\}\le n.\ }
\]

Here \(\sigma(F_{\mathcal H})\) is the **least number of nonzero test vectors** in an attaining family in the published representation of the free \(p\)-convex norm. An optimal family always exists. In particular, the lattice norm is computable by a rational linear program, independent of the exponent after taking its \(p\)-th power, and the universal finite-test bound \(n\) is sharp.

For a simple graph viewed as a two-uniform hypergraph, the theorem yields the following complete families of exact examples:

\[
\begin{array}{c|c|c}
\mathcal H&\|F_{\mathcal H}\|_{X_p}^p&\sigma(F_{\mathcal H})\\\hline
K_{2k}&k&k\\
K_{2k+1}&k+\tfrac12&k+2\\
C_{2k}&k&k\quad(k\ge2)\\
C_{2k+1}&k+\tfrac12&2k+1\quad(k\ge1)
\end{array}
\]

The seven-line Fano hypergraph on seven vertices has \(\|F_{\mathcal H}\|_{X_p}^{p}=7/3\) and \(\sigma(F_{\mathcal H})=7\). This exhibits a non-half-integral norm power already for a highly symmetric three-uniform hypergraph.

## Assumptions and scope
All spaces and lattice functions are over the real scalars. The hyperedge family contains no empty set and no repeated hyperedge, and isolated vertices are allowed. Only \(1\le p<\infty\) is claimed. For a dual vector \(u=(u_1,\ldots,u_n)\in(\ell_1^n)^*=\ell_\infty^n\), the lattice function takes the explicit coordinate form

\[
F_{\mathcal H}(u)=\max_{S\in\mathcal H}\min_{i\in S}|u_i|.
\]

An **admissible test family** consists of finitely many dual vectors \(u^{(1)},\dots,u^{(m)}\) such that \(\sum_{j=1}^m|u_i^{(j)}|^p\le1\) for every coordinate \(i\). It attains the norm if \(\sum_{j=1}^mF_{\mathcal H}(u^{(j)})^p=\|F_{\mathcal H}\|_{X_p}^p\). Only test vectors with a positive contribution are counted in \(\sigma\); zero-contribution vectors may be removed.

## Proof
**Step 1: the norm's coordinate-resource representation.** Formula (1.1) and the functional model identified in Theorem 6.1 of Jardón-Sánchez, Laustsen, Taylor, Tradacete and Troitsky [1] give

\[
\|F_{\mathcal H}\|_{X_p}^p=\sup_{m\ge1}\ \sup_{\substack{u^{(1)},\ldots,u^{(m)}\in\mathbb R^n\\\sum_j|u_i^{(j)}|^p\le1\ \forall i}}\ \sum_{j=1}^m F_{\mathcal H}(u^{(j)})^p.
\]

Indeed, the weak \(p\)-constraint in that representation is \(\sup_{\|x\|_1\le1}\sum_j|\langle x,u^{(j)}\rangle|^p\le1\). Since the summand is convex in \(x\), its maximum on the \(\ell_1\)-unit ball occurs at a signed coordinate vector. It is thus exactly \(\max_i\sum_j|u_i^{(j)}|^p\). The same formula for \(p=1\) follows from the earlier free Banach lattice representation [2].

**Step 2: every test family gives a fractional matching.** Let an admissible family be fixed; discard its zero-contribution rows. For each remaining row \(j\), choose an edge \(S_j\in\mathcal H\) realizing the maximum and put

\[
t_j=F_{\mathcal H}(u^{(j)})^p=\min_{i\in S_j}|u_i^{(j)}|^p>0,
\qquad w_S=\sum_{\{j:S_j=S\}}t_j.
\]

For any coordinate \(i\), the fractional matching load satisfies

\[
\sum_{S\ni i}w_S=\sum_{\{j:i\in S_j\}}t_j\le\sum_j|u_i^{(j)}|^p\le1.
\]

Thus \(w\) is feasible and \(\sum_jF_{\mathcal H}(u^{(j)})^p=\sum_Sw_S\le\nu^*(\mathcal H)\). Furthermore the number of positive coordinates of \(w\) does not exceed the number of contributing test vectors.

**Step 3: every fractional matching gives an attaining test family.** Conversely, let \(w\) be any feasible fractional matching. For each edge with \(w_S>0\) form a test vector supported on that edge:

\[
u_i^{S}=\begin{cases}w_S^{1/p},&i\in S,\\0,&i\notin S.\end{cases}
\]

Coordinate feasibility is exactly the matching capacity inequality. On this vector, the selected edge evaluates to \(w_S^{1/p}\) while every edge evaluates to at most \(w_S^{1/p}\), so \(F_{\mathcal H}(u^{S})^p=w_S\). Hence the test family achieves precisely \(\sum_Sw_S\). A finite linear program with bounded feasible region has an optimizer; choosing one proves equality of the norm power with \(\nu^*(\mathcal H)\) and attainment. The support comparison in Steps 2–3 proves the claimed **exact** formula for \(\sigma\).

**Step 4: sharp uniform length bound.** Take an extreme optimal fractional matching. If its positive support had more than \(n\) edges, the corresponding incidence columns in \(\mathbb R^n\) would be linearly dependent. Perturbing their strictly positive weights a sufficiently small amount in both directions would preserve every incidence load and nonnegativity, contradicting extremality. Therefore an extreme optimum has at most \(n\) positive entries, and the construction above gives at most \(n\) norming vectors.

**Step 5: complete graphs and cycles.** For any graph on \(n\) vertices, summing all vertex capacity constraints gives \(2\sum_ew_e\le n\). The complete graphs and cycles attain \(n/2\): use disjoint unit-weight edges if \(n\) is even; if \(n\) is odd, use one triangle with edge weights \(1/2\) plus disjoint unit edges for the complete graph, or put weight \(1/2\) on every edge of the odd cycle. The dual matching certificate assigning vertex price \(1/2\) verifies optimality.

To determine the **least support for odd complete graphs**, note that any optimal matching saturates all \(n\) vertex constraints. In the graph of positive-weight edges, every degree-one vertex forces its incident edge to have weight one, so that edge forms an isolated two-vertex component. Every other component has minimum degree at least two and thus at least as many edges as vertices. Since \(n\) is odd, at least one of these other components has odd cardinality at least three. Consequently any optimal matching has at least \((n+3)/2\) positive edges. The triangle-plus-disjoint-edges construction has exactly that many. For even complete graphs, support at least \(n/2\) follows because an edge covers at most two saturated vertices, and the perfect matching attains it.

For an odd cycle, equality of the total capacity bound forces \(w_{i-1}+w_i=1\) at each vertex (cyclic indices). Because the length is odd, these equations have the unique solution \(w_i=1/2\) for all edges. Hence the minimum support is the number of vertices. Even cycles admit a perfect matching of cardinality \(n/2\), which is also minimal.

**Step 6: seven-line projective-plane example.** Let the seven hyperedges, with vertices numbered from \(0\) to \(6\), be

\[
\{0,1,2\},\ \{0,3,4\},\ \{0,5,6\},\ \{1,3,5\},\ \{1,4,6\},\ \{2,3,6\},\ \{2,4,5\}.
\]

Every vertex lies on three edges and every two distinct edges meet at exactly one vertex. Put \(w_S=1/3\) for every edge and vertex-cover prices \(y_i=1/3\). The primal and dual objectives both equal \(7/3\), so the optimal value is \(7/3\). Because all seven dual prices are strictly positive, complementary slackness forces all seven vertex loads to equal one at any optimum. Writing \(A\) for the seven-by-seven vertex-edge incidence matrix, its Gram matrix satisfies \(A^{\mathsf T}A=2I+J\), which is invertible. Thus the unique optimal matching is the uniform one, and its support is seven. This also proves sharpness of the general length bound.

## Verification
The complete finite proof appears above; it does not rely on enumeration. The standalone standard-library script `verify.py` checks exact rational dual and primal certificates for all \(1,098\) labeled simple graphs on two through five vertices, as well as \(84\) explicit parametric certificates for complete graphs, cycles, stars, complete uniform hypergraphs and the seven-line projective plane. For each certificate it constructs the norm-attaining test vectors in \(p\)-th power coordinates and checks the coordinate budget and attained objective. Run with `python3 verify.py`. The actual embedded script was extracted and executed successfully. Its finite sweep is not a proof for arbitrary hypergraphs or exponents.

## Relationship to prior work
The key analytic input is the free \(p\)-convex norm representation in [1], which is substantially more general but does not evaluate this class of join-of-meets polynomials as a fractional matching linear program, determine their exact minimum number of norming vectors, or give the graph/projective-plane certificate examples. The ordinary free Banach lattice representation [2] yields the \(p=1\) starting point, but likewise does not carry out these classifications. The study [3] concerns free lattices on infinite classical sequence generators and estimates for coordinate-modulus sequences rather than the present finite hypergraph polynomial. Fractional matching and covering linear programs are classical combinatorial objects, used here as an exact isometric invariant of a different, canonical family of Banach-lattice elements. This result does **not** assert that fractional matching theory itself is new.

A geometrically related class of edge functions is the envelope of coordinate geometric means \(\max_{\{i,j\}}\sqrt{|u_iu_j|}\). Its pointwise inequality against the meet envelope does **not** determine this norm or any optimal test-length parameter: for a star with \(m\) leaves, the meet-envelope norm power here is \(1\), while its geometric-mean counterpart has norm power \(\sqrt m\). The two classifications are distinct. Searches under edge packing, dual hypergraph vertex cover, join-of-meets, lattice polynomials, and nonlinear \(p\)-summing formulations did not uncover a stronger published exact statement. Such searches do not establish exhaustive novelty.

## Limitations
The theorem is for real free \(p\)-convex lattices generated by finite-dimensional \(\ell_1\), not arbitrary generating Banach spaces, infinite hypergraphs, or the \(p=\infty\) endpoint. The shortest-length formula is expressed through a possibly degenerate optimal face of a rational linear program; outside the displayed families, an explicit structural closed form for this length is not asserted. Only exact attainment of the published finite-family norm representation is at issue, not norm-attaining functionals or infinite-dimensional operator attainment. All conclusions are self-reviewed and have not received independent audit. The result may have equivalent expressions in less directly indexed research literature.

## References
[1] H. Jardón-Sánchez, N. J. Laustsen, M. A. Taylor, P. Tradacete, V. G. Troitsky, *Free Banach lattices under convexity conditions*, arXiv:2101.03510v1 (first public 2021-01-10); open-access journal version, https://doi.org/10.1007/s13398-021-01155-8. See formula (1.1), Section 6 and Theorem 6.1.

[2] A. Avilés, J. D. Rodríguez, P. Tradacete, *The free Banach lattice generated by a Banach space*, arXiv:1706.08147v1 (2017); see Section 2 for the ordinary free-lattice norm.

[3] A. Avilés, P. Tradacete, I. Villanueva, *The free Banach lattices generated by* \(\ell_p\) *and* \(c_0\), arXiv:1806.02553v1 (2018); see Sections 1–3.
