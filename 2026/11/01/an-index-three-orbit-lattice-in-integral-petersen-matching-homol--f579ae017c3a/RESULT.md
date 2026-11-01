# An index-three orbit lattice in integral Petersen matching homology

## Finding

Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph, with vertices the two-element subsets of \(\{0,1,2,3,4\}\) and adjacency given by disjointness. Let \(X=\mathcal M(P)\) be the **ordinary matching complex**: its 15 vertices are the edges of \(P\), and its simplices are mutually vertex-disjoint edge sets. The natural group \(S_5=\operatorname{Aut}(P)\) acts simplicially.

The **new integral equivariant conclusions** are:

1. The complete degree-two integral module has a primitive, five-element orbit basis:
   \[\widetilde H_2(X;\mathbb Z)\cong\operatorname{sgn}\otimes_{\mathbb Z}\mathbb Z^{\{0,1,2,3,4\}}.\]
   This is an **integral** isomorphism, not just an isomorphism after tensoring with \(\mathbb Q\).
2. The degree-three group is \(\widetilde H_3(X;\mathbb Z)\cong\mathbb Z^5\), and its *entire integral* \(S_5\)-action is specified by the four integral \(5\times5\) matrices in `generator_matrices.json`, using the intrinsic adjacent swaps \((01),(12),(23),(34)\) and the exact critical-simplex basis stated there.
3. Let \(T=S_{\{0,1\}}\times S_{\{2,3,4\}}\cong S_2\times S_3\) be the stabilizer of the distinguished unordered pair \(\{0,1\}\). The fixed sublattice \(\widetilde H_3(X;\mathbb Z)^T\) is infinite cyclic. If \(v\) is either primitive generator and \(L=\langle g v:g\in S_5\rangle_{\mathbb Z}\), then
   \[\boxed{\left[\widetilde H_3(X;\mathbb Z):L\right]=3,\qquad \widetilde H_3(X;\mathbb Z)/L\cong\mathbb Z/3.}\]
   The index is independent of the choice of sign of \(v\). In particular, the ten natural unordered-pair orbit classes generate a proper index-three sublattice of integral third homology, even though they span it rationally.

The ordinary homotopy type \(X\simeq\bigvee^5 S^2\vee\bigvee^5S^3\) and the rational \(S_5\)-character are known from preceding calculations and **are not claimed as new**. The findings here are the primitive *integral* orbit basis, complete generator matrices over \(\mathbb Z\), and the intrinsic index-three obstruction.

## Assumptions and scope

All simplicial chains are **oriented integer chains**. Label the ten Petersen vertices by lexicographically ordered two-subsets of \(\{0,1,2,3,4\}\), and the 15 edges by lexicographically ordered disjoint pairs of vertex indices, as constructed verbatim in `verify_integral_petersen.py`. A simplex of \(X\) is encoded by the 15-bit mask of its ordered edge set; its orientation is increasing edge-index order. The only coefficient ring used to establish the two lattice statements is \(\mathbb Z\); no prime-field extrapolation is involved. The complete computation has 331 nonempty faces in dimensions 0 through 4, with face vector \((15,75,145,90,6)\).

## Proof

**Integral chain model.** The standalone program exhausts all masks from 0 through \(2^{15}-1\), retaining a mask precisely when its selected graph edges have pairwise disjoint endpoints. It constructs the standard signed boundary for every retained simplex and verifies \(\partial^2=0\). The stated face vector is exhaustive, not a sample.

**Acyclic reduction.** Pair faces in the fixed toggle order of edge indices
`[12,10,6,11,14,0,4,1,7,13,5,2,8,9,3]`, processing the currently unmatched faces in increasing (cardinality, integer mask) order. Every admissible pair differs by one edge. There are 160 matched pairs and exactly eleven critical cells: one vertex, five 2-simplices, five 3-simplices. Orient every nonmatching cover down and every matching cover up. Exhaustive topological sorting visits **all 331** face-poset vertices, certifying acyclicity. The 160 integer unit cancellations eliminate the matched chain generators without introducing denominators; all differential entries between surviving critical generators are exactly zero. Thus the two homology groups are free of rank five and the surviving critical generators yield a complete integral chain basis.

