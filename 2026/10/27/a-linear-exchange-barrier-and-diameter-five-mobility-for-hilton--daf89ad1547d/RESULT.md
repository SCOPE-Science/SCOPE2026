# A linear exchange barrier and diameter-five mobility for Hilton–Milner triple-system extremizers

## Finding
Let \(n\ge 7\) and let \(\mathscr E_n\) be the collection of **all** maximum-cardinality nontrivial pairwise-intersecting families of triples on \([n]\). A family is nontrivial if its members have empty total intersection. The classical Hilton–Milner equality classification gives \(|F|=3n-8\) for every \(F\in\mathscr E_n\), with exactly the two types defined below.

For an integer \(r\ge 0\), form the batch-exchange graph \(\mathcal R_r(n)\) on \(\mathscr E_n\): two distinct families \(F,G\) are adjacent when \(|F\setminus G|=|G\setminus F|\le r\). Thus an exchange replaces at most \(r\) *whole triples* simultaneously; all vertices of the graph must remain optimal and nontrivial, but the intermediate partial deletion/addition operations are not required to be valid families.

**Theorem.** For all \(n\ge7\), every \(\mathcal R_r(n)\) with \(r<n-4\) has no edges. At the sharp threshold \(r=n-4\), the graph is connected and self-centered with radius and diameter exactly \(5\). Its \((n-2)\binom n3\) vertices form a \(3(n-3)\)-regular graph with
\[
 |E(\mathcal R_{n-4}(n))|=\tfrac32(n-2)(n-3)\binom n3.
\]
Each induced subgraph on the Hilton–Milner families with a fixed distinguished center is the Johnson graph \(J(n-1,3)\). A path can change center only through a triangle-type vertex, with the incidence rule given below.

## Assumptions and scope
Set \(V=[n]\), with \(n\ge 7\). All triples are unordered three-element subsets of \(V\). For each \(T\in\binom V3\), define the triangle-type family
\[
\mathcal A(T)=\{e\in\tbinom V3:|e\cap T|\ge2\}.
\]
For each \(x\in V\) and \(S\in\binom{V\setminus\{x\}}3\), define the Hilton–Milner family
\[
\mathcal H(x,S)=\{S\}\cup\{e\in\tbinom V3:x\in e,\ e\cap S\ne\varnothing\}.
\]
These are all the labeled extremizers by the \(k=3\) equality case of the classical Hilton–Milner theorem, stated in Polcyn–Ruciński [1, Theorem 2]. The constructions are distinct for \(n\ge7\): \(x\) is the unique highest-degree point in \(\mathcal H(x,S)\), and \(S\) is its unique triple avoiding \(x\). The three highest-degree points in \(\mathcal A(T)\) determine \(T\). In particular the two types cannot coincide.

## Proof
**1. Complete overlap bound.** For distinct triangle types, putting \(j=|T\cap U|\), one obtains \(|\mathcal A(T)\cap\mathcal A(U)|=n,4,0\) for \(j=2,1,0\), respectively. When \(j=2\) there are \(n-2\) triples containing the common pair and two triples using just one point of that pair and both of the noncommon points. When \(j=1\), a common triple must use the common point and one point from each of the two disjoint remaining pairs. For \(j=0\), every candidate would require four points.

For distinct Hilton–Milner families with the same center \(x\), putting \(j=|S\cap R|\), the overlap is \(2n-4,n+2,9\) for \(j=2,1,0\), respectively. Their distinct special triples cannot contribute; the count by inclusion–exclusion of pairs meeting both \(S\) and \(R\) on \(V\setminus\{x\}\) is \(\binom{n-1}2-2\binom{n-4}2+\binom{n-7+j}2\), interpreted as zero for each binomial with fewer than two available points. For distinct centers, common triples are either of the form \(\{x,y,z\}\) or one of at most two exceptional special triples, giving an upper bound of \(n\).

For \(\mathcal A(T)\) and \(\mathcal H(x,S)\), if \(x\in T\) and \(j=|S\cap(T\setminus\{x\})|\), the overlap is \(2n-4,n,6\) for \(j=2,1,0\), respectively. Here the pair appended to \(x\) must hit both \(S\) and \(T\setminus\{x\}\), and \(S\) itself contributes precisely when \(j=2\). If \(x\notin T\), the overlap is at most four: at most three triples of \(\mathcal A(T)\) contain \(x\), and the special triple \(S\) contributes at most one. For \(n\ge7\), all counts are strictly below \(2n-4\) except the indicated \(j=2\) cases. Since each family has \(3n-8\) triples, any two distinct extremizers require replacement of at least \((3n-8)-(2n-4)=n-4\) triples.

**2. Exact graph at the threshold.** Equality in the overlap bound occurs precisely in the following two cases:

* \(\mathcal H(x,S)\sim\mathcal H(x,R)\) when \(|S\cap R|=2\);
* \(\mathcal A(T)\sim\mathcal H(x,S)\) when \(x\in T\) and \(T\setminus\{x\}\subset S\).

There are no triangle–triangle edges and no edges between Hilton–Milner families with different centers. Each center layer is therefore \(J(n-1,3)\), with degree \(3(n-4)\). Each Hilton–Milner vertex also has exactly three triangle neighbors, obtained by choosing two of the three points of \(S\). Each triangle vertex has \(3(n-3)\) Hilton–Milner neighbors: choose its center from \(T\), then choose the third element of \(S\) outside \(T\). Therefore all vertices have degree \(3(n-3)\). The equality types number \(\binom n3+n\binom{n-1}3=(n-2)\binom n3\), and the handshaking identity gives the asserted edge count. The center layers are connected Johnson graphs; any pair of centers \(x,y\) is joined through a triangle family on \(\{x,y,z\}\), so the entire threshold graph is connected.

