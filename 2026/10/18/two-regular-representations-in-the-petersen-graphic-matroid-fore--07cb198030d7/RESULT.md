# Two regular representations in the Petersen graphic-matroid forest complex

## Finding
Let \(P=KG(5,2)\) be the Petersen graph, whose ten vertices are the two-element subsets of \(\{0,1,2,3,4\}\), with an edge between two vertices when their subsets are disjoint. Let \(K=\operatorname{Ind}(M(P))\) be the independence complex of its graphic matroid: the fifteen *edges of* \(P\) are the simplicial vertices, and a set of these edges is a face if and only if it contains no graph cycle. The five-label relabeling action of \(S_5\) on \(P\) induces an action on \(K\).

**Theorem.** Over the rational numbers, this action satisfies
\[
\widetilde H_i(K;\mathbb Q)\cong
\begin{cases}
\mathbb Q[S_5]\oplus\mathbb Q[S_5],& i=8,\\
0,&i\ne8,
\end{cases}
\]
as rational \(S_5\)-representations. Thus the top homology has dimension \(240\); its character equals \(240\) at the identity and \(0\) at every other permutation. Every rational irreducible Specht module occurs with multiplicity twice its dimension, and the \(S_5\)-fixed subspace has dimension \(2\). Nonequivariantly, \(K\simeq\bigvee^{240}S^8\).

## Assumptions and scope
All graphs are finite and simple. The Petersen graph is the Kneser graph \(KG(5,2)\) with the graph model above. The forest complex uses edge subsets, not matchings, vertex-independent sets, directed Morse matchings, or two-particle configurations. A face with \(k\) graph edges is a simplex of dimension \(k-1\); the empty forest is retained in the augmented cellular chain complex. Homology groups in the equivariant assertion have coefficients in \(\mathbb Q\). The separate sphere-wedge assertion refers to ordinary homotopy type, not an equivariant wedge equivalence.

## Proof
**1. Homological concentration.** The Petersen graph is connected, so its graphic matroid has rank \(10-1=9\), and every maximal forest has nine graph edges. It has no bridge: the graph-edge transitive action of \(S_5\) and the graph five-cycle through vertex labels \(01,23,04,12,34,01\) exhibit a cycle containing every edge after relabeling. Hence the matroid is coloopless. Matroid independence complexes are shellable; for a coloopless rank-nine matroid the standard result states that \(K\) is homotopy equivalent to a wedge of eight-spheres, with number equal to the Tutte evaluation \(T_{M(P)}(0,1)\). In particular the sole potentially nonzero reduced homology is in degree eight, is integral free, and is finite-dimensional.

**2. Signed fixed-forest Lefschetz formula.** For \(g\in S_5\), let \(\mathcal O(g)\) be the set of orbits of the induced permutation of the fifteen edges of \(P\). For a subset \(J\subseteq\mathcal O(g)\), put \(F_J=\bigcup_{O\in J}O\). The forest \(F_J\) is fixed setwise by \(g\). Conversely every setwise invariant forest is of this form. A setwise invariant forest with \(k\) edges occupying exactly \(t\) orbits gives a signed simplicial trace \((-1)^{k-t}\) on its \((k-1)\)-chain generator because the edge permutation on this face is a product of \(t\) cycles. Its contribution to the reduced Lefschetz number is therefore \((-1)^{k-1}(-1)^{k-t}=(-1)^{t+1}\), including the empty face using the augmentation sign. As degree eight is the only nonzero reduced homology, the actual rational trace is exactly
\[
\operatorname{tr}\bigl(g\mid\widetilde H_8(K;\mathbb Q)\bigr)
=-\sum_{\substack{J\subseteq\mathcal O(g)\\F_J\text{ is a forest}}}(-1)^{|J|}.
\tag{1}
\]
This calculation is valid for all finite-order simplicial automorphisms; no assumption of freeness of the action is made.

**3. Exact finite evaluation.** In the canonical model, list the ten two-subsets lexicographically; list the fifteen unordered pairs of disjoint two-subsets lexicographically. For each of the seven conjugacy types of \(S_5\), choose its successive-cycle representative. Compute the induced edge permutation; partition the fifteen graph edges into its cycles. For each subset of those cycles, take their union and use union-find on the ten graph vertices to test whether it is a forest. Let \(a_t(g)\) be the number of valid unions selecting exactly \(t\) edge cycles. The complete nonzero lists \((a_0,a_1,\ldots)\) are:

