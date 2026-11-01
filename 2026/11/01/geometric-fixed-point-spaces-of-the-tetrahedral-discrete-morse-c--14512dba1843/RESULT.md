# Geometric fixed-point spaces of the tetrahedral discrete-Morse complex

## Finding
Let \(\Delta^3\) denote the full simplicial tetrahedron on four vertices, and let \(X=\mathcal M(\Delta^3)\) be the **ordinary, non-pure** simplicial complex of nonempty acyclic matchings of its Hasse diagram. Permutations of the four vertices act naturally on \(X\). For each nonidentity permutation \(g\in S_4\), its **geometric fixed-point space** has the complete homotopy classification

\[
|X|^{\langle g\rangle}\simeq
\begin{cases}
S^2, &\text{cycle type }(2,1,1),\\
S^1\sqcup S^1, &\text{cycle type }(2,2),\\
\{\mathrm{pt}\}, &\text{cycle type }(3,1),\\
\varnothing, &\text{cycle type }(4).
\end{cases}
\]

For the identity the entire space is the previously established \(\bigvee^{99}S^4\), so these four new classifications complete the fixed-locus table for all conjugacy classes. The first case is proved by **60 explicit simplicial elementary collapses** to the six-vertex octahedral two-sphere. The second case is a disjoint union of two four-edge cycles *without any collapse*. These statements concern fixed points in the geometric realization, not setwise fixed vertices of the original simplicial complex, and not homotopy fixed points or a Borel construction.

## Assumptions and scope
Represent the fifteen nonempty faces of \(\Delta^3\) by the nonzero four-bit masks \(1,\ldots,15\). Its Hasse diagram has exactly 28 cover relations \((a,b)\), with \(a\subset b\) and \(|b|=|a|+1\). Each cover relation is one vertex of \(X\). A nonempty set \(W\) of these 28 relations is a simplex precisely when its relations have pairwise disjoint endpoints and the directed Hasse graph obtained by reversing the arrows belonging to \(W\) is acyclic. The whole geometric realization \(|X|\) carries the simplicial action of \(S_4\) induced by permutation of the four tetrahedral vertices.

For a fixed permutation \(g\), let \(\mathcal O_g\) denote the orbits of \(\langle g\rangle\) on the 28 primitive relations. An orbit \(O\) is **admissible** if \(O\) itself is an acyclic matching. Define an orbit complex \(F_g\): its vertices are the admissible orbits, and a nonempty collection of these vertices is a face exactly when their union is an acyclic matching. An inadmissible orbit can never appear in an invariant simplex.

## Proof
**1. Orbit-simplex realization lemma.** The geometric realization of a simplicial complex embeds in the standard simplex with one barycentric coordinate per simplicial vertex. A point is fixed by \(g\) exactly when its coordinates are constant on each \(\langle g\rangle\)-orbit. Its positive-coordinate support must be a face. Assign to each admissible orbit the point with equal weight \(1/|O|\) on every member and weight zero elsewhere. Taking convex combinations over compatible orbit collections defines a piecewise-linear homeomorphism \(|F_g|\cong |X|^{\langle g\rangle}\), because barycentric coordinates give a unique inverse by summing within each orbit. This justifies reducing a *geometric* fixed-locus calculation to the orbit complex.

**2. Finite exhaustive construction.** List every cover relation directly from the fifteen nonempty face masks. Each class representative acts by permuting bits. Compute its cover-relation orbits, retain precisely those passing the acyclic-matching test, and enumerate **every** nonempty subset of retained orbit vertices. Each union is accepted if and only if its endpoints are disjoint and the reversed-edge Hasse graph has no directed cycle. The algorithm checks this both by a topological sort of all fifteen faces and, separately, by searching for closed alternating gradient paths within each dimension. These criteria agree on every considered subset, not just on the surviving faces.

The resulting exact orbit-complex face vectors, ordered from dimension zero upward, are

\[
\begin{array}{c|c|c}
\text{cycle type}&\#\text{ orbit vertices}&\text{face vector}\\\hline
(2,1,1)&10&(10,36,56,36,8)\\
(2,2)&8&(8,8)\\
(3,1)&3&(3,3,1)\\
(4)&0&()
\end{array}
\]

The complete lists of orbit vertices and a certificate of the 60 collapse pairs are included in `certificate.json`; the standalone `verification.py` independently regenerates the orbit faces from the defining Hasse diagram and checks the certificates.

