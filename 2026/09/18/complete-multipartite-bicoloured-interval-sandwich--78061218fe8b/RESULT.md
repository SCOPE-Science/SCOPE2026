# Complete multipartite graphs in the bicoloured-interval and interval-sandwich classes

## Result

Let
\[
G=K_{n_1,\ldots,n_r}
\]
be a finite complete multipartite graph, with the part sizes ordered as
\(n_1\ge n_2\ge\cdots\ge n_r\ge1\), with the convention \(n_2=0\) when \(r=1\). Then the following are equivalent:

1. \(G\) is a bicoloured-interval graph.
2. \(G\) is an interval-sandwich graph.
3. \(n_2\le2\), i.e. at most one part has size at least three.
4. \(G\) has no induced \(K_{3,3}\).

Moreover, whenever these conditions hold, \(G\) has a bicoloured-interval representation in which **all vertices receive the same colour**. Thus, on complete multipartite graphs, the bicoloured-interval and interval-sandwich classes coincide, and every positive instance already lies in the monochromatic centre-containment subclass.

## Definitions

For a closed interval \(I_v\subset\mathbb R\), write \(c_v\) for its centre. A bicoloured-interval representation assigns to each vertex an interval and one of two colours, with two vertices adjacent precisely when

- their colours differ and their intervals intersect, or
- their colours agree and the centre of one interval lies in the other.

An interval-sandwich representation is a family of intervals for which the graph lies between the centre-containment graph and the interval intersection graph: every centre-containment pair is an edge, and every graph edge is an intersecting pair.

For centred intervals with radii \(\rho_u,\rho_v\), the same-colour adjacency condition is simply
\[
|c_u-c_v|\le \max\{\rho_u,\rho_v\}.
\]

## Obstruction: \(K_{3,3}\) is not interval-sandwich

We first give a self-contained proof of the only obstruction needed below.

Suppose three vertices \(a_1,a_2,a_3\) are pairwise nonadjacent in an interval-sandwich representation, and order their centres as
\[
c_{a_1}<c_{a_2}<c_{a_3}.
\]
Because a nonedge cannot be a centre-containment pair, \(c_{a_2}\notin I_{a_1}\) and \(c_{a_2}\notin I_{a_3}\). Hence the right endpoint of \(I_{a_1}\) lies strictly left of \(c_{a_2}\), while the left endpoint of \(I_{a_3}\) lies strictly right of \(c_{a_2}\). In particular, the two extreme intervals \(I_{a_1}\) and \(I_{a_3}\) are disjoint.

Now suppose an interval-sandwich representation of \(K_{3,3}\) existed, with independent parts \(A\) and \(B\). Order the centres of the three intervals from \(A\) and let \(a_2\) be the middle one. The two extreme \(A\)-intervals are separated by \(c_{a_2}\). Every interval belonging to \(B\) must intersect both extreme \(A\)-intervals, since every cross-part pair is an edge and graph edges must correspond to intersecting intervals. Being an interval, it must therefore contain the point \(c_{a_2}\). Thus all three \(B\)-intervals have a common point.

But applying the preceding observation to the independent triple \(B\) says its two extreme intervals are disjoint. They cannot share a common point. This contradiction proves that \(K_{3,3}\) is not interval-sandwich.

The interval-sandwich property is hereditary under taking induced subgraphs by restricting a representation. Therefore any complete multipartite graph with two parts of size at least three is not interval-sandwich.

## Explicit monochromatic construction

Assume now that at most one part has size at least three.

If every part is a singleton, \(G\) is complete and identical intervals with one common colour give a representation. Otherwise choose a part \(A\) of size \(m\ge2\); if a part of size at least three exists, choose that one. Every remaining nonsingleton part then has size exactly two.

Write
\[
A=\{a_0,\ldots,a_{m-1}\},\qquad D=2m-2.
\]
Give every vertex the same colour. For \(0\le i<m\), assign
\[
c(a_i)=2i,\qquad \rho(a_i)=1.
\]
Index the remaining two-vertex parts as
\[
P_k=\{x_k,y_k\},\qquad 1\le k\le t,
\]
and assign
\[
c(x_k)=-k,\qquad c(y_k)=D+k,
\]
with common radius
\[
\rho(x_k)=\rho(y_k)=R_k:=D+2k-1.
\]
Finally, for every singleton part vertex \(z\), set
\[
c(z)=0,\qquad \rho(z)=D+2t+1.
\]

