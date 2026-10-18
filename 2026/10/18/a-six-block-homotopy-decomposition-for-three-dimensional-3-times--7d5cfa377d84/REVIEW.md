# Scientific assessment

## Correctness — PASS

The all-parameter proof verifies the quantifiers directly: any two nonattacking cells on a 3-by-3-by-\(n\) board determine exactly one permutation between the first two axes, and each individual cell belongs to exactly two such permutation blocks. Distinct blocks meet in \(n\) discrete vertices only when their permutations differ by a transposition; triple intersections vanish. The resulting connected gluing multigraph is the six-node \(K_{3,3}\) with \(n\) parallel edges on each of its nine edges, giving first Betti number \(9n-5\). Homotopy pushout gluing along discrete vertices yields six ordinary chessboard complexes wedged with that many circles. The ordinary \(3\times n\) chessboard factors are proved casewise: elementary collapses at \(n=3\), oriented closed surface classification at \(n=4\), and the published connectivity bound followed by Hurewicz and homological Whitehead at all \(n\ge5\). Face counts give all sphere multiplicities. The checker reproduces concrete finite combinatorics and ranks for \(3\le n\le7\); those samples are not the all-parameter proof. No unresolved critical lemma remains.

## Originality — PASS, subject to residual literature risk

The closest verified primary text is Björner--Lovász--Vrećica--Živaljević (1994), *Chessboard Complexes and Matching Complexes*, DOI `10.1112/jlms/49.1.25`: Theorem 1.1 supplies ordinary chessboard connectivity and Section 3 treats embeddings/direct summands for higher-dimensional chessboards. Neither inspected statement identifies the six permutation blocks of a three-axis \(3\times3\times n\) board, the \(K_{3,3}\) gluing multigraph, or the resulting fundamental-group and homotopy classification. Vrećica--Živaljević (arXiv:0710.5252) studies cycle-free chessboards and mentions the ordinary torus, rather than this three-way matching complex. Wachs's survey, Section 9, expressly discusses multidimensional rook complexes, top homology and uncompleted generalizations, but states no six-block homotopy decomposition for this subclass. Targeted searches also considered hypergraph matching complexes, alternative \(\Delta_{3,3,n}\) notation, categorical-product graph constructions and published closely related results. No covering equality/stronger implication was found. Search failure alone is not novelty proof, and an unindexed analogous decomposition remains a residual risk.

## Mathematical value — PASS

The three-axis rook complex is an intrinsically defined matching complex of complete tripartite 3-uniform hypergraphs, a natural test family in higher-dimensional chessboard topology. Its complete homotopy type for all \(n\) is not a routine numerical restatement of the two-axis connectivity theorem: six genuine torus summands arise at \(n=4\), whereas for arbitrarily large \(n\) the fundamental group remains free and nontrivial even though every ordinary factor is simply connected. The six-block gluing argument gives a structural explanation of the persistent \(9n-5\) circle classes, with full free integral homology and nonlinear degree-two sphere multiplicities. There is no claim of a general family across all side lengths or an equivariant splitting.

## Closest literature and scientific limits

The earlier connectivity and torus facts are fully credited, not claimed as new. The principal original comparison is the mismatch between the published ordinary-chessboard statements and the newly established three-axis homotopy splitting. Independent verification and absolute priority are not asserted. The package contains a self-contained finite consistency checker and an all-parameter written proof; no downloaded third-party article is embedded.

Self-review: passed. Independent audit: not yet performed.
