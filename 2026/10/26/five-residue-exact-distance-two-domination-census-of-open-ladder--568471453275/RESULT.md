# Five-residue exact-distance-two domination census of open ladders

## Finding

Let \(L_n=P_n\square K_2\), for each integer \(n\ge1\), and call \(D\subseteq V(L_n)\) an exact-distance-two dominating set when every vertex outside \(D\) has a vertex of \(D\) at **graph distance exactly two**. Put \(m=\lceil n/5\rceil\) and \(e=5m-n\in\{0,1,2,3,4\}\). The minimum size and the number \(H_n\) of minimum-cardinality such sets (vertices of the ladder individually distinguished) are
\[
\gamma_{h}(L_n)=2m,
\qquad
H_n=\left([t^e](1+t+t^2)^2(1+t+t^2+t^3+t^4)^{m-1}\right)^2.
\]
The coefficient formula is interpreted in the usual polynomial sense, including \(m=1\). It gives a complete structural classification of the optimizers and their multiplicities for every ladder. In particular \(H_{5m}=1\), and for fixed \(e\in\{0,1,2,3,4\}\) the number \(H_{5m-e}\) is a polynomial in \(m\) of degree \(2e\) with leading coefficient \(1/(e!)^2\), whenever \(m\ge1\) and \(5m-e\ge1\). For example, the counts for \(n=1,2,\dots,10\) are \(1,4,9,4,1,81,64,36,9,1\).

## Assumptions and scope

The graph has two horizontal paths of \(n\) vertices and one vertical rung at every column. Distance is ordinary shortest-path distance in this original connected ladder, not distance in a graph power. A selected vertex needs no distance-two witness; only omitted vertices do. A minimum set is counted once as a labeled vertex subset, without quotienting by reflection or row swapping. No asymptotic square-grid limit is assumed.

## Proof

Write vertices as \((i,r)\) with \(1\le i\le n\) and \(r\in\{0,1\}\). Their ladder distance is \(|i-j|+|r-s|\). Thus two distinct vertices are distance two exactly when they are in the same row at column difference two, or in different rows at column difference one. The parity \(i+r\pmod2\) is constant along all distance-two edges. For each of the two parity classes, exactly one vertex occurs in each column, with a distance-two edge between the vertices of columns \(i\) and \(j\) precisely when \(1\le |i-j|\le2\). Therefore the distance-two adjacency graph is the disjoint union of **two copies of the square of a path**, \(P_n^2\). The stated exact-distance domination problem is equivalent, vertex for vertex, to ordinary closed-neighborhood domination independently on those two copies.

A dominating set of the path square, written \(1\le c_1<\cdots<c_k\le n\), covers the consecutive radius-two intervals \([c_j-2,c_j+2]\cap[1,n]\). These intervals cover every column exactly when \(c_1\le3\), \(c_k\ge n-2\), and \(c_{j+1}-c_j\le5\) for all \(1\le j<k\). Each interval contains at most five columns, so \(k\ge\lceil n/5\rceil=m\); selecting centers at roughly five-column spacing supplies an \(m\)-element solution (the bounded nonnegative-slack construction below also supplies one). Hence the optimum is \(m\) in each parity class, or \(2m\) in the ladder.

For an optimum with \(k=m\), set the two endpoint deficits \(a_0=3-c_1\) and \(a_m=c_m-(n-2)\), both in \(\{0,1,2\}\), and the internal deficits \(a_j=5-(c_{j+1}-c_j)\in\{0,1,2,3,4\}\). They satisfy the exact telescoping identity
\[
 a_0+a_1+\cdots+a_m=5m-n=e.
\]
Conversely, any such bounded nonnegative tuple with this sum reconstructs a unique increasing center sequence via \(c_1=3-a_0\) and \(c_{j+1}=c_j+5-a_j\). The telescoping identity gives \(c_m=n-2+a_m\). The endpoints lie within \([1,n]\), and the positive inter-center gaps are at most five. Thus this is a bijection between all minimum path-square dominating sets and the coefficient's monomials, establishing the unsquared count. Since the two parity classes are vertex-disjoint and independent, each pair of their minimum sets gives one minimum ladder set and vice versa. Squaring proves the displayed formula.

For fixed \(e\le4\), expand the coefficient using the fact that \(1+t+\cdots+t^4\) has constant term one and coefficient of \(t\) one. Its \(e\)-th coefficient after exponentiation is a polynomial in \(m\) of degree \(e\), with leading coefficient \(1/e!\); multiplying by the fixed endpoint polynomial does not change that leading term. Squaring gives degree \(2e\) and coefficient \(1/(e!)^2\). For \(e=0\), there is only the all-zero deficit tuple, so \(H_{5m}=1\).

## Verification

A standalone checker `verify.py` accompanies this result. It constructs the exact-distance graph directly from the ladder metric, verifies the two-component path-square isomorphism, brute-forces the minimum set size and count for \(1\le n\le9\), and independently counts center sequences for \(1\le n\le18\). All values equal the unrestricted formulas. This finite check is corroboration, not the infinite proof.

## Relationship to prior work

The exact-distance-two definition is the established hop-domination notion. Das, Das and Sadhukhan (2026) investigate exact-distance domination of **square grids** with asymptotic coverage bounds and establish the square-grid density for distance two; they do not state the two-row ladder optimum multiplicity formula in the inspected article. Henning and Jafari Rad (2017) consider hop domination in general graphs. The 2026 honeycomb/butterfly network study treats different graph families. The key reduction to two path squares makes the optimum size elementary; the distinct contribution here is the exact all-order enumerator of *all* optimum solutions, including the five-residue polynomial growth law. No claim is made to originality of the definition or of elementary path-square domination bounds.

## Limitations

Only two-row open ladders and exact distance two are covered. This theorem does not address exact-distance \(k>2\), closed cylindrical ladders, general rectangular grids, or counts of nonminimum sets. Accessible search and manuscript inspection did not find an equivalent census, but absence from search results cannot guarantee publication uniqueness. Independent peer verification has not been performed.

## References

1. S. Das, S. Das, and A. Sadhukhan, *Exact-Distance Domination in Grid Graphs*, arXiv:2607.29648 (first public version July 31, 2026), https://arxiv.org/abs/2607.29648. The article considers square grids and asymptotic bounds, not the all-cardinality minimum-solution census for two-row ladders.
2. M. A. Henning and N. Jafari Rad, *On 2-Step and Hop Dominating Sets in Graphs*, Graphs and Combinatorics **33** (2017), 913–927, https://doi.org/10.1007/s00373-017-1789-0. Background definition and general results.
3. *Hop and 2-Hop Domination on Honeycomb and Butterfly Networks*, Symmetry **18** (2026), article 662, https://doi.org/10.3390/sym18040662. Other families, no exact ladder minimum-set enumeration identified.
