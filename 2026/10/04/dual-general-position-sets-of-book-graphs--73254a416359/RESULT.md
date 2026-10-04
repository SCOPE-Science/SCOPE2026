# Dual general position sets of book graphs
## Finding
For every integer \(r\ge2\), let \(B_r\) be the book graph formed from \(r\) copies of \(C_4\) sharing a common edge \(xy\), with page \(i\) given by the cycle \(x a_i b_i y x\). Then the nonempty dual general position sets of \(B_r\) are exactly the \(r\) internal page pairs \(\{a_i,b_i\}\). Consequently \[\operatorname{gp}_{\mathrm d}(B_r)=2\] and \(B_r\) has exactly \(r\) maximum dual general position sets.

## Assumptions and scope
All graphs are finite, simple, and connected. For \(r\ge2\), let \(B_r\) be the book graph obtained from \(r\) copies of \(C_4\) sharing the common edge \(xy\). On page \(i\), the remaining two vertices are \(a_i,b_i\), and the page cycle is
\[
x a_i b_i y x.
\]

For \(X\subseteq V(G)\), two vertices are \(X\)-positionable when every shortest path joining them has no internal vertex in \(X\). A set \(X\) is in dual general position when every pair of vertices both in \(X\), and every pair both in \(V(G)\setminus X\), are \(X\)-positionable.

Equivalently, \(X\) is a dual general position set exactly when \(X\) is a general position set and \(G-X\) is convex: the second condition is simply the requirement that every shortest path between two vertices outside \(X\) remain outside \(X\).

## Proof
Let \(X\ne\varnothing\) be a dual general position set.

First, neither spine endpoint belongs to \(X\). Suppose \(x\in X\). Its neighborhood is
\[
N(x)=\{y,a_1,\ldots,a_r\},
\]
and these \(r+1\) vertices are pairwise nonadjacent. Because \(B_r-X\) is convex, at most one vertex of \(N(x)\) can lie outside \(X\): if distinct \(p,q\in N(x)\setminus X\), then
\[
p-x-q
\]
is a shortest \(p,q\)-path with internal vertex \(x\in X\), contradicting convexity of the complement. Hence at least \(r\) neighbors of \(x\) lie in \(X\). Since \(r\ge2\), two distinct neighbors \(p,q\) of \(x\) lie in \(X\), but then the same length-two geodesic \(p-x-q\) has the internal vertex \(x\in X\), contradicting that \(X\) is in general position. Thus \(x\notin X\). By symmetry,
\[
y\notin X.
\]

Now fix a page \(i\). If \(a_i\in X\) but \(b_i\notin X\), then both \(x\) and \(b_i\) lie outside \(X\), while
\[
x-a_i-b_i
\]
is a shortest \(x,b_i\)-path with internal vertex \(a_i\in X\). This contradicts convexity of \(B_r-X\). Therefore \(a_i\in X\) implies \(b_i\in X\). The symmetric argument shows that \(b_i\in X\) implies \(a_i\in X\). Hence \(X\) is a union of complete internal page pairs \(\{a_i,b_i\}\).

It cannot contain two distinct page pairs. Indeed, suppose pages \(i\ne j\) both lie in \(X\). The vertices \(a_i\) and \(b_j\) have distance \(3\): their neighbor sets are
\[
N(a_i)=\{x,b_i\},\qquad N(b_j)=\{y,a_j\},
\]
which are disjoint, while
\[
a_i-b_i-y-b_j
\]
is a path of length \(3\). Hence this path is geodesic, but its internal vertex \(b_i\) belongs to \(X\), contradicting the general position property. Thus every nonempty dual general position set is exactly one pair \(\{a_i,b_i\}\).

Conversely, fix \(i\) and set \(X=\{a_i,b_i\}\). Since \(a_i\) and \(b_i\) are adjacent, \(X\) is a general position set. Any path between vertices outside \(X\) that enters the deleted page must traverse the three-edge segment
\[
x-a_i-b_i-y
\]
or its reverse. Replacing that segment by the edge \(xy\) strictly shortens the path. Therefore no shortest path between vertices of \(B_r-X\) uses \(a_i\) or \(b_i\), so \(B_r-X\) is convex. Hence \(X\) is dual general position.

Therefore the only nonempty dual general position sets are the \(r\) internal page pairs. In particular,
\[
\operatorname{gp}_{\mathrm d}(B_r)=2,
\]
and there are exactly \(r\) maximum sets.

## Verification
The included checker constructs \(B_r\), computes all-pairs distances, and tests the dual general position definition directly. A selected vertex is detected on a shortest path using the equality
\[
d(u,z)+d(z,v)=d(u,v).
\]

For every \(2\le r\le9\), the checker enumerates every vertex subset and compares the complete set of nonempty dual general position sets with the theorem's \(r\) internal page pairs.

## Relationship to prior work
The paper introducing dual general position explicitly studies generalized theta graphs. A book graph \(B_r\) is the generalized theta graph
\[
\Theta(1,3,\ldots,3),
\]
with one path of length \(1\) and \(r\) paths of length \(3\). Proposition 3.6 of that source proves only that this case has positive dual general position number, by exhibiting the two internal vertices of a length-three path as a dual general position set. It does not determine the exact maximum, classify all dual general position sets, or count the maximum sets.

A later paper on the same invariant studies strong and lexicographic graph products. Its inspected full text contains no occurrence of book or theta and therefore does not cover this family.

## Limitations
The theorem is restricted to square-page book graphs with \(r\ge2\). The boundary case \(B_1=C_4\) has additional dual general position pairs and is intentionally excluded. No claim is made for triangular books, longer-cycle books, or arbitrary generalized theta graphs. The finite exhaustive verification is corroborative only; the all-\(r\) conclusion follows from the proof.

## References
1. J. Tian, S. Klavžar, “Variety of general position problems in graphs,” arXiv:2402.17338v1, 27 February 2024; Bulletin of the Malaysian Mathematical Sciences Society 48 (2025), Article 5, DOI 10.1007/s40840-024-01788-z.
2. P. Dokyeesun, S. Klavžar, D. Kuziak, J. Tian, “General position problems in strong and lexicographic products of graphs,” arXiv:2408.15951v1, 28 August 2024.
