# Sharp universal stability of quadratic projection on finite metric graphs

## Finding

Let \(G=(V,E)\) be any finite connected simple graph containing at least one edge. Realize every edge \(e\) as an interval of length \(\ell_e>0\), equipped with a positive density \(\rho_e\) constant along that edge. Write \(\mu\) for the resulting metric-graph measure and let \(S_2(G)\) be the real vector space of continuous functions whose restriction to each edge is a polynomial of degree at most two. No derivative matching is imposed at vertices. Let \(P_G\) denote \(L^2(G,\mu)\)-orthogonal projection onto \(S_2(G)\).

**Theorem.** For every such finite metric graph,
\[
1\leq\|P_G\|_{L^\infty(G)\to L^\infty(G)}<\frac{79}{25}.
\]
The constant is optimal uniformly over all graph sizes, topologies, positive lengths, and edgewise constant positive densities, although no fixed finite graph attains it. For unit-edge hypercubes \(Q_d\), \(d\geq1\),
\[
\frac{79}{25}-\frac{158}{25d}
\leq\|P_{Q_d}\|_{L^\infty\to L^\infty}<\frac{79}{25},
\qquad
\lim_{d\to\infty}\|P_{Q_d}\|_{L^\infty\to L^\infty}=\frac{79}{25}.
\]
Here the lower estimate is useful asymptotically; it is not asserted to be optimal for fixed \(d\).

Moreover, for measurable inputs \(0\leq f\leq1\), the largest possible **negative excursion** over this class of graphs, evaluation points, and inputs has the sharp unattained supremum
\[
\sup_{G,\,z\in G,\,0\leq f\leq1}\bigl(-(P_G f)(z)\bigr)_+
=\frac{27}{25}.
\]
The inequalities use essential-supremum norms on inputs; projection outputs are continuous. For any evaluation point \(z\), write its reproducing kernel as \(K_z\). The exact operator norm identity \(\|P_G\|=\max_{z\in G}\int_G|K_z|\,d\mu\) follows because the pointwise maximizer is the measurable sign of \(K_z\).

## Assumptions and scope

An edge \(e=uv\) is parameterized by \(x\in[0,1]\), so \(d\mu|_e=w_e\,dx\) with \(w_e=\rho_e\ell_e>0\). For each orientation define the quadratic shape functions
\[
q_0(x)=1-\frac72x+\frac52x^2,\qquad
q_1(x)=-\frac32x+\frac52x^2,\qquad
b(x)=4x(1-x).
\]
The two \(q\)-functions have the appropriate nodal endpoint values; \(b\) vanishes at both endpoints. Their nodal coefficients are globally identified at shared graph vertices, while one coefficient of \(b\) is independent on every edge. These functions span \(S_2(G)\) uniquely. Positive edge lengths and densities are arbitrary; no geometric regularity or degree bound is assumed.

## Proof

**1. Exact orthogonal decomposition and positive inverse.** Direct polynomial integration gives
\[
\int_0^1q_0^2=\int_0^1q_1^2=\frac18,\qquad
\int_0^1q_0q_1=-\frac1{24},\qquad
\int_0^1q_i b=0,\qquad
\int_0^1b^2=\frac8{15}.
\]
Let \(d_v=\sum_{e\ni v}w_e\). The nodal Gram matrix is
\[
H=\frac{3D-A}{24},
\]
where \(D=\operatorname{diag}(d_v)\) and \(A\) has entries \(w_{uv}\) on edges and zero elsewhere. All edge-bubble basis vectors are orthogonal to the nodal space and to one another. Since \(T=D^{-1}A\) is stochastic,
\[
H^{-1}=8\sum_{j=0}^{\infty}3^{-j}T^jD^{-1}.
\]
The series converges absolutely in operator norm. Connectedness implies that every entry of \(H^{-1}\) is **strictly positive** (also true for a one-edge graph). Fix a vertex \(v\) and put \(a_u=(H^{-1})_{vu}>0\). Summing \(Ha=e_v\) over all vertices and using \(\sum_u A_{uw}=d_w\) gives the exact normalization
\[
\sum_{u\in V}d_ua_u=12.
\]

