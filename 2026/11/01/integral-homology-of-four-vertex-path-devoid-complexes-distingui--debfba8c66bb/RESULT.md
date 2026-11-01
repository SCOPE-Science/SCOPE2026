# Integral homology of four-vertex-path-devoid complexes distinguishes the Shrikhande and rook graphs

## Finding

Let \(P_4\) be a four-vertex path (three edges) and define the *path-devoid complex* by
\[
\mathcal D(G;P_4)=\{S\subseteq V(G):G[S]\text{ contains no subgraph isomorphic to }P_4\}.
\]
A subgraph here need **not** be induced: extra edges among its four vertices do not eliminate a copy of the path. For the Shrikhande graph \(\mathrm{Sh}\) and the \(4\times4\) rook graph \(R\), the complete reduced **integral** homology is
\[
\widetilde H_i(\mathcal D(\mathrm{Sh};P_4);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{32}&i=3,\\
\mathbb Z^{45}&i=4,\\
\mathbb Z^{6}&i=5,\\
0&\text{otherwise},
\end{cases}
\]
\[
\widetilde H_i(\mathcal D(R;P_4);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{73}&i=4,\\
\mathbb Z^{18}&i=5,\\
0&\text{otherwise}.
\end{cases}
\]
Both graphs have strongly regular parameters \((16,6,2,2)\), so this construction distinguishes graphs not distinguished by those parameters. In particular, only the Shrikhande complex has nonzero reduced integral third homology.

## Assumptions and scope

Each graph has sixteen vertices indexed by \((a,b)\in\mathbb Z_4^2\). The rook graph joins distinct \((a,b)\), \((c,d)\) if \(a=c\) or \(b=d\). The Shrikhande graph is the Cayley graph whose six difference vectors are \((\pm1,0)\), \((0,\pm1)\), \((1,1)\), \((-1,-1)\), with arithmetic modulo four. The claim uses the simplicial complex of **all** vertex subsets inducing no three-edge simple path (regardless of possible chords), not an induced-path-free or graph-independence complex. Reduced homology has coefficients in \(\mathbb Z\), including torsion assessment; no statement about a sphere-wedge homotopy type is asserted.

## Proof

The attached standalone verifier `checks/verify.py` executes the following deterministic finite proof, which uses exact integers and no external software dependency. It first generates the adjacency structure directly from the defining formulas. It verifies regularity, pairwise common-neighbor counts and the triangle counts. It then identifies every four-element vertex set carrying an ordinary \(P_4\) as a subgraph, using four pairwise distinct vertices in a three-edge order. As a separate check, for every four-set it exhausts all orderings and agrees with the forbidden-set enumeration. It obtains **636** forbidden four-sets for \(\mathrm{Sh}\) and **620** for \(R\).

Deleting all faces containing any forbidden four-set gives precisely the complexes in the theorem. Including the empty simplex, they have respectively **3,193** and **3,305** faces. Their nonempty face vectors by dimensions zero through six are
\[
(16,120,560,1184,1008,288,16)\qquad(\mathrm{Sh})
\]
and, by dimensions zero through five,
\[
(16,120,560,1200,1104,304)\qquad(R).
\]
Every surviving face has all of its nonempty proper faces, verified directly.

A deterministic sequential vertex-toggle matching on the face poset pairs each as-yet-unmatched face \(\sigma\) with \(\sigma\cup\{v\}\) whenever both exist and \(v\notin\sigma\), processing the sixteen vertices in their specified order. Acyclicity is established by an independent complete topological sort of the directed Hasse diagram (matched incidences reversed), consisting of **13,536** incidences for \(\mathrm{Sh}\) and **14,064** for \(R\). The only unmatched cells by dimension are
\[
\mathrm{Sh}:(c_0,c_3,c_4,c_5)=(1,38,51,6),
\qquad
R:(c_0,c_2,c_3,c_4,c_5)=(1,1,17,89,18).
\]
There are no unlisted critical cells. Standard integral algebraic discrete-Morse cancellation, with orientation from ascending vertex order, computes exact signed boundary matrices by recursively eliminating matched face/coface pairs. All products of adjacent differentials vanish, checked over the integers.

For \(\mathrm{Sh}\), the only nonzero Morse boundary is \(\partial_4:\mathbb Z^{51}\to\mathbb Z^{38}\), with rank **6**, Smith diagonal consisting of six units and no other nonzero diagonal entries. For \(R\), \(\partial_3:\mathbb Z^{17}\to\mathbb Z\) has rank **1** and \(\partial_4:\mathbb Z^{89}\to\mathbb Z^{17}\) has rank **16**; both have exclusively unit Smith factors. In particular, each of the dimension-five boundary maps vanishes. Integer unit-pivot row/column elimination leaves exactly a zero residual matrix in every degree. Such operations are unimodular and therefore certify integral ranks and the absence of torsion, not merely ranks over a field. Subtracting successive boundary ranks from the enumerated critical-cell counts gives precisely the displayed groups.

## Verification

Run `python3 checks/verify.py` from the unpacked package with Python 3 supporting `int.bit_count()` (version 3.8 or later with a compatible implementation; Python 3.10+ recommended). The script re-generates the input graphs, forbidden sets, entire simplicial complexes, complete Morse acyclic matching, and every integer Morse differential, then independently computes the mod-two homology ranks from the original simplicial boundary maps. The final line must be `VERIFY_OK`; the recorded deterministic output is at `checks/verification_output.txt`. The checks involve every one of the \(2^{16}=65,536\) vertex subsets of each graph. They do not extrapolate a finite sample to an infinite family.

## Relationship to prior work

Demet Taylan, *Matching Trees for Simplicial Complexes and Homotopy Type of Devoid Complexes of Graphs*, publicly posted January 27, 2015, arXiv:1501.06754, defines \(\mathcal D(G;F)\) with forbidden ordinary subgraphs and develops reductions and matching-tree techniques. The results inspected there determine special graph families including paths, cycles and forests; they do not give the two sixteen-vertex strongly regular calculations here. Previously studied independence, neighborhood, Čech and graph-cut complexes on these graphs impose different face conditions. Their known homology does not entail the displayed homology without an additional, presently unproved comparison map.

## Limitations

This is a pair of finite integral homology classifications, not a classification of all strongly regular graphs, not a formula for all devoid complexes, and not a wedge-of-spheres homotopy classification. The integral conclusion is supported by reproducible exhaustive finite proofs and exact unimodular reductions. Possible equivalent unindexed literature is an originality risk. Independent external mathematical validation has not been performed.

## References

- D. Taylan, *Matching Trees for Simplicial Complexes and Homotopy Type of Devoid Complexes of Graphs*, arXiv:1501.06754, version 1 publicly posted 2015-01-27. https://arxiv.org/abs/1501.06754
- R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics **134** (1998), 90–145. Standard justification for passage from an acyclic face-poset matching to a Morse chain model.
