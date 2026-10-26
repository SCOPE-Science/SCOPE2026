# Locating-hop domination of complete prisms: exact enumerators and a five-column minimality transition

## Finding

Let \(H_n=K_n\square K_2\), where \(n\ge3\). A locating-hop dominating set is a subset \(S\) for which each vertex outside \(S\) has at least one vertex of \(S\) at distance exactly two, and any two vertices outside \(S\) have distinct sets of distance-two neighbors in \(S\).

Write \(A,B\subseteq[n]\) for the index sets selected in the two clique layers. **All** locating-hop dominating sets are exactly these three types:

1. \(A=\varnothing,B=[n]\), or \(B=\varnothing,A=[n]\).
2. \(|A|,|B|\ge2\) and \(|A\cup B|\ge n-1\).
3. Up to interchange of the layers, \(|A|=1\), and either \(|B|=n\), or \(|B|=n-1\) with \(A\subseteq B\).

Let \(P_n(z)\) count all such sets by their selected cardinalities and let \(Q_n(z)\) count the inclusion-minimal such sets. Then

\[
P_n(z)=(2z+z^2)^n+n(2z+z^2)^{n-1}-2n^2z^{n-1}-2nz^n+6\mathbf{1}_{\{n=3\}}z^2.
\]

\[
Q_n(z)=\begin{cases}
14z^3,&n=3,\\
56z^4,&n=4,\\
n(2^{n-1}-2n)z^{n-1}+(2n(n-1)+2)z^n,&n\ge5.
\end{cases}
\]

For \(n\ge5\), the minimum sets have \(n-1\) vertices; there are exactly \(n(2^{n-1}-2n)\) of them, each using one vertex in each of \(n-1\) columns, with at least two selected vertices in each layer. Exactly \(2n(n-1)+2\) additional inclusion-minimal sets have \(n\) vertices. At \(n=3,4\), all inclusion-minimal sets have minimum size. Thus

\[
\gamma_{lh}(H_n)=\begin{cases}n,&n=3,4,\\n-1,&n\ge5,\end{cases}
\qquad \Gamma_{lh}(H_n)=n\quad(n\ge3).
\]

## Assumptions and scope

The graphs are finite, undirected, and simple. In \(H_n\) the vertices are \((0,i),(1,i)\) for \(i\in[n]\); within either fixed layer, all distinct indices are adjacent, and the two vertices in any one column are adjacent. The distance-two open neighborhood contains vertices at graph distance **exactly** two, not merely at distance at most two. A set is inclusion-minimal if deleting any one of its selected vertices destroys locating-hop domination; because the property is upward closed, this is equivalent to containing no proper locating-hop dominating subset. These formulas concern labeled vertices, without quotienting by automorphisms. The usual locating-hop domination concept combines hop domination with the distinct-signature locating-hop condition.

## Proof

**Distance-two reduction.** In \(H_n\),
\[
N_2((0,i))=\{(1,j):j\ne i\},\qquad N_2((1,i))=\{(0,j):j\ne i\}.
\]
Consequently, the signature of an unselected vertex \((0,i)\) is \(B\setminus\{i\}\) in layer one; the opposite signatures are \(A\setminus\{i\}\). Signatures in opposite layers, whenever nonempty, live on disjoint vertex sets and are therefore distinct. For distinct unselected indices \(i,j\) in the same layer, their signatures coincide if and only if neither \(i\) nor \(j\) is selected in the opposite layer. Distinguishability in the first layer requires at most one index missing from \(A\cup B\), and the other layer has the same requirement. This is precisely \(|A\cup B|\ge n-1\).

**Nonemptiness.** If \(A\) is empty, a vertex in the other layer has no distance-two selected neighbor unless that other layer is full, giving type 1. For \(|A|,|B|\ge2\), removing one index from either layer still leaves a witness, so the union criterion is sufficient and necessary. If \(|A|=1\), a vertex in the opposite layer can have empty signature only at its unique selected index, if this opposite-layer vertex is omitted. Thus its index must belong to \(B\); additionally, the union criterion requires all but at most one index covered, giving exactly type 3. This proves the complete classification.

**All-set generating function.** First count all ordered layer selections with at most one entirely empty column. A nonempty column is chosen in one of three states, contributing \(2z+z^2\), and one entirely empty column may be selected in \(n\) ways. The resulting polynomial is \((2z+z^2)^n+n(2z+z^2)^{n-1}\). Delete the invalid configurations: (i) either layer empty with one index absent from the other, contributing \(2nz^{n-1}\); (ii) one layer containing a singleton, the other containing \(n-2\) indices disjoint from that singleton, contributing \(2n(n-1)z^{n-1}\); (iii) one layer containing a singleton at exactly the one index absent from an \((n-1)\)-set in the other layer, contributing \(2nz^n\). Types (i)--(iii) are disjoint for \(n\ge4\). When \(n=3\), the two orientations of type (ii) count the same \(6\) size-two selections twice; add \(6z^2\). This proves \(P_n\).

