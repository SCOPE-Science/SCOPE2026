# The Heawood perfect-matching homology is a sign twist of ordinary matching homology

## Finding
Let \(H\) be the Heawood graph, the fourteen-vertex incidence graph of the Fano plane, and write \(P=\mathcal M_{\mathrm p}(H)\) for the perfect-matching complex of all graph-edge sets extendible to a perfect matching. Write \(M=\mathcal M(H)\) for its ordinary matching complex, allowing all matchings. Both carry the natural action of the full graph automorphism group \(G=\operatorname{Aut}(H)\), of order \(336\). Let \(\varepsilon:G\to\{\pm1\}\) be \(+1\) on automorphisms preserving the point/line bipartition and \(-1\) on those exchanging it.

**Theorem.** The rational reduced homology representations of the two distinct complexes satisfy
\[
\boxed{\widetilde H_2(P;\mathbb Q)\cong_{\mathbb Q[G]}\varepsilon\otimes\widetilde H_4(M;\mathbb Q)}.
\]
In particular, writing \(B\le G\) for the index-two subgroup preserving the bipartition, let \(T_7\) be the augmentation kernel of the rational permutation module on the eight Sylow-seven subgroups of \(B\), and let \(W_8\) be the eight-dimensional rational irreducible representation defined by the character comparison below. Then
\[
\boxed{\widetilde H_2(P;\mathbb Q)\cong\varepsilon\otimes(\mathbf1\oplus T_7\oplus W_8)}.
\]
Every other reduced rational homology group of \(P\) vanishes. The full \(G\)-invariant second homology of \(P\) is zero, whereas its \(B\)-invariant second homology is one-dimensional. By contrast, the known full \(G\)-invariant fourth homology of \(M\) is one-dimensional. The known nonequivariant sphere-wedge homotopy types and the known ordinary-matching representation are **prior work**; the new assertion is the equivariant classification of \(P\) and its precise sign-twisted relationship to \(M\).

The complete character table has eight types, distinguished by bipartition action and element order:

| Bipartition | Element order | Number of elements | \(\chi_{\widetilde H_2(P)}\) | \(\chi_{\widetilde H_4(M)}\) |
|---|---:|---:|---:|---:|
| Preserved | 1 | 1 | 16 | 16 |
| Preserved | 2 | 21 | 0 | 0 |
| Preserved | 3 | 56 | 1 | 1 |
| Preserved | 4 | 42 | 0 | 0 |
| Preserved | 7 | 48 | 2 | 2 |
| Exchanged | 2 | 28 | -4 | 4 |
| Exchanged | 6 | 56 | -1 | 1 |
| Exchanged | 8 | 84 | 0 | 0 |

For instance, a bipartition-exchanging involution has trace \(-4\) on \(\widetilde H_2(P;\mathbb Q)\) but trace \(+4\) on \(\widetilde H_4(M;\mathbb Q)\). Hence the two representations are genuinely different; the sign twist is not a cosmetic rewriting.

## Assumptions and scope
All graphs are finite simple undirected graphs, and all representations in this theorem are over \(\mathbb Q\). Represent the seven Fano points and seven Fano lines by the nonzero vectors and covectors in \(\mathbb F_2^3\), identified with the binary integers \(1,\ldots,7\). Declare point \(p\) incident to line \(\ell\) exactly when their binary dot product is zero. This gives exactly \(21\) incidences, forming the bipartite graph \(H\).

A face of \(P\) is a set of graph edges contained in *some* seven-edge perfect matching; a face of \(M\) is any pairwise-disjoint set of graph edges. Thus \(P\subsetneq M\) is an inclusion of simplicial complexes on the same \(21\) vertices, but their nonzero reduced homology lies in different degrees. Neither complex has one vertex per perfect matching. Automorphisms of the graph act on both complexes by permuting the graph-edge vertices; \(G\) has \(168\) automorphisms preserving and \(168\) exchanging the two graph bipartition classes.

The result does not identify homology in degree two with homology in degree four by a natural chain map or suspension. It is an **abstract isomorphism of rational group modules**, established through equality of their complete characters.

