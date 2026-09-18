# Exact phylogenetic rank of complete multipartite graphs

## Result

Let
\[
G=K_{n_1,\ldots,n_r}
\]
be a connected complete multipartite graph, so \(r\ge 2\) and every \(n_i\ge 1\). Let
\[
q=\bigl|\{i:n_i\ge 2\}\bigr|,
\qquad
s=\bigl|\{i:n_i=1\}\bigr|.
\]
Write \(\operatorname{pr}(G)\) for the phylogenetic rank: the minimum number of metric trees whose \(\ell_\infty\)-product contains the graph metric of \(G\) isometrically.

Then
\[
\boxed{\operatorname{pr}(G)=\max\!\left\{1,\ q+\mathbf 1_{\{s\ge 2\}}\right\}.}
\]

Equivalently, if \(\overline G\) is viewed as a disjoint union of cliques, the rank is the number of nontrivial components of \(\overline G\), plus one exactly when \(\overline G\) has at least two isolated vertices, with the all-isolated case giving rank one.

In particular:

- if every part has size at least two, then \(\operatorname{pr}(G)=r\);
- the known complete-bipartite value \(\operatorname{pr}(K_{m,n})=2\) for \(m,n\ge2\) is recovered;
- if \(M\) is a matching of size \(t\ge1\) in \(K_n\), then
  \[
  \operatorname{pr}(K_n-M)=
  \begin{cases}
  t,&n-2t\le1,\\
  t+1,&n-2t\ge2.
  \end{cases}
  \]
  Thus the previously treated perfect-matching case extends to deletion of an arbitrary matching.

## Proof

Distances in a complete multipartite graph have only two nonzero values:
\[
d_G(u,v)=
\begin{cases}
2,&u\ne v\text{ and }u,v\text{ lie in the same part},\\
1,&u,v\text{ lie in different parts}.
\end{cases}
\]

### Upper bound

For each non-singleton part \(V_i\), construct a metric tree \(T_i\) that is a star with center \(c_i\) and one unit-length leaf for every vertex of \(V_i\). Map each vertex of \(V_i\) to its corresponding leaf and map every vertex outside \(V_i\) to \(c_i\).

The resulting coordinate metric has value \(2\) on distinct pairs inside \(V_i\), value \(1\) between \(V_i\) and its complement, and value \(0\) on pairs wholly outside \(V_i\).

If \(s\ge2\), add one further star coordinate \(T_0\): give each singleton-part vertex its own leaf at distance \(1/2\) from a common center and map every vertex in a non-singleton part to the center. This coordinate gives distance \(1\) between two singleton-part vertices and at most \(1/2\) on every other relevant pair.

Taking the supremum over these coordinates reproduces exactly the graph metric. Hence
\[
\operatorname{pr}(G)\le q+\mathbf 1_{\{s\ge2\}}
\]
when \(q+\mathbf 1_{\{s\ge2\}}>0\). If \(q=0\), then \(G\) is complete and one star with all leaves at distance \(1/2\) realizes its unit metric, so \(\operatorname{pr}(G)\le1\).

### Lower bound from the four-point condition

For each non-singleton part \(V_i\), choose distinct vertices \(a_i,b_i\in V_i\). Their graph distance is \(2\), so in any isometric embedding into a supremum of \(k\) tree metrics there must be at least one coordinate tree in which
\[
d(a_i,b_i)=2.
\]

A single coordinate tree cannot realize distance \(2\) simultaneously for chosen pairs from two distinct non-singleton parts. Indeed, suppose it did for \(\{a_i,b_i\}\) and \(\{a_j,b_j\}\), with \(i\ne j\). Every cross-part graph distance is \(1\), so every coordinate distance across these parts is at most \(1\). The three four-point sums in that coordinate would therefore satisfy
\[
d(a_i,b_i)+d(a_j,b_j)=4,
\]
whereas
\[
d(a_i,a_j)+d(b_i,b_j)\le2,
\qquad
d(a_i,b_j)+d(b_i,a_j)\le2.
\]
For a tree metric, the maximum of the three four-point sums is attained at least twice. Here the first sum is the unique maximum, a contradiction. Consequently the \(q\) chosen within-part pairs require \(q\) distinct tree coordinates, and
\[
\operatorname{pr}(G)\ge q.
\]