**3. Transposition.** Label the ten admissible orbit vertices as in `certificate.json` (zero-indexed, ordered by their least Hasse relation). Each pair \((a,b)\) in its `collapse_pairs` array encodes a pair of simplex bitmasks. The verifier checks at the moment of every deletion that \(a\) is a codimension-one face of \(b\), that \(b\) is its *only strict coface*, and that both belong to the remaining complex. Thus all sixty listed deletions are valid elementary simplicial collapses. The remaining complex has vertices \(4,5,6,7,8,9\); its three missing edges are exactly \(\{4,7\},\{5,8\},\{6,9\}\). Every nonempty subset selecting at most one endpoint from each of these three opposite pairs is present, and there are no other faces. This is the join of three copies of \(S^0\), namely the boundary of a three-dimensional octahedron, homeomorphic to \(S^2\).

**4. Double transposition, three-cycle and four-cycle.** In cycle type \((2,2)\), all faces are vertices or edges. Its eight vertices have degree two, and the graph has exactly two connected components of four vertices each; hence it is precisely two disjoint four-cycles. For type \((3,1)\), the three admissible vertices span all three edges and their filled triangle, so \(F_g\) is a simplex and contractible. For type \((4)\), no Hasse-relation orbit is an admissible matching, hence the geometric fixed space is empty. Conjugating \(g\) conjugates the action on \(X\), so these representatives cover every nonidentity permutation.

## Verification
From the exact package directory run `python3 verification.py certificate.json` using Python 3 and its standard library. It asserts the 28 Hasse relations, enumerates every possible orbit-vertex subset for representatives of all four nontrivial cycle types, and compares two independently implemented acyclicity criteria. It verifies all listed orbit blocks and face vectors; for type \((2,1,1)\), it checks **all 60 free-face collapse pairs** and tests equality of the final face set with the full boundary of an octahedron, rather than inferring a sphere from Betti numbers. For type \((2,2)\) it checks the number, size and vertex degrees of both graph components; for type \((3,1)\) it checks that the full triangle is present; for type \((4)\) it checks that no admissible orbit exists. Finally it checks face vectors for **all 24 permutations**.

As an independent consistency check, the ordinary Euler characteristics of these four geometric fixed spaces are \((2,0,1,0)\), exactly the equivariant Lefschetz numbers computed previously from the rational \(S_4\) homology character of \(X\). The Euler-characteristic comparison does **not** prove the new homotopy statements; the explicit orbit enumeration, free-face collapses and graph decomposition do.

## Relationship to prior work
Scoville's 2026 paper gives the Hasse definition, face vector and nonequivariant homotopy equivalence \(X\simeq\bigvee^{99}S^4\) (Theorem 20 and Tables 1–2). Earlier work of Lin and Scoville identifies the natural automorphism action. Two publicly accessible 2026 calculations determine the **rational** \(S_4\)-character \((99,1,-1,0,-1)\); one enumerates the setwise-fixed simplex counts \((146,16,7,0)\) for the four nonidentity cycle types. Those counts and characters determine only Euler characteristics of the geometric fixed loci. They neither establish the octahedral collapse nor determine that the double-transposition fixed locus is two disconnected circles. The present statement computes the complete nonidentity *geometric fixed-point homotopy types*, not a new calculation of that known rational character.

## Limitations
The classification is for the full tetrahedral discrete-Morse matching complex, not the boundary complex, its pure subcomplex, its generalized non-acyclic variant, or simplices of greater dimension. It computes homotopy types of individual fixed loci but not the full \(S_4\)-equivariant homotopy type with all inter-subgroup restriction maps. It is an exact finite proof, not an infinite-family extrapolation. Searches cannot exclude unindexed or implicit equivalent earlier treatments.

## References
1. N. A. Scoville, *The complex of discrete Morse matchings of the n-simplex: homotopy types and structural results*, arXiv:2604.18172v1, first posted 2026-04-20, Theorem 20 and Tables 1–2. https://arxiv.org/abs/2604.18172
2. M. Lin and N. A. Scoville, *On the automorphism group of the Morse complex*, arXiv:1904.10907v1 (2019), subsequently *Advances in Applied Mathematics* 131 (2021), 102250. https://arxiv.org/abs/1904.10907
3. *The complete \(S_4\)-character on tetrahedral discrete Morse matching homology*, publicly accessible mathematical finding (2026-10-11); exact signed traces and setwise-fixed simplex counts. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-complete-s-4-character-on-tetrahedral-discrete-morse-matchin--aa2567a7706d
4. *The \(S_4\)-character of tetrahedral Morse-complex homology*, publicly accessible mathematical finding (2026-10-11), with signed chain-trace vectors. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-s-4-character-of-tetrahedral-morse-complex-homology--3b1fdcb3c035
