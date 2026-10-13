# All edge metric generators of lollipop graphs
## Finding
For integers \(k\ge3\) and \(\ell\ge1\), define the lollipop graph \(L(k,\ell)\) as follows. Its clique is \(\{a\}\cup X\cong K_k\), with \(|X|=k-1\), and a path of length \(\ell\) is attached at \(a\):
\[
a p_1 p_2\cdots p_\ell.
\]
For a vertex \(v\) and an edge \(e=uw\), put \(d(v,e)=\min\{d(v,u),d(v,w)\}\). A set \(S\subseteq V(L(k,\ell))\) is an edge metric generator when every two distinct edges have different distance vectors to \(S\).

Then \(S\) is an edge metric generator if and only if exactly one of the following holds:

1. \(X\subseteq S\); or
2. \(|X\setminus S|=1\) and \(S\cap\{p_1,\ldots,p_\ell\}\ne\varnothing\).

Thus, for the edge-resolving-set enumerator
\[
E_{k,\ell}(x)=\sum_{S	ext{ edge metric generator}}x^{|S|},
\]
one has
\[
E_{k,\ell}(x)=x^{k-1}(1+x)^{\ell+1}+(k-1)x^{k-2}(1+x)\big((1+x)^\ell-1\big).
\]
In particular,
\[
\operatorname{edim}(L(k,\ell))=k-1,
\qquad
b_e(L(k,\ell))=1+(k-1)\ell,
\]
where \(b_e\) denotes the number of edge metric bases, and
\[
E_{k,\ell}(1)=2^{\ell+1}+2(k-1)(2^\ell-1).
\]
The attachment vertex \(a\) is in no edge metric basis, every other vertex lies in at least one edge metric basis, and no vertex lies in every edge metric basis.

## Assumptions and scope
All graphs are finite, simple, connected, and unweighted. The parameters satisfy \(k\ge3\) and \(\ell\ge1\). The path vertices \(p_1,\ldots,p_\ell\) are new and are disjoint from the clique except that the path is joined to the clique through the edge \(a p_1\). The result concerns ordinary edge metric generators, not vertex metric generators, strong resolving sets, or fault-tolerant edge metric generators.

## Proof
Write \(P=\{p_1,\ldots,p_\ell\}\).

First suppose that two distinct vertices \(x,y\in X\) are omitted from \(S\). The clique edges \(ax\) and \(ay\) have equal distance to every vertex outside \(\{x,y\}\): the vertex \(a\) has distance \(0\) to both, every vertex of \(X\setminus\{x,y\}\) has distance \(1\) to both, and \(p_j\) has distance \(j\) to both. Hence no edge metric generator can omit two vertices of \(X\), so \(|X\setminus S|\le1\).

Now suppose \(X\setminus S=\{x_0\}\) and \(S\cap P=\varnothing\). The two edges \(ax_0\) and \(a p_1\) have the same distance to every possible landmark in \(S\subseteq X\cup\{a\}\): \(a\) has distance \(0\) to both, while every selected vertex of \(X\) has distance \(1\) to both. Thus a set omitting one vertex of \(X\) must contain at least one path vertex.

For sufficiency, first assume \(X\subseteq S\). It is enough to check \(X\) itself because edge resolvability is monotone under adding landmarks. Relative to \(X\), a clique edge \(a x\) has exactly one zero coordinate, a clique edge \(xy\) with \(x,y\in X\) has exactly two zero coordinates, and the path edge \(p_{r-1}p_r\), where \(p_0=a\), has the constant vector whose entries are all \(r\). These signatures are pairwise distinct, so \(X\) resolves all edges.

