# Translation-parity homology of ordinary three-cut complexes on toroidal grids

## Finding
Let \(m,n\ge 5\) be integers, \(N=mn\), and let \(G=C_m\mathbin{\square}C_n\) be the Cartesian product of two cycles. The ordinary three-cut complex \(X=\Delta_3(G)\) has facets complementary to disconnected induced triples. The translation group \(T=(\mathbb Z/m\mathbb Z)\times(\mathbb Z/n\mathbb Z)\) acts on \(X\). For a translation \(t=(a,b)\), put
\[
\sigma(t)=(-1)^{an(m-1)+bm(n-1)},\qquad B=\frac{N(N-13)}2+2.
\]
Here \(\sigma(t)\) is the sign of the induced permutation of the \(N\) vertices, and the equation \(2t=0\) is in \(T\). The complete reduced rational homology characters of \(X\) are
\[
\chi_{N-5}(t)=\sigma(t),\qquad
\chi_{N-4}(t)=\sigma(t)\begin{cases}
 B,&t=0,\\
 2-N/2,&t\ne0\text{ and }2t=0,\\
 2,&2t\ne0.
\end{cases}
\]
All other reduced rational homology vanishes. Thus these formulas determine the homology of \(X/H\) over \(\mathbb Q\) for **every** subgroup \(H\le T\), by taking the average of the displayed characters over \(H\).

In particular, the two potentially nonzero reduced rational Betti numbers of the full translation quotient \(|X|/T\) are
\[
\widetilde\beta_{N-5}(|X|/T;\mathbb Q)=
\begin{cases}1,&m\equiv n\pmod 2,\\0,&m\not\equiv n\pmod2,\end{cases}
\]
\[
\widetilde\beta_{N-4}(|X|/T;\mathbb Q)=
\begin{cases}
 (N-9)/2,&m,n\text{ both odd},\\
 (N-12)/2,&m,n\text{ both even},\\
 (N-13-(-1)^{N/2})/2,&m,n\text{ of opposite parity}.
\end{cases}
\]
The top one-dimensional homology of \(X\) therefore survives passage to the translation quotient exactly when the two cycle lengths have the same parity.

## Assumptions and scope
All graphs are finite simple graphs and all homology in the theorem has rational coefficients. The graph \(C_j\) means the ordinary \(j\)-cycle and the Cartesian product uses nearest-neighbor edges. The ordinary cut complex is distinct from the *total* cut complex. The quotient is the topological orbit space of the geometric realization, not the graph quotient followed by a new cut-complex construction. The bound \(m,n\ge5\) is used in the unique-square and unique-straight-two-path arguments; no assertion is made for smaller circumferences.

## Proof
**1. A concrete Alexander dual.** Let \(Y=X^\vee\) be the combinatorial Alexander dual on the same \(N\) vertices. By the definition of the three-cut complex, a set is a face of \(Y\) exactly when it contains no disconnected induced triple. Since \(G\) is triangle-free, every connected triple is a length-two induced path. It follows that \(Y\) contains all vertices, all \(\binom N2\) edges, and exactly \(6N\) triangles, with one triangle for each unordered pair of neighbors of a center vertex. Any four-vertex face has all four triples connected, so its induced graph is a four-cycle; these are precisely the \(N\) elementary square faces of the toroidal grid, each contributing a tetrahedron. There are no higher-dimensional faces: a five-element vertex set all of whose triples induce two edges would have \(3|E|=2\binom53=20\), an impossibility.

**2. Integral homotopy calculation.** Each of the \(2N\) length-two *straight* paths contains the edge between its endpoints, and this edge belongs to no other triangle or tetrahedron when \(m,n\ge5\). Collapse all these free edge–triangle pairs. Every remaining triangle is a corner of a unique elementary square. For each square, collapse its tetrahedron with one corner triangle, and then collapse one diagonal edge with its now-unique remaining incident triangle. The two remaining corner triangles triangulate the corresponding square along the other diagonal. These operations are independent between distinct squares because the diagonal edges and corner triangles belong to unique squares. The remaining two-dimensional subcomplex is a triangulated torus with \(N\) vertices, \(3N\) edges, and \(2N\) triangles. All other surviving edges were never part of any remaining triangle, so they attach as independent one-cells to this connected torus. Their number is
\[
\binom N2-2N-N-3N=\binom N2-6N=\frac{N(N-13)}2.
\]
Thus \(Y\simeq (S^1\times S^1)\vee\bigvee^{N(N-13)/2}S^1\), so \(\widetilde H_2(Y;\mathbb Q)\cong\mathbb Q\), \(\widetilde H_1(Y;\mathbb Q)\cong\mathbb Q^B\), and all other reduced groups vanish.

**3. The orientation character.** Orient the two cycles in their positive coordinate directions. For each elementary square with positively ordered corners \((v_{00},v_{10},v_{11},v_{01})\), take the oriented pair of triangles \([v_{00},v_{10},v_{11}]+[v_{00},v_{11},v_{01}]\). Summing over all squares produces a two-cycle \(z\), since interior grid edges cancel and both directions are periodic. It represents the generator of \(H_2(Y;\mathbb Q)\): the above collapses map it to the fundamental class of the triangulated torus. Every translation preserves this sum, hence \(\chi_{H_2(Y)}(t)=1\) for every \(t\in T\).

