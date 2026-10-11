# Hexagonal-prism total three-cut complex: a \(22\)-sphere wedge and its dihedral character

## Finding
Let \(G=C_6\square K_2\) be the twelve-vertex hexagonal-prism graph. The total three-cut complex \(X=\Delta^t_3(G)\), whose facets are the complements of independent triples of graph vertices, has the complete homotopy type
\[
X\simeq \bigvee^{22} S^6.
\]
Its sixth integral reduced homology is free of rank \(22\); all other reduced integral homology vanishes. The pure eight-dimensional complex \(X\) is not shellable.

The natural graph-symmetry group is \(D_6\times C_2\). Let \(r\) cyclically rotate the six columns, \(s\) reflect them, and \(\tau\) swap the two layers, so \(r^6=s^2=\tau^2=1\), \(srs=r^{-1}\), and \(\tau\) is central. Write \(\chi_{\alpha,\beta}\) for the one-dimensional rational representation of \(D_6\) satisfying \(\chi_{\alpha,\beta}(r)=\alpha\), \(\chi_{\alpha,\beta}(s)=\beta\), with signs \(\alpha,\beta\in\{\pm1\}\). Write \(\rho_1,\rho_2\) for its two two-dimensional rational irreducibles (rotation characters \(2\cos(2\pi j m/6)\) on \(r^m\), zero on reflections, for \(j=1,2\)), and \(\varepsilon\) for the nontrivial character of the central \(C_2\). With \(\mathbf 1\) the trivial character, the full rational homology representation is
\[
\begin{aligned}
\widetilde H_6(X;\mathbb Q)\cong{}&
(4\chi_{+,+}\oplus\chi_{-,+}\oplus\chi_{-,-}\oplus2\rho_1\oplus3\rho_2)\boxtimes\mathbf 1\\
&\oplus(\chi_{+,+}\oplus\chi_{-,-}\oplus\rho_1\oplus\rho_2)\boxtimes\varepsilon.
\end{aligned}
\]
The layer exchange consequently acts with \(+1\) and \(-1\) eigenspaces of dimensions \(16\) and \(6\), respectively. No equivariant homotopy equivalence or integral representation decomposition is asserted.

## Assumptions and scope
The graph has vertices \((\ell,i)\), where \(\ell\in\{0,1\}\) and \(i\in\mathbb Z/6\mathbb Z\), with edges \((\ell,i)\sim(\ell,i+1)\) and \((0,i)\sim(1,i)\). Index vertices by \(6\ell+i\). A subset \(F\) is a face of \(X\) exactly when its complement contains three pairwise nonadjacent vertices; its facets are the complements of all such independent triples. All constructions are on this single graph and over the specified coefficient rings. The homotopy equivalence is nonequivariant; the character decomposition concerns the graph-induced homology action.

## Proof
**Exact face enumeration.** The graph has \(18\) edges. Enumerating the \(\binom{12}{3}\) vertex triples and excluding those containing a graph edge gives precisely \(76\) independent triples; complementing them and taking all subsets gives all \(3762\) faces, including the empty face. The nonempty face counts by dimension \(0,\ldots,8\) are
\[
(12,66,220,495,792,924,792,384,76).
\]
Each maximal face has nine vertices, hence \(X\) is pure of dimension eight.

**Complete discrete-Morse matching.** Label each face by its twelve-bit integer indicator. Begin with all faces available. At each pivot \(i=0,1,\ldots,11\), pair every still-available face \(F\) not containing \(i\) with \(F\cup\{i\}\), provided this second face is still available; remove both before advancing. The exact procedure in `verify.py` makes \(1870\) pairs in the augmented face poset and leaves \(22\) unpaired faces, each of cardinality seven. The pair between the empty face and vertex \(0\) is omitted for the ordinary face poset. The remaining \(1869\) matched pairs leave exactly one critical vertex (vertex \(0\)) and \(22\) critical six-faces.

To verify **acyclicity**, orient every inclusion edge in the ordinary face Hasse diagram from the lower face to the upper face, reversing precisely the matched edges. The verifier constructs all \(21,576\) dimension-one face incidences and performs a topological sort of the resulting directed graph; all \(3761\) nonempty faces are visited. Thus no directed cycle exists, and Forman's discrete Morse theorem yields a CW complex with one zero-cell and twenty-two six-cells and no other cells. Every attaching map of a six-cell lands in the zero-skeleton (there are no intermediate cells), so its homotopy type is \(\bigvee^{22}S^6\). The homology and nonshellability conclusions follow: a pure shellable complex has no reduced homology strictly below its top dimension.

