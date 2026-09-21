# Sharp zero-forcing metric-dimension gap for trees of fixed order

## Statement

Let \(T\) be a tree of order \(n\ge 4\). Write \(Z(T)\) for its zero forcing number and
\(\dim(T)\) for its metric dimension. Then

\[
\boxed{0\le Z(T)-\dim(T)\le \left\lfloor\frac{n-4}{3}\right\rfloor.}
\]

The upper bound is sharp for every \(n\ge 4\).

There is also a useful structural refinement. Suppose \(T\) is not a path. Let
\(\ell(T)\) be its number of leaves, \(e(T)\) its number of exterior major vertices,
let \(M\) be the set of vertices of degree at least \(3\), and let
\(H=T[M]\) be the forest induced by the major vertices. If \(\nu(H)\) denotes the
matching number of \(H\), then

\[
\boxed{Z(T)-\dim(T)\le e(T)-1-\nu(H).}
\]

For orders \(n=3m+1\ge 7\), the order bound has a unique equality case up to
isomorphism. It is the tree \(C_m\) obtained from a path on \(m\) degree-\(3\)
major vertices by subdividing every edge of that path exactly once, attaching two
leaves to each end major vertex, and attaching one leaf to every internal major
vertex. Thus \(C_m\) has \(m\) major vertices, \(m-1\) degree-\(2\) vertices, and
\(m+2\) leaves.

For \(n=3m+2\) and \(n=3m+3\), sharp examples are obtained from \(C_m\) by
subdividing one pendant edge once or twice, respectively. For \(m=1\), take
\(C_1=K_{1,3}\).

## Proof

The lower bound \(Z(T)\ge \dim(T)\) for trees is known. We prove the upper bound.

Assume first that \(T\) is not a path. Let \(\ell=\ell(T)\) and \(e=e(T)\).
The standard formula for the metric dimension of a non-path tree is

\[
\dim(T)=\ell-e.
\]

For trees, the zero forcing number equals the minimum vertex-disjoint path-cover
number \(P(T)\):

\[
Z(T)=P(T).
\]

We first prove

\[
P(T)\le \ell-1-\nu(H).
\]

Let \(F\) be a maximum matching of \(H\), so \(|F|=\nu(H)\). For a major vertex
\(v\), let \(\varepsilon_v=1\) when \(v\) is incident with an edge of \(F\), and
\(\varepsilon_v=0\) otherwise. Start an edge-deletion set \(D\) with all edges of
\(F\). For every major vertex \(v\), additionally choose

\[
d(v)-2-\varepsilon_v
\]

incident edges that are not in \(F\), and add them to \(D\). Such a choice is
always possible. After these deletions every major vertex has degree at most \(2\);
all other vertices already have degree at most \(2\). Hence \(T-D\) is a spanning
forest of paths.

For a tree,

\[
\sum_{v\in M}(d(v)-2)=\ell-2.
\]

Since a matching edge accounts for two matched major vertices,

\[
|D|
 \le |F|+\sum_{v\in M}(d(v)-2-\varepsilon_v)
 = \nu(H)+(\ell-2)-2\nu(H)
 = \ell-2-\nu(H).
\]

Deleting \(|D|\) edges from a tree gives \(|D|+1\) components, all paths, so

\[
P(T)\le |D|+1\le \ell-1-\nu(H).
\]

Therefore

\[
Z(T)-\dim(T)
 =P(T)-(\ell-e)
 \le e-1-\nu(H).
\]

It remains to control \(e-\nu(H)\) by the order. Because \(H\) is a forest, it is
bipartite. By the König theorem, \(H\) has a vertex cover \(C\) of size
\(\nu(H)\). Let \(E_{\rm ext}\) be the set of exterior major vertices and put

\[
S=E_{\rm ext}\setminus C.
\]

The set \(S\) is independent: an edge of \(H\) with both ends in \(S\) would not
be covered by \(C\). Moreover,

