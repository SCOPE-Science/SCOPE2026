# Euclidean inradius of weighted graphical zonotopes is a cut expansion constant
## Finding
Let \(G=(V,E)\) be a finite connected simple graph with \(n=|V|\ge 2\), and assign a positive weight \(w_e\) to each edge. Define the weighted graphical zonotope
\[
Z_{G,w}=\sum_{\{i,j\}\in E}[w_{ij}e_i,w_{ij}e_j]\subset\mathbb R^V.
\]
For a nonempty proper set \(S\subset V\), write \(w(\partial S)\) for the total weight of edges with exactly one endpoint in \(S\). Then, in the affine hull of \(Z_{G,w}\) with its induced Euclidean metric,
\[
 r(Z_{G,w})=\frac12\min_{\varnothing\ne S\subsetneq V}
 w(\partial S)\sqrt{\frac{n}{|S|(n-|S|)}}.
\]
The point
\[
 c=\frac12\sum_{\{i,j\}\in E}w_{ij}(e_i+e_j)
\]
is a Chebyshev center. Thus the Euclidean thickness of this canonical zonotope is exactly a centered-cardinality \(L^2\) cut-expansion constant of the graph.

## Assumptions and scope
The graph is finite, simple, connected, and has at least two vertices; all edge weights are strictly positive. Connectivity makes the translated zonotope full-dimensional in the zero-sum subspace
\[
 H=\left\{u\in\mathbb R^V:\sum_{i\in V}u_i=0\right\}.
\]
All radii are intrinsic to this affine hull. For \(S\subset V\), set
\[
 v_S=\mathbf 1_S-\frac{|S|}n\mathbf 1,
 \qquad
 \|v_S\|_2=\sqrt{\frac{|S|(n-|S|)}n}.
\]
No assertion is made here for disconnected graphs, zero-weight edges that disconnect the support graph, other norms, circumradii, or John ellipsoids.

## Proof
Translate by the symmetry center and write
\[
 K=Z_{G,w}-c
 =\sum_{\{i,j\}\in E}
 \left[-\frac{w_{ij}}2(e_i-e_j),\frac{w_{ij}}2(e_i-e_j)\right]\subset H.
\]
The body \(K\) is centrally symmetric. If a Euclidean ball \(a+rB_H\) lies in \(K\), then so does \(-a+rB_H\); convexity and midpoint averaging imply \(rB_H\subset K\). Hence an optimal ball may be centered at the origin.

For \(u\in H\), the support function of the centered zonotope is
\[
 h_K(u)=\frac12\sum_{\{i,j\}\in E}w_{ij}|u_i-u_j|.
\]
Therefore
\[
 r(K)=\frac12\inf_{u\in H\setminus\{0\}}
 \frac{\sum_{\{i,j\}\in E}w_{ij}|u_i-u_j|}{\|u\|_2}.
\]
It remains to evaluate this finite-graph total-variation quotient.

Fix nonzero \(u\in H\), put \(m=\min_i u_i\), \(M=\max_i u_i\), and for \(t\in(m,M)\) set \(S_t=\{i:u_i>t\}\). Since \(u\) has mean zero, the layer-cake identity gives
\[
 u=\int_m^M\left(\mathbf1_{S_t}-\frac{|S_t|}n\mathbf1\right)dt.
\]
The discrete coarea identity gives
\[
 \sum_{\{i,j\}\in E}w_{ij}|u_i-u_j|
 =\int_m^M w(\partial S_t)\,dt.
\]
Define
\[
 \Phi_2(G,w)=\min_{\varnothing\ne S\subsetneq V}
 \frac{w(\partial S)}{\|v_S\|_2}.
\]
Then \(w(\partial S_t)\ge\Phi_2(G,w)\|v_{S_t}\|_2\) for every nontrivial level set. The triangle inequality applied to the layer-cake integral yields
\[
 \|u\|_2\le\int_m^M\|v_{S_t}\|_2\,dt,
\]
and hence
\[
 \sum_{\{i,j\}\in E}w_{ij}|u_i-u_j|
 \ge\Phi_2(G,w)\|u\|_2.
\]
Conversely, for every nontrivial \(S\), the centered cut vector \(v_S\) satisfies
\[
 \sum_{\{i,j\}\in E}w_{ij}|(v_S)_i-(v_S)_j|=w(\partial S).
\]
Choosing a minimizing cut therefore attains the lower bound. Thus the quotient infimum is exactly \(\Phi_2(G,w)\), and substituting \(\|v_S\|_2=\sqrt{|S|(n-|S|)/n}\) proves the formula.

Two checks illustrate the normalization. For the unweighted complete graph \(K_n\),
\[
 r(Z_{K_n})=\frac12\sqrt{n(n-1)}.
\]
For the unweighted path \(P_n\), a central one-edge cut gives
\[
 r(Z_{P_n})=\frac12\sqrt{\frac{n}{\lfloor n^2/4\rfloor}}.
\]

## Verification
The proof above is analytic and valid for every finite connected weighted graph under the stated assumptions. The accompanying `verify.py` is a corroborative exact-arithmetic check, not a substitute for the proof. It enumerates every connected labeled simple graph on \(2\) through \(5\) vertices, tests two positive integer weightings of every graph, checks all nontrivial cuts, and checks the variational lower bound on every nonzero mean-zero vector in \(\{-1,0,1\}^n\). Its replay output is:

`VERIFY_OK graphical-zonotope-inradius connected_graphs=771 weightings=1542 cut_checks=44796 vector_checks=74220 n=2..5`

## Relationship to prior work
Padrol, Pilaud, and Poullot define the graphical zonotope as the Minkowski sum of the edge segments \([e_u,e_v]\) and study its deformation cone; their published classification lists MSC 52B11 first. The inspected full text contains no inradius or Cheeger statement. Xu studies graphical zonotopes through face-vector invariance, again with a combinatorial rather than metric objective.

The coarea mechanism itself is classical in Cheeger and total-variation theory. Mazón's treatment of weighted graph Cheeger cuts uses the standard cut denominator based on vertex volume and an \(L^1\)-median normalization. That result does not imply the centered-cardinality \(L^2\) quotient above and does not identify a graphical-zonotope inradius. The new content claimed here is the exact Euclidean-inradius identification, including arbitrary positive edge weights, rather than novelty of the coarea method.

## Limitations
The theorem does not characterize every Chebyshev center when the center is nonunique; it only proves that the symmetry center is one. It is specific to the standard Euclidean realization and intrinsic affine-hull metric. The literature search did not reveal a prior statement of this exact polytope-metric identity, but differently named finite-graph Sobolev constants are a residual originality risk; no claim is made that the underlying total-variation inequality is new in isolation.

## References
1. A. Padrol, V. Pilaud, G. Poullot, *Deformed Graphical Zonotopes*, arXiv:2111.12422, first posted 2021-11-24; Discrete & Computational Geometry 73 (2025), 447–465, DOI 10.1007/s00454-023-00586-x.
2. Z. Xu, *Graphical zonotopes with the same face vector*, arXiv:1809.08764, first posted 2018-09-24.
3. J. M. Mazón, *The Cheeger Cut and Cheeger Problem in Metric Graphs*, arXiv:2203.07760; Analysis and Mathematical Physics 12 (2022), Article 117, DOI 10.1007/s13324-022-00729-y.
