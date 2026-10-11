# Symmetric-group characters and contractible quotients of rank-span-two Boolean complexes
## Finding
For every integer \(n\ge4\), let \(P_n\) be the poset of nonempty proper subsets of \([n]=\{1,\ldots,n\}\) ordered by strict inclusion. Let \(K_n\) be the rank-span-two filtered order complex: its simplices are strict chains \(A_0\subsetneq\cdots\subsetneq A_r\) for which \(|A_r|-|A_0|\le2\). The symmetric group \(S_n\) acts on \(K_n\) by permuting ground-set labels.

**Theorem.** The complex \(K_n\) is homotopy equivalent to \(\beta_n\) copies of \(S^2\) joined at a point, where
\[
\beta_n=2^{n-3}(n^2-5n+8)-n^2+3n-3.
\]
Its reduced integral homology is therefore free, supported only in degree two. If \(g\in S_n\) has \(c\) cycles in total, \(f\) fixed letters, and \(t\) cycles of length two, then its complete rational degree-two homology character is
\[
\boxed{\operatorname{tr}\!\left(g\mid\widetilde H_2(K_n;\mathbb Q)\right)=2^c-3-(f+t)(2^{c-1}-2)+\binom f2(2^{c-2}-2).}
\]
The last summand is defined to be zero when \(f<2\). In addition, the **topological quotient** \(|K_n|/S_n\) is contractible, not merely rationally acyclic. Hence \(\widetilde H^*(|K_n|/S_n;\mathbb Q)=0\).

## Assumptions and scope
The rank of a subset is its cardinality; rank span means the difference between maximum and minimum cardinalities of vertices in one chain, not the choice of a fixed set of ranks. A simplex of \(K_n\) has dimension at most two. All assertions hold for each integer \(n\ge4\), without stabilization or genericity assumptions. The character expression is an equality of actual traces on rational homology, not an assertion of a canonical basis.

## Proof
**1. Simple connectivity and integral homotopy type.** Let \(L_n=\Delta(P_n)\) be the full order complex. This is the barycentric subdivision of the boundary of the \((n-1)\)-simplex and therefore \(|L_n|\cong S^{n-2}\). Since \(n\ge4\), \(L_n\) is simply connected. A cover relation in \(P_n\) is inclusion of sets whose cardinalities differ by one. For each inclusion edge \(A\subsetneq B\) of \(L_n\), replace the edge by any saturated path of cover relations from \(A\) to \(B\), which lies in \(K_n\). Any two such saturated paths differ by adjacent transpositions of the order of added letters. Each adjacent transposition is a homotopy in \(K_n\): the two two-edge paths around \(A\subsetneq A\cup\{i,j\}\) are joined by the two triangles using the rank-gap-two diagonal. Here the notation \(A\) denotes the subset at the moment of the swap; it may vary through the path.

Consequently, for any three comparable vertices \(A\subsetneq B\subsetneq C\) of \(L_n\), the saturated replacements of its three edges form a null-homotopic loop in \(K_n\), since the direct replacement from \(A\) to \(C\) and the concatenation via \(B\) differ only in their ordering of added letters. Every edge of \(L_n\) thus has a homotopic cover-path replacement, and every triangular relation of the simply connected \(L_n\) becomes a relation in \(K_n\). This proves \(\pi_1(K_n)=0\). In particular, \(K_n\) is connected. Since \(K_n\) is two-dimensional, its integral \(H_2\) is free. The Hurewicz isomorphism and the homology version of Whitehead's theorem give \(K_n\simeq\bigvee^{\beta_n}S^2\), with multiplicity obtained below. These are homotopy equivalences, not asserted equivariant homotopy equivalences.

**2. Face counts.** The number of vertices is \(v=2^n-2\). Every edge has rank gap one or two. There are \(e_1=n(2^{n-1}-2)\) rank-gap-one edges: choose the newly added letter and any nonempty subset of its complement that does not produce the full set. There are \(e_2=\binom n2(2^{n-2}-2)\) gap-two edges. Each gap-two edge has exactly two intermediate one-letter subsets, and thus determines exactly two triangles. Therefore \(e=e_1+e_2\) and \(q=2e_2\). For a connected simply connected two-complex, reduced Euler characteristic equals the rank of \(H_2\); hence
\[
\beta_n=v-e+q-1=2^n-3-n(2^{n-1}-2)+\binom n2(2^{n-2}-2).
\]
Expanding the right-hand side gives the stated closed form; it is positive for all \(n\ge4\).