| Cycle type on five labels | Counts of forest unions by selected edge orbits | Alternating sum | Homology trace |
| --- | --- | ---: | ---: |
| \((1,1,1,1,1)\) | 1, 15, 105, 455, 1365, 2991, 4875, 5805, 4680, 2000 | -240 | 240 |
| \((2,1,1,1)\) | 1, 9, 36, 80, 99, 63, 16 | 0 | 0 |
| \((2,2,1)\) | 1, 9, 36, 80, 97, 45 | 0 | 0 |
| \((3,1,1)\) | 1, 5, 9, 5 | 0 | 0 |
| \((3,2)\) | 1, 2, 1 | 0 | 0 |
| \((4,1)\) | 1, 5, 9, 5 | 0 | 0 |
| \((5)\) | 1, 1 | 0 | 0 |

The complete forest count by number of graph edges (from zero through nine) is the identity-row list. Its total is \(22{,}292\). Formula (1) gives the last column; the complete, reproducible enumerator and an independent signed-face enumeration over all \(120\) group elements are in `verify.py`.

**4. Representation identification.** The regular \(S_5\)-character takes value \(120\) at the identity and zero elsewhere. The preceding calculation is twice that character. Over characteristic zero, irreducible characters determine semisimple representations; moreover the irreducible representations of \(S_5\) are defined over \(\mathbb Q\) and are absolutely irreducible. It follows that \(\widetilde H_8(K;\mathbb Q)\cong\mathbb Q[S_5]^{\oplus2}\) as rational modules. The invariant subspace of each regular copy has dimension one, proving the fixed-subspace assertion. The prior shellability theorem and identity character yield the ordinary \(240\)-sphere wedge.

## Verification
The self-contained standard-library program `verify.py` independently checks (a) all \(2^{15}=32768\) candidate edge subsets, of which exactly \(22292\) are forests, (b) the seven orbit-union polynomials above, and (c) a second, direct oriented-simplex trace calculation for **each of the 120 permutations** of the five labels. It asserts \(240\) at the identity and \(0\) for the other \(119\). The finite enumeration exhausts the mathematical domain of (1); it is not used as a substitute for the cited general shellability theorem. The two implementations check different sign conventions: the orbit method weights edge cycles, whereas the direct method measures inversion parity on every invariant oriented face.

## Relationship to prior work
The matroid independence-complex shellability and wedge-of-spheres theorem is classical and is explicitly summarized and developed by Ardila, Castillo and Samper [1, Section 1 and Theorem 1.3]. The rank-nine concentration and ordinary wedge implication rely on that theorem and are not claimed as new general facts. Moci and Pezzoli [2, especially Sections 1 and 4–7] develop a general representation-theoretic relationship between matroid independence homology and homology of lattices of flats, and analyze particular families such as complete graphs. Their framework is a relevant general method, but their inspected text does not state the complete \(S_5\)-character of the Petersen graphic-matroid forest complex or its twice-regular decomposition. The present contribution is the exact symmetry-resolved evaluation for this canonical matroid, not a new generic matroid-shellability principle.

## Limitations
The decomposition is established over \(\mathbb Q\) only; the theorem does not assert an integral isomorphism with two integral group rings, an integral equivariant sphere-wedge splitting, or a classification for other graphs. Ordinary sphere-wedge homotopy follows from known matroid shellability, but the action on any chosen wedge model is not identified. As with literature-dependent novelty assessments, an unindexed or inaccessible calculation of the identical Petersen \(S_5\)-module could alter the originality assessment; no claim of universal bibliographic uniqueness is made.

## References
1. F. Ardila, F. Castillo, J. A. Samper, *The topology of the external activity complex of a matroid*, arXiv:1410.3870, initially public 2014-10-14; https://arxiv.org/abs/1410.3870 .
2. L. Moci, G. M. Pezzoli, *Representations of automorphism groups on the homology of matroids*, arXiv:2001.03760, initially public 2020-01-11; https://arxiv.org/abs/2001.03760 .
3. A. E. Brouwer, *Petersen graph* (graph model and automorphism group), https://aeb.win.tue.nl/graphs/Petersen.html .
