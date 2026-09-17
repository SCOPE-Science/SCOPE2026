# Balanced complete bipartite graphs uniquely maximize geodesic subpaths at diameter two

## Statement

Let \(G\) be a finite simple connected graph on \(n\ge 3\) vertices with
\(\operatorname{diam}(G)=2\). Then
\[
\operatorname{gpn}(G)
\le
n+\frac n2\left\lfloor\frac{n^2}4\right\rfloor .
\]
Equality holds if and only if
\[
G\cong K_{\lfloor n/2\rfloor,\lceil n/2\rceil}.
\]

Here \(\operatorname{gpn}(G)\) is the geodesic subpath number introduced by
Knor, Sedlar, Škrekovski and Zhang: the total number of shortest paths between
unordered vertex pairs, plus the \(n\) zero-length paths.

The proof follows from a more general weighted induced-\(P_3\) inequality.

## Weighted open-triangle lemma

For an arbitrary simple \(n\)-vertex graph \(H\), write \(m(H)=|E(H)|\) and let
\(p_3(H)\) be the number of three-vertex sets inducing a copy of \(P_3\). Then
\[
m(H)+p_3(H)
\le
\frac n2\left\lfloor\frac{n^2}4\right\rfloor . \tag{1}
\]

For \(n\ge4\), equality in (1) holds if and only if
\[
H\cong K_{\lfloor n/2\rfloor,\lceil n/2\rceil}.
\]
For \(n=3\), both \(K_3\) and \(K_{1,2}\) attain equality.

### Proof

For \(x\in V(H)\), let \(N(x)\) be its open neighborhood and put
\[
c_x=e_H\bigl(N(x),\,V(H)\setminus N(x)\bigr).
\]
Every edge \(uv\) is counted in \(c_u\) and \(c_v\). For a third vertex
\(x\notin\{u,v\}\), the edge \(uv\) is counted in \(c_x\) exactly when
\(x\) is adjacent to exactly one of \(u,v\), which is exactly when
\(\{u,v,x\}\) induces a \(P_3\) having \(uv\) as one of its two edges.
Consequently every induced \(P_3\) contributes twice, and
\[
\sum_{x\in V(H)}c_x=2m(H)+2p_3(H). \tag{2}
\]

If \(d(x)=|N(x)|\), then
\[
c_x\le d(x)(n-d(x))
\le \left\lfloor\frac{n^2}4\right\rfloor .
\]
Summing and using (2) proves (1).

Suppose equality holds. Then for every vertex \(x\),
\[
d(x)\in\{\lfloor n/2\rfloor,\lceil n/2\rceil\}
\]
and every possible edge between \(N(x)\) and \(V(H)\setminus N(x)\) is
present. If \(x\) and \(y\) are nonadjacent, then every member of \(N(x)\)
is adjacent to \(y\), so \(N(x)\subseteq N(y)\); symmetry gives
\(N(x)=N(y)\). Thus nonadjacency (together with equality of a vertex with
itself) partitions \(V(H)\) into independent twin classes, and \(H\) is
complete multipartite. A vertex in a part of size \(s\) has degree \(n-s\),
so every part has size either \(\lfloor n/2\rfloor\) or
\(\lceil n/2\rceil\). For \(n\ge4\), three such parts already contain more
than \(n\) vertices, hence there are exactly two parts, of the two balanced
sizes. For \(n=3\), the additional all-singleton partition gives \(K_3\).
This proves the equality statement. \(\square\)

## Diameter-two consequence

If \(\operatorname{diam}(G)=2\), each adjacent pair contributes exactly one
geodesic. For a nonadjacent pair \(\{u,v\}\), every geodesic has length two
and is specified by one common neighbor of \(u\) and \(v\). Hence the total
number of length-two geodesics is exactly the number \(p_3(G)\) of induced
three-vertex paths. Therefore
\[
\operatorname{gpn}(G)=n+m(G)+p_3(G).
\]
Applying (1) yields the stated upper bound.

For \(n\ge4\), equality in (1) already forces the balanced complete bipartite
graph, which has diameter two. For \(n=3\), the two equality graphs in the
weighted lemma are \(K_3\) and \(K_{1,2}\); the diameter-two hypothesis
excludes \(K_3\). Thus the extremal graph is unique for every \(n\ge3\).

For \(K_{a,b}\) with \(a+b=n\),
\[
\operatorname{gpn}(K_{a,b})
=n+ab+a\binom b2+b\binom a2
=n+\frac{nab}2,
\]
so the balanced choice \(ab=\lfloor n^2/4\rfloor\) attains the bound.

## Context

Knor, Sedlar, Škrekovski and Zhang introduced the geodesic subpath number and
determined it for several graph families. Their concluding discussion notes
that balanced complete bipartite graphs are the natural maximizers inside the
complete bipartite family, while deleting a perfect matching can increase the
geodesic subpath number; they ask for the extremal bipartite graphs in general.
The result above gives an exact theorem on a different natural boundary:
among *all* diameter-two graphs, including graphs with triangles, no graph
beats the balanced complete bipartite graph. The matching-deletion examples
that motivate their broader bipartite problem have diameter at least three.

Pyatkin, Lykhovyd and Butenko previously determined the maximum possible
number of induced open triangles \(p_3(H)\) alone and found the same balanced
complete bipartite extremizer. Inequality (1) is a weighted strengthening
tailored to the geodesic problem: the quantity that must be maximized at
diameter two is \(m(H)+p_3(H)\), not \(p_3(H)\) alone.

## Limitations

Originality is asserted only to the best of our knowledge. The closest prior
work on open triangles establishes the unweighted \(p_3\) extremum, and the
recent geodesic-subpath paper does not state the diameter-two extremal theorem.
The full text of some closely related open-triangle papers was not inspected;
the residual originality risk is described in `REVIEW.md`. No independent
validation is asserted.

## References

1. M. Knor, J. Sedlar, R. Škrekovski, X.-D. Zhang,
   “Counting Geodesic Paths in Graphs,” *Mediterranean Journal of
   Mathematics* **23**, 171 (2026).
   https://doi.org/10.1007/s00009-026-03159-3
2. A. Pyatkin, E. Lykhovyd, S. Butenko,
   “The maximum number of induced open triangles in graphs of a given order,”
   *Optimization Letters* **13** (2019), 1927–1935.
   https://doi.org/10.1007/s11590-018-1330-2
3. K. Bhargava, N. N. Dattatreya, R. Rajendra,
   “On Stress of a Vertex in a Graph,” arXiv:2208.13493.
   https://arxiv.org/abs/2208.13493
