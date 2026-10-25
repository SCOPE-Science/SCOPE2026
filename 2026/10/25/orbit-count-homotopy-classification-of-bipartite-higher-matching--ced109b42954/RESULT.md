# Orbit-count homotopy classification of bipartite higher-matching fixed spaces

## Finding
For an integer \(n\ge2\), let \(X_n=M_{n-1}(K_{n,n})\). Its vertices are the \(n^2\) cells of an \(n\)-by-\(n\) board; a face is a selection with no completely filled row or column. Let arbitrary subgroups \(H_L,H_R\le S_n\) act independently on the two parts, and put \(H=H_L\times H_R\). Let \(s\) and \(t\) be the numbers of row and column orbits.

**Theorem.** If \(s=1\) or \(t=1\), the geometric fixed-point space \(|X_n|^H\) is empty. For \(s,t\ge2\), it is piecewise-linearly homeomorphic to the realization of the forbidden-full-line complex \(N_{s,t}\) on an \(s\)-by-\(t\) board, and
\[
|X_n|^H\simeq S^{(s-1)(t-1)-1}.
\]
In particular the homotopy type depends only on the *numbers* of row and column orbits, not on their sizes or on the internal structure of the subgroups. Here \(S^0\) has two components; for all higher dimensions the fixed-point space is connected and its reduced integral homology has one generator in the displayed degree.

## Assumptions and scope
All groups are finite and act simplicially on the same underlying complex. The theorem covers every pair of row- and column-permutation subgroups, including the trivial groups, and hence every product subgroup of \(S_n\times S_n\). It does not cover arbitrary nonproduct subgroups or subgroups exchanging the two bipartite parts. Geometric fixed points refer to points fixed in the realization, rather than the subcomplex on pointwise-fixed vertices.

For \(a,b\ge1\), define \(N_{a,b}\) on vertices \((i,j)\) with \(1\le i\le a\), \(1\le j\le b\). Its faces are cell sets that contain neither any entire row nor any entire column. When \(a=1\) or \(b=1\), it has no nonempty simplex and its realization is empty.

## Proof
**Step 1: describe the geometric fixed points.** For a finite simplicial group action, let \(\mathcal O\) denote the orbits of the action on vertices. A fixed point has equal barycentric coordinates on all vertices of an orbit. Thus it is determined by nonnegative orbit weights \(w_O\), summing to one, whose positive-weight orbits have union a face. Conversely such weights assign coordinate \(w_O/|O|\) to each vertex of \(O\) and give a fixed point. These mutually inverse affine maps on faces give a piecewise-linear homeomorphism from the realization of the orbit-face complex to the geometric fixed-point space.

The \(H\)-orbits of edge-vertices of \(X_n\) are precisely the Cartesian products \(R_i\times C_j\) of row orbits and column orbits. Selecting every edge in \(R_i\times C_j\) for several orbit rectangles fills an original row exactly when all quotient cells in the corresponding quotient row are selected; the same holds for columns. The orbit-face complex is therefore exactly \(N_{s,t}\).

**Step 2: a rectangular Morse lemma.** We establish, for all \(a,b\ge2\),
\[
|N_{a,b}|\simeq S^{(a-1)(b-1)-1}.
\]
Starting with all faces (including the empty face), visit cells \((1,1),(1,2),\ldots,(1,b),(2,1),\ldots,(a-1,b)\) in that order. At a visited cell \(e\), pair each as-yet-unpaired face \(F\) lacking \(e\) with \(F\cup\{e\}\) whenever both faces are still present, and delete both from the remaining set. The sequential element-matching lemma guarantees the union of these pairs is acyclic [1, Proposition 2.4].

To count critical faces, consider the first row of an arbitrary \(r\)-by-\(b\) board, with \(r\ge2\). Immediately after toggling \((1,1)\), the remaining faces lack \((1,1)\) and split into two disjoint classes. Class A has every \((1,j)\) for \(2\le j\le b\) present, while column 1 is *not* complete among rows \(2,\ldots,r\). Class B has every cell in column 1 among rows \(2,\ldots,r\) present; it may also have some other first-row cells.

