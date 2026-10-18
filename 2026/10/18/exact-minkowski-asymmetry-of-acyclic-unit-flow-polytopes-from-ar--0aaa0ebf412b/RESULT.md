# Exact Minkowski asymmetry of acyclic unit-flow polytopes from arc antichains

## Finding

Let \(G=(V,E)\) be any finite directed acyclic graph with at least two distinct directed source-to-sink routes. The **unit-flow polytope** \(F(G)\) consists of all nonnegative arc vectors with flow conservation at non-source, non-sink vertices and total outflow \(1\) from all sources. Thus its vertices are the incidence vectors of source-to-sink routes.

Order the arcs by \(e\prec f\) if the head of \(e\) reaches the tail of \(f\) by a directed path (possibly a path of length zero). Let \(w\) denote the width, or largest antichain cardinality, of this arc poset. Then \(w\ge2\), and the Minkowski asymmetry of \(F(G)\), computed in its affine hull, satisfies
\[
\boxed{s(F(G))=w-1.}
\]
Moreover, **the complete set of minimizing Minkowski centers** is
\[
\boxed{\mathcal M(F(G))=\{c\in F(G):c_e\ge 1/w\text{ for every }e\in E\}.}
\]
In the natural flow lattice, the Ehrhart codegree obeys
\[
\boxed{\operatorname{codeg}(F(G))=w=s(F(G))+1.}
\]
Consequently this affine invariant is computable in polynomial time: form the transitive closure of the arc precedence relation and compute a maximum matching in the corresponding bipartite poset graph. If the matching size is \(\nu\), then \(w=|E|-\nu\).

**Example (a non-Gorenstein product).** Take a source with three two-arc branches meeting at a middle vertex, then two two-arc branches leading to the sink. Its route polytope is affinely \(\Delta_2\times\Delta_1\). The arc-poset width is \(3\), so the asymmetry is \(2\) and the lattice codegree is \(3\). At an optimal center the three first-stage branch masses must equal \(1/3\), while each of the two second-stage masses may vary between \(1/3\) and \(2/3\), summing to \(1\). Thus the set of minimizing centers is a nondegenerate line segment, even though the polytope is not Gorenstein.

## Assumptions and scope

The graph is finite and acyclic, may have several sources and sinks, and may be disconnected. Each edge is a directed arc and every arc belongs to at least one source-to-sink route. A source has zero indegree and a sink zero outdegree; isolated vertices are immaterial. A route is a maximal directed path beginning at a source and ending at a sink. The restriction to at least two routes ensures positive affine dimension; the assertion is not made for a singleton polytope. Parallel arcs, if present, are treated as distinct coordinates.

Write \(\chi_R\in\{0,1\}^E\) for a route-incidence vector. Flow conservation means \(\sum_{e:\operatorname{head}(e)=v}x_e=\sum_{e:\operatorname{tail}(e)=v}x_e\) at every nonterminal vertex \(v\). Total strength is \(\sum_{v\text{ a source}}\sum_{e:\operatorname{tail}(e)=v}x_e=1\). For a positive-dimensional convex body \(P\), our asymmetry convention is
\[
s(P)=\min_{c\in P}\inf\{\lambda\ge1:-(P-c)\subseteq\lambda(P-c)\}.
\]
Its relative lattice is \(\operatorname{aff}(F(G))\cap\mathbb Z^E\); the codegree is the smallest positive integer \(k\) for which \(\operatorname{relint}(kF(G))\) contains an integer point.

## Proof

**1. Routes, the arc poset, and minimum coverage.** Repeatedly following an arc with positive flow in a finite directed acyclic graph must lead from a source to a sink. Subtracting the minimum positive flow along such a route and iterating decomposes every unit flow into a convex combination of route-incidence vectors. Hence
\[
F(G)=\operatorname{conv}\{\chi_R:R\text{ a source-to-sink route}\}.
\]
In particular every arc is used by at least one route. The relation \(\prec\) is a strict partial order: a directed cycle would be required to have \(e\prec e\) or both \(e\prec f\) and \(f\prec e\). A route's arcs form a chain, while any finite chain can be joined by the connecting directed paths witnessing precedence and extended at either end to a full source-to-sink route. Consequently covering all arcs by routes is equivalent to covering the arc poset by chains. Dilworth's chain-partition theorem shows that the minimum number of routes covering all arcs is exactly the width \(w\). Choose such a cover \(R_1,\ldots,R_w\), allowing different routes to share arcs.

**2. Lower bound for asymmetry.** Let \(c\in F(G)\), and suppose
\[
-(F(G)-c)\subseteq\lambda(F(G)-c).
\]
Equivalently \((\lambda+1)c-x\in\lambda F(G)\) for every \(x\in F(G)\). For any arc \(e\), some route \(R\) contains it; nonnegativity of the \(e\)-coordinate of \((\lambda+1)c-\chi_R\) therefore yields \(c_e\ge1/(\lambda+1)\). Choose an antichain \(A\subseteq E\) of cardinality \(w\). Each route contains at most one arc of \(A\), so convexity gives \(\sum_{e\in A}c_e\le1\). It follows that
\[
1\ge\sum_{e\in A}c_e\ge\frac{w}{\lambda+1},\qquad \lambda\ge w-1.
\]
Since there are at least two routes, \(w\ge2\): if all arcs belonged to a single precedence chain, all routes would necessarily use the same sequence of arcs.