## Proof
**Step 1: complete finite complexes.** A perfect matching is an incidence-compatible bijection from the seven points to the seven lines. Exhaustively iterating these bijections gives \(24\) perfect matchings. An independent subset-dynamic-programming permanent calculation gives the same count. Taking all subsets of the \(24\) perfect matchings yields exactly \(2,201\) nonempty faces of \(P\); enumerating all compatible edge subsets gives exactly \(3,461\) nonempty faces of \(M\). In dimension order zero through six the face-number vectors are
\[
(f_0,\ldots,f_6)(P)=(21,168,560,756,504,168,24),
\]
\[
(f_0,\ldots,f_6)(M)=(21,168,644,1218,1050,336,24).
\]
The attached standalone program reconstructs both sets from the stated graph definition rather than taking their sizes as input. In particular, this enumeration covers every face, not a sample.

**Step 2: rational homology concentration.** Exact binary elimination of each complete simplicial boundary matrix gives, in degrees one through six,
\[
(\operatorname{rank}_{\mathbb F_2}\partial_k)_{k=1}^6(P)
=(20,148,396,360,144,24),
\]
\[
(\operatorname{rank}_{\mathbb F_2}\partial_k)_{k=1}^6(M)
=(20,148,496,722,312,24).
\]
These binary ranks *also* force the ranks over \(\mathbb Q\), without treating mod-two homology as an integral calculation. For an integer matrix, rational rank is at least mod-two rank. The chain identities impose \(\operatorname{rank}\partial_k+\operatorname{rank}\partial_{k+1}\le f_k\), while \(\operatorname{rank}\partial_1\le f_0-1=20\); also \(\operatorname{rank}\partial_6\le f_6=24\). Successively imposing these upper bounds from both ends leaves no room for a rational rank strictly above the displayed binary rank. For example, for \(P\) the first three forced equalities are \(20\), \(168-20=148\), and \(560-148=412\) as an *upper bound* at the next step, tightened to \(396\) by the adjacent inequality with the lower bound \(360\) on the next boundary. All inequalities are applied simultaneously by the verifier, giving equality throughout. Consequently
\[
\widetilde H_i(P;\mathbb Q)=\begin{cases}\mathbb Q^{16},&i=2,\\0,&i\ne2,\end{cases}
\qquad
\widetilde H_i(M;\mathbb Q)=\begin{cases}\mathbb Q^{16},&i=4,\\0,&i\ne4.\end{cases}
\]

**Step 3: all graph symmetries.** Every color-preserving automorphism of the Fano incidence graph comes from an invertible linear map of \(\mathbb F_2^3\): it acts on points by the map and on lines by its contragredient. Enumerating all nonsingular binary three-by-three matrices produces exactly \(168\) edge permutations. Compose each with the point-line duality that interchanges vectors and covectors to obtain another \(168\) permutations. These are all the automorphisms: the connected bipartite graph has a unique bipartition, and a color-preserving automorphism is determined by its Fano point permutation. Thus all \(336\) cases are exhausted.

**Step 4: complete Lefschetz characters, with a second calculation.** For any \(g\in G\), its action on an oriented simplex fixed setwise contributes the parity of the induced vertex permutation to the simplicial-chain trace. Since each complex has one nonzero reduced rational homology degree, the alternating Lefschetz formula reads, in both cases,
\[
\chi_{\mathrm{top}}(g)=-1+
\sum_{\substack{\varnothing\ne\sigma\text{ a face}\\g\sigma=\sigma}}
(-1)^{\dim\sigma}\operatorname{sgn}(g|_\sigma).
\]
The program computes this signed sum directly for every group element. Independently, it decomposes each graph-edge permutation into cycles and selects every union of edge cycles that forms an allowed face. In that calculation, if \(J\) is the chosen set of permutation cycles, including the empty choice, the same reduced trace equals
\[
\chi_{\mathrm{top}}(g)=-\sum_{J:\ \cup J\text{ a face}}(-1)^{|J|}.
\]
The two independent algorithms agree for all \(336\) elements **for each of the two complexes**. Their results are the eight rows of the table above. In every case \(\chi_{\widetilde H_2(P)}(g)=\varepsilon(g)\chi_{\widetilde H_4(M)}(g)\).