\[
|S|\ge e-\nu(H).
\]

Every vertex of \(S\) has degree at least \(3\). Since \(S\) is independent, no
edge of \(T\) is incident with two vertices of \(S\), and hence

\[
n-1=|E(T)|
 \ge \sum_{v\in S}d(v)
 \ge 3|S|
 \ge 3(e-\nu(H)).
\]

Thus

\[
e-\nu(H)\le \left\lfloor\frac{n-1}{3}\right\rfloor,
\]

and consequently

\[
Z(T)-\dim(T)
 \le \left\lfloor\frac{n-1}{3}\right\rfloor-1
 = \left\lfloor\frac{n-4}{3}\right\rfloor.
\]

If \(T\) is a path, \(Z(T)=\dim(T)=1\), so the same order bound holds for
\(n\ge4\).

## Sharpness

For \(m\ge2\), the tree \(C_m\) described above has

\[
|V(C_m)|=m+(m-1)+(m+2)=3m+1.
\]

Its \(m\) major vertices all have degree \(3\), are pairwise nonadjacent, and all
are exterior. Thus \(\ell=m+2\) and \(e=m\), so

\[
\dim(C_m)=\ell-e=2.
\]

Any spanning path forest obtained by deleting edges must delete at least one edge
incident with each degree-\(3\) major vertex. Since the major vertices are
pairwise nonadjacent, one deleted edge cannot serve two of them. At least \(m\)
edges must therefore be deleted, so \(P(C_m)\ge m+1\). Conversely, delete one
pendant edge at each major vertex; what remains is one path together with \(m\)
isolated leaves. Hence \(P(C_m)=m+1\), and therefore

\[
Z(C_m)-\dim(C_m)=(m+1)-2=m-1
=\left\lfloor\frac{(3m+1)-4}{3}\right\rfloor.
\]

The same argument is unchanged if one pendant edge is subdivided once or twice:
the leaf count, exterior-major set, degrees of the major vertices, and the fact
that the major vertices are pairwise nonadjacent all remain unchanged. This gives
sharp examples of orders \(3m+2\) and \(3m+3\). The case \(m=1\) gives the sharp
value \(0\) for orders \(4,5,6\).

## Uniqueness when \(n\equiv1\pmod 3\)

Let \(n=3m+1\ge7\), and suppose

\[
Z(T)-\dim(T)=m-1.
\]

Equality in the preceding inequalities forces

\[
e-\nu(H)=m.
\]

Take a minimum vertex cover \(C\) of \(H\), of size \(\nu(H)\), and again set
\(S=E_{\rm ext}\setminus C\). We have \(|S|\ge m\), while

\[
3|S|\le |E(T)|=3m.
\]

Hence \(|S|=m\); every vertex of \(S\) has degree exactly \(3\); and every edge of
\(T\) is incident with a vertex of \(S\). Equality \(|S|=e-\nu(H)\) also implies
that every vertex of \(C\) is exterior.

There cannot be an exterior major vertex \(x\notin S\). Indeed, take a terminal
leaf path belonging to \(x\). Its first edge \(xy\) must be incident with \(S\).
Since \(x\notin S\), this forces \(y\in S\), so the path encounters another major
vertex immediately, contradicting terminality. Therefore \(E_{\rm ext}=S\).
Since every vertex of \(C\) is exterior but \(C\cap S=\varnothing\), it follows
that \(C=\varnothing\), hence \(\nu(H)=0\) and \(H\) has no edges.

There are no interior major vertices either. If \(x\) were one, then every edge
incident with \(x\) would have its other endpoint in \(S\), producing a
major-major edge in \(H\), a contradiction. Thus the major vertices are exactly
the vertices of \(S\), each of degree \(3\), and they are pairwise nonadjacent.