**4. The exact translation traces.** A nonidentity translation has no fixed vertex. It fixes no induced length-two-path triangle, since the path's unique middle vertex would have to be fixed; and it fixes no elementary square set, since a nontrivial shift cannot stabilize a two-element consecutive subset of either cyclic coordinate of length at least five. The only possibly stabilized edges in the complete one-skeleton are the \(N/2\) pairs swapped by a nonzero translation of order two; these contribute \(-N/2\) to the oriented one-chain trace. At the identity the unreduced chain-trace vector in dimensions zero through three is \((N,\binom N2,6N,N)\). The reduced Hopf trace formula
\[
\chi_{H_2(Y)}(t)-\chi_{H_1(Y)}(t)=\chi_{C_0(Y)}(t)-1-\chi_{C_1(Y)}(t)+\chi_{C_2(Y)}(t)-\chi_{C_3(Y)}(t)
\]
gives \(\chi_{H_1(Y)}(0)=B\), \(\chi_{H_1(Y)}(t)=2-N/2\) for nonzero order-two translations, and \(\chi_{H_1(Y)}(t)=2\) for all other nonidentity translations.

**5. Equivariant Alexander duality.** Combinatorial Alexander duality is equivariant after tensoring by the sign representation of the ground-set permutation: \(\widetilde H_i(X;\mathbb Q)\cong \operatorname{sgn}_N\otimes\widetilde H^{N-i-3}(Y;\mathbb Q)\). The dual of a translation representation has the same character here, because the preceding trace depends only on whether a translation is zero or has order two, and \(\sigma(t)=\sigma(t^{-1})\). In particular the character on \(\widetilde H_{N-5}(X)\) is \(\sigma\), and that on \(\widetilde H_{N-4}(X)\) is the trace from Step 4 multiplied by \(\sigma\). The sign of translation by one unit in the first coordinate is \((-1)^{n(m-1)}\), and similarly in the second coordinate it is \((-1)^{m(n-1)}\), yielding the formula for \(\sigma(a,b)\).

**6. Quotients.** For a finite group action on a finite complex, barycentric subdivision and averaging in characteristic zero identify \(H_*(|X|/H;\mathbb Q)\) with the \(H\)-invariant rational homology of \(X\). In particular, its Betti numbers are the character averages. The group \(T\) has \(0\), \(1\), or \(3\) nonzero elements of order two when the cycle lengths are respectively both odd, of opposite parity, or both even. If both lengths have the same parity, \(\sigma\) is trivial and the lower-degree average is \((N-9-t)/2\), with \(t=0\) or \(3\). In the opposite-parity case \(\sigma\) is nontrivial, its sum over \(T\) vanishes, and the unique nonzero order-two element has sign \((-1)^{N/2}\); the lower-degree average is then \((N-13-(-1)^{N/2})/2\). The top-degree average is respectively one or zero. This proves all claims.

## Verification
The included standalone `check_torus_translation.py` constructs the full Alexander dual through dimension three from the stated definitions. For \((m,n)=(5,5),(5,6),(5,8),(6,6),(6,7)\), it forms orbit-sum chain bases of the translation-invariant and sign-twisted chain complexes and computes their boundary ranks over \(\mathbb Q\) with sparse exact rational elimination. It verifies \(\partial^2=0\) and the predicted Betti numbers in each case; the output terminates with `TOROIDAL_CUT_TRANSLATION_INVARIANTS_OK`. The infinite-parameter theorem is proved in Steps 1–6, not inferred from these finite computations. Run with `python check_torus_translation.py` using Python's standard library.

## Relationship to prior work
The cut-complex definition and foundational nonequivariant and equivariant techniques were introduced by Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue (arXiv:2304.13675). Their sequel (arXiv:2407.08158) treats rectangular path-product grids and symmetry on cycles and graph unions; a toroidal product of two cycles with its full translation action is a distinct graph family and representation problem. The underlying toroidal-grid three-cut complex has a known nonequivariant sphere-and-circle Alexander-dual structure; that ungraded information alone does not determine the translation characters or the parity-dependent homology of translation quotients. No equivalence or stronger direct result was identified in the checked sources; unindexed literature may remain.

## Limitations
This is a rational representation and quotient-homology result. It does not determine integral torsion, quotient fundamental groups, or the action of reflections and coordinate swaps, and it assumes both cyclic lengths are at least five. The checker handles specified finite cases only. The literature comparison is based on identified accessible sources and is not an exhaustive proof that no equivalent result exists.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Topology of Cut Complexes of Graphs*, first posted 2023-04-26, arXiv:2304.13675, https://arxiv.org/abs/2304.13675 .
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram, L. Xue, *Topology of Cut Complexes II*, first posted 2024-07-11, arXiv:2407.08158, https://arxiv.org/abs/2407.08158 .
