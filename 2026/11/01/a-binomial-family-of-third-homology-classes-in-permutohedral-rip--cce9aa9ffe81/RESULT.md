# A binomial family of third-homology classes in permutohedral Rips complexes

## Finding
For each integer \(n\geq1\), let \(P_n\) be the Cayley graph of the permutation group \(\mathfrak S_n\) in which two permutation words are adjacent if one is obtained from the other by swapping two consecutive positions. Give its vertices the shortest-path (Kendall adjacent-swap) metric, and let \(K_n=\operatorname{VR}_{\leq2}(P_n)=\operatorname{Cl}(P_n^2)\) be the **inclusive** scale-two Vietoris--Rips complex.

The first nonzero degree-three mod-two homology occurs at six letters:
\[
\widetilde H_3(K_n;\mathbb F_2)=0\quad(1\leq n\leq5),
\qquad
\widetilde H_3(K_6;\mathbb F_2)\cong(\mathbb F_2)^{90}.
\]
More strongly, for every \(n\geq6\), deletion and insertion of labels induce a **split injection**
\[
\bigoplus_{T\in\binom{[n]}6}\widetilde H_3(K_6;\mathbb F_2)
\longhookrightarrow\widetilde H_3(K_n;\mathbb F_2),
\]
where \(\binom{[n]}6\) denotes the six-element subsets of the label set \([n]\). Consequently,
\[
\boxed{\dim_{\mathbb F_2}\widetilde H_3(K_n;\mathbb F_2)\geq 90\binom n6\qquad(n\geq6).}
\]
The complete reduced mod-two homology at the first exceptional size is
\[
\widetilde H_j(K_6;\mathbb F_2)\cong
\begin{cases}
(\mathbb F_2)^{869},&j=2,\\
(\mathbb F_2)^{90},&j=3,\\
0,&j\notin\{2,3\}.
\end{cases}
\]

## Assumptions and scope
A permutation is a word listing every label exactly once. A graph edge swaps entries in **adjacent positions**; swapping arbitrary positions would define a different metric. The graph distance equals the number of discordant label pairs (Kendall tau distance). The Rips threshold \(2\) includes equality. Homology throughout this finding has coefficients \(\mathbb F_2\), not integral or rational coefficients. For the degenerate zero-label case used in the proof, regard \(K_0\) as a single point.

## Proof
**1. Exhaustive finite computation up to six labels.** Enumerate the \(n!\) permutation words, add adjacent-position swaps, and connect two distinct vertices if their graph distance is at most two. The maximal cliques of this square graph generate *all* simplices of \(K_n\). The certificate enumerates maximal cliques by Bron--Kerbosch recursion and then every nonempty subset of each. It indexes simplices in increasing vertex order and constructs each mod-two simplicial boundary column by deleting one vertex in every possible position. Exact Gaussian elimination with binary-integer XORs gives the following results (the boundary-rank sequence starts at \(\partial_1\)):

| \(n\) | Face counts \((f_0,f_1,\ldots)\) | Ranks \((\partial_1,\partial_2,\ldots)\) | Nonzero reduced mod-two Betti numbers |
|---:|---|---|---|
| 1 | \((1)\) | none | none |
| 2 | \((2,1)\) | \((1)\) | none |
| 3 | \((6,12,8)\) | \((5,7)\) | \(\widetilde\beta_2=1\) |
| 4 | \((24,96,112,30)\) | \((23,73,30)\) | \(\widetilde\beta_2=9\) |
| 5 | \((120,780,1320,690,120)\) | \((119,661,570,120)\) | \(\widetilde\beta_2=89\) |
| 6 | \((720,6840,15360,12060,4320,720)\) | \((719,6121,8370,3600,720)\) | \(\widetilde\beta_2=869,\ \widetilde\beta_3=90\) |

In particular, the exact rank identity for six labels is
\[
\dim\widetilde H_3(K_6;\mathbb F_2)
=f_3-\operatorname{rank}(\partial_3)-\operatorname{rank}(\partial_4)
=12060-8370-3600=90.
\]
At five labels, the analogous calculation gives \(690-570-120=0\). At four labels, all 30 top-dimensional tetrahedra have independent boundaries; at three or fewer labels there are no three-simplices. The complete ranks also give the displayed mod-two homology in all degrees at six labels. The finite computations are reproducible, fully enumerated boundary-matrix proofs, not statistical estimates or extrapolations.

Two independently organized implementations verify the crucial finite ranks: `verify_rips.py` constructs the graph by adjacent swaps, finds maximal cliques and reduces boundary **columns**, whereas `verify_independent.py` constructs graph distances by counting discordant pairs, enumerates faces directly and reduces boundary **rows**. The latter independently reproduces the face counts and the ranks of \(\partial_3\) and \(\partial_4\) for five and six letters.

**2. Split family of independent degree-three classes.** For a label subset \(T\subseteq[n]\), deleting all letters outside \(T\) from a permutation word gives a map \(\pi_T\) to words on \(T\). One adjacent swap of the original word either becomes an adjacent swap of the restricted word or leaves it unchanged. Thus \(\pi_T\) is \(1\)-Lipschitz for adjacent-swap distance and induces a simplicial map on scale-two Rips complexes.

