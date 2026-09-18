# Phylogenetic rank of complete multipartite graphs

## Statement

Let
\[
G=K_{n_1,\ldots,n_r},\qquad r\ge 2,\quad n_i\ge 1,
\]
be a connected complete multipartite graph. Let
\[
q=\bigl|\{i:n_i\ge 2\}\bigr|,\qquad
s=\bigl|\{i:n_i=1\}\bigr|.
\]
Then the Pachter--Sturmfels phylogenetic rank of the graph metric of \(G\) is
\[
\boxed{
r_{\mathrm{phy}}(G)=q+\mathbf 1_{\{s\ge2\}}.
}
\]

Equivalently, in the complement \(\overline G\), count the clique components of size at least two, and add one exactly when there are at least two isolated vertices.

Thus, within complete multipartite graphs, the phylogenetic rank depends only on which parts are singletons and which are non-singletons; the actual sizes of the non-singleton parts do not affect the rank.

A direct corollary is the complete classification, within this family, of graphs of phylogenetic rank at most \(k\):
\[
r_{\mathrm{phy}}(G)\le k
\quad\Longleftrightarrow\quad
q+\mathbf 1_{\{s\ge2\}}\le k.
\]

## Definitions

The graph metric gives every edge length \(1\). The phylogenetic rank \(r_{\mathrm{phy}}(G)\) is the least \(k\) such that there are metric trees
\[
\Gamma_1,\ldots,\Gamma_k
\]
and an isometric embedding
\[
\iota:G\longrightarrow \Gamma_1\times\cdots\times\Gamma_k,
\]
where the product is equipped with the supremum metric. Consequently, every coordinate map is \(1\)-Lipschitz.

## Proof

### Upper bound

Write the non-singleton parts as \(P_1,\ldots,P_q\).

For each \(i\in[q]\), let \(\Gamma_i\) be a metric star with center \(c_i\), one leaf \(\ell_v\) for each \(v\in P_i\), and every spoke of length \(1\). Define
\[
\phi_i(v)=
\begin{cases}
\ell_v,&v\in P_i,\\
c_i,&v\notin P_i.
\end{cases}
\]
Then the coordinate distance \(d_i\) satisfies:
\[
d_i(u,v)=
\begin{cases}
2,&u,v\in P_i,\ u\ne v,\\
1,&|\{u,v\}\cap P_i|=1,\\
0,&u,v\notin P_i.
\end{cases}
\]
Hence \(d_i\le d_G\) for every pair, and the distance \(2\) between two vertices in \(P_i\) is realized exactly in coordinate \(i\).

If \(s\le1\), the product of these \(q\) coordinates already realizes every distance in \(G\): vertices in the same non-singleton part have distance \(2\), and every pair in distinct parts has distance \(1\).

Now suppose \(s\ge2\). Add one more star \(\Gamma_0\) with center \(c_0\), one leaf for each singleton-part vertex, and every spoke of length \(1/2\). Map every singleton vertex to its own leaf and every non-singleton vertex to \(c_0\). This coordinate realizes distance \(1\) between every two singleton vertices, while all its distances are at most the corresponding graph distances. Together with the \(q\) coordinates above, every graph distance is realized.

If \(q=0\), then \(G=K_s\) and this single half-unit star is itself an isometric realization of the graph metric.

Therefore
\[
r_{\mathrm{phy}}(G)\le q+\mathbf 1_{\{s\ge2\}}.
\]

### Lower bound: one coordinate per non-singleton part

For each non-singleton part \(P_i\), choose distinct vertices
\[
a_i,b_i\in P_i.
\]
Then
\[
d_G(a_i,b_i)=2.
\]
In any isometric embedding into a supremum product, at least one coordinate tree must realize this distance exactly.

No coordinate can realize the distance \(2\) for selected pairs from two different parts. Indeed, suppose a tree coordinate realizes
\[
d(a_i,b_i)=d(a_j,b_j)=2,\qquad i\ne j.
\]
Every cross pair lies in different multipartite parts, so its graph distance is \(1\); since a coordinate map is \(1\)-Lipschitz, all four cross distances in that tree are at most \(1\). The three four-point sums therefore have one value
\[
d(a_i,b_i)+d(a_j,b_j)=4
\]
and two values at most \(2\). This violates the four-point condition for a tree metric, according to which the maximum of the three sums is attained at least twice.

Hence the \(q\) chosen within-part pairs require \(q\) distinct coordinates:
\[
r_{\mathrm{phy}}(G)\ge q.
\]

### Why two singleton parts force one more coordinate

Assume \(s\ge2\). If \(q=0\), then \(G\) has at least two vertices and has positive distances, so its rank is at least \(1\), giving the desired lower bound.

Suppose \(q\ge1\), and assume for contradiction that a rank-\(q\) embedding exists. By the previous argument, each of its \(q\) coordinates must be assigned to a different selected pair \(a_i,b_i\) and must realize that pair at distance \(2\).