**Inclusion-minimal classification.** The sets with an empty layer are precisely the two full-layer sets. A set having one selected vertex in one layer is inclusion-minimal precisely when the other layer contains all but one index and the singleton belongs to that set. Indeed, when the opposite layer is full, one can remove the vertex at the singleton index; and in the indicated \((1,n-1)\) pattern, removing any chosen vertex violates the three-type criterion. These yield \(2n(n-1)+2\) sets of size \(n\).

For the remaining sets, both layers contain at least two vertices. If \(n\ge5\), a set is inclusion-minimal precisely when \(A\cap B=\varnothing\) and \(|A\cup B|=n-1\). In that case deleting any selected vertex reduces the union to \(n-2\), and neither layer can become a permitted singleton: the other selected layer contains at most \(n-3\) vertices. Conversely, if the union is full, at least one layer contains three selected vertices and one may delete a vertex while preserving the union lower bound and retaining at least two vertices in each layer. If the union misses exactly one index but its intersection is nonempty, the total selected cardinality is at least \(n\); at least one layer then contains three vertices, and one can delete an intersection vertex from that layer without changing the union. Hence those sets are not minimal. Choose the single missed index and partition the other \(n-1\) indices between the two layers, with at least two in each: their number is \(n(2^{n-1}-2n)\).

When \(n=4\), the only extra minimal sets with at least two selected vertices per layer have \(|A|=|B|=2\) and \(|A\cup B|\ge3\). All are inclusion-minimal because removing any vertex leaves a singleton layer with only two vertices selected in the other, forbidden by type 3. They number \(\binom42+4\cdot3\cdot2=6+24=30\). Adding the \(26\) singleton/empty-layer minima yields \(56\). When \(n=3\), the other two-or-more case cannot attain the required size lower bound as an inclusion-minimal set, and the \(2+2\cdot3\cdot2=14\) preceding sets are all the minima. This establishes \(Q_n\) and its extremal conclusions.

## Verification

Run `python3 check_locating_hop.py` using the accompanying standalone verifier. For \(n=3,4,5,6,7,8\), it constructs the adjacency graph from first principles, independently computes all distance-two neighborhoods by breadth-first search, tests every one of the \(2^{2n}\) vertex subsets against the *definition*, checks the characterization, and compares both exact polynomial coefficient tables and inclusion-minimality. In total, \(87{,}360\) subsets were enumerated. All comparisons passed. This is finite verification, not a proof for unbounded \(n\); the preceding proof is the basis of the infinite statement.

## Relationship to prior work

The locating-hop dominating-set definition is due to Canoy and Salasalan (2022). Pagcu, Malacas, and Canoy (2022) study locating-hop sets on joins and coronas, without the nonempty hop-domination requirement. The distance-two graph of \(H_n\), namely the graph whose edges join vertices of \(H_n\) at distance exactly two, is exactly the crown graph \(K_{n,n}-M_n\). Hence this finding is equivalently an **ordinary locating-domination classification and pair of polynomials for the crown graph**; that equivalence was explicitly included in the novelty comparisons. Work on ordinary locating domination of near-complete regular graphs does not cover this crown graph family (its bipartite adjacency structure is different). The 2022 literature on locating-domination polynomial enumerators provides general techniques but not these two explicit crown/prism polynomials in inspected material.

## Limitations

The original Canoy--Salasalan article was available by bibliographic abstract but not accessible as complete text. Its uninspected details, as well as other unindexed or differently worded crown-graph results, pose residual originality risk. The exact verified public date \(2022\text{-}10\text{-}31\) belongs to the accessible Pagcu--Malacas--Canoy source; the Canoy--Salasalan paper is known to have appeared earlier in 2022, but its precise day was not verified, so no earlier calendar date is asserted. No independent mathematical audit has occurred. No claims are made for graphs beyond \(K_n\square K_2\) with \(n\ge3\).

## References

1. S. R. Canoy Jr. and G. P. Salasalan, *Locating-Hop Domination in Graphs*, Kyungpook Mathematical Journal **62** (2022), 193--204. DOI: 10.5666/KMJ.2022.62.1.193. Abstract/metadata consulted; full text was not inspected.
2. E. M. Pagcu, G. Malacas, and S. R. Canoy Jr., *Locating Hop Sets in a Graph*, European Journal of Pure and Applied Mathematics **15** (2022), 1705--1715; published 2022-10-31. DOI: 10.29020/nybg.ejpam.v15i4.4500. Full text inspected (definitions, joins, corona, conclusions).
3. A. Gafur et al., *On Locating-Dominating Set of Regular Graphs*, Journal of Mathematics (2021), article 8147514. DOI: 10.1155/2021/8147514. Full online article inspected; its regular-graph families do not include the crown graphs used here.
