# Integral and equivariant homology of three-cut complexes of rook graphs

## Finding

For integers \(m,n\ge3\), let \(G_{m,n}=K_m\mathbin{\square}K_n\) be the Cartesian product of complete graphs, with vertices \([m]\times[n]\) and edges between vertices sharing a row or a column. Write \(N=mn\), and let \(\Delta=\Delta_3(G_{m,n})\) denote the **ordinary** three-cut complex: its facets are the complements of the three-element sets inducing disconnected subgraphs. Then
\[
\widetilde H_d(\Delta;\mathbb Z)=
\begin{cases}
\mathbb Z^{\binom m2\binom n2-(m-1)(n-1)},&d=mn-5,\\
0,&d\ne mn-5.
\end{cases}
\]
The complex is pure of dimension \(mn-4\) and is **not shellable**.

There is also a complete integral coordinate-permutation representation. Let \(P_r=\mathbb Z^r\) be the natural permutation lattice, with basis \(e_i\), and let \(W_r=\ker(P_r\xrightarrow{\sum}\mathbb Z)\). Put
\[
\phi:\bigwedge^2P_m\otimes\bigwedge^2P_n\longrightarrow W_m\otimes W_n,
\qquad
\phi((e_i\wedge e_j)\otimes(f_k\wedge f_\ell))
 =(e_i-e_j)\otimes(f_k-f_\ell).
\]
This homomorphism is surjective. Writing \(L_{m,n}=\ker\phi\), the natural \(S_m\times S_n\)-module satisfies
\[
\widetilde H_{mn-5}(\Delta;\mathbb Z)
\cong \mathbb Z_{\varepsilon_{m,n}}\otimes\operatorname{Hom}_{\mathbb Z}(L_{m,n},\mathbb Z),
\qquad \varepsilon_{m,n}(\sigma,\tau)
=\operatorname{sgn}(\sigma)^n\operatorname{sgn}(\tau)^m.
\]
In particular, defining \(f(\sigma)\) to be the number of fixed points and \(t(\sigma)\) the number of two-cycles of \(\sigma\), the full rational character is
\[
\chi(\sigma,\tau)=\varepsilon_{m,n}(\sigma,\tau)\Big[
\big(\tbinom{f(\sigma)}2-t(\sigma)\big)
\big(\tbinom{f(\tau)}2-t(\tau)\big)
-(f(\sigma)-1)(f(\tau)-1)
\Big].
\]

## Assumptions and scope

The statement uses the original *ordinary* cut-complex definition, not a total cut complex. The inequalities \(m,n\ge3\) deliberately exclude the previously studied clique prism, which has one factor of order two. No claim is made for other cut sizes. Coordinate swapping when \(m=n\) lies outside the stated action \(S_m\times S_n\).

## Proof

**1. Alexander dual and its exact facets.** Set \(\Gamma=\Delta^\vee\) using combinatorial Alexander duality on all \(N\) graph vertices. Thus a vertex subset \(S\) belongs to \(\Gamma\) precisely if it contains no disconnected induced triple. Suppose \(S\) has a nonadjacent pair \(a=(i,k)\) and \(b=(j,\ell)\), with \(i\ne j\) and \(k\ne\ell\). Any other vertex of \(S\) must be adjacent to both \(a\) and \(b\), for otherwise these three vertices induce a disconnected triple. The only common neighbors are \((i,\ell)\) and \((j,k)\). Hence \(S\) lies in the corresponding four-vertex rectangle. If \(S\) contains no nonadjacent pair, it is a clique of the rook graph and hence lies entirely in one row or one column. Conversely, any set inside one row, one column, or a four-vertex rectangle has every triple connected. It follows that the maximal faces of \(\Gamma\) are exactly the \(m\) row simplices, the \(n\) column simplices, and the \(\binom m2\binom n2\) rectangle tetrahedra.

