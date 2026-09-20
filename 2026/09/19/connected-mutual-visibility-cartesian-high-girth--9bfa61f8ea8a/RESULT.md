# Connected mutual-visibility in Cartesian products of high-girth graphs

## Result

Let \(G\) and \(H\) be connected finite simple graphs of order at least \(2\), with
\[
g(G)\ge 5,\qquad g(H)\ge 5,
\]
where acyclic graphs have infinite girth. Then
\[
\boxed{\mu_c(G\square H)=3.}
\]

More strongly, the maximum connected mutual-visibility sets are exactly the **Cartesian corners**
\[
\{(g,h),(g',h),(g,h')\},
\]
where \(gg'\in E(G)\) and \(hh'\in E(H)\). Consequently the number of maximum connected mutual-visibility sets is
\[
\boxed{4|E(G)|\,|E(H)|.}
\]

Thus the value is independent of the orders, diameters, degrees, and detailed shapes of the two factors once both factors have girth at least five.

## Definitions

For \(S\subseteq V(X)\), two vertices \(u,v\in S\) are \(S\)-visible if there is a \(u,v\)-geodesic whose internal vertices avoid \(S\). The set \(S\) is a connected mutual-visibility set if every two vertices of \(S\) are \(S\)-visible and \(X[S]\) is connected. Its maximum cardinality is denoted \(\mu_c(X)\).

The Cartesian product \(G\square H\) has vertex set \(V(G)\times V(H)\); vertices \((g,h)\) and \((g',h')\) are adjacent exactly when either \(g=g'\) and \(hh'\in E(H)\), or \(h=h'\) and \(gg'\in E(G)\).

## Proof

Let \(X=G\square H\), and let \(S\) be a connected mutual-visibility set in \(X\).

### 1. At most one selected neighbour in each factor direction

Fix \(x=(g,h)\in S\). Suppose that two distinct neighbours
\[
y=(g_1,h),\qquad z=(g_2,h)
\]
of \(x\) also belong to \(S\). Since \(g(G)\ge5\), the vertices \(g_1,g_2\) are non-adjacent and have no common neighbour other than \(g\): adjacency would create a triangle, and a second common neighbour would create a 4-cycle. Hence \(g_1-g-g_2\) is the unique \(g_1,g_2\)-geodesic. It follows that
\[
y-x-z
\]
is the unique \(y,z\)-geodesic in \(G\square H\). Its internal vertex \(x\) lies in \(S\), contradicting mutual visibility.

Therefore every vertex of \(X[S]\) has at most one neighbour in the \(G\)-direction. By symmetry it has at most one neighbour in the \(H\)-direction. Hence
\[
\Delta(X[S])\le2.
\]
Since \(X[S]\) is connected, it is a path or a cycle.

### 2. No connected mutual-visibility set has four or more vertices

Assume first that \(X[S]\) is a path with at least four vertices, and take four consecutive vertices
\[
v_0,v_1,v_2,v_3.
\]
At each internal vertex the two incident path edges must use different factor directions by Step 1, so the directions alternate. Up to symmetry they are \(G,H,G\). Write
\[
v_0=(g_0,h_0),\quad
v_1=(g_1,h_0),\quad
v_2=(g_1,h_1),\quad
v_3=(g_2,h_1).
\]
Because the four vertices are consecutive in an induced path, \(v_0v_3\notin E(X)\); in particular \(g_2\ne g_0\). The walk \(g_0-g_1-g_2\) is therefore a 2-path. Since \(g(G)\ge5\), it is the unique \(g_0,g_2\)-geodesic, while \(h_0h_1\) is the unique one-edge \(h_0,h_1\)-geodesic.

Hence every \(v_0,v_3\)-geodesic in the Cartesian product is obtained by shuffling those two forced \(G\)-steps with the one \(H\)-step. If the \(H\)-step is last, the geodesic passes through \(v_1\); if it is first, it passes through \(v_2\); and if it is between the two \(G\)-steps, it passes through both \(v_1\) and \(v_2\). Thus every \(v_0,v_3\)-geodesic has an internal vertex in \(S\), a contradiction.

The same four-consecutive-vertices argument excludes induced cycles of length at least five.

It remains to exclude a 4-cycle. By Step 1 its edge directions alternate, so it is a Cartesian square. Opposite vertices are at distance two, and their only two geodesics pass through the other two square vertices. Both internal vertices lie in \(S\), again contradicting mutual visibility.

Therefore
\[
|S|\le3.
\]

### 3. Existence and classification of the triples

Choose any edges \(gg'\in E(G)\) and \(hh'\in E(H)\). Then
\[
C=\{(g,h),(g',h),(g,h')\}
\]
induces a \(P_3\). Its only nonadjacent pair, \((g',h)\) and \((g,h')\), has the length-two geodesic
\[
(g',h)-(g',h')-(g,h')
\]
whose internal vertex is outside \(C\). Thus \(C\) is a connected mutual-visibility set, and so \(\mu_c(X)\ge3\). Together with Step 2 this proves
\[
\mu_c(G\square H)=3.
\]

For the structural statement, let \(S\) be any connected mutual-visibility set of size three. Since both factors are triangle-free, their Cartesian product is triangle-free, so \(X[S]\cong P_3\). If the two edges incident with its middle vertex had the same factor direction, Step 1 would be violated. Hence they use different directions, and \(S\) is exactly a Cartesian corner. The preceding construction shows every Cartesian corner works.