For each six-subset \(T\), choose the increasing order on its labels to identify its permutation words with \(\mathfrak S_6\), and define \(\iota_T:\mathfrak S_6\to\mathfrak S_n\) by placing a permuted word on \(T\) first and then appending the labels of \([n]\setminus T\) in increasing order. This is an isometric embedding and \(\pi_T\circ\iota_T\) is the identity. For two different six-subsets \(T\ne U\), the composite \(\pi_T\circ\iota_U\) factors through the permutation space on \(T\cap U\): it first deletes all letters outside \(T\cap U\) and then appends the fixed letters of \(T\setminus U\). The factorization consists of \(1\)-Lipschitz maps and hence induces a factorization through \(K_{|T\cap U|}\). Since \(|T\cap U|\leq5\) and the preceding calculation established \(\widetilde H_3(K_r;\mathbb F_2)=0\) for \(0\leq r\leq5\), it follows that
\[
(\pi_T)_*(\iota_U)_*=\begin{cases}
\operatorname{id},&T=U,\\
0,&T\ne U
\end{cases}
\quad\text{on }\widetilde H_3(-;\mathbb F_2).
\]
Therefore the direct sum of the insertion maps is split injective, with retraction given by the direct sum of the deletion maps. There are \(\binom n6\) six-subsets, and each contributes an independent \(90\)-dimensional summand. This proves the claimed bound for **every** \(n\geq6\).

## Verification
Execute `python3 verify_rips.py` and `python3 verify_independent.py` from the directory of these files; both require only Python 3's standard library. The first prints `EXACT_GF2_VERIFY_OK`, the second `INDEPENDENT_CHECK_OK`. The first reconstructs 720 vertices, 2,940 maximal cliques, and 40,020 nonempty faces at six labels and checks all boundary ranks. The second uses independent metric, simplex-generation and row-reduction procedures. The accompanying `rank_certificate.json` and `verification_output.txt` record the exact outcomes, while the programs recompute rather than trust those records. The general split-injection argument is mathematical and does not rely on finite testing for larger \(n\).

## Relationship to prior work
Adamaszek's *Clique complexes and graph powers* (first public version April 3, 2011) establishes the graph-power/Rips correspondence and broad graph-square homotopy criteria, but its cycle classifications do not concern the permutohedral Cayley graphs. Its high-girth and square-neighborhood hypotheses cannot determine the present complexes, which contain commuting-generator four-cycles.

Adams and Virk (first public version September 12, 2023) develop lower bounds and homology-propagation arguments for graph-metric Vietoris--Rips complexes of **binary hypercubes**. Their coordinate-subcube projections motivate a useful conceptual comparison, but their stated theorems concern the Hamming-cube family and do not provide six-letter permutohedral homology ranks or a bound for adjacent-transposition Cayley graphs. The present subset-of-labels splitting is proved directly and does not claim to be the first abstract use of projection-based propagation.

The published *Complete mod-two Rips persistence of the four-letter permutahedron* computes the complete characteristic-two barcode for \(n=4\), including nine second-homology classes at scale two, but explicitly leaves higher symmetric groups open. The separate published *Complete graph-metric Vietoris--Rips filtration of the truncated octahedral graph* gives a homotopy refinement at \(n=4\), not at \(n\geq5\). The published *Complete Vietoris--Rips homotopy of the full transposition graph on 24 permutations* studies a **different metric**, generated by all transpositions rather than adjacent-position swaps. None of these statements implies the six-label degree-three rank or the subset-indexed split lower bound. A nonindexed equivalent computation remains possible; a negative search is not a proof of priority.

## Limitations
This result establishes mod-two homology only. It does **not** establish that the ninety classes at six letters lift to free integral homology, determine torsion, classify the homotopy type, or compute the exact third Betti number for \(n>6\). It addresses only the inclusive scale-two adjacent-swap metric; other scales, Euclidean permutohedral distance and the all-transposition metric differ. The split injections are vector-space statements and are not claimed to give an equivariant decomposition under the full symmetric-group action. Publication-priority verification and independent mathematical audit remain outstanding.

## References
1. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433v1, first public posting 2011-04-03; *Israel Journal of Mathematics* **196** (2013), 295--319. https://arxiv.org/abs/1104.0433
2. *Complete mod-two Rips persistence of the four-letter permutahedron*, public mathematical-results repository, October 11, 2026. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-complete-mod-two-rips-persistence-of-the-four-letter-permutahedr--5b20bd61b710
3. *Complete graph-metric Vietoris--Rips filtration of the truncated octahedral graph*, public mathematical-results repository, October 11, 2026. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-complete-graph-metric-vietoris-rips-filtration-of-the-truncated--3b8391bcadb8
4. H. Adams and Ž. Virk, *Lower bounds on the homology of Vietoris--Rips complexes of hypercube graphs*, arXiv:2309.06222v1, first public posting 2023-09-12. https://arxiv.org/abs/2309.06222
5. *Complete Vietoris--Rips homotopy of the full transposition graph on 24 permutations*, public mathematical-results repository, October 11, 2026. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-complete-vietoris-rips-homotopy-of-the-full-transposition-graph--eabeb40a2e42