**2. Sharp uniform vertex estimate.** Orthogonal reproduction shows that the evaluation kernel at vertex \(v\), on an oriented edge \(e=uw\), is
\[
K_v|_e(x)=a_uq_0(x)+a_wq_1(x).
\]
The roots of \(q_0\) are \(2/5,1\); those of \(q_1\) are \(0,3/5\). Exact antidifferentiation gives
\[
\int_0^1|q_0(x)|\,dx
=\int_0^1|q_1(x)|\,dx=\frac{79}{300}=:c.
\]
Consequently
\[
\|K_v\|_{L^1(G)}
\leq c\sum_{e=uw}w_e(a_u+a_w)
=c\sum_{u\in V}d_ua_u
=12c=\frac{79}{25}=:C.
\]
The inequality is **strict**, because \(a_u,a_w>0\) and \(q_0q_1<0\) on a set of positive length on every edge. In particular, positive nodal coupling prevents equality on any finite graph.

**3. Interior evaluation never exceeds the vertex ceiling.** Consider \(z\) at normalized coordinate \(s\in(0,1)\) on \(e=uw\). Orthogonality of bubbles yields the exact reproducing-kernel identity
\[
K_z=q_0(s)K_u+q_1(s)K_w
+\frac{b(s)}{w_e(8/15)}\,b_e,
\]
where \(b_e\) equals \(b\) on edge \(e\) and vanishes elsewhere. Since \(b\geq0\) and \(\int_0^1b=2/3\), the triangle inequality gives
\[
\|K_z\|_1
\leq C\bigl(|q_0(s)|+|q_1(s)|\bigr)+\frac54b(s)
=C\bigl(|q_0(s)|+|q_1(s)|\bigr)+5s(1-s).
\]
By reflection it suffices to take \(0<s\leq1/2\). When \(0<s\leq2/5\), the right side is \(C(1-2s)+5s(1-s)<C\), since its derivative is \(5-2C-10s<0\). When \(2/5\leq s\leq1/2\), the right side is \(5(C+1)s(1-s)-C\leq(C+5)/4=51/25<C\). Thus all interior kernels have norm strictly below \(C\). Their \(L^1\) norms depend continuously on the evaluation point. Compactness of a finite metric graph now gives \(\|P_G\|<C\). The lower bound \(\|P_G\|\geq1\) follows from \(P_G1=1\).

**4. Hypercubes prove universal sharpness.** Put unit edge masses on the \(d\)-dimensional hypercube \(Q_d\), and fix a root vertex \(o\). Let \(W\) be the transition matrix of the simple random walk on \(Q_d\) and let \(r(u)\) be the Hamming distance of \(u\) from \(o\). The symmetric regular-graph inverse formula gives
\[
a_u=(H^{-1})_{ou}=\frac8d\sum_{j=0}^{\infty}3^{-j}(W^j)_{ou}.
\]
For each edge orient from shell \(r\) to shell \(r+1\), with the farther endpoint denoted \(u^+\). Since each vertex at Hamming distance \(r\) has precisely \(r\) incoming edges, and a random walk of length \(j\) has distance at most \(j\),
\[
\sum_{e=uw}\min(a_u,a_w)
\leq\sum_e a_{u^+}
=\sum_u r(u)a_u
\leq\frac8d\sum_{j=0}^{\infty}j3^{-j}
=\frac6d.
\]
On one edge, cancellation between opposite-sign shape functions obeys the exact identity and ensuing inequality
\[
\begin{aligned}
&c(a_u+a_w)-\int_0^1|a_uq_0+a_wq_1|\,dx\\
&\quad=2\int_{q_0q_1<0}\min\bigl(a_u|q_0|,a_w|q_1|\bigr)\,dx
\leq4c\min(a_u,a_w).
\end{aligned}
\]
Summing all edges and applying the exact normalization from Step 1 therefore gives
\[
\|P_{Q_d}\|\geq\|K_o\|_1
\geq12c-4c\frac6d
=\frac{79}{25}-\frac{158}{25d}.
\]
Together with the strict universal bound, this proves sharpness and the limit. Hypercubes have no leaves once \(d\geq2\).

