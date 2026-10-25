# The full dihedral homology character of five-by-five nonattacking kings

## Finding

Let \(K=\operatorname{Ind}(P_5\boxtimes P_5)\) be the independence complex of the chessboard king graph, with edges joining distinct squares at Chebyshev distance at most one. The dihedral group \(D_4\) of square symmetries acts simplicially. Order its conjugacy classes as identity, quarter-turn, half-turn, reflection in a horizontal or vertical axis, and diagonal reflection, with respective class sizes \((1,2,1,2,2)\). The **complete graded rational homology characters** are

\[\chi_{\widetilde H_3}=(45,-1,5,3,-3),\quad \chi_{\widetilde H_4}=(32,0,0,4,0),\quad \chi_{\widetilde H_5}=(2,0,-2,0,0).\]

All other reduced homology groups vanish integrally, and the three displayed groups are free of respective integral ranks \(45,32,2\). Write \(A_1,A_2,B_1,B_2\) for the one-dimensional characters with class values \((1,1,1,1,1)\), \((1,1,1,-1,-1)\), \((1,-1,1,1,-1)\), and \((1,-1,1,-1,1)\); write \(E=(2,0,-2,0,0)\) for the two-dimensional character. As rational representations,

\[\widetilde H_3(K;\mathbb Q)\cong6A_1\oplus6A_2\oplus8B_1\oplus5B_2\oplus10E,\]
\[\widetilde H_4(K;\mathbb Q)\cong5A_1\oplus3A_2\oplus5B_1\oplus3B_2\oplus8E,\qquad\widetilde H_5(K;\mathbb Q)\cong E.\]

## Assumptions and scope

The complex is the ordinary independence complex of the simple strong-product graph on \(\{0,1,2,3,4\}^2\), not the Cartesian grid. A face contains no pair of squares in adjoining rows/columns/diagonals. Simplicial chains are over \(\mathbb Z\), with vertices oriented in increasing row-major order. Reduced homology and the induced integral chain actions use this fixed orientation. The representation statement is over \(\mathbb Q\); no assertion is made about irreducible integral lattice splitting.

## Proof

**Complete matching.** Encode each face by a 25-bit word, representing the five rows by masks without adjacent set bits; masks on consecutive rows are compatible precisely when no chosen bits are equal or adjacent in column. This exhaustive characterization gives \(6427\) faces including the empty face. In row-major column-priority order, for each vertex \((r,c)\), match every still-unmatched face omitting that vertex with its face obtained by adjoining that vertex, whenever both remain unmatched. Exactly \(3174\) distinct covering pairs are obtained, leaving \(79\) unmatched faces: \(45\) of dimension three, \(32\) of dimension four, and \(2\) of dimension five. The empty face is paired with a vertex. Construct the directed Hasse diagram with each matching cover arrow reversed; the verifier topologically sorts **all** its \(6427\) vertices and confirms that the graph is acyclic. Each of the \(79\) unmatched nonempty faces is maximal, and hence the integral Morse differential is zero. Equivalently, there is a standard acyclic ordinary matching with one critical vertex and the \(79\) positive-dimensional critical faces. Discrete Morse theory gives the stated integral groups and no other reduced homology.

**Exact integral symmetry computation.** For a matched lower simplex \(s\) paired with upper simplex \(u\), orient the unit coefficient \(\epsilon=[u:s]\in\{\pm1\}\). Recursively eliminate the lower simplex from any chain using the identity \(\epsilon u\) and its other faces. Because the matching is acyclic, the resulting chain projection \(p\) is a well-defined integral chain map to the critical-cell complex. Recursively fill the matched lower faces of the boundary of each critical simplex \(q\), obtaining an integral cycle \(z_q\) with \(p(z_q)=q\). The checker verifies \(\partial z_q=0\), \(p(z_q)=q\), and \(p\partial=0\) on every enumerated simplex. Thus the lifts give integral homology generators and the matrices of \(g_*\) in these bases have entries equal to the coefficients of \(p(gz_q)\).

Use the eight vertex permutations induced by the planar dihedral symmetries, including the sign of each permutation of oriented simplex vertices. The checker forms every such exact integer action matrix in degrees three, four, and five. It verifies the relations \(R^4=H^2=1\) and \(HRH=R^{-1}\), including the independently constructed half-turn matrices. The matrix traces are the displayed class characters. An independent signed simplicial fixed-face Lefschetz sum equals the alternating homological trace for every group element, providing a separate consistency test. Finally the standard character inner product, weighted by the five class sizes, gives the five irreducible multiplicities displayed above.

## Verification

The self-contained `verify_king_d4.py` uses only the Python standard library. Run `python3 verify_king_d4.py`. It enumerates every face, checks the complete matching and directed-acyclic topological order, checks integral cycle-lift and projection identities, constructs all homology action matrices, checks dihedral relations and independent Lefschetz sums, and computes the exact integer character decompositions. Successful execution prints each degree's five character values and multiplicities, followed by a PASS line. No random sampling, floating-point computation, external tables, or unverified rank inference is used.

## Relationship to prior work

The 2025 study of strong products of paths (arXiv:2505.06457, especially Theorem 33 and Corollary 34) already gives a **nonequivariant wedge-of-spheres theorem** for sufficiently narrow king graphs, covering the present board. Consequently the wedge property and bare homology ranks are *not presented as independently novel here*. The new statement identifies the complete graded dihedral action, including its sign-sensitive orientations and the faithful two-dimensional top-degree summand, data that cannot be deduced from an underlying nonequivariant wedge decomposition. The 2026 treatment of acyclic matchings in graph independence complexes (arXiv:2604.12606) provides related general Morse methods rather than this board-specific graded symmetry calculation. Related published computer-generated graph-topology records involving Cartesian grids, categorical products, and unrelated independence complexes do not imply the character calculation by graph or group equivalence.

## Limitations

This is a complete exact result for the specific \(5\times5\) board, not an infinite-width formula. The non-equivariant homotopy type falls under earlier broad work. The computation provides the rational representation and explicit integral generators but does not classify its \(\mathbb Z[D_4]\)-module isomorphism type. Exhaustive arithmetic verifies the stated finite chain complex, not novelty in all unindexed literature; an independently checked published equivalent representation might still exist. Independent scientific validation has not been performed.

## References

- J. A. Carnero Bravo, *Independence complexes of strong products of paths*, arXiv:2505.06457 (public 2025-05-09), notably Theorem 33 and Corollary 34.
- S. Barik et al., *Acyclic matchings and homotopy types of independence complexes* (related discrete-Morse methods), arXiv:2604.12606 (public 2026-04-14).
- R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145 (general discrete-Morse foundation).
