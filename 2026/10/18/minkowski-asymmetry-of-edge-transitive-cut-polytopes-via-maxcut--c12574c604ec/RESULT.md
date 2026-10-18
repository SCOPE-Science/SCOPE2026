# Minkowski asymmetry of edge-transitive cut polytopes via MaxCut

## Finding

Let \(G=(V,E)\) be a finite simple undirected graph with at least one edge; isolated vertices are permitted. Suppose its automorphism group is transitive on its edge set. Set \(m=|E|\), and let
\[
P_G=\operatorname{conv}\{\chi_{\delta(S)}:S\subseteq V\}\subset\mathbb R^E,\qquad
M=\max_{S\subseteq V}|\delta(S)|.
\]
For a full-dimensional convex body \(P\), its Minkowski asymmetry is
\[
s(P)=\min_{c\in\mathbb R^{\dim P}}\inf\{s\ge1:-(P-c)\subseteq s(P-c)\}.
\]
Then \(M>m/2\),
\[
\boxed{s(P_G)=\frac{m}{2M-m}},\qquad
\boxed{c_*=\tfrac12\mathbf1_E},
\]
and \(c_*\) is the **unique** minimizing Minkowski center.

For every integer \(r\ge2\), every integer \(a\ge1\), and the complete \(r\)-partite graph with \(r\) equal parts of size \(a\),
\[
\boxed{s(P_{K_{a,\ldots,a}})=
\begin{cases}r-1,&r\text{ even},\\r,&r\text{ odd}.
\end{cases}}
\]
Thus asymmetry is invariant under equal-size vertex blowup in this family, though the ambient dimension grows quadratically with \(a\). In particular, this gives \(r-1\) for even complete graphs \(K_r\) and \(r\) for odd ones.

## Assumptions and scope

Graphs are simple and finite; disconnected edge-transitive graphs and isolated vertices are allowed. All cut vectors use ordinary nonnegative \(0/1\) coordinates, not signed roots or correlation coordinates. The convex body is the *whole* cut polytope in the Euclidean edge-coordinate space; the Minkowski asymmetry is affine-invariant and does not depend on a Euclidean norm. Transitivity is on edges, not necessarily vertices. The formula does not claim to hold for arbitrary non-edge-transitive or weighted graphs.

## Proof

**Full dimensionality.** The empty cut gives the zero vector. For each edge \(uv\in E\), the identity
\[
2\mathbf e_{uv}=\chi_{\delta(\{u\})}+\chi_{\delta(\{v\})}-\chi_{\delta(\{u,v\})}
\]
holds coordinatewise, so the cut vectors span \(\mathbb R^E\). The average over all vertex sign assignments is \(h=\tfrac12\mathbf1_E\); as an average with positive weights of all cut vectors, \(h\) is interior.

**Switching and optimal center.** For a cut vector \(d\in\{0,1\}^E\), let \(T_d\) be the affine involution
\[
(T_d x)_e=d_e+(1-2d_e)x_e.
\]
Since cut vectors add by symmetric difference modulo two, \(T_d(P_G)=P_G\). If \(c\) is a feasible center for dilation \(s\), then so is \(T_d(c)\): affine transformations commute with homotheties about their transformed centers. The feasible-center set is convex, since its conditions are \((s+1)c-x\in sP_G\) for every \(x\in P_G\). Averaging \(T_d(c)\) over the vertex-sign switching group produces \(h\), since every edge coordinate is complemented in half the group elements. Hence \(h\) minimizes asymmetry.

**Exact radial threshold.** At \(c=h\), the image of the reflected cut vertex \(d\) under \(T_d\) is the constant vector \(t\mathbf1_E\), where \(t=(s+1)/(2s)\). Thus
\[
-(P_G-h)\subseteq s(P_G-h)
\quad\Longleftrightarrow\quad t\mathbf1_E\in P_G.
\]
Let \(t_*\) be the largest scalar for which \(t_*\mathbf1_E\in P_G\). The linear inequality \(\sum_{e\in E}x_e\le M\) valid for \(P_G\) yields \(t_*\le M/m\). Choose a maximum cut and average its incidence vector over the graph automorphism group. Edge transitivity forces every coordinate to equal \(M/m\), proving equality \(t_*=M/m\). To see \(M>m/2\), choose a random vertex bipartition with the two sides as balanced as possible; each fixed edge crosses with probability greater than \(1/2\) when \(|V|\ge2\). Consequently a cut strictly exceeds half the edges. Rearranging \(t_*=(s+1)/(2s)\) gives \(s=m/(2M-m)\).

