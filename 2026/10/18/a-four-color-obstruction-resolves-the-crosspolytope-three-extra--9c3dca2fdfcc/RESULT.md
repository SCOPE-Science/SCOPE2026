# A four-color obstruction resolves the crosspolytope three-extra-copy conjecture

## Finding
For every integer \(d\ge6\), the unit crosspolytope
\[
K_d=\left\{x\in\mathbb R^d:\sum_{i=1}^d|x_i|\le1\right\}
\]
has exact homothetic covering functional
\[
\gamma_{2d+3}(K_d)=\frac{d-1}{d}.
\]
Here \(\gamma_m(K_d)\) is the minimum positive \(\lambda\) for which at most \(m\) translates of \(\lambda K_d\) cover all of \(K_d\). This establishes the previously proposed all-dimension case of the three-extra-copy conjecture.

## Assumptions and scope
All distances below are in the \(\ell_1\) norm \(\|x\|_1=\sum_i|x_i|\). The translates may have arbitrary real centers. All sets are closed, and coverings must include every point of the body. The new assertion is for every integer \(d\ge6\); earlier-dimensional instances were already established in the source literature.

For \(i\in\{1,\ldots,d\}\), write \(e_i\) for the standard basis vector. The \(2d\) vertices of \(K_d\) are \(\pm e_i\). Each sign vector \(\sigma\in\{-1,+1\}^d\) labels a facet with barycenter \(u_\sigma=\sigma/d\). Define \(H_d\) on the sign vectors by joining distinct \(\sigma,\tau\) precisely when their Hamming distance is at least \(d-1\). This is the binary Hamming-distance graph \(H_2(d,d-1)\) in the notation of Harney and Gluesing-Luerssen.

## Proof
Put \(r=(d-1)/d\).

**Upper bound.** We claim that the \(2d\) translates \(rK_d+e_i/d\) and \(rK_d-e_i/d\), for \(1\le i\le d\), cover \(K_d\). Fix \(x\in K_d\), set \(s=\|x\|_1\le1\), and choose a coordinate with \(t=|x_i|\ge s/d\). Choose the center \(\varepsilon e_i/d\) whose nonzero sign agrees with \(x_i\) (arbitrary for a zero coordinate). Then
\[
\left\|x-\varepsilon e_i/d\right\|_1=s-t+|t-1/d|.
\]
If \(t\ge1/d\), this is \(s-1/d\le r\). If \(0\le t\le1/d\), it equals \(s+1/d-2t\), which is at most \((d-2)t+1/d\le(d-1)/d=r\), because \(s\le dt\) and \(d\ge2\). Thus \(\gamma_{2d+3}(K_d)\le r\).

**Lower bound: vertices cannot share a copy.** Suppose, for a contradiction, that \(K_d\) is covered by at most \(2d+3\) translates of \(\lambda K_d\) with \(0<\lambda<r\). Any two distinct vertices \(v,w\in\{\pm e_i\}\) satisfy \(\|v-w\|_1=2\). Two points lying in a common translated \(\lambda K_d\) have \(\ell_1\) distance at most \(2\lambda<2\). Therefore the \(2d\) vertices occupy distinct covering copies, leaving at most three copies that contain none of these vertices.

**Lower bound: facet barycenters cannot share vertex copies.** Every facet barycenter \(u_\sigma=\sigma/d\) lies in \(K_d\). For any vertex \(v=\varepsilon e_i\), direct calculation gives
\[
\|u_\sigma-v\|_1=\begin{cases}
2(d-1)/d,&\varepsilon=\sigma_i,\\
2,&\varepsilon=-\sigma_i.
\end{cases}
\]
These distances are at least \(2r>2\lambda\). Hence no vertex-containing copy can contain a facet barycenter. All \(2^d\) barycenters must be covered by at most three remaining copies.

**Lower bound: a forbidden three-coloring.** If two sign vectors have Hamming distance \(h\), their facet barycenters have separation
\[
\|u_\sigma-u_\tau\|_1=2h/d.
\]
Whenever \(h\ge d-1\), this is at least \(2r>2\lambda\), so such barycenters cannot lie in the same remaining copy. Assign to each barycenter one of the (at most three) covering copies. That assignment would be a proper three-coloring of \(H_d\).

