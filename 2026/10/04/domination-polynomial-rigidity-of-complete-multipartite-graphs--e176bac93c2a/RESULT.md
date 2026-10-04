# Domination-polynomial rigidity of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph, with \(r\ge2\) and \(N=\sum_i n_i\). Its bivariate domination polynomial satisfies \[J(G;x,y)=1+\sum_{i=1}^r y^{N-n_i}\big((1+x)^{n_i}-1\big)+(x+y)^N-y^N-\sum_{i=1}^r y^{N-n_i}\big((x+y)^{n_i}-y^{n_i}\big).\] Within the class of connected complete multipartite graphs, both \(J(G;x,y)\) and the ordinary domination polynomial \(D(G;x)\) determine \(G\) up to isomorphism. More explicitly, if \(m_t\) is the number of parts of size \(t\), then \(m_t=[x y^{N-t}]J(G;x,y)/t\). For the ordinary polynomial, \[Q_G(x)=(1+x)^N-D(G;x)=1+\sum_{t\ge2}m_t\big((1+x)^t-x^t-1\big),\] so the largest non-singleton part size is one more than the degree of \(Q_G-1\), its multiplicity is the leading coefficient divided by that part size, and iterating this subtraction recovers all non-singleton parts; the remaining vertices are singleton parts.

## Assumptions and scope
All graphs are finite, simple, and undirected. The bivariate domination polynomial is
\[
J(G;x,y)=\sum_{W\subseteq V(G)}x^{|W|}y^{|N[W]|-|W|},
\]
where \(N[W]\) is the closed neighborhood of \(W\). The ordinary domination polynomial is
\[
D(G;x)=\sum_{W\subseteq V(G),\ N[W]=V(G)}x^{|W|}.
\]
The rigidity statements below are restricted to the class of connected complete multipartite graphs; they do not assert global domination uniqueness among arbitrary graphs.

## Proof
Write the parts of \(G\) as \(X_1,\ldots,X_r\), with \(|X_i|=n_i\).

For a nonempty set \(W\) contained in a single part \(X_i\), every vertex outside \(X_i\) is adjacent to every vertex of \(W\), while no vertex of \(X_i\setminus W\) is adjacent to \(W\). Hence
\[
|N[W]|-|W|=N-n_i.
\]
The total contribution of nonempty subsets contained in \(X_i\) is therefore
\[
y^{N-n_i}\big((1+x)^{n_i}-1\big).
\]

If \(W\) meets at least two parts, then every vertex outside \(W\) has a neighbor in \(W\), so \(N[W]=V(G)\) and the contribution is \(x^{|W|}y^{N-|W|}\). Summing this weight over all subsets gives \((x+y)^N\); to retain only subsets meeting at least two parts, subtract the empty-set term \(y^N\) and, for every part \(X_i\), subtract
\[
y^{N-n_i}\big((x+y)^{n_i}-y^{n_i}\big),
\]
which is exactly the contribution that the nonempty subsets of \(X_i\) would have received under the full-neighborhood weight. Adding back the actual one-part contributions and the empty set proves the displayed formula for \(J(G;x,y)\).

The coefficient of \(x y^q\) in \(J\) records vertices whose external neighborhood has size \(q\). A vertex in a part of size \(t\) has exactly \(N-t\) neighbors, so
\[
[x y^{N-t}]J(G;x,y)=t m_t.
\]
Also \(N=\deg_x J\), because the whole vertex set contributes \(x^N\). Thus every multiplicity \(m_t\) is recovered from \(J\), proving injectivity of \(J\) on complete multipartite isomorphism types.

For the ordinary domination polynomial, every vertex set meeting at least two parts dominates \(G\). A set contained in one part dominates only when it is the whole part. Therefore
\[
D(G;x)=(1+x)^N-\sum_i(1+x)^{n_i}+(r-1)+\sum_i x^{n_i}.
\]
Rearranging gives
\[
Q_G(x):=(1+x)^N-D(G;x)
=1+\sum_i\big((1+x)^{n_i}-x^{n_i}-1\big).
\]
Singleton parts contribute zero to the sum. If \(M\ge2\) is the largest part size and occurs \(m_M\) times, then the highest positive degree of \(Q_G-1\) is \(M-1\), with coefficient
\[
m_M\binom{M}{M-1}=m_M M.
\]
Hence \(M\) and \(m_M\) are recovered from \(D\). Subtract
\[
m_M\big((1+x)^M-x^M-1\big)
\]
from \(Q_G\) and repeat. This uniquely recovers every non-singleton part size and multiplicity. Finally, the number of singleton parts is the number of vertices not yet assigned, namely
\[
N-\sum_{t\ge2}t m_t.
\]
Thus the ordinary domination polynomial is also injective on connected complete multipartite isomorphism types.

## Verification
The included checker independently enumerates all vertex subsets for every complete multipartite isomorphism type of orders two through ten. It computes external neighborhoods and domination directly from part labels, checks the displayed formulas, reconstructs the part sizes independently from \(J\) and from \(D\), and confirms no collisions among the tested types. It also checks the ordinary-polynomial inversion formula, without vertex-subset enumeration, for every complete multipartite isomorphism type through order thirty.

## Relationship to prior work
Preen and Murray introduced the bivariate domination polynomial and developed recurrence and reduction methods. Their full-text indexed version gives the complete-graph formula, path recurrences, cut-vertex/cut-edge reductions, and examples of non-isomorphic graphs sharing the same bivariate polynomial. A full-text search of that indexed paper found no occurrence of “multipartite”; the only “bipartite” occurrences found were in discussion of related bipartition-polynomial literature.

Beaton and Brown proved that domination polynomials of complete multipartite graphs are unimodal. Their proof observes that every dependent vertex set dominates and writes the ordinary domination polynomial as the dependent-set polynomial plus one monomial for each whole part. That statement yields the ordinary polynomial formula above, but the inspected source does not state the inverse reconstruction or the restricted-class uniqueness theorem.

Targeted searches for domination-equivalent complete multipartite graphs, reconstruction from the domination polynomial, and bivariate domination polynomials of complete multipartite graphs did not locate an equivalent rigidity theorem.

## Limitations
The injectivity results are only within the class of connected complete multipartite graphs. They do not rule out a non-multipartite graph sharing the same ordinary or bivariate domination polynomial with a complete multipartite graph. The exhaustive computation is finite corroboration and does not replace the proof. Literature searches cannot exclude a differently phrased or non-indexed prior reconstruction theorem.

## References
1. J. Preen and A. Murray, “Bivariate Domination Polynomial,” arXiv:1708.03890v1 (2017); Journal of Combinatorial Mathematics and Combinatorial Computing 111 (2019), 39–52.
2. I. Beaton and J. I. Brown, “On the Unimodality of Domination Polynomials,” arXiv:2012.11813v1 (2020); Graphs and Combinatorics (2022), DOI 10.1007/s00373-022-02487-x.