**Unique center.** Write any other minimizing center as \(c=h+z\), and put \(s=m/(2M-m)\). For each cut vector \(d\), the reflected point \(y_d=((s+1)c-d)/s\) lies in \(P_G\). Switching gives
\[
T_d(y_d)=\frac Mm\mathbf1_E+\frac{s+1}{s}\big((1-2d_e)z_e\big)_{e\in E}.
\]
Apply the maximum-cut inequality to obtain
\[
\sum_{uv\in E}\sigma_u\sigma_v z_{uv}\le0
\quad\text{for all }\sigma\in\{-1,1\}^{V},
\]
where \(d_{uv}=(1-\sigma_u\sigma_v)/2\). Its expectation over independent uniform vertex signs is zero, hence every inequality is equality. Multiplying the equality by \(\sigma_u\sigma_v\) and averaging, the pairwise-orthogonality of distinct edge characters \(\sigma_u\sigma_v\) implies \(z_{uv}=0\). Thus \(c=h\) uniquely.

**Balanced complete multipartite graphs.** For \(K_{a,\ldots,a}\) with \(r\) parts, write \(x_i\in\{0,\ldots,a\}\) for the number of vertices of part \(i\) assigned to the first shore. A cut contains
\[
F(x_1,\ldots,x_r)=\sum_{i<j}\big(a(x_i+x_j)-2x_ix_j\big)
\]
edges. This is affine in each coordinate separately. From any maximizing assignment, choose for each part a maximizing endpoint \(x_i\in\{0,a\}\), preserving optimality. Thus some maximum cut assigns every part monochromatically. If \(k\) whole parts lie on one side, its size is \(a^2k(r-k)\). Therefore
\[
M=a^2\left\lfloor r^2/4\right\rfloor,
\quad m=a^2\binom r2.
\]
Substitution gives \(s=r-1\) for even \(r\), and \(s=r\) for odd \(r\), independent of \(a\), with the unique center as above.

The proof also supplies a constructive polyhedral certificate: \((M/m)\mathbf1_E\) is the average of automorphic images of any maximum cut, and switching this average by each cut produces every reflected cut vertex at the optimal dilation.

## Verification

The accompanying standalone `verify.py` uses only the Python standard library and exact integer/rational arithmetic. Run `python verify.py`. It enumerates all edge-transitive labeled simple graphs on two through five vertices, checks every max-cut automorphism average and switching identity, and checks the closed balanced multipartite expression for \(2\le r\le11\), \(1\le a\le6\). Where the total vertex count is at most twelve, it also exhaustively computes the maximum cut for that multipartite graph. The observed check totals are 174 graphs, 1,508 automorphism actions, 2,422 cut switches, and 60 multipartite parameter pairs. The infinite statements, center uniqueness and dimension independence are proved above, not inferred from enumeration.

## Relationship to prior work

Nikolaev, *On 1-skeleton of the cut polytopes* (arXiv:2402.13591v1, first posted 2024-02-21), analyzes graph diameter and clique number of cut-polytope skeletons, including complete multipartite graphs. These are combinatorial graph distances, not affine reflection asymmetry. Deza and Dutour Sikirić, *Enumeration of the facets of cut polytopes over some highly symmetric graphs* (arXiv:1501.05407v6), determine facet orbits of specified highly symmetric graphs and explicitly describe switching symmetries. Their treatment provides group-structure background, not the stated Minkowski optimal-center or MaxCut-ratio theorem. Chimani, Juhnke-Kubitzke, Nover and Römer, *Cut Polytopes of Minor-free Graphs* (arXiv:1903.01817v1), study facets and simplicity/simpliciality in minor-restricted classes. Barahona and Mahjoub, *On the Cut Polytope* (1986), develop the classical cut-polytope framework and facet/switching methods. The result here uses familiar switching and averaging facts to determine a different affine-invariant quantity.

An odd-girth formula for \(K_5\)-minor-free cut polytopes does not imply this classification beyond that class: already \(K_5\) has asymmetry \(5\), whereas every nonbipartite graph in the minor-free classification with a triangle has asymmetry \(3\). The hypotheses are materially different; no implication is inferred across them.

## Limitations

The universal formula assumes edge transitivity, and the explicit parity law assumes equal part sizes. MaxCut may be hard to evaluate on other edge-transitive graph families, so the ratio does not universally provide a polynomial-time numerical evaluation. The result concerns the usual cut polytope, not a weighted variant, a projected cut polytope, or a one-skeleton graph diameter. Literature searches and examination of the specified primary works do not establish universal publication priority; an earlier equivalent statement under coefficient-of-symmetry or orbit-averaging terminology remains possible. No independent audit has been conducted.

## References

1. A. V. Nikolaev, *On 1-skeleton of the cut polytopes*, arXiv:2402.13591v1 (2024), https://arxiv.org/html/2402.13591v1 .
2. M. Deza and M. Dutour Sikirić, *Enumeration of the facets of cut polytopes over some highly symmetric graphs*, arXiv:1501.05407v6 (2015), https://arxiv.org/html/1501.05407v6 .
3. M. Chimani, M. Juhnke-Kubitzke, A. Nover and T. Römer, *Cut Polytopes of Minor-free Graphs*, arXiv:1903.01817v1 (2019), https://arxiv.org/html/1903.01817v1 .
4. F. Barahona and A. R. Mahjoub, *On the cut polytope*, Mathematical Programming 36 (1986), 157–173, https://www.lamsade.dauphine.fr/~mahjoub/Papers/BM86.pdf .