**Group action and character.** A graph automorphism preserves the rung edges because each rung participates in two distinct induced square faces whereas each rim edge participates in one. Rungs are therefore invariant as a class. Their two-endpoint positions inherit the six-cycle adjacencies, permitting precisely \(D_6\) permutations of the columns and an independent uniform layer exchange. These give all \(24\) graph automorphisms, namely \((\ell,i)\mapsto(\ell\oplus e,\sigma i+m)\) for \(e\in\{0,1\}\), \(\sigma\in\{\pm1\}\) and \(m\in\mathbb Z/6\mathbb Z\).

On the oriented simplicial chain basis, a fixed simplex contributes its orientation sign to the simplicial trace; a non-fixed simplex contributes zero. Subtracting the empty-face trace gives the reduced Lefschetz number. Since the only nonzero reduced rational homology is in even degree six, the reduced Lefschetz number equals the trace on \(\widetilde H_6(X;\mathbb Q)\). Directly summing over all simplices produces this complete character: for \(e\in\{0,1\}\),
\[
\begin{array}{c|cc}
 g& e=0&e=1\\\hline
 r^0\tau^e&22&10\\
 r^m\tau^e,\ m\in\{1,2,4,5\}&1&1\\
 r^3\tau^e&4&4\\
 r^m s\tau^e,\ m\text{ even}&4&4\\
 r^m s\tau^e,\ m\text{ odd}&6&2
\end{array}
\]
The standard character inner product against each of the eight one-dimensional irreducibles and four two-dimensional irreducibles of \(D_6\times C_2\) gives exactly the multiplicities in the finding. These integer inner products and the dimension sum \(22\) are recomputed over exact rational arithmetic in `verify.py`. For the layer exchange the trace is \(10\), so the eigenspace dimensions are \((22+10)/2=16\) and \((22-10)/2=6\).

## Verification
Run `python3 verify.py` from a directory containing the complete package file `verify.py`; it uses only the Python standard library. It reconstructs the graph edges, independent triples, every face and its dimensions, the matching and complete Hasse diagram, and proves matching acyclicity by exhaustive topological sorting. Independently, it computes every augmented simplicial boundary rank over \(\mathbb F_2\), obtaining \(\widetilde\beta_6=22\) and no other nonzero reduced Betti numbers. It constructs all \(24\) automorphisms, computes the orientation-signed reduced Lefschetz traces, and checks every multiplicity by exact character inner products. Its final successful output begins `VERIFY_OK`; these checks were reproduced from this package's actual script. The integral homotopy statement follows from the complete discrete-Morse matching, **not** from the finite-field homology calculation alone.

## Relationship to prior work
Bayer–Denker–Jelić Milutinović–Rowlands–Sundaram–Xue define total cut complexes and analyze several graph families. Their clique-prism result concerns \(K_n\square K_2\), whose independence number is two, so it cannot cover the nonempty total three-cut complex of \(C_6\square K_2\). Their cycle and open-grid results do not give this annular grid's homotopy or symmetry character. Chandrakar–Hazra–Rout–Singh calculate total three-cut complexes of open two-row and three-row path grids, not the circularly closed two-row grid. Filakovský's square-sequence constructions require sequentially attached cells along single edges or length-two paths, rather than closing a final square along two disjoint rungs. Carnero Bravo's path-product and cycle results likewise do not supply the claimed total-three-cut cylindrical case. Related published exact computations for the Petersen, Heawood and Wagner graphs concern different graphs and do not imply this statement. The novelty claim is limited to the exact hexagonal prism homotopy and its rational symmetry module, not the general definition or known machinery.

## Limitations
This is a single finite graph, not a formula for all cyclic prisms, all grids or all total cut complexes. The homotopy equivalence is not claimed equivariant, and the representation decomposition is rational rather than an explicit integral lattice decomposition. The enumerative proof is exhaustive for this finite complex and reproducible, but no separate independent mathematical audit has been performed. An unindexed equivalent result or a presently unidentified stronger theorem could affect originality.

## References
- M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Total Cut Complexes of Graphs*, arXiv:2209.13503, first posted 2022-09-27. https://arxiv.org/abs/2209.13503
- H. Chandrakar, S. Hazra, S. Rout and N. Singh, *Topology of Total Cut and Cut Complexes of Grid Graphs*, arXiv:2408.07646. https://arxiv.org/abs/2408.07646
- M. Filakovský, *Topology of k-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365. https://arxiv.org/abs/2602.11365
- A. Carnero Bravo, *Total Cut Complexes and Their Duals*, arXiv:2602.21427. https://arxiv.org/abs/2602.21427
