# A local all-step RK4 positivity law for every unweighted bipartite network

## Finding

Let \(G=(V,E)\) be any finite connected simple unweighted bipartite graph with at least two vertices. Let \(A\) be its adjacency matrix, \(d_v\) the degree of vertex \(v\), and \(L=\operatorname{diag}(d_v)-A\). Classical fourth-order Runge–Kutta applied to graph heat diffusion has completed step
\[
T(h)=I-hL+\frac{h^2L^2}{2}-\frac{h^3L^3}{6}+\frac{h^4L^4}{24},\qquad h\ge0.
\]
For an edge \(e=uv\), put \(s_e=d_u+d_v\) and define
\[
\begin{aligned}
p_e&=d_u^2+d_ud_v+d_v^2+(A^3)_{uv},\\
q_e&=d_u^3+d_u^2d_v+d_ud_v^2+d_v^3
  +\sum_{(u,x,y,v)\in\mathcal W_3(u,v)}(d_u+d_x+d_y+d_v),\\
g_e(h)&=1-\frac{s_eh}{2}+\frac{p_eh^2}{6}-\frac{q_eh^3}{24},
\end{aligned}
\]
where \(\mathcal W_3(u,v)\) comprises all *directed walks of exactly three edges* from \(u\) to \(v\), including walks that revisit vertices. The cubic \(g_e\) is strictly decreasing on \([0,\infty)\) and has one positive simple root \(\theta_e\).

For every unordered pair \(u,v\) of graph distance three, put
\[
N_{uv}=|\mathcal W_3(u,v)|=(A^3)_{uv},\qquad
W_{uv}=\sum_{(u,x,y,v)\in\mathcal W_3(u,v)}(d_u+d_x+d_y+d_v),
\]
and \(\eta_{uv}=4N_{uv}/W_{uv}\). Take the minimum over an empty collection of distance-three pairs to be \(+\infty\). Then the **exact global criterion, with no later recovery**, is
\[
\boxed{T(h)\ge0\text{ entrywise}\quad\Longleftrightarrow\quad
0\le h\le h_*(G):=\min\left\{\min_{e\in E}\theta_e,\ \min_{\operatorname{dist}(u,v)=3}\eta_{uv}\right\}.}
\]
For every \(h>0\), diagonal entries and entries between vertices at distance two or four are strictly positive, and entries at distance five or more are identically zero. Only edge entries and distance-three entries can become negative; each such entry has one permanent sign change. Because \(L\mathbf1=0\), the nonnegative updates are also stochastic.

The two kinds of obstructions are genuinely independent. On the six-vertex path \(P_6\), the sharp value is \(h_*=1/2\), determined by a distance-three pair; every edge remains positive at that value. On the seven-vertex double star whose two centers have degrees three and four, the central edge has
\[
g(h)=1-\frac72h+\frac{43}{6}h^2-\frac{247}{24}h^3,
\qquad g(4/9)=-95/2187<0,
\]
while every distance-three pair has threshold \(4/9\). Thus its sharp threshold is the unique root of this edge cubic, strictly less than \(4/9\) (approximately \(0.4306090574\)).

## Assumptions and scope