Finally suppose \(X\setminus S=\{x_0\}\) and choose \(p_j\in S\cap P\). Again by monotonicity it is enough to use
\[
T=(X\setminus\{x_0\})\cup\{p_j\}.
\]
Put \(X'=X\setminus\{x_0\}\), which is nonempty because \(k\ge3\). On the coordinates indexed by \(X'\), the clique edges have only \(0\) and \(1\) entries. More precisely, \(a x_0\) has the all-one vector; \(a x\) has a single zero at \(x\); \(x x_0\) has the same zero pattern as \(a x\); and \(xy\) has zeros at \(x\) and \(y\). The landmark \(p_j\) separates the two single-zero types because
\[
d(p_j,a x)=j,\qquad d(p_j,x x_0)=j+1.
\]
It also distinguishes \(a x_0\) from the first path edge, since
\[
d(p_j,a x_0)=j,\qquad d(p_j,a p_1)=j-1.
\]
For every path edge \(p_{r-1}p_r\), all coordinates from \(X'\) equal \(r\). Hence distinct path edges have distinct signatures. Path edges with \(r\ge2\) cannot collide with clique edges because their \(X'\)-coordinates are at least \(2\), while the case \(r=1\) was separated from the only all-one clique signature above. Thus \(T\), and therefore \(S\), is an edge metric generator.

The polynomial follows by counting the two disjoint cases. If \(X\subseteq S\), the \(\ell+1\) vertices in \(\{a\}\cup P\) are arbitrary, contributing \(x^{k-1}(1+x)^{\ell+1}\). If one vertex of \(X\) is omitted, there are \(k-1\) choices for it, \(a\) is optional, and a nonempty subset of \(P\) is required, giving \((k-1)x^{k-2}(1+x)((1+x)^\ell-1)\).

The least degree is \(k-1\). At that degree there is one basis \(X\), together with the \((k-1)\ell\) bases \((X\setminus\{x\})\cup\{p_j\}\). These bases also prove the final forced/void statements.

## Verification
A standalone verifier reconstructs \(L(k,\ell)\), computes all vertex-to-edge distances by breadth-first search, exhaustively tests every vertex subset against the definition of edge metric generator, and compares the result with the stated if-and-only-if criterion and polynomial. It checks all \(3\le k\le6\) and \(1\le\ell\le5\), through order \(11\).

The replay result is:

`VERIFY_OK k_range=3..6 ell_range=1..5 subset_checks=7440 criterion_checks=7440 coefficient_checks=170 minimum_checks=20 max_order=11`

The computation is a finite stress test. The theorem for arbitrary parameters is established by the preceding proof, not by extrapolation from the checked range.

## Relationship to prior work
Kelenc, Tratnik, and Yero introduced edge metric dimension and the vertex-to-edge distance used here. Their earliest public arXiv version is dated 2016-01-31 and lists MSC 05C12 first. The inspected foundational full text develops the general invariant and several standard graph families but does not treat lollipop graphs.

A later study of vertices that are forced into, or excluded from, all edge metric bases develops those basis-membership notions and realization constructions. Its searchable full text was checked under lollipop, clique-path, and path-attachment formulations; no lollipop classification matching the theorem above was located. The present result therefore gives, for this natural clique-with-tail family, the complete generator set system rather than only a minimum dimension: it determines every coefficient of the enumerator and, as a corollary, all edge metric bases and the unique edge-basis-void vertex.

## Limitations
The result is restricted to the stated lollipop normalization with \(k\ge3\). It does not address weighted graphs, multiple tails, or fault-tolerant variants. The literature search included direct lollipop terminology, clique-path aliases, edge-basis membership terminology, semantic database searches, and relevant full-text sources, but poorly indexed equivalent work remains a residual originality risk.

## References
1. A. Kelenc, N. Tratnik, and I. G. Yero, “Uniquely identifying the edges of a graph: the edge metric dimension,” arXiv:1602.00291, first public version 2016-01-31. DOI: 10.48550/arXiv.1602.00291.
2. A. Hakanen, V. Junnila, T. Laihonen, and I. G. Yero, “On the vertices belonging to all edge metric bases,” Discrete Applied Mathematics, DOI: 10.1016/j.dam.2025.08.054.
