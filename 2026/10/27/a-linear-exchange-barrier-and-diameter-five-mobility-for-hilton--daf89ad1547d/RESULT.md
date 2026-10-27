# A linear exchange barrier and diameter-five mobility for Hilton–Milner triple-system extremizers

## Finding
Let \(n\ge 7\) and let \(\mathscr E_n\) be the collection of **all** maximum-cardinality nontrivial pairwise-intersecting families of triples on \([n]\). A family is nontrivial if its members have empty total intersection. The classical Hilton–Milner equality classification gives \(|F|=3n-8\) for every \(F\in\mathscr E_n\), with exactly the two types defined below.

For an integer \(r\ge 0\), form the batch-exchange graph \(\mathcal R_r(n)\) on \(\mathscr E_n\): two distinct families \(F,G\) are adjacent when \(|F\setminus G|=|G\setminus F|\le r\). Thus an exchange replaces at most \(r\) *whole triples* simultaneously; all vertices of the graph must remain optimal and nontrivial, but the intermediate partial deletion/addition operations are not required to be valid families.

**Theorem.** For all \(n\ge7\), every \(\mathcal R_r(n)\) with \(r<n-4\) has no edges. At the sharp threshold \(r=n-4\), the graph is connected and self-centered with radius and diameter exactly \(5\). Its \((n-2)\binom n3\) vertices form a \(3(n-3)\)-regular graph with
\[
|E(\mathcal R_{n-4}(n))|=\tfrac32(n-2)(n-3)\binom n3.
\]
More precisely, its induced subgraph on the Hilton–Milner families with a fixed distinguished center is the Johnson graph \(J(n-1,3)\), and the only edges between distinct center layers pass through the triangle-type families according to the explicit rule in the proof. In particular, a growing batch of \(n-4\) triples is necessary for any move, yet at that first feasible batch size any two optimal families are at graph distance at most five.

## Assumptions and scope
Set \(V=[n]\), with \(n\ge 7\). All triples are unordered three-element subsets of \(V\). For each \(T\in\binom V3\), define the triangle-type family
\[
\mathcal A(T)=\{e\in\tbinom V3:|e\cap T|\ge2\}.
\]
For each \(x\in V\) and \(S\in\binom{V\setminus\{x\}}3\), define the Hilton–Milner family
\[
\mathcal H(x,S)=\{S\}\cup\{e\in\tbinom V3:x\in e,\ e\cap S\ne\varnothing\}.
\]
These are all the labeled extremizers by the \(k=3\) equality case of the classical Hilton–Milner theorem, also stated explicitly as Theorem 2 and Theorem 4(ii) in Polcyn–Ruciński [1]. The extremal characterization is preexisting; this result concerns the optimal-state exchange graph. The constructions are distinct for \(n\ge7\): \(x\) is the unique high-degree point in \(\mathcal H(x,S)\), \(S\) its unique triple avoiding \(x\), and \(T\) is determined by the three high-degree points in \(\mathcal A(T)\).

## Proof
**1. Complete overlap bound.** The common-triple counts between distinct extremizers follow by counting triples containing the displayed prescribed pairs. For distinct triangle types, putting \(j=|T\cap U|\), one obtains \(|\mathcal A(T)\cap\mathcal A(U)|=n,4,0\) for \(j=2,1,0\), respectively.

For distinct Hilton–Milner families with the same center \(x\), putting \(j=|S\cap R|\), the overlap is \(2n-4,n+2,9\) for \(j=2,1,0\), respectively. Indeed their special triples are different, so the overlap counts pairs meeting both \(S\) and \(R\), appended to their common center. For distinct centers, common triples are either of the form \(\{x,y,z\}\) or one of at most two exceptional special triples, giving an upper bound of \(n\).

For \(\mathcal A(T)\) and \(\mathcal H(x,S)\), if \(x\in T\) and \(j=|S\cap(T\setminus\{x\})|\), the overlap is \(2n-4,n,6\) for \(j=2,1,0\), respectively. If \(x\notin T\), the overlap is at most four: at most three triples of \(\mathcal A(T)\) contain \(x\), and the special triple \(S\) contributes at most one. For \(n\ge7\), all counts are strictly below \(2n-4\) except the indicated \(j=2\) cases. Since each family has \(3n-8\) triples, any two distinct extremizers require replacement of at least \((3n-8)-(2n-4)=n-4\) triples.

**2. Exact graph at the threshold.** Equality in the overlap bound occurs precisely in the following two cases:

* \(\mathcal H(x,S)\sim\mathcal H(x,R)\) when \(|S\cap R|=2\);
* \(\mathcal A(T)\sim\mathcal H(x,S)\) when \(x\in T\) and \(T\setminus\{x\}\subset S\).

There are no triangle–triangle edges and no edges between Hilton–Milner families with different centers. Each center layer is therefore \(J(n-1,3)\), with degree \(3(n-4)\). Each Hilton–Milner vertex also has exactly three triangle neighbors, obtained by choosing two of the three points of \(S\). Each triangle vertex has \(3(n-3)\) Hilton–Milner neighbors: choose its center from \(T\), then choose the third element of \(S\) outside \(T\). Therefore all vertices have degree \(3(n-3)\). The equality types number \(\binom n3+n\binom{n-1}3=(n-2)\binom n3\), and the handshaking identity gives the asserted edge count. The center layers are connected Johnson graphs; any pair of centers \(x,y\) is joined through a triangle family on \(\{x,y,z\}\), so the entire threshold graph is connected.