The graph is finite, connected, simple, undirected, unweighted and bipartite. The claim concerns entrywise positivity of the *completed* classical RK4 step for the fixed linear autonomous system \(z'=-Lz\), not positivity of intermediate RK stages, a nonlinear SSP guarantee, or a spectral-stability condition. Vertices may have arbitrarily unequal degrees, and squares and longer even cycles are allowed. All degree sums and walk counts refer to this graph. We impose no bound on vertex number or degree beyond finiteness and connectedness.

## Proof

**1. Bipartite sign switching and four-step locality.** Let \(S\) be diagonal with entries \(+1\) and \(-1\) on the two bipartition classes. Define the signless Laplacian \(B=\operatorname{diag}(d_v)+A\). Then \(L=SBS\), so \((L^j)_{uv}=\sigma_u\sigma_v(B^j)_{uv}\). Powers of \(B\) count walks that may stay at a vertex, with weight \(d_v\) for each stay; each actual traversal of an edge has weight one. This gives the following exact entry formulas by the parity and minimum number of actual edge traversals.

For \(\operatorname{dist}(u,v)=1\), expansion of the one-edge traversals and three-edge traversals gives
\[
T(h)_{uv}=h\left(1-\frac{s_eh}{2}+\frac{p_eh^2}{6}-\frac{q_eh^3}{24}\right)=h g_e(h).
\]
For \(\operatorname{dist}(u,v)=3\), only three-edge traversals contribute through order four, giving
\[
T(h)_{uv}=\frac{h^3}{24}\bigl(4N_{uv}-hW_{uv}\bigr).
\]
For \(\operatorname{dist}(u,v)=4\), only four-edge traversals contribute, giving \(T(h)_{uv}=h^4(A^4)_{uv}/24>0\). For distance at least five, every off-diagonal coefficient is zero.

**2. Distance-two entries never fail positivity.** For distance-two vertices \(u,v\), write \(\mathcal W_2(u,v)=\{(u,w,v):u\sim w\sim v\}\), and for one such walk set \(s=d_u+d_w+d_v\), \(H_2=d_u^2+d_w^2+d_v^2+d_ud_w+d_ud_v+d_wd_v\). Enumerating the ways to insert stays into a two-edge walk gives
\[
T(h)_{uv}=\frac{h^2}{24}\left[\sum_{(u,w,v)\in\mathcal W_2(u,v)}(12-4sh+H_2h^2)+h^2(A^4)_{uv}\right].
\]
The identity \(2H_2=s^2+d_u^2+d_w^2+d_v^2\) and Cauchy–Schwarz imply \(H_2\ge 2s^2/3\). Consequently \(12-4sh+H_2h^2\) has discriminant at most \(-16s^2<0\) and positive leading coefficient; it is strictly positive for every real \(h\). At least one two-edge walk exists, and \((A^4)_{uv}\ge0\), proving the claim.

**3. Every edge polynomial decreases globally.** Let \(a=d_u\), \(b=d_v\), \(s=a+b\), and \(N=(A^3)_{uv}\). Choosing the first and last interior neighbors of a three-step walk yields the elementary bound \(0\le N\le ab\). Therefore
\[
p_e=a^2+ab+b^2+N=s^2-ab+N\le s^2.
\]
Every summand added to \(a^3+a^2b+ab^2+b^3\) in \(q_e\) is nonnegative, so
\[
q_e\ge a^3+a^2b+ab^2+b^3=s(s^2-2ab)\ge s^3/2.
\]
The derivative is \(g_e'(h)=-s/2+(p_e/3)h-(q_e/8)h^2\). Its discriminant is
\[
\frac{p_e^2}{9}-\frac{s q_e}{4}\le
\frac{s^4}{9}-\frac{s^4}{8}=-\frac{s^4}{72}<0.
\]
The quadratic has negative leading coefficient and is negative at zero; hence \(g_e'(h)<0\) for all real \(h\). Since \(g_e(0)=1\) and \(g_e(h)\to-\infty\), exactly one positive simple root exists, with permanent negativity afterward.

**4. Diagonal positivity.** The scalar RK4 stability polynomial \(R_4(x)=\sum_{j=0}^4(-x)^j/j!\) satisfies
\[
R_4(x)=e^{-x}+\frac1{24}\int_0^x e^{-(x-t)}t^4\,dt>0\qquad (x\ge0).
\]
As \(L\) is real symmetric positive semidefinite, \(T(h)=R_4(hL)\) is positive definite for every finite \(h\ge0\). In particular, every diagonal entry is positive.

**5. Sharpness and no recovery.** By the preceding steps, all entries are nonnegative precisely while all edge cubics \(g_e(h)\ge0\) and all distance-three linear factors \(4N_{uv}-hW_{uv}\ge0\). Every edge cubic and every distance-three linear factor has a single strict transition from positive to negative. Their finite minimum is the claimed sharp threshold. At and below it every entry is nonnegative, and at every strictly larger \(h\) at least one of the same entries stays negative. This proves both directions and the no-recovery assertion.

## Verification

Run `python3 verify.py` with Python 3 and no third-party dependencies. It enumerates all connected labelled simple bipartite graphs with 2 through 6 vertices (3,249 graphs), checks their exact integer walk identities and 18,537 edge derivative-discriminant inequalities, and checks the entrywise positivity equivalence at six rational timesteps per graph using exact rational RK4 matrices. It also verifies a seven-vertex double-star witness including \(g(4/9)=-95/2187\). The script prints `VERIFY_OK` on success. These finite checks do not substitute for the all-graph proof above.

For \(P_6\), the four consecutive degree-two vertices force a distance-three cutoff \(4/8=1/2\); all other distance-three degree sums are at most eight, and all edge cubics are positive at \(1/2\), proving the stated sharp value. For the double star, all distance-three paths consist of a leaf, two centers of degrees three and four, and another leaf, so their degree sum is nine. The central-edge cubic is strictly negative at \(4/9\), whereas the five other pendant edges attached to the two centers have, respectively, \(g(4/9)=859/2187\) (two edges) and \(g(4/9)=541/2187\) (three edges); thus their roots are larger than \(4/9\). Its unique root is therefore the global threshold.

## Relationship to prior work

Gottlieb–Shu–Tadmor (2001) develops SSP guarantees based on decomposition into forward-Euler steps; these are method-level guarantees and do not provide the exact positivity horizon of a fixed irregular graph's completed RK4 matrix. Horváth–Song–Terlaky (first public preprint 2014, Theorems 3.3–3.4 and Section 3.3.1) gives general Taylor-polynomial invariance threshold machinery through polynomial zero tests; it does not classify the unweighted bipartite graph entry types, prove the all-step single-crossing property, or reduce the entire problem to edges and distance-three walks. General first-zero testing is compatible with, but does not logically establish, the no-recovery theorem here.

The formula specializes to existing narrower regular-bipartite RK4 classifications: a noncomplete connected regular bipartite graph has a distance-three constraint at \(h=1/d\), whereas the complete balanced bipartite case has no such pair. Special-case agreement is not claimed as an additional discovery. The generalization to arbitrary unequal degrees, including the independent edge- and distance-three-controlled examples, is the substantive structural statement.

## Limitations

The proof does not cover weighted or directed graphs, nonbipartite graphs, alternative Runge–Kutta stability polynomials, or positivity of internal stages. It does not prove novelty against every unpublished or unindexed source, and independent mathematical validation remains unperformed. A standard general polynomial root-finding method can numerically calculate a first positivity loss for a specified matrix; the present theorem instead identifies all entries that matter and proves no recovery over an infinite graph class.

## References

1. S. Gottlieb, C.-W. Shu and E. Tadmor, *Strong Stability-Preserving High-Order Time Discretization Methods*, SIAM Review 43 (2001), 89–112. DOI: https://doi.org/10.1137/S003614450036757X. Author-hosted PDF: https://www.math.umd.edu/~tadmor/pub/linear-stability/Gottlieb-Shu-Tadmor.SIREV-01.pdf.
2. Z. Horváth, Y. Song and T. Terlaky, *Steplength Thresholds for Invariance Preserving of Discretization Methods of Dynamical Systems on a Polyhedron*, arXiv:1406.6755, first submitted 2014-06-26. https://arxiv.org/abs/1406.6755; https://arxiv.org/pdf/1406.6755.
