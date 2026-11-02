# Geodetic and minimal-geodetic cardinality polynomials of crown graphs

## Finding
For every integer \(n\ge3\), let \(C_n\) be the crown graph with shores \(A=\{a_i:i\in[n]\}\) and \(B=\{b_i:i\in[n]\}\), in which \(a_i\) is adjacent to \(b_j\) exactly when \(i\ne j\). A vertex subset \(S\) is geodetic if every vertex lies on at least one shortest path between two vertices of \(S\), endpoints included. Let \(\mathcal G_n(z)\) count **all** geodetic sets by size, and \(\mathcal M_n(z)\) count inclusion-minimal geodetic sets by size.

The complete polynomials are
\[
\mathcal G_n(z)=(1+z)^{2n}-(1+2z)^n+2z^n
+\sum_{k=6}^{n}\binom nk\bigl(2^k-2-2k-k(k-1)\bigr)z^k
\]
and
\[
\boxed{\mathcal M_n(z)=nz^2+2z^n+\binom n3\binom{n-3}{3}z^6.}
\]
Here a binomial coefficient with nonnegative upper index smaller than its lower index equals zero, and an empty sum is zero; terms of equal degree are combined.

More precisely, with \(X=\{i:a_i\in S\}\) and \(Y=\{i:b_i\in S\}\), the set \(S\) is geodetic exactly when at least one of the following holds:

1. \(X\cap Y\ne\varnothing\).
2. \((X,Y)=([n],\varnothing)\) or \((\varnothing,[n])\).
3. \(X\cap Y=\varnothing\) and \(|X|,|Y|\ge3\).

The inclusion-minimal sets are exactly the \(n\) deleted-matching pairs \(\{a_i,b_i\}\), the two entire shores, and all sets obtained by choosing disjoint three-element index subsets \(X,Y\subseteq[n]\) and taking \(\{a_i:i\in X\}\cup\{b_j:j\in Y\}\).

Consequently the geodetic number is \(g(C_n)=2\), the *upper geodetic number* (largest size of an inclusion-minimal geodetic set) is \(g^+(C_n)=n\), and for \(n\ge7\) the complete attainable minimal-cardinality spectrum is \(\{2,6,n\}\). In particular, for \(n\ge8\), all sizes \(7,8,\ldots,n-1\) are absent. The total number of inclusion-minimal geodetic sets is \(n+2+\binom n3\binom{n-3}{3}\).

## Assumptions and scope
The graph is finite, simple, undirected, and connected for every \(n\ge3\). Every geodesic interval \(I[u,v]\) includes all vertices on **any** shortest \(u\)-to-\(v\) path; thus \(S\) is geodetic when \(\bigcup_{u,v\in S,\,u\ne v}I[u,v]=V(C_n)\). This differs from *strong geodetic* sets, which commit to one fixed shortest path per selected pair, and from iterative geodesic-hull sets. Inclusion-minimality means that deleting any one selected vertex destroys geodetic coverage; this is equivalent to excluding every proper geodetic subset because the property is upward closed.

## Proof
**1. Intervals and a matched pair.** Distinct same-shore vertices are at distance two. For distinct indices \(j,k\), the intermediate vertices of shortest paths from \(b_j\) to \(b_k\) are exactly \(a_i\) with \(i\notin\{j,k\}\); the symmetric assertion holds for selected \(a_j,a_k\). Opposite-shore vertices with distinct indices are adjacent and their interval consists only of the endpoints. The matched-index pair \(a_i,b_i\), though nonadjacent, is at distance three: for distinct \(j,k\not=i\) the path \(a_i,b_j,a_k,b_i\) has length three. As \(n\ge3\), varying \(j,k\) covers **every** vertex outside the pair. Thus any set containing a matched-index pair is geodetic.

**2. Necessity without a matched pair.** Suppose \(X\cap Y=\varnothing\). Because every cross-shore selected pair is adjacent, selected vertices in different shores add no nontrivial interval vertices. An omitted \(a_i\) can be covered only by a pair of selected vertices \(b_j,b_k\) with \(i\notin\{j,k\}\). Equivalently \(|Y\setminus\{i\}|\ge2\). Similarly an omitted \(b_i\) is covered exactly when \(|X\setminus\{i\}|\ge2\).

If \(X=\varnothing\), there are no selected \(A\)-endpoints and no paths with internal \(B\)-vertices, so every \(b_i\) must already be selected: \(Y=[n]\). Conversely that entire shore is geodetic since for each \(a_i\) there are two distinct \(b_j,b_k\) with indices other than \(i\). The symmetric case follows. If both \(X,Y\) are nonempty, take \(i\in X\). Then \(b_i\) is omitted (disjointness), so its coverage requires \(|X\setminus\{i\}|\ge2\), that is \(|X|\ge3\). Likewise \(i\in Y\) forces \(|Y|\ge3\). These inequalities suffice: when \(i\notin X\), its coverage by \(Y\) is automatic if \(i\notin Y\) since \(|Y|\ge3\), or if \(i\in Y\) since \(|Y|-1\ge2\). The same reasoning applies to omitted \(b_i\). Hence the stated three-case characterization is necessary and sufficient.