Class A remains unchanged under the later first-row toggles: deleting one of its first-row cells produces a face that was already paired when \((1,1)\) was toggled. On class B, at each subsequent \((1,j)\), any pair for which the remaining rows do not completely fill column \(j\) is removed. The survivors in class B must therefore have their first-row \((1,j)\) absent and their lower rows fill column \(j\) completely. After all \(b-1\) such stages, every column among rows \(2,\ldots,r\) would be complete, forcing each such row to be complete and violating the face condition. No class-B face remains.

Consequently the survivors after all toggles of the first row are **exactly** the faces that have first-row cells \((1,2),\ldots,(1,b)\), lack \((1,1)\), and whose restriction to rows \(2,\ldots,r\) is a face of \(N_{r-1,b}\). In particular column 1 is not complete among the lower rows, as required by the class-A condition. The same argument repeats on the lower board. After \(a-1\) rows the residual board is \(1\)-by-\(b\), whose only face is the empty face. There is exactly one unmatched face, namely
\[
C=\{(i,j):1\le i\le a-1,\ 2\le j\le b\}.
\]
It has \((a-1)(b-1)\) vertices and dimension \(d=(a-1)(b-1)-1\). The empty face was matched at the first step. By discrete Morse theory [1, Theorem 2.1 and Corollary 2.2], the complex is homotopy equivalent to the CW complex with a base vertex and a single \(d\)-cell, attached trivially when \(d>0\), and to two isolated points when \(d=0\). Thus it is homotopy equivalent to \(S^d\), which completes the proof.

## Verification
The self-contained script `verify_rectangular_fixed.py` enumerates all faces and follows this exact cell order for every rectangle with \(2\le a,b\le4\). In all nine cases the unpaired set is exactly \(\{C\}\). It separately enumerates 34 actions generated by row and column permutations on boards of sizes three and four, checking face-by-face that expanding selected edge orbits agrees with the quotient-row/quotient-column face condition. The script uses only the Python standard library, prints `RECTANGULAR_FIXED_ORBIT_CHECKS_OK 9 34`, and provides finite corroboration rather than a proof for arbitrary dimensions. The universal arguments are above.

## Relationship to prior work
Singh's published homotopy theorem [1, Theorem 1.2] treats the **square** special case \(N_{n,n}=M_{n-1}(K_{n,n})\), with a closely related greedy element matching. The present statement extends the underlying combinatorial sphere calculation to all rectangles with distinct row and column near-full capacities and uses an explicit orbit-face identification to obtain the geometric fixed-point spaces for every product subgroup. It does not claim that the square sphere or sequential Morse matching is new.

Reiner and Roberts [2, Theorem 3.3] determine characteristic-zero **homology representations** for general chessboard complexes with multiplicities; those results do not supply the homotopy equivalence type of geometric fixed-point spaces. The multiple-chessboard formulation in [3, Section 2.2] assumes column occupancy at most one, whereas this theorem allows near-full columns and rows simultaneously. None of these statements alone gives the subgroup orbit-count classification in the theorem.

## Limitations
The result gives a homotopy sphere, not necessarily a PL-homeomorphic standard sphere or an equivariant equivalence to a representation sphere. It concerns geometric fixed points of product subgroups only; an involution interchanging the two bipartite parts is not covered. Earlier literature's square theorem and rational homology information are acknowledged, and unindexed differently formulated equivalent treatments of the general rectangular lemma remain possible. There has been no independent mathematical audit.

## References
[1] A. Singh, *Higher matching complexes of complete graphs and complete bipartite graphs*, arXiv:2006.13632 (first public version 2020-06-24), Theorem 1.2; Proposition 2.4; Section 4. https://arxiv.org/abs/2006.13632

[2] V. Reiner and J. Roberts, *Resolutions and homology of simplicial complexes with symmetry*, 2000, Theorem 3.3. https://www-users.cse.umn.edu/~rober005/chessmatch.pdf

[3] D. Jojić, I. Nekrasov, G. Panina and R. Živaljević, *Alexander \(r\)-tuples and Bier complexes*, arXiv:1607.07157 (2016), Section 2.2. https://arxiv.org/abs/1607.07157