It remains to show the extra coordinate is necessary when \(s\ge2\). Assume for contradiction that \(q\ge1\), \(s\ge2\), and an isometric representation uses exactly \(q\) tree coordinates. Because no coordinate can realize two of the chosen distance-two pairs, the \(q\) pairs \((a_i,b_i)\) force a bijection between pairs and coordinates. Fix the coordinate assigned to \(V_i\), so
\[
d(a_i,b_i)=2.
\]

Let \(x\) be any singleton-part vertex. Since \(x\) lies in a different part from \(a_i,b_i\),
\[
d_G(x,a_i)=d_G(x,b_i)=1,
\]
and hence both coordinate distances are at most \(1\). The triangle inequality gives
\[
2=d(a_i,b_i)\le d(a_i,x)+d(x,b_i)\le2,
\]
so equality holds throughout:
\[
d(a_i,x)=d(x,b_i)=1.
\]
In a tree there is a unique midpoint of the geodesic from \(a_i\) to \(b_i\); therefore every singleton-part vertex maps in this coordinate to that same midpoint. If \(x\) and \(y\) are two singleton-part vertices, then their coordinate distance is thus \(0\). The same argument applies in every one of the \(q\) coordinates, so their supremum distance is \(0\), contradicting
\[
d_G(x,y)=1.
\]
Therefore at least \(q+1\) coordinates are required when \(s\ge2\).

If \(q=0\), then \(G\) is a nontrivial complete graph and its nonzero metric cannot be represented by zero trees, so \(\operatorname{pr}(G)\ge1\). This completes the proof.

## Context

Ashworth, Clarke, Giansiracusa, Jones, Quijas-Aceves and Ren introduced the graph-theoretic phylogenetic rank in the current form and study its basic structure. Their Proposition 3.5 proves that complete bipartite graphs \(K_{m,n}\) with \(m,n\ge2\) have rank two. Their Theorem 3.3 includes the family obtained from a complete graph of even order by deleting a perfect matching, with rank \(n/2\). They also ask for characterizations of graphs of rank at most \(k\).

The theorem above gives a single exact formula for the whole complete multipartite class. It simultaneously recovers both of those complete-multipartite subfamilies and extends the perfect-matching example to deletion of an arbitrary matching.

An older notion also called "tree rank" appears in work of Cartwright and Chan on tropical ranks of symmetric matrices. That paper explicitly notes that its tree rank, defined using the tropical Grassmannian, differs from the phylogenetic-rank notion originating in Pachter and Sturmfels; it therefore does not supply the formula proved here.

## Originality and limitations

To the best of our knowledge, no prior source gives the complete-multipartite formula above. Exact and synonymous searches covered "phylogenetic rank", "tree rank", isometric embeddings into products of metric trees, \(\ell_\infty\)-products, complete multipartite graphs, complete tripartite graphs, and matching-deleted complete graphs. The primary 2026 paper was inspected for its definitions, complete-bipartite theorem, matching-deletion example, and open problems; it contains no complete-multipartite theorem.

Residual originality risk remains. The phylogenetic-rank parameter originates in Pachter and Sturmfels, and the relevant book section was not inspected in full here. In addition, the 2026 graph-theoretic paper is very recent, so unindexed or parallel work may exist. The originality claim is therefore qualified strictly as "to the best of our knowledge."

No independent validation is asserted.

## References

1. F. Ashworth, O. Clarke, J. Giansiracusa, J. Jones, J. Quijas-Aceves, and Y. Ren, *The phylogenetic rank of a graph*, arXiv:2609.19372 (2026).
2. D. Cartwright and M. Chan, *Three notions of tropical rank for symmetric matrices*, Discrete Mathematics & Theoretical Computer Science, Proc. AN (2010), DOI: 10.46298/dmtcs.2865.
3. L. Pachter and B. Sturmfels, *Algebraic Statistics for Computational Biology*, Cambridge University Press (2005), Chapter 3.