However, Harney and Gluesing-Luerssen, *On Robust Colorings of Hamming-Distance Graphs*, Theorem 3.3, establish \(\chi(H_2(d,d-1))=4\) for every \(d\ge3\). Their definition of adjacency is exactly Hamming distance at least \(d-1\), so the theorem applies with no change of graph. For completeness about its hypothesis, \(H_d\) is a cubelike graph with generators the all-one binary vector and the binary vectors obtained by changing one of its coordinates; it is nonbipartite. In fact, if \(d\) is odd the latter \(d\) generators have zero sum, an odd-length relation, while if \(d\) is even all \(d+1\) generators have zero sum, also an odd-length relation. The cited theorem derives the sharp lower chromatic bound from Payan's nonbipartite-cubelike theorem, and exhibits a four-coloring. Thus a proper three-coloring is impossible. This contradicts the hypothetical covering, proving \(\gamma_{2d+3}(K_d)\ge r\). Together with the upper bound, the asserted equality follows. \(\square\)

## Verification
The accompanying standalone \(checker.py\) performs exact-rational finite checks of the vertex separations, vertex-to-facet-barycenter separations, the Hamming-distance identification, the existence of the two-coordinate four-coloring, and the explicit covering on finite rational grids. It checks \(d=3,4,5,6,7,8\), with grid samples in the first three dimensions. All tests pass. No finite test is used to justify the unbounded chromatic theorem or the universal covering statement; those depend on the written argument and the cited theorem.

## Relationship to prior work
Antal Joós, *Covering the Crosspolytope with Crosspolytopes* (first arXiv posting 30 April 2023), proved the same covering ratio for \(2d,2d+1,2d+2\) copies in dimensions \(d\ge4\), and for \(2d+3\) copies only when \(d=4,5\). Its Conjecture 2 asks for the equality at \(2d+3\) copies for all \(d\ge6\). In his proof of Theorem 4, the incompatible pairs among facet barycenters are identified and low-dimensional cases are treated by hand. The present step recognizes the complete incompatible-pair graph as \(H_2(d,d-1)\), whose chromatic number is already known to equal four. Thus neither the 2023 covering results alone nor the earlier coloring theorem alone asserts this crosspolytope covering equality; their precise combination resolves the outstanding range.

Lian and Zhang (2021) worked in dimension three. Lian, Xia, Xue, and Zhang (2026) investigate asymptotic upper bounds for the different functional using \(2^d\) homothets; those upper bounds do not imply the present lower bound for \(2d+3\) homothets.

## Limitations
The assertion concerns translates of *positively scaled* unit crosspolytopes, not coverings by Euclidean balls, arbitrary orientations, or arbitrary centrally symmetric polytopes. It does not determine the next covering threshold at \(2d+4\) copies. The proof uses an established, nontrivial infinite-family chromatic-number theorem; the included checker independently tests only finite instances. The 2026 covering-functional article was accessible through its abstract and bibliographic data, not its full text, and an unindexed equivalent argument remains a bibliographic risk. Independent mathematical review has not been performed.

## References
1. Antal Joós, *Covering the Crosspolytope with Crosspolytopes*, arXiv:2305.00569v1 (30 April 2023); revised arXiv:2305.00569v2 (23 May 2023), Theorem 4 and Conjecture 2. Journal version: *Contributions to Discrete Mathematics* 20 (2025), 300–310, DOI: 10.55016/ojs/cdm.v20i2.77509.
2. Isaiah Harney and Heide Gluesing-Luerssen, *On Robust Colorings of Hamming-Distance Graphs*, arXiv:1609.00263 (first posted 1 September 2016), *Electronic Journal of Combinatorics* 25 (2018), #P4.3, Theorem 3.3, DOI: 10.37236/6495.
3. Yanlu Lian and Yuqin Zhang, *Covering the crosspolytope with its smaller homothetic copies*, arXiv:2103.10004 (2021), dimensional-three covering values.
4. Yanlu Lian, Yu Xia, Fei Xue, and Yuqin Zhang, *On the Covering Functionals of Simplices and Cross-Polytopes*, *Results in Mathematics* 81 (2026), article 82, DOI: 10.1007/s00025-026-02651-2; covering functional with \(2^d\) translates.