**Equivariant reconstruction.** At every unit cancellation \((a,b)\) with incidence \(u=\pm1\), both the integral inclusion of survivors and the projection onto survivors are updated by the explicit elementary chain-contraction formulas implemented in the verifier. These maps lift every critical generator to a signed integer simplicial cycle; the program verifies its original boundary is zero and that projection sends it to the corresponding critical basis vector. Applying the 120 permutations of the five symbols, tracking the sign of each induced simplex permutation, and projecting gives exact integer homology action matrices. The four adjacent-swap matrices have integral inverses and satisfy the Coxeter relations; all 120 traces match \(\chi_2(g)=\operatorname{sgn}(g)f(g)\) and \(\chi_3(g)=\binom{f(g)}2+c_2(g)-f(g)\), where \(f(g)\) and \(c_2(g)\) count fixed symbols and 2-cycles. The latter equalities are consistency checks and not the claimed integral refinement.

**Degree two.** In the critical basis with bitmasks `[73,530,2180,2336,24640]`, the vector `[0,0,0,0,1]` changes sign under all three adjacent transpositions stabilizing symbol 0. Its five signed translates under transpositions of 0 with each symbol form the change-of-basis matrix in `generator_matrices.json`. Its exact integer determinant is **\(-1\)**. The resulting primitive basis is permuted by \(S_5\) with the common sign twist, proving the first assertion over \(\mathbb Z\).

**Degree three.** In the critical basis `[650,652,788,8353,16652]`, the simultaneous fixed integer vectors of \((01),(23),(34)\) form the rank-one lattice generated primitively by
\[v=(0,0,-1,1,1)^{\mathsf T}.\]
Take one translate under a permutation carrying \(\{0,1\}\) to each of the ten two-element subsets of five symbols. Their \(5\times10\) integer column matrix is recorded in `generator_matrices.json`. Its Smith diagonal, recomputed from the exact matrix over \(\mathbb Z\), is **\((1,1,1,1,3)\)**. This proves rank five and index three, independently of coordinate choices. Stabilizer invariance guarantees the ten columns are well-defined up to the chosen pair representatives, and the full group orbit has precisely ten vectors.

## Verification

Run `python verify_integral_petersen.py` with Python 3 and SymPy installed; it needs no data files, network calls, or external certificates. Its recorded output is `verification_output.txt` and its precise generator matrices are `generator_matrices.json`. The script checks 331 nonempty simplices, the complete Hasse graph, 160 unit cancellations, zero Morse differentials, integral cycle representatives, the full set of 120 automorphisms, four integral Coxeter generators, a unimodular degree-two change of basis and the degree-three Smith diagonal \((1,1,1,1,3)\). Assertions terminate execution on any failed check. In addition to the text proof, the exact executable path from original simplices to the two module statements is supplied.

## Relationship to prior work

General matching-complex homology and discrete Morse methods are classical (see Jonsson). Zaslavsky treats matchings **as edge sets** of the same Petersen graph in §3.2, classifies their automorphism orbits, and computes automorphism groups of signed Petersen graphs in §8; these are combinatorial inputs, not an integral homology module calculation. Earlier same-object calculations already determined this matching complex's ordinary homotopy type and its two rational \(S_5\)-characters. Rational module isomorphisms cannot decide the index of an integral orbit or whether an orbit basis is unimodular: both new conclusions require lattice computation. Results on the graph \(\mathcal M(K_5)\), which is itself isomorphic to the Petersen graph, concern a **different simplicial complex** than \(\mathcal M(P)\); results on \(\mathcal M_2(P)\), the two-matching complex, likewise concern different objects.

## Limitations

The computation is exact but specific to the ordinary matching complex of the ten-vertex Petersen graph and its natural \(S_5\)-action. It does not classify the integral lattices of other graph matching complexes, construct a canonical geometric preferred sign for the primitive fixed vector, or determine equivariant homotopy types and quotient-space torsion. The index-three quotient is a **quotient of homology lattices**, not an assertion that \(X\) has three-torsion in its homology; the homology groups here are torsion-free. No independent mathematical audit has been performed. An equivalent unindexed integral action computation remains possible.

## References

1. J. Jonsson, *Simplicial Complexes of Graphs*, Lecture Notes in Mathematics 1928, Springer, first print publication 15 November 2007, DOI `10.1007/978-3-540-75859-4`, chapter 11 (general matching complexes and Morse techniques).
2. T. Zaslavsky, *Six Signed Petersen Graphs, and Their Automorphisms*, dated 27 November 2011, author manuscript `https://people.math.binghamton.edu/zaslav/Tpapers/6sp.pdf`, especially §§3.2 and 8.2 (matchings and group actions on signed graph data).
3. Previous calculations of the Petersen ordinary matching complex's rational \(S_5\)-character and integral homotopy type; these previously available conclusions are explicitly excluded from the novelty claim.