**3. Inclusion-minimal sets.** In the first case, one matched-index pair is already geodetic by step 1. Minimality therefore forces the selected set to be precisely that two-vertex pair. Without a matched pair, a full shore is minimal since deleting any vertex leaves a one-shore proper subset that fails the necessity argument in step 2. In the disjoint mixed-shore case, each shore must contain at least three selected vertices; removing any selected vertex preserves disjointness, so inclusion-minimality holds exactly when each shore contains precisely three vertices. These three families are disjoint and exhaustive. They contribute respectively \(nz^2\), \(2z^n\), and \(\binom n3\binom{n-3}{3}z^6\), proving the minimal polynomial.

**4. All-set polynomial.** At each index \(i\), a vertex subset has one of four states: neither vertex, only \(a_i\), only \(b_i\), or both. Sets containing at least one both-state are counted by \((1+z)^{2n}-(1+2z)^n\). The two entire shores contribute \(2z^n\). For disjoint mixed shores both of size at least three, choose \(k\) occupied indices, and assign each to \(A\) or \(B\). The number of assignments is \(2^k-2\sum_{j=0}^2\binom kj=2^k-2-2k-k(k-1)\). Summing from \(k=6\) to \(n\) gives the claimed all-set polynomial. Since the three structural families are disjoint, there is no double-counting.

**5. Consequences.** The first family establishes the minimum two; no singleton can be geodetic in the nontrivial graph. The largest of the three possible inclusion-minimal sizes \(2,n,6\) (with size six present only for \(n\ge6\)) is \(n\). For \(n\ge7\), all three sizes are distinct. The missing consecutive interval and total count follow from the polynomial. The family is connected, \((n-1)\)-regular, bipartite, and vertex-transitive, since exchanging shores and permuting all matched index-pairs transitively moves any vertex to any other.

## Verification
The accompanying Python 3 program `verify_crown_geodetic.py` builds the graphs independently, computes shortest-path distances by breadth-first search, constructs intervals by the distance identity \(d(u,w)+d(w,v)=d(u,v)\), then exhaustively checks every nonempty subset for \(3\le n\le9\). It independently tests the structural criterion, the two cardinality formulas, and inclusion-minimality by single-vertex deletions. The recorded successful run reported `VERIFY_OK graph_orders=7 tested_subsets=349497 structural_and_polynomial_agreement=true`. This finite experiment corroborates the proof but cannot establish the infinite theorem by itself.

## Relationship to prior work
Gledel and Iršič (2018, arXiv:1810.04004, Section 3) determine the **strong geodetic number** of crown graphs by fixing one geodesic per selected pair. That is a different, more restrictive covering convention; their scalar theorem does not enumerate ordinary geodetic sets or inclusion-minimal ordinary geodetic sets. Bergougnoux, Defrain, and Mc Inerney (2023, arXiv:2309.17419, Section 4) develop general algorithms and transversal reductions for enumerating minimal geodetic sets; their treatment does not provide this crown-graph structural classification or these closed polynomials. The geodetic-set and upper-geodetic-number notions precede both papers; no priority is claimed for those definitions or for the easy scalar minimum of two. Searches under deleted-perfect-matching, tensor-product, and bipartite-double-cover terminology found no implication of the full polynomial theorem. This is a best-knowledge literature comparison, not a guarantee of first publication.

## Limitations
The result concerns ordinary *all-shortest-path* geodetic coverage, not strong geodetic coverage, geodesic hull closure, connected geodetic sets, or edge-geodetic sets. The theorem assumes \(n\ge3\), because the deleted-matching graph at \(n=2\) is disconnected. It is a complete family-specific enumeration, not an algorithmic complexity result for arbitrary graphs. Publication priority remains provisional because older related literature, including some geodetic-polynomial papers, was not fully accessible. No independent mathematical audit has been performed.

## References
1. V. Gledel and V. Iršič, *Strong geodetic number of complete bipartite graphs, crown graphs and hypercubes*, arXiv:1810.04004, first public 9 October 2018. https://arxiv.org/abs/1810.04004
2. B. Bergougnoux, O. Defrain, and F. Mc Inerney, *Enumerating minimal solution sets for metric graph problems*, arXiv:2309.17419, first public 29 September 2023. https://arxiv.org/abs/2309.17419
3. G. Chartrand, F. Harary, and P. Zhang, *Geodetic sets in graphs*, Discussiones Mathematicae Graph Theory **20** (2000), foundational definitions and upper geodetic number (abstract accessible).