**3. Uniform diameter upper bound.** Every two Hilton–Milner vertices with the same center are at Johnson distance at most three. For different centers \(x\ne y\), choose \(z\in S\setminus\{y\}\). At cost at most one Johnson move, change \(S\) to a triple containing \(y,z\). From that vertex cross through \(\mathcal A(\{x,y,z\})\) to a \(y\)-centered Hilton–Milner vertex with special triple containing \(x,z\) and at least one point of the target \(R\). At most two Johnson moves then reach \(\mathcal H(y,R)\). Total length: at most \(1+2+2=5\).

If two triangle vertices share two base points, a common Hilton–Milner neighbor gives distance two. If they share one point, use two consecutive special triples in the Johnson layer centered at that point, giving distance three. If they are disjoint, choose an intermediate triangle with two points of the first triple and one of the second; the preceding two constructions yield a walk of length \(2+3=5\).

Finally, from \(\mathcal A(T)\) to \(\mathcal H(x,S)\), if \(x\in T\), first enter the \(x\)-center Johnson layer with a triple containing \(T\setminus\{x\}\) and at least one element of \(S\), and use at most two Johnson moves (total at most three). If \(x\notin T\), choose distinct \(y,a\in T\), go first to \(\mathcal H(y,(T\setminus\{y\})\cup\{x\})\), then via \(\mathcal A(\{x,y,a\})\) into the \(x\)-center layer, choosing a triple that contains \(y,a\) and meets \(S\). The last Johnson segment costs at most two moves, so the total is at most five.

**4. Diameter and radius lower bounds.** Choose disjoint three-sets \(T,U\) (possible for \(n\ge7\)). A path of length at most four between \(\mathcal A(T)\) and \(\mathcal A(U)\) would either stay within a single center layer, forcing \(T\cap U\ne\emptyset\), or have the shape triangle–Hilton–triangle–Hilton–triangle. In the latter case the intermediate triangle would share at least two elements with each of \(T\) and \(U\), impossible for disjoint triples. Thus their distance is five.

Every Hilton–Milner vertex \(\mathcal H(x,S)\) also has eccentricity at least five: choose \(T\) disjoint from \(S\cup\{x\}\), possible since \(n-4\ge3\). To reach \(\mathcal A(T)\), a path must change from center \(x\) to a center in \(T\) through a triangle vertex. A path of length at most four could permit at most one such center-changing bridge and at most one Johnson move on its two sides. If the bridging triangle is \(\{x,y,z\}\) with \(y\in T\) and \(z\in T\), reaching its \(x\)-layer neighbor requires inserting two elements of \(T\) into \(S\), costing at least two Johnson moves. If \(z\notin T\), the bridging \(y\)-layer special triple contains \(x,z\), whereas a final neighbor of \(\mathcal A(T)\) in that layer contains both elements of \(T\setminus\{y\}\); those two triples are at Johnson distance at least two, and inserting \(y\) on the \(x\)-side additionally costs a Johnson move. Either way a walk of length at most four is impossible. Thus every vertex has eccentricity five, and radius and diameter are both five.

## Verification
The standalone scripts `verify_bitset.py` and `verify_pairwise.py` independently build the two types of extremizers from their defining triple sets and compare all distinct pairs, rather than assuming the overlap formulas. They check membership sizes, unique labels, the absence of any shorter exchange, the exact adjacency cases, regularity, edge totals, and distances. The bitset program treats \(n=7,8,9,10\), using the two symmetric vertex types as breadth-first-search roots. The independently constructed frozenset implementation treats \(n=7,8,9\) and additionally checks every vertex's eccentricity at \(n=7\). Both were actually executed with Python's standard library; recorded stdout files accompany them. They verify finite instances only; the universal statement follows from the preceding arguments and the cited classification theorem.

## Relationship to prior work
The extremal cardinality \(3n-8\) and the two equality types are classical Hilton–Milner results, restated in Polcyn–Ruciński [1]. Kostochka–Mubayi [2] give more general structural results for large intersecting families of triples, again without the optimum-preserving batch-exchange graph. The existing independent-set reconfiguration literature, e.g. Bonsma [3], studies different reachability constraints (including non-optimal intermediate sets) and does not state this sharp extremizer-overlap threshold or the diameter-five graph. Published mathematical-record and database searches, including searches for Kneser-graph interpretations, did not reveal direct stronger coverage. The new assertion is the exact reconfiguration structure derived by a fresh casewise intersection analysis and global path arguments, not the preexisting extremal classification.

## Limitations
The theorem concerns labeled maximum **nontrivial** intersecting *triple* families for \(n\ge7\) only. It does not address near-extremizers, larger uniformity, single-triple transformations through suboptimal families, or step-by-step validity of intermediate deleted sets. The finite scripts are consistency checks, not proofs of the infinite theorem. A differently named or unindexed result may precede this overlap-graph analysis; independent publication-priority review has not been performed.

## References
[1] J. Polcyn and A. Ruciński, *A hierarchy of maximal intersecting triple systems*, arXiv:1608.06114v1, submitted 22 August 2016; Theorem 2, formulas for \(H_1,H_2\), Theorem 4(ii), and proof of Theorem 4. https://arxiv.org/html/1608.06114v1

[2] A. Kostochka and D. Mubayi, *The structure of large intersecting families*, arXiv:1602.01391, first submitted 3 February 2016; Introduction and results for triples. https://arxiv.org/abs/1602.01391

[3] P. Bonsma, *Independent Set Reconfiguration in Cographs and their Generalizations*, Journal of Graph Theory 83 (2016), 164–195; abstract specifies token addition/removal reachability for a different state space. https://doi.org/10.1002/jgt.21992