Finally, a corner has a unique degree-two centre. For a fixed centre \((g,h)\), there are \(d_G(g)d_H(h)\) choices, so the total number is
\[
\sum_{g\in V(G)}\sum_{h\in V(H)}d_G(g)d_H(h)
=
\left(\sum_g d_G(g)\right)\left(\sum_h d_H(h)\right)
=
4|E(G)||E(H)|.
\]
This completes the proof.

## Consequences

For all \(m,n\ge2\),
\[
\boxed{\mu_c(P_m\square P_n)=3},
\qquad
\#\{\mu_c\text{-sets}\}=4(m-1)(n-1).
\]
For \(m\ge5,n\ge2\),
\[
\mu_c(C_m\square P_n)=3,
\qquad
\#\{\mu_c\text{-sets}\}=4m(n-1),
\]
and for \(m,n\ge5\),
\[
\mu_c(C_m\square C_n)=3,
\qquad
\#\{\mu_c\text{-sets}\}=4mn.
\]

The grid case sharply separates connected mutual visibility from ordinary mutual visibility. Di Stefano proved
\[
\mu(P_m\square P_n)=2\min\{m,n\}\qquad(m,n\ge4),
\]
whereas the connected parameter is always \(3\). Hence the additive and multiplicative gaps between \(\mu\) and \(\mu_c\) are unbounded even within planar bipartite graphs.

There is also a useful extremal interpretation. Each nontrivial factor has an edge, so \(G\square H\) contains a 4-cycle. The characterization \(\mu_c(X)=2\) iff \(g(X)\ge5\) from Tonny K B and Shikhi M therefore implies that these products cannot have connected mutual-visibility number \(2\). The theorem shows that they nevertheless always attain the next possible value, \(3\), regardless of size.

## Literature context and originality

Connected mutual visibility was introduced by Tonny K B and Shikhi M in arXiv:2609.18877 (submitted 16 September 2026). Their paper defines \(\mu_c\), proves \(\mu_c(X)=2\) exactly for graphs of girth at least five, and determines the parameter for several graph classes and operations. The current version does not state a Cartesian-product formula.

Cartesian products have been studied extensively for the earlier mutual-visibility variants. Cicerone, Di Stefano, and Klavžar (arXiv:2112.13024) study ordinary mutual visibility in Cartesian products; Di Stefano's original work determines the rectangular-grid value; and Korže and Vesel (Results in Mathematics 79 (2024), 116) treat products of paths and cycles. These results concern ordinary mutual visibility, without the requirement that the selected set induce a connected subgraph.

Bujtás, Klavžar, and Tian's work on lower mutual visibility also notes that a three-vertex corner is a maximal ordinary mutual-visibility set in a rectangular grid. That is a different extremal parameter: it minimizes the size of a maximal ordinary mutual-visibility set and does not bound the maximum size of a connected mutual-visibility set.

No source located under connected-mutual-visibility, Cartesian-product, grid, and product-graph formulations states the theorem above or the classification/count of maximum sets. Originality is therefore claimed only **to the best of our knowledge**. Because connected mutual visibility is a newly introduced invariant, very recent parallel or not-yet-indexed work is the principal residual originality risk.

## Verification

A standalone definition-level verifier is included in `artifacts/verify_connected_mv_products.py`. Using NetworkX 3.6.1, it takes all connected graph-atlas factor types of orders \(2\) through \(5\) with girth at least five, checks every unordered pair of factor types, enumerates every three-vertex subset of the product, and confirms that the connected mutual-visibility triples are exactly the predicted Cartesian corners. It also enumerates every four-vertex subset and confirms that none is a connected mutual-visibility set. The test covers 8 factor types, 36 unordered products, and product order up to 25.

The finite computation is supporting evidence only; the general result follows from the proof above.

## Limitations

The girth assumptions are essential to the proof and are not claimed to be necessary for the conclusion. Products in which one factor contains triangles or 4-cycles are not classified here. The theorem concerns products of exactly two factors; higher Cartesian powers can behave differently. The originality assessment is necessarily provisional because the connected parameter was introduced only very recently. Independent audit and independent validation have not been performed.

## References

1. Tonny K B and Shikhi M, *Connected Mutual-Visibility in Graphs*, arXiv:2609.18877 (2026). https://arxiv.org/abs/2609.18877
2. S. Cicerone, G. Di Stefano, and S. Klavžar, *On the mutual visibility in Cartesian products and triangle-free graphs*, arXiv:2112.13024 (2021/2022). https://arxiv.org/abs/2112.13024
3. G. Di Stefano, *Mutual visibility in graphs*, Applied Mathematics and Computation 419 (2022), 126850. https://doi.org/10.1016/j.amc.2021.126850
4. D. Korže and A. Vesel, *Mutual-Visibility Sets in Cartesian Products of Paths and Cycles*, Results in Mathematics 79 (2024), 116. https://doi.org/10.1007/s00025-024-02139-x
5. C. Bujtás, S. Klavžar, and J. Tian, *Lower (total) mutual-visibility number in graphs*, Applied Mathematics and Computation 465 (2024), 128411. https://doi.org/10.1016/j.amc.2023.128411