**5. Positivity defect.** Because \(1\in S_2(G)\), every evaluation kernel satisfies \(\int_GK_z\,d\mu=1\). For any such signed integrable kernel, the minimum of \(\int fK_z\,d\mu\) over measurable \(0\leq f\leq1\) equals its negative-part integral
\[
\int_{K_z<0}K_z\,d\mu=\frac{1-\|K_z\|_1}{2}.
\]
It is realized by \(f=\mathbf1_{\{K_z<0\}}\). Hence the largest negative excursion for a fixed graph is \((\|P_G\|-1)/2\). Combining strict finite-graph bounds with the hypercube limiting sequence establishes the stated sharp, unattained universal value \(27/25\).

## Verification

The standalone `verify.py` uses exact rational arithmetic. It reconstructs the local Gram identities, the value \(\int|q_i|=79/300\), the envelope constants, and reproducing kernels from **two independent global bases**: the orthogonal nodal/bubble decomposition and the ordinary quadratic Lagrange basis. It checks explicit graphs with nonuniform rational edge masses and hypercubes, and separately verifies finite Hamming-shell estimates. Executing `python3 verify.py` produces a pass message with the exact number of assertions. No finite experiment is used as proof of the all-graphs theorem or infinite hypercube limit; those are established in Steps 1–5.

## Relationship to prior work

Classical one-dimensional spline stability establishes uniform bounds for orthogonal projections on arbitrary interval meshes; Grigorieff and Sloan develop more general discrete spline projections. Oswald exhibits unbounded projector norms for **linear** splines on certain two-dimensional triangulations. Post develops metric-graph spectral analysis, while Arioli and Benzi study **linear finite elements** for differential equations on metric graphs. These results motivate the question but, in the material inspected, neither identify the edgewise-**quadratic** universal constant \(79/25\) nor establish its hypercube sharpness and positivity defect. The passage from intervals and simplicial two-dimensional meshes to arbitrarily branched one-dimensional metric graphs is essential: positivity of the exact nodal inverse and edge bubble orthogonality survive unrestricted graph degrees and edge weights.

## Limitations

The result assumes a finite connected simple graph, positive edge lengths, density constant on each edge, and unrestricted continuous quadratics with **no derivative matching** at vertices. It does not establish a uniform bound with nonconstant edge densities, cubics or higher degrees, derivative-matched splines, or infinite graphs. The hypercube error estimate is a valid explicit upper bound on the deficit, not an exact finite-dimensional norm or asserted optimal rate. Publication-priority assessment remains limited by the availability and indexing of older specialist spline and finite-element literature; independent audit is not claimed here.

## References

1. P. Oswald, *A counterexample concerning the \(L^2\)-projector onto linear spline spaces*, arXiv:math/0611573v1 (first public arXiv submission 2006-11-19), https://arxiv.org/abs/math/0611573 .
2. R. D. Grigorieff and I. H. Sloan, *Stability of discrete orthogonal projections for continuous splines*, Bull. Austral. Math. Soc. **58** (1998), 307–332, https://doi.org/10.1017/S0004972700032263 .
3. O. Post, *Spectral analysis of metric graphs and related spaces*, arXiv:0712.1507v1 (first public arXiv submission 2007-12-10), https://arxiv.org/abs/0712.1507 .
4. M. Arioli and M. Benzi, *A finite element method for quantum graphs*, Emory technical report TR-2015-009 (2015); later IMA J. Numer. Anal. **38** (2018), 1119–1163, https://doi.org/10.1093/imanum/drx029 .
5. M. Crouzeix and V. Thomée, *The stability in \(L^p\) and \(W^{1,p}\) of the \(L^2\)-projection onto finite element function spaces*, Math. Comp. **48** (1987), 521–532, https://doi.org/10.1090/S0025-5718-1987-0878688-2 .