**3. All permutation traces.** Any permutation fixing a chain setwise fixes every chain vertex individually, because distinct chain vertices have different cardinalities. Thus there is no orientation sign from a nontrivial permutation of simplex vertices. Let the permutation have \(c\) cycles, \(f\) one-cycles and \(t\) two-cycles. A fixed subset is a union of its cycles, so the number of fixed vertices is \(v_g=2^c-2\). A fixed rank-gap-one edge can add only a fixed letter, whence \(e_{1,g}=f(2^{c-1}-2)\). A fixed rank-gap-two edge must add either two distinct fixed letters or a complete two-cycle, whence
\[
e_{2,g}=\binom f2(2^{c-2}-2)+t(2^{c-1}-2).
\]
The first term is zero if \(f<2\). A fixed two-simplex adds two distinct fixed letters in one of their two orders, giving
\[
q_g=f(f-1)(2^{c-2}-2),
\]
under the same zero convention. Each factor of the form \(2^a-2\) deletes exactly the two invalid choices making the initial subset empty or the terminal subset full; the conditions \(n\ge4\) and the presence of the indicated cycles ensure that these choices are distinct whenever its coefficient is nonzero. As there is no reduced homology outside degree two, the reduced simplicial Lefschetz identity gives
\[
\operatorname{tr}(g\mid\widetilde H_2(K_n;\mathbb Q))=v_g-e_{1,g}-e_{2,g}+q_g-1.
\]
Simplifying proves the character formula. Because rational representations of a finite group are semisimple, these traces on all conjugacy classes determine the entire rational representation up to isomorphism.

**4. Topological orbit quotient.** An ordered inclusion flag is determined up to \(S_n\)-permutation by its strictly increasing sequence of cardinalities. The action preserves these ranks and therefore has no simplex inversions. Consequently, the quotient is the honest simplicial complex \(R_{n-1}\) on ranks \(1,\ldots,n-1\), in which a set of ranks is a face precisely when its maximum minus minimum is at most two. Equivalently, \(R_{n-1}\) is the clique complex of the square of the \((n-1)\)-vertex path. The first vertex is dominated by the next: all its cofaces can be extended to include the next rank. Removing this dominated endpoint repeatedly (and finally retaining the last vertex) provides a simplicial strong collapse to a point. Hence the quotient is contractible.

## Verification
A standalone standard-Python checker, `verify.py`, generates all simplices independently for \(4\le n\le8\), constructs the exact degree-two boundary over \(\mathbb F_2\), and verifies the predicted rank and Betti number. It also enumerates fixed simplices directly for a representative of every permutation cycle type (60 conjugacy classes in total), compares all signed Lefschetz traces to the formula, and checks the full face counts. The five measured Betti numbers are \(1,19,91,321,981\); the total number of simplices enumerated in these five cases is \(10{,}146\). Execute `python3 verify.py` from the folder containing the supplied script. Its successful final line starts with `VERIFY_OK`. Finite tests support but do not prove the infinite-family assertions; the argument above is the proof.

## Relationship to prior work
Kitajima's public 2025 poster introduces rank-function filtered order complexes and gives shellability and wedge-of-spheres results for appropriate posets; the later 2026 preprint develops the theory systematically. Those general **nonequivariant** statements account for the expected shape of the homotopy type. The contribution here is a concrete cycle-type formula determining the **entire** rational permutation character, together with an explicit contractible orbit quotient, for the proper Boolean lattice at rank span two. Hersh and Sundaram study **rank-selected** Boolean and geometric-lattice order complexes, where a fixed set of allowed ranks is chosen globally. A rank-span restriction instead takes the union of moving rank windows and is not a fixed-rank selection; their displayed stability statements do not directly give the present character or orbit-space assertion.

## Limitations
The assertion is limited to the proper Boolean lattice and to rank span two; it does not describe the characters for higher spans or general geometric lattices. It does not claim an equivariant wedge decomposition, an integral \(S_n\)-module splitting, or an explicit integral equivariant basis. The complete text of Kitajima's closely relevant preprint could not be inspected, so a prior equivalent character calculation in its uninspected portions remains a substantive originality risk. An unindexed equivalent treatment is also possible.

## References
1. Yoh Kitajima, "Filtered order complexes and magnitude homology of pure shellable posets," poster abstract, Arrangements in Osaka 2025, poster session December 15, 2025, https://sites.google.com/view/arrangements-in-osaka-2025/posters .
2. Yoh Kitajima, "Filtered order complexes and magnitude homology of finite graded posets," arXiv:2606.15241, first public version June 13, 2026, https://arxiv.org/abs/2606.15241 .
3. Patricia Hersh and Sheila Sundaram, "Stability and ribbon bases for the rank-selected homology of geometric lattices," arXiv:2604.06479, first public version April 7, 2026, https://arxiv.org/abs/2604.06479 .