**3. Uniform diameter upper bound.** Every two Hilton–Milner vertices with the same center are at Johnson distance at most three. For different centers \(x\ne y\), choose \(z\in S\setminus\{y\}\). At cost at most one Johnson move, change \(S\) to a triple containing \(y,z\). From that vertex cross through \(\mathcal A(\{x,y,z\})\) to a \(y\)-centered Hilton–Milner vertex with special triple containing \(x,z\) and at least one point of the target \(R\). At most two Johnson moves then reach \(\mathcal H(y,R)\). Total length: at most \(1+2+2=5\).

If two triangle vertices share two base points, a common Hilton–Milner neighbor gives distance at most two. If they share one point, enter the layer centered at that point and choose the two special triples so that each contains its required pair and the triples share two points. One Johnson move between the special triples gives a path of length three. If the bases are disjoint, choose an intermediate triangle with two points of the first triple and one of the second; the preceding two constructions yield a walk of length \(2+3=5\).

Finally, from \(\mathcal A(T)\) to \(\mathcal H(x,S)\), if \(x\in T\), first enter the \(x\)-center Johnson layer with a triple containing \(T\setminus\{x\}\) and at least one element of \(S\), and use at most two Johnson moves (total at most three). If \(x\notin T\), choose distinct \(y,a\in T\), go first to \(\mathcal H(y,(T\setminus\{y\})\cup\{x\})\), then via \(\mathcal A(\{x,y,a\})\) into the \(x\)-center layer, choosing a triple that contains \(y,a\) and meets \(S\). The last Johnson segment costs at most two moves, so the total is at most five.

**4. Diameter and radius lower bounds.** Choose disjoint three-sets \(T,U\). A path of length at most four between \(\mathcal A(T)\) and \(\mathcal A(U)\) would either use only one center layer, forcing \(T\cap U\ne\emptyset\), or have the shape triangle–Hilton–triangle–Hilton–triangle. Two distinct triangle vertices with a common Hilton–Milner neighbor have a common center and their respective noncenter pairs lie in the same special triple, so they share at least two base points. In the second path shape, the intermediate triangle would thus share at least two elements with each of \(T\) and \(U\), impossible because the bases are disjoint. Thus these triangle vertices are at distance five. Every triangle vertex admits such a disjoint base.

For each Hilton–Milner vertex \(\mathcal H(x,S)\), choose \(T\) disjoint from \(S\cup\{x\}\), possible since \(n-4\ge3\). A path to \(\mathcal A(T)\) must change from center \(x\) to some center in \(T\) before its final edge. A path of length at most four must have exactly one center-changing two-edge bridge, exactly one final edge to \(\mathcal A(T)\), and at most one Johnson move in total; an additional visit to a triangle before the final edge would already cost two further edges. Write the bridge as passing through \(\mathcal A(\{x,y,z\})\), with \(y\in T\). If \(z\in T\), reaching the \(x\)-side neighbor of the bridge requires inserting both \(y\) and \(z\) into \(S\), so needs at least two Johnson moves. If \(z\notin T\), the \(x\)-side still needs at least one Johnson move to insert \(y\). On the \(y\)-side, a bridge neighbor's special triple contains \(\{x,z\}\), whereas a final neighbor's special triple contains \(T\setminus\{y\}\). These are disjoint pairs, so no triple contains both, and at least one more Johnson move is needed on the \(y\)-side. In both cases at least two moves are needed, ruling out paths of length at most four. Thus every vertex has eccentricity five, and radius and diameter are both five.

## Verification
The standalone scripts `verify_bitset.py` and `verify_pairwise.py` build the two types of extremizers from their defining triple sets and compare all distinct pairs rather than assuming the overlap formulas. They check membership sizes, unique labels, absence of shorter exchanges, exact adjacency, regularity, edge totals and distances. The bitset program treats \(n=7,8,9,10\), using the two symmetric vertex types as breadth-first-search roots. The independently constructed frozenset implementation treats \(n=7,8,9\) and additionally checks every vertex's eccentricity at \(n=7\). The accompanying outputs record finite instances only; the universal statement follows from the proof and the cited classification theorem.

## Relationship to prior work
The extremal cardinality \(3n-8\) and the two equality types are classical Hilton–Milner results, restated in Polcyn–Ruciński [1]. Kostochka–Mubayi [2] give more general structural results for large intersecting families of triples. Intersecting triple families are independent sets of the Kneser graph, but the exchange graph here restricts every vertex to the nontrivial optimum sector and allows batches of replacements. For comparison, Bonsma [3] studies token addition/removal reachability, a different transition model. The contribution here is the threshold and exact reconfiguration structure for the restricted optimum sector.

## Limitations
The theorem concerns labeled maximum **nontrivial** intersecting *triple* families for \(n\ge7\) only. It does not address near-extremizers, larger uniformity, single-triple transformations through suboptimal families, or step-by-step validity of intermediate deleted sets. The finite scripts are consistency checks, not proofs of the infinite theorem. This comparison does not exclude differently named or unindexed equivalent results.

## References
[1] J. Polcyn and A. Ruciński, *A hierarchy of maximal intersecting triple systems*, arXiv:1608.06114v1, 22 August 2016, Theorem 2 and definitions of \(H_1,H_2\). https://arxiv.org/html/1608.06114v1

[2] A. Kostochka and D. Mubayi, *The structure of large intersecting families*, arXiv:1602.01391, 3 February 2016. https://arxiv.org/abs/1602.01391

[3] P. Bonsma, *Independent Set Reconfiguration in Cographs and their Generalizations*, Journal of Graph Theory 83 (2016), 164–195. https://doi.org/10.1002/jgt.21992