**3. A matching center and complete characterization.** Define
\[
c_0=\frac1w\sum_{i=1}^w\chi_{R_i}\in F(G).
\]
The route cover ensures \((c_0)_e\ge1/w\) for each arc. More generally let \(c\in F(G)\) satisfy \(c_e\ge1/w\) for all \(e\). For every route \(R\), the vector \(wc-\chi_R\) is coordinatewise nonnegative, satisfies flow conservation, and has total strength \(w-1\). Thus \(wc-\chi_R\in(w-1)F(G)\). By convexity the same containment holds with \(\chi_R\) replaced by any \(x\in F(G)\). Therefore
\[
-(F(G)-c)\subseteq(w-1)(F(G)-c),
\]
attaining the lower bound. Conversely any center attaining \(w-1\) must obey \(c_e\ge1/w\) by Step 2. This proves both formulas for the asymmetry and its complete center set.

**4. Lattice codegree.** The relative interior of the unit-flow polytope is precisely the set of feasible flows with strictly positive arc coordinates. Indeed \(F(G)\) is the intersection of its affine conservation-and-strength space with coordinate halfspaces \(x_e\ge0\), and each such coordinate is positive somewhere in \(F(G)\), because every arc occurs in a route. Hence an integer point in \(\operatorname{relint}(kF(G))\) is an integer flow of total strength \(k\) that is positive on every arc. Integer path decomposition in an acyclic graph expresses it as the sum of exactly \(k\) route-incidence vectors. Such a point exists if and only if those \(k\) routes cover every arc. By Step 1 the minimum \(k\) is \(w\). The matching formula is the standard constructive proof of Dilworth's theorem, applied to the transitive closure of the arc poset.

## Verification

The accompanying standalone Python 3 program `verify.py` uses only standard-library integer arithmetic. It enumerates all nonempty topologically ordered DAGs on \(3\), \(4\), and \(5\) vertices, together with \(300\) reproducibly seeded examples on \(6\) vertices. It enumerates every source-to-sink route and checks the arc-poset precedence matrix, all antichains, the minimum route-cover size, the exact covering-center construction, and all reflected vertices. In total the test reports \(1{,}393\) graphs, \(5{,}538\) routes, \(47{,}468\) antichains, and \(5{,}228\) covering routes. The finite checks support—but do not substitute for—the unrestricted proof above. Reproduce by running `python3 verify.py`.

## Relationship to prior work

Von Bell, Braun, Bruegge, Hanely, Peterson, Serhiyenko and Yip study strength-one acyclic flow polytopes and their triangulations, poset structures and Gorenstein criteria [1]. Their route-vertex formulation is used here; the inspected material does not state a Minkowski-asymmetry classification by the width of an arc poset. Braun and Cornejo investigate Gorenstein flow polytopes [2], and, for specially balanced DAGs, use an edge-disjoint route partition to determine codegree. Such partitions form a proper special setting: the theorem here uses possibly overlapping minimal route **covers** in arbitrary DAGs, including non-Gorenstein polytopes, and additionally determines asymmetry and every optimal center. Dilworth's classical theorem [3] connects arc antichains with route covers, but does not by itself formulate the geometric containment argument. Integrally equivalent order-polytope descriptions available for some planar DAGs do not cover all acyclic digraphs considered here.

## Limitations

The statement excludes zero-dimensional flow polytopes and does not address networks with directed cycles, capacity constraints, or nonunit source-sink demands. The entire graph must be acyclic. The codegree identity uses the natural integral flow lattice. The verification program is finite and is not an exhaustive test over all directed acyclic graphs. While comparisons with directly related primary literature did not reveal an equivalent result, an alternative formulation through general lattice-polytope symmetry theorems remains a bibliographic-priority risk; no independent priority or correctness audit has been performed.

## References

1. M. von Bell, B. Braun, K. Bruegge, D. Hanely, Z. Peterson, K. Serhiyenko and M. Yip, *Triangulations of Flow Polytopes, Ample Framings, and Gentle Algebras*, arXiv:2203.01896v1 (first posted 2022-03-03), https://arxiv.org/abs/2203.01896 .
2. B. Braun and A. Cornejo, *Equatorial Flow Triangulations of Gorenstein Flow Polytopes*, arXiv:2408.05320v1 (first posted 2024-08-09), https://arxiv.org/abs/2408.05320 .
3. R. P. Dilworth, *A decomposition theorem for partially ordered sets*, Annals of Mathematics **51** (1950), 161–166.