Every edge of \(T\) is incident with a major vertex. Hence every degree-\(2\)
vertex is adjacent to two major vertices, and every leaf is adjacent to a major
vertex. Suppress all degree-\(2\) vertices. The resulting tree on the \(m\) major
vertices has maximum degree at most \(2\), because every major vertex is exterior
and therefore has at least one leaf neighbor. It is consequently a path. Its end
major vertices have two leaf neighbors, its internal major vertices have one,
and every core edge is represented by exactly one degree-\(2\) vertex. This is
precisely \(C_m\), proving uniqueness.

## Computational check

A direct enumeration of all nonisomorphic trees of orders \(4\) through \(17\)
agrees with the theorem. The observed maximum gaps are

\[
0,0,0,1,1,1,2,2,2,3,3,3,4,4,
\]

for \(n=4,\ldots,17\), respectively. For \(n=7,10,13,16\), exactly one
nonisomorphic tree attains the maximum, agreeing with the uniqueness statement.
The accompanying script computes the path-cover number by a tree dynamic program
and the metric dimension from the leaf/exterior-major formula.

## Context and originality

Eroh, Kang and Yi proved \(\dim(T)\le Z(T)\) for every tree, recalled
\(\dim(T)=\ell(T)-e(T)\) for non-path trees, and used \(Z(T)=P(T)\). They also
gave tree families for which \(Z(T)-\dim(T)\) is arbitrarily large, but did not
state an order-constrained maximum in the inspected full text.

Davila and Henning studied path covers of trees in relation to total forcing and
matching, including invariance under trimming and several extremal
characterizations. Their inspected preprint does not state the order-sharp
zero-forcing/metric-dimension gap above.

Later work on metric dimension and zero forcing for sparse graphs focuses mainly
on cyclomatic-number bounds in the opposite comparison direction, while recent
work on distance- and path-based covering parameters gives leaf/cyclomatic-number
bounds for path partitions. Searches for the exact formula, synonymous
formulations involving path covers and metric dimension, and equivalent
order-extremal tree statements did not locate the theorem above.

To the best of our knowledge, the order-sharp bound, the intermediate
\(e-1-\nu(H)\) refinement, and the uniqueness theorem for orders
\(n\equiv1\pmod3\) are new.

## Scientific limitations

The originality search cannot exclude unindexed literature or equivalent results
phrased entirely in path-partition, minimum-rank, or specialized tree
terminology. The result applies to trees and to the ordinary zero forcing and
ordinary metric dimension parameters. The uniqueness statement is only asserted
for the congruence class \(n\equiv1\pmod3\), \(n\ge7\); other orders have multiple
extremal trees.

## References

1. L. Eroh, C. X. Kang, E. Yi, *A Comparison between the Metric Dimension and
   Zero Forcing Number of Trees and Unicyclic Graphs*, Acta Mathematica Sinica,
   English Series 33 (2017), 731-747. https://doi.org/10.1007/s10114-017-4699-4
   ; preprint: https://arxiv.org/abs/1408.5943
2. F. Barioli et al. (AIM Minimum Rank--Special Graphs Work Group),
   *Zero forcing sets and the minimum rank of graphs*, Linear Algebra and its
   Applications 428 (2008), 1628-1648.
3. R. Davila, M. A. Henning, *Matching, Path Covers, and Total Forcing Sets*,
   Quaestiones Mathematicae 43 (2020), 131-147.
   https://doi.org/10.2989/16073606.2018.1542525 ;
   preprint: https://arxiv.org/abs/1801.05318
4. N. Bousquet, Q. Deschamps, A. Parreau, I. M. Pelayo,
   *Metric dimension on sparse graphs and its applications to zero forcing sets*,
   arXiv:2111.07845. https://arxiv.org/abs/2111.07845
5. D. Chakraborty, F. Foucaud, A. Hakanen,
   *Distance-based (and path-based) covering problems for graphs of given
   cyclomatic number*, Discrete Mathematics 348 (2025), 114595.
   https://doi.org/10.1016/j.disc.2025.114595
