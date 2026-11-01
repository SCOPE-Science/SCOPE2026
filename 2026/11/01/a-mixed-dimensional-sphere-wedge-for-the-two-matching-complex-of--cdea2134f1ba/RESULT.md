# A mixed-dimensional sphere wedge for the two-matching complex of \(K_{4,5}\)

## Finding

For the two-matching complex \(M_2(K_{4,5})\), there is an integral homotopy equivalence
\[
|M_2(K_{4,5})|\simeq\left(\bigvee^{42}S^6\right)\vee\left(\bigvee^3 S^7\right).
\]
In particular, \(\widetilde H_6\cong\mathbb Z^{42}\), \(\widetilde H_7\cong\mathbb Z^3\), and all other reduced integral homology vanishes. The complex is pure of dimension seven and is **not shellable**, because a pure shellable complex has reduced homology only in top dimension. This is a finite, exact classification of the named complex; no assertion about larger rectangular graphs is made.

## Assumptions and scope

Label the four left vertices \(r\in\{0,1,2,3\}\) and five right vertices \(c\in\{0,1,2,3,4\}\). Identify the edge \((r,c)\) with bit position \(5r+c\). A mask \(F\in\{0,\ldots,2^{20}-1\}\) represents a face exactly when each row and each column of its \(4\times5\) binary incidence matrix has at most two ones. The empty mask is included in the simplicial complex, but the nonempty face poset is used for the discrete-Morse matching.

The same object is the three-clique-free complex \(\operatorname{CF}_3(K_4\square K_5)\), because a triangle in the line graph of a triangle-free graph consists precisely of three edges incident at a common endpoint.

## Proof

**1. Exhaustive faces and facets.** The executable `verify.py` checks all \(2^{20}\) edge masks against these nine degree constraints. It constructs exactly \(37,440\) nonempty faces, with face numbers by dimensions zero through seven
\[
(20,190,1080,3900,8880,12120,8760,2490).
\]
For each face it also checks whether an admissible edge can be added; exactly \(2,490\) faces are inclusion-maximal, and all have eight edges. Thus the complex is pure seven-dimensional. Both loops explicitly range over all possible masks or all remaining possible bit positions, not samples.

**2. Acyclic matching.** Starting with all nonempty faces, process edge-bit positions \(j=0,1,\ldots,19\) in order. At position \(j\), pair every still-unpaired face without bit \(j\) to its still-unpaired coface obtained by toggling that bit, whenever both occur in the remaining face set. Remove these two faces permanently before proceeding. Exactly \(18,697\) pairs result, leaving one critical zero-face, 42 critical six-faces and three critical seven-faces. The program checks every one of the \(217,580\) codimension-one face incidences, directing matched incidences upward and all others downward. Kahn's topological-sort algorithm consumes all \(37,440\) nodes, so the directed Hasse graph is acyclic. By the discrete-Morse theorem, the original complex is homotopy equivalent to a CW complex having precisely these critical cells and no cells of dimensions one through five.

**3. Exact integral attaching degrees.** Give each oriented face the increasing-bit orientation; deletion of its \(k\)-th present bit has signed incidence \((-1)^k\). For a six-face \(f\), let \(R(f)\) be its integer vector in the free group on the 42 critical six-cells after Morse reduction. If \(f\) is critical then \(R(f)\) is its basis vector. If \(f\) is the upper face of a five-to-six matched pair then \(R(f)=0\). If instead it is the lower face of the matched pair \((f,g)\), with \(g\) a seven-face, solve \(\partial g=0\) for \(f\):
\[
R(f)=-[g:f]\sum_{h\subset g,\ \dim h=6,\ h\ne f}[g:h]R(h),
\]
where every incidence number \([g:h]\) is \(+1\) or \(-1\). All recursive dependencies follow the acyclic matching, so this is a terminating exact integer computation. Apply \(R\) to the complete oriented boundaries of all three critical seven-faces. `verify.py` checks every entry of the resulting \(42\times3\) integer matrix, and **all entries are zero**.

**4. Homotopy rather than just homology.** The Morse CW complex's six-skeleton is the wedge of 42 six-spheres: one point, no cells in dimensions one through five, and 42 six-cells. The Hurewicz map \(\pi_6(\bigvee^{42}S^6)\to H_6(\bigvee^{42}S^6;\mathbb Z)\) is an isomorphism, since this skeleton is five-connected. Hence each seven-cell attaching map is nullhomotopic exactly when its column of integral degrees is zero. All three attaching maps are nullhomotopic, yielding the displayed wedge decomposition.

## Verification

Run `python3 verify.py` with Python 3.8 or newer; it uses only the standard library. The verifier checks the full face vector, purity and facets; all matched face pairs; every directed Hasse incidence and global acyclicity; all 126 entries of the signed integral Morse boundary; and, independently, the raw simplicial chain ranks over \(\mathbb F_2\). The latter give reduced mod-two Betti numbers \((0,0,0,0,0,0,42,3)\). The final status is `ALL_VERIFY_OK`. In the integral calculation, exactly 8,556 six-face reductions are evaluated with caching. No logarithm or finite-sample extrapolation substitutes for the exhaustive proof.

## Relationship to prior work

Singh's higher-matching-complex theorems [2] determine certain complete-bipartite cases with \(m>r\ge n\), or \(r=n-1\) on \(K_{n,n}\); neither hypothesis applies to \(r=2\) on \(K_{4,5}\). Singh also notes the Reiner–Roberts rational-homology calculation [3], which does not by itself determine an integral homotopy type. Previously reported exact homotopy computations for \(M_2(K_{3,5})\) and \(M_2(K_{4,4})\) [4,5] concern different graphs and do not imply this mixed-dimensional classification. Ghosh and Selvaraja [1] develop shellability theory for clique-free complexes; their published abstract specifies sufficient shellability conditions for a chordal-graph class, whereas \(K_4\square K_5\) contains induced four-cycles and is not chordal.

## Limitations

The calculation establishes an ordinary integral homotopy equivalence for the single graph \(K_{4,5}\), not an equivariant splitting, a classification of all \(M_2(K_{m,n})\), or an integral description of natural inclusion maps. The recent clique-free manuscript [1] could not be inspected in full; originality comparisons with its complete text and with unindexed computations consequently retain uncertainty. Rational Betti ranks may already follow from broader representation-theoretic methods [3]; the claim here is the **explicit integral homotopy type** and resulting non-shellability, not priority for those ranks.

## References

[1] R. Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623, first posted 2026-02-10. https://arxiv.org/abs/2602.09623

[2] A. Singh, *Higher matching complexes of complete graphs and complete bipartite graphs*, arXiv:2006.13632, first posted 2020-06-24, particularly Theorem 1.2. https://arxiv.org/abs/2006.13632

[3] V. Reiner and J. Roberts, *Minimal resolutions and the homology of matching and chessboard complexes*, Journal of Algebraic Combinatorics 11 (2000), 135–154, especially the rational-homology theorem cited in [2].

[4] *The two-matching complex of \(K_{4,4}\) is a wedge of fifteen five-spheres*, publicly indexed mathematical finding, 2026-10-11, identifier `2026/10/11/SCOPE-the-two-matching-complex-of-k-4-4-is-a-wedge-of-fifteen-five-sph--915eed6b65e5`.

[5] *The two-matching complex of \(K_{3,5}\) is a wedge of 91 five-spheres*, publicly indexed mathematical finding, 2026-10-11, identifier `2026/10/11/SCOPE-the-two-matching-complex-of-k-3-5-is-a-wedge-of-91-five-spheres--ea5e14157f12`.