**Step 5: identify the representations.** Maschke's theorem makes finite-group rational representations semisimple. Equality of character values on every element therefore gives the first displayed isomorphism. For the finer decomposition, enumerate the eight distinct Sylow-seven subgroups of the \(168\)-element color-preserving group \(B\). The character of their reduced eight-point permutation module \(T_7\) is the number of subgroups fixed under conjugation, minus one. Define the remaining character \(\chi_{W_8}=\chi_{\widetilde H_4(M)}-1-\chi_{T_7}\). The attached verifier evaluates the usual group-character inner products by summing over all \(336\) elements and obtains the exact identity matrix for \(\mathbf1,T_7,W_8\). In particular the residual character is irreducible and has dimension eight. This independently identifies the known ordinary-module decomposition and hence its twist for \(P\).

Finally, character averaging gives the dimension of invariants. The full-group average of \(\chi_{\widetilde H_2(P)}\) is zero; the average over \(B\) is one, while the full-group average for \(\chi_{\widetilde H_4(M)}\) is one. These are exact finite sums, not extrapolations.

## Verification
Execute `python3 verify_heawood_duality.py` using the Python 3 standard library; it requires no imported data. It checks the \(21\) incidences, all \(24\) perfect matchings (with an independent permanent computation), all \(2,201\) and \(3,461\) nonempty simplices, all complete mod-two boundary ranks, the forced rational ranks, every one of the \(336\) symmetry actions, two independent signed fixed-face computations for both complexes, the full character comparison, the Sylow-seven action, exact representation inner products, and the claimed invariant dimensions. The expected final output line is `VERIFY_OK`. The accompanying `verify_output.txt` records one successful run; the executable algorithm, not its log, provides the finite certificate.

## Relationship to prior work
A publicly available complete Morse reduction (identifier `0994476b8c0d`) already establishes the *nonequivariant* homotopy equivalence \(P\simeq\bigvee^{16}S^2\). A separate public calculation (identifier `d7a042784870`) already gives the ordinary complex's full rational automorphism module \(\widetilde H_4(M;\mathbb Q)\cong\mathbf1\oplus T_7\oplus W_8\); the prior ordinary homotopy classification is likewise not new. These two reports were examined in their full principal result/proof text. Neither asserts the point-line-exchanging symmetry character on \(\widetilde H_2(P;\mathbb Q)\), and neither nonequivariant sphere multiplicities nor the symmetry representation of the *larger, distinct complex* logically determines it. In particular, \(\varepsilon\) is nontrivial, as witnessed by the differing involution trace and invariant dimension.

The recent work of Agarwal and Basak on independence and perfect-matching complexes of Möbius and circular ladder graphs motivates checking the symmetry-sensitive topology of extendible-matching complexes beyond those graph families. Its perfect-matching theorems concern ladder graphs, not the Fano incidence graph or an arbitrary-graph equivariant classification. Bayer, Jelić Milutinović and Vega address the perfect-matching topology of honeycomb graphs; this does not cover the nonplanar Heawood graph. Unlike those results, the present theorem is narrowly about a canonical incidence graph and the *complete rational automorphism action*. No claim of universal novelty is inferred from unsuccessful searches alone.

## Limitations
This is a finite graph-specific result established by exhaustive but fully supplied exact algorithms. The representation isomorphism is rational, not an integral lattice isomorphism, a canonical chain map, an equivariant homotopy equivalence, or a theorem for projective planes of arbitrary order. The two previously known sphere-wedge homotopy types and the ordinary matching-complex module decomposition are explicitly excluded from the novelty claim. The complete comparison of indexed and accessible primary sources leaves the usual risk of unindexed or differently named overlapping results; independent external mathematical audit has not been performed.

## References
1. A. Agarwal and M. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601, first public 2026-08-31, especially the perfect-matching definitions and ladder results.
2. *Perfect Morse reduction of the Heawood perfect-matching complex*, public mathematical report, identifier `0994476b8c0d` (2026); used as prior nonequivariant context, not a newly proved claim.
3. *Full automorphism module of the Heawood matching complex*, public mathematical report, identifier `d7a042784870` (2026); used as prior ordinary-complex rational representation.
4. M. Bayer, M. Jelić Milutinović and J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803 (2022).
5. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145. Forman's methods underlie the previously known homotopy calculations but are not needed to infer the new character comparison from its exact chain counts.