**2. Relative cellular homology.** Let \(B\subset\Gamma\) be the union of the row and column simplices. Every nonempty intersection of one row simplex with one column simplex is a single vertex, all same-type distinct simplices are disjoint. The nerve lemma (or a simultaneous contraction of these simplices to stars) gives \(B\simeq K_{m,n}\), so \(H_1(B;\mathbb Z)\cong W_m\otimes W_n\) and \(H_i(B;\mathbb Z)=0\) for \(i\ge2\). Each rectangle tetrahedron intersects \(B\) in its four-cycle boundary. Distinct rectangle tetrahedra intersect each other only in faces already in \(B\). Thus by relative excision and the relative homology of a tetrahedron against its square perimeter,
\[
H_i(\Gamma,B;\mathbb Z)=0\quad(i\ne2),\qquad
H_2(\Gamma,B;\mathbb Z)\cong\bigwedge^2 P_m\otimes\bigwedge^2 P_n.
\]
Orient each square using the alternating orientations in its row pair and column pair. The boundary homomorphism in the pair long exact sequence sends its oriented relative class to the corresponding four-cycle in the bipartite nerve; it is exactly \(\phi\) above. Every simple bipartite four-cycle is in the image and these span \(W_m\otimes W_n\), hence \(\phi\) is surjective. The long exact sequence gives \(\widetilde H_2(\Gamma;\mathbb Z)=L_{m,n}\), with all other reduced homology zero. The kernel is a free lattice, and its rank is the difference of the ranks of the domain and target, namely \(\binom m2\binom n2-(m-1)(n-1)\). In fact the square relations kill the fundamental group of \(K_{m,n}\), and \(\Gamma\simeq\bigvee^{\operatorname{rank}L_{m,n}}S^2\); only its integral homology is required below.

**3. Equivariant Alexander duality.** Integral combinatorial Alexander duality gives
\[
\widetilde H_d(\Delta;\mathbb Z)\cong\widetilde H^{N-d-3}(\Gamma;\mathbb Z).
\]
Naturality under vertex permutations includes the orientation character of the full \(N\)-element vertex set, namely \(\varepsilon_{m,n}(\sigma,\tau)=\operatorname{sgn}(\sigma)^n\operatorname{sgn}(\tau)^m\). By the universal coefficient theorem, \(H^2(\Gamma;\mathbb Z)=\operatorname{Hom}(L_{m,n},\mathbb Z)\), with no torsion. This proves the integral module and degree statements. Since the character of \(\bigwedge^2P_r\) at \(\sigma\) is \(\binom{f(\sigma)}2-t(\sigma)\), and that of \(W_r\) is \(f(\sigma)-1\), taking the virtual difference in the exact sequence and applying the orientation twist proves the rational formula.

**4. Shellability boundary.** Every facet of \(\Delta\) has \(N-3\) vertices, so \(\dim\Delta=N-4\). The homology group in degree \(N-5\) has positive rank when \(m,n\ge3\), and is strictly below the top dimension. A pure shellable simplicial complex has reduced homology concentrated in its top dimension; thus \(\Delta\) cannot be shellable.

## Verification

The accompanying standalone `verify.py` constructs both complexes directly from every induced triple, independently verifies the complete maximal-face classification for sizes \((m,n)=(2,3),(3,3),(3,4)\), and computes all augmented boundary ranks over \(\mathbb F_2\). It also calculates signed simplicial Lefschetz traces on \(\Delta\) for all \(12+36+144=192\) coordinate automorphisms of these cases, checking the formula and orientation twist. A complete run reports `VERIFY_OK`. These finite checks supplement the all-parameter proof; they do not substitute for it.

## Relationship to prior work

Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram, and Xue introduced ordinary cut complexes and examined the clique prisms \(K_n\mathbin{\square}K_2\), complete multipartite graphs, and other families in *Topology of Cut Complexes of Graphs*. Their subsequent *Topology of Cut Complexes II* treats rectangular **path-grid graphs** \(P_m\mathbin{\square}P_n\) and other families. Neither of these full texts gives the above complete integral, equivariant ordinary three-cut classification for \(K_m\mathbin{\square}K_n\) with both factors at least three. Rook graphs are also the line graphs of complete bipartite graphs, whereas the latter's matching/chessboard complexes are different complexes.

## Limitations

The representation statement is for coordinate permutations only; it does not resolve the additional factor-swap action when \(m=n\). The non-shellability conclusion does not characterize more refined homotopy invariants of \(\Delta\) such as its full cup-product or simple-homotopy type. Unindexed equivalent literature may exist; absence from the searched literature cannot certify priority. No external independent validation has occurred.

## References

1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first submitted 26 April 2023, Sections 1, 6 and 7 (especially Section 7.3).
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram, L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158, first submitted 11 July 2024, Section 5.