We verify that the centre-containment graph of these intervals is exactly \(G\).

### Nonedges inside parts

For distinct \(a_i,a_j\),
\[
|c(a_i)-c(a_j)|\ge2>1
 =\max\{\rho(a_i),\rho(a_j)\},
\]
so no two vertices of \(A\) are adjacent.

For a two-vertex part \(P_k\),
\[
|c(x_k)-c(y_k)|=D+2k=R_k+1,
\]
so \(x_k y_k\) is also a nonedge.

These are all the required nonedges.

### Edges between different parts

For any \(a_i\in A\), the farthest centre of \(A\) from either centre in \(P_k\) is at distance at most \(D+k\), while
\[
D+k\le D+2k-1=R_k.
\]
Hence each vertex of \(P_k\) is adjacent to every vertex of \(A\).

For two distinct two-vertex parts \(P_j,P_k\), assume \(j<k\). Same-side centre distances equal \(k-j\), and the two cross-side distances equal \(D+j+k\). Since
\[
D+j+k\le D+2k-1=R_k,
\]
the radius of the outer pair \(P_k\) witnesses all four adjacencies between \(P_j\) and \(P_k\).

A singleton interval has radius \(D+2t+1\), which contains the centres of all intervals constructed above. Hence every singleton vertex is adjacent to every vertex outside its own singleton part, including all other singleton vertices.

Thus the resulting monochromatic bicoloured-interval graph is exactly \(G\).

## Equivalence with induced \(K_{3,3}\)-freeness

A complete multipartite graph contains an induced \(K_{3,3}\) if and only if two distinct parts each contain at least three vertices: each independent side of an induced \(K_{3,3}\) must lie in one multipartite part. Hence condition 3 is equivalent to condition 4.

Combining the explicit construction, the inclusion of bicoloured-interval graphs in interval-sandwich graphs, and the \(K_{3,3}\) obstruction proves all four equivalences.

## Context and significance

Basit, Suter and Zhang introduced bicoloured-interval and interval-sandwich graphs in 2026 and state that they determine which complete bipartite graphs belong to the two classes. The theorem above extends the structural question from two parts to arbitrary complete multipartite graphs and shows an additional collapse: the two new classes have exactly the same complete multipartite members, and every such member has a monochromatic representation.

The criterion is especially simple: within complete multipartite graphs, a single induced graph, \(K_{3,3}\), is the complete obstruction.

## Limitations and originality scope

The statement concerns only complete multipartite graphs and does not characterize either graph class in general. Originality is claimed only to the best of our knowledge. Exact and synonymous searches for bicoloured-interval, interval-sandwich, centre/center-containment, max-point-tolerance, interval-catch, and complete multipartite formulations did not locate this multipartite characterization.

The full theorem text of the 40-page Basit--Suter--Zhang preprint was not inspected; its arXiv abstract was inspected and explicitly advertises classifications of complete bipartite graphs, but not complete multipartite graphs. Because that source is very recent, an unindexed remark or parallel result remains the main residual originality risk. Older central interval-catch and central max-point-tolerance literature was searched by equivalent terminology; no complete-multipartite classification matching the theorem above was located.

## References

1. Abdul Basit, David Suter, Erchuan Zhang, *Bicoloured-interval and interval-sandwich graphs: two new classes in the tolerance hierarchy*, arXiv:2609.12293 (2026).
2. Sanchita Paul, Shamik Ghosh, *On some subclasses of interval catch digraphs*, Electronic Journal of Graph Theory and Applications 10(1), 157--171 (2022), DOI: 10.5614/ejgta.2022.10.1.10.
3. Sanchita Paul, Shamik Ghosh, *On central-max-point tolerance graphs and some subclasses of interval catch digraphs*, arXiv:1712.00008.