Fix the coordinate that realizes \(d(a_i,b_i)=2\), and let \(x\notin P_i\). In \(G\),
\[
d_G(x,a_i)=d_G(x,b_i)=1.
\]
Thus in this coordinate tree,
\[
d(x,a_i)\le1,\qquad d(x,b_i)\le1.
\]
Since \(d(a_i,b_i)=2\), the triangle inequality is tight, and the unique point lying within distance \(1\) of both endpoints is the midpoint of the geodesic from \(a_i\) to \(b_i\). Consequently every vertex outside \(P_i\) maps to that same midpoint in this coordinate.

Take two distinct singleton-part vertices \(x,y\). They lie outside every non-singleton part, so in every one of the \(q\) coordinates their images coincide. Their product distance would therefore be \(0\), contradicting
\[
d_G(x,y)=1.
\]
Thus
\[
r_{\mathrm{phy}}(G)\ge q+1
\]
when \(s\ge2\). Together with the upper bound, this proves the formula.

## Consequences and relation to known examples

The formula simultaneously recovers several examples that are treated separately in the recent graph-phylogenetic-rank literature:

- \(K_n\) has \(q=0\) and \(s=n\), hence rank \(1\).
- A star \(K_{m,1}\) has \(q=1,s=1\), hence rank \(1\).
- \(K_{m,n}\) with \(m,n\ge2\) has \(q=2,s=0\), hence rank \(2\), matching Proposition 3.5 of Ashworth--Clarke--Giansiracusa--Jones--Quijas-Aceves--Ren.
- \(K_4-e=K_{2,1,1}\) has rank \(2\), matching their Example 3.6.
- The cocktail-party graph \(K_{2,2,\ldots,2}\), equivalently a complete graph minus a perfect matching, has rank \(n/2\), matching Theorem 3.3(2) of the same paper.

The theorem also gives arbitrarily large phylogenetic rank inside a very structured diameter-two perfect graph family. In particular, it gives a complete answer to the rank-\(\le k\) classification problem inside complete multipartite graphs, a natural special case of Question 7.3 in the recent paper.

For an \(n\)-vertex complete multipartite graph,
\[
r_{\mathrm{phy}}(G)\le \left\lfloor\frac n2\right\rfloor.
\]
This follows immediately because every non-singleton part consumes at least two vertices, while the singleton correction can occur only when at least two singleton vertices are present.

## Literature context and originality

Ashworth, Clarke, Giansiracusa, Jones, Quijas-Aceves, and Ren introduced a systematic graph-theoretic study of the Pachter--Sturmfels phylogenetic rank in September 2026. Their paper proves the complete-bipartite value, the complete-graph and rank-one cases, and several rank-\(n/2\) families including complete graphs minus perfect matchings. The current full text contains no occurrence of “multipartite” and does not state the formula above; its Question 7.3 asks for structural characterizations of graphs of bounded phylogenetic rank.

The underlying max-mixture notion goes back to Pachter--Sturmfels and is stated explicitly by Speyer--Sturmfels as the least number of tree metrics whose pointwise maximum is the given metric.

An adjacent notion called “tree rank” was studied by Cartwright and Chan in 2010 for tropical secant sets. Their paper explicitly notes that its tree-rank convention differs from the Pachter--Sturmfels mixture notion. Its complete-multipartite cover characterization for \(0/1\) dissimilarity matrices therefore does not establish the theorem above. This distinction was checked because terminology around “tree rank” is not uniform.

Originality is asserted only to the best of our knowledge. Exact and synonymous searches for complete multipartite graph metrics, partition/two-distance metrics, products of metric trees, max-mixtures of tree metrics, and tree/phylogenetic rank did not locate this formula or an equivalent classification. The main residual risk is older or poorly indexed metric-embedding literature using different terminology, or very recent parallel work following the September 2026 preprint.

## Verification and limitations

The proof is exact and does not rely on computation. The lower bound uses only the four-point condition and the uniqueness of a geodesic midpoint in a metric tree; the upper bound is an explicit collection of metric-star coordinates.

The result is restricted to connected complete multipartite graph metrics. It does not characterize arbitrary graphs of phylogenetic rank at most \(k\), and it does not address the maximal phylogenetic rank among all \(n\)-vertex graphs.

## References

1. F. Ashworth, O. Clarke, J. Giansiracusa, J. Jones, J. Quijas-Aceves, Y. Ren, *The phylogenetic rank of a graph*, arXiv:2609.19372 (2026). https://arxiv.org/abs/2609.19372
2. D. Speyer, B. Sturmfels, *Tropical Mathematics*, Mathematics Magazine 82(3) (2009), 163--173. https://doi.org/10.1080/0025570X.2009.11953615 ; https://arxiv.org/abs/math/0408099
3. D. Cartwright, M. Chan, *Three notions of tropical rank for symmetric matrices*, Discrete Mathematics and Theoretical Computer Science Proceedings AN (2010), 203--214. https://doi.org/10.46298/dmtcs.2865
4. P. Buneman, *A note on the metric properties of trees*, Journal of Combinatorial Theory, Series B 17(1) (1974), 48--50. https://doi.org/10.1016/0095-8956(74)90047-1
