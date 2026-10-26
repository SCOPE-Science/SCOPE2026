# The induced-matching polynomial of rectangular rook graphs

## Finding
For integers \(m,n\ge1\), the rectangular rook graph \(R_{m,n}=K_m\square K_n\) has induced-matching polynomial
\[
I_{m,n}(z)=\sum_{\substack{h,v\ge0\\h+2v\le m\\2h+v\le n}}
\frac{m!\,n!}{h!\,v!\,2^{h+v}(m-h-2v)!(n-v-2h)!}\,z^{h+v}.
\]
Here \(h\) is the number of selected edges lying within rows and \(v\) is the number lying within columns. In particular,
\[
\nu_s(R_{m,n})=\deg I_{m,n}=\min\left\{m,n,\left\lfloor\frac{m+n}{3}\right\rfloor\right\}.
\]

## Assumptions and scope
The graph \(R_{m,n}\) has vertices \((i,j)\), with \(1\le i\le m\) and \(1\le j\le n\); two distinct vertices are adjacent exactly when they share a row or a column. An induced matching is a set of edges such that no endpoint of one selected edge is adjacent to an endpoint of another selected edge. Write \(\nu_s(G)\) for the maximum size of an induced matching in \(G\). The polynomial includes the empty matching and counts labeled edges on the labeled rectangular board. The claim applies to all positive integers \(m,n\), including one-row or one-column boards.

## Proof
Every selected edge is either row-oriented or column-oriented. If there are \(h\) row-oriented edges and \(v\) column-oriented edges, their row coordinates must be all distinct across the \(h\) row indices and the \(2v\) endpoints of column-oriented edges. Likewise, their column coordinates must be all distinct across the \(2h\) endpoints of row-oriented edges and the \(v\) column indices of column-oriented edges. Thus a profile is feasible exactly when
\[
h+2v\le m,\qquad 2h+v\le n.
\]
For a fixed feasible profile, choose the \(h\) rows of row-oriented edges and the \(v\) columns of column-oriented edges. Choose and pair \(2v\) additional rows, assigning each pair to one of the chosen columns; this gives \(\binom{m}{h}\binom{m-h}{2v}(2v)!/2^v\) choices. Choose and pair \(2h\) additional columns, assigning each pair to one of the chosen rows; this gives \(\binom{n}{v}\binom{n-v}{2h}(2h)!/2^h\) choices. Their product simplifies to
\[
N_{m,n}(h,v)=\frac{m!\,n!}{h!\,v!\,2^{h+v}(m-h-2v)!(n-v-2h)!}.
\]
Summing \(N_{m,n}(h,v)z^{h+v}\) over the feasible profiles proves the polynomial formula.

For any feasible profile, the two inequalities imply \(h+v\le m\), \(h+v\le n\), and \(3(h+v)\le m+n\). Hence the degree is at most \(k=\min\{m,n,\lfloor(m+n)/3\rfloor\}\). To attain it, set \(h=\max\{0,2k-m\}\) and \(v=k-h\). Then \(h+2v=2k-h\le m\), while \(2h+v=h+k\le n\), using \(k\le m,n\) and \(3k\le m+n\). The feasible profile can be realized by choosing disjoint row and column coordinates as counted above, so a matching of size \(k\) exists. This proves the degree formula.

## Verification
The proof is symbolic and covers all positive \(m,n\). The included standard-library script independently enumerates induced matchings on each board with \(1\le m,n\le4\) and checks every polynomial coefficient against the formula. Those finite checks are supplemental; the all-parameter result follows from the proof, not from enumeration. The formula is also consistent with the equivalent interpretation of an induced matching in \(R_{m,n}=L(K_{m,n})\) as a vertex-disjoint packing of three-vertex paths in \(K_{m,n}\).

## Relationship to prior work
Induced matchings are a classical graph invariant, and prior work studies their computation on broad graph classes. A separate literature studies induced \(P_3\)-packing partition numbers in complete bipartite graphs when perfect or almost-perfect packings exist. The latter partition parameter is not the all-size enumerator proved here: it does not give the number of packings of each size or the profile counts \(N_{m,n}(h,v)\). Searches of published-finding corpus for the rook-graph induced-matching number, the equivalent complete-bipartite \(P_3\)-packing polynomial, and the strong-matching formulation returned related work but no directly covering formula. This is a best-knowledge novelty assessment, not a proof that no equivalent result exists.

## Limitations
No asymptotic analysis of the coefficients, weighted variant, or algorithmic application is established here. The enumerator is an exact benchmark for counting conflict-free pairs of adjacent positions on complete rectangular interaction boards; its broader use in statistical-mechanical or scheduling models is not developed. The literature search is not exhaustive, and independent audit has not been performed.

## References
1. K. Cameron, R. Sritharan, and Y. Tang, “Finding a maximum induced matching in weakly chordal graphs,” *Discrete Mathematics* 266 (2003), 133–142. DOI: 10.1016/S0012-365X(02)00803-8. First published 6 May 2003.
2. S. Klavžar and I. Peterin, “Characterizing subgraphs of Hamming graphs,” *Journal of Graph Theory* 49 (2005), 302–312. DOI: 10.1002/jgt.20084. First published 8 April 2005.
3. S. Maria Jesu Raja, I. Rajasingh, and A. Xavier, “Induced H-packing k-partition of graphs,” *International Journal of Computer Mathematics: Computer Systems Theory* (published online 15 January 2021). DOI: 10.1080/23799927.2020.1871418.
