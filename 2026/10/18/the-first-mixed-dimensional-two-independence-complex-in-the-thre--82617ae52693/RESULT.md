# The first mixed-dimensional two-independence complex in the three-row rook sequence

## Finding
For integers \(1\le n\le6\), let \(R_n=K_3\mathbin{\square}K_n=L(K_{3,n})\) be the rook graph of a \(3\)-by-\(n\) board. Write \(X_n=\operatorname{Ind}_2(R_n)\) for its two-independence complex: a set of squares is a face precisely when every connected component of the graph induced on those squares has at most two vertices. The **complete integral homotopy types** in the stated range are
\[
\begin{aligned}
X_1&\simeq S^1,\\
X_2&\simeq\bigvee^{4}S^1,\\
X_3&\simeq\bigvee^{5}S^2,\\
X_4&\simeq\bigvee^{13}S^3,\\
X_5&\simeq\bigvee^{61}S^3,\\
X_6&\simeq\bigvee^{113}S^3\vee\bigvee^{7}S^4.
\end{aligned}
\]
In particular, the three-by-six rook graph is the **first** graph in this sequence whose two-independence complex has reduced integral homology in more than one degree. The theorem is finite in its column parameter: no assertion about \(n\ge7\) or a periodic pattern is made.

## Assumptions and scope
The graphs are finite, simple, undirected, and loop-free. Vertices of \(R_n\) are cells \((i,j)\), where \(0\le i<3\) and \(0\le j<n\); different cells are adjacent when they share a row or column. Faces use the **induced** graph condition, not a choice of a degree-constrained subset of rook edges. A selected cell has induced degree equal to the number of other selected cells in its row plus the number in its column. Thus if \(r_i\) and \(c_j\) are the selected row and column populations, the defining condition is exactly
\[
(i,j)\text{ selected}\quad\Longrightarrow\quad r_i+c_j\le3.
\]
Indeed, a simple graph has components of order at most two precisely when every vertex has degree at most one. Each row contains at most two selected cells, so every face has at most six vertices, and complete finite enumeration through dimension five is exhaustive.

## Proof
**Step 1: Enumerate the exact complexes.** Encode a face as a nonzero bit mask on \(3n\) squares, with bit \(in+j\) corresponding to \((i,j)\). Test each of the \(2^{3n}-1\) possible nonempty masks by checking induced adjacency degrees. The complete dimension-by-dimension counts for \(n=1,2,3,4,5,6\) respectively are
\[
\begin{array}{c|r|l}
n&\text{nonempty faces}&(f_0,f_1,f_2,f_3,f_4,f_5)\text{ with trailing zeros omitted}\\\hline
1&6&(3,3)\\
2&27&(6,15,6)\\
3&96&(9,36,42,9)\\
4&300&(12,66,132,90)\\
5&870&(15,105,300,360,90)\\
6&2361&(18,153,570,990,540,90)
\end{array}
\]

**Step 2: Construct explicit acyclic integer discrete-Morse reductions.** In each finite complex, process the vertices in the pivot order below; for each pivot \(v\), pair every still-unpaired face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\), whenever both are still unpaired, and remove both. In this algorithm the displayed orders are **zero-based bit indices**. Every pair is a covering relation in the nonempty face poset:

```
1: 0 1 2
2: 0 1 2 3 4 5
3: 0 7 3 2 6 4 1 5 8
4: 0 6 8 5 3 1 9 2 4 7 10 11
5: 3 6 9 13 12 5 2 10 11 4 0 8 7 1 14
6: 10 5 14 16 2 11 6 0 13 3 8 12 4 17 1 7 15 9
```

Acyclicity is not assumed from the construction: the supplied exact checker constructs **every** Hasse cover, directs unmatched covers downward and matched covers upward, and verifies that the resulting directed graph admits a full topological ordering. The cover counts are \(6,48,234,888,3000,9216\); all directed Hasse graphs are acyclic. Their matching sizes are \(2,11,45,143,404,1120\), respectively. The remaining critical-cell dimension counts are
\[
\begin{array}{c|l}
n&\text{critical cells by dimension}\\\hline
1&(0:1,1:1)\\
2&(0:1,1:4)\\
3&(0:1,2:5)\\
4&(0:1,3:13)\\
5&(0:1,3:61)\\
6&(0:1,3:113,4:7).
\end{array}
\]
Consequently, Forman's discrete-Morse theorem supplies CW complexes with these exact cell counts and their homotopy types equal to \(X_n\).

**Step 3: Compute all integral Morse boundaries exactly.** Orient each simplicial face by increasing bit index. For a matched pair \(\sigma\subset\tau\), let \([\tau:\sigma]\in\{+1,-1\}\) denote incidence. To project a face \(\sigma\) onto critical faces of its dimension, set \(P(\sigma)=\sigma\) for a critical face, \(P(\sigma)=0\) for a matched upper face, and for a matched lower face with upper partner \(\tau\) use
\[
P(\sigma)=-[\tau:\sigma]\sum_{\substack{\rho\subset\tau\\|\rho|=|\sigma|\\\rho\ne\sigma}}[\tau:\rho]P(\rho).
\]
Because the matching is acyclic, this recursion terminates. The integral Morse differential of a critical face \(\eta\) is \(\sum_{\rho\subset\eta}[\eta:\rho]P(\rho)\). The supplied program performs these operations with exact Python integers and checks that **every resulting Morse differential is zero**, including all seven potentially nontrivial maps from degree four to degree three when \(n=6\).

**Step 4: Promote the CW complexes to integral homotopy wedge classifications.** For \(n\le5\), the reduced CW complex has one vertex and cells in only one positive degree, so it is a wedge of spheres in that degree. For \(n=6\), its three-skeleton is \(\bigvee^{113}S^3\) and its seven four-cells attach by maps in
\[
\pi_3\bigl(\bigvee^{113}S^3\bigr)\cong H_3\bigl(\bigvee^{113}S^3;\mathbb Z\bigr)\cong\mathbb Z^{113},
\]
where the first isomorphism is Hurewicz. The integer Morse differential records these attaching degrees; it is zero. Hence each attaching map is null-homotopic, and the claimed \(113\)-plus-\(7\) sphere wedge follows.

## Verification
The self-contained script `rook_2_independence_verify.py` derives the face sets directly from the induced rook adjacency graph, generates all matching pairs from the displayed pivot words, checks every covering relation and directed-cycle condition, and evaluates the signed integral Morse boundary via an exact terminating recursion. Its successful output is included as `rook_2_independence_verify.out`.

The independently written `rook_homology_crosscheck.py` generates faces using row/column populations instead of adjacency masks, constructs mod-two boundary matrices by ordered combinations, reduces them over \(\mathbb F_2\), and verifies the Betti numbers for every case. Its successful output is included as `rook_homology_crosscheck.out`. The latter test alone would not establish integral torsion-freeness or the wedge decomposition; those conclusions follow from the exact discrete-Morse certificate.

## Relationship to prior work
Sawant's 2026 theorem (arXiv:2605.25150v1, Theorem 3.6) treats two-independence complexes of **trees**, and explicitly observes equivalence with three-path-free complexes. Every \(R_n\) with \(n\ge2\) contains a four-cycle, so that theorem does not imply this calculation. Ghosh and Selvaraja (arXiv:2505.06614) study chordality and shellability of higher independence complexes for specific graph classes and constructions; the present finite three-row rook homotopy types are not identified there. Carnero Bravo (arXiv:2505.06457) studies **ordinary** independence complexes of graph products, which use the stricter no-adjacent-vertices face condition; classical chessboard-complex results thus do not establish these two-independence conclusions.

Related indexed records on three-cut complexes of rook graphs, neighborhood complexes of rook graphs, ordinary rook independence complexes, and capacity-two bipartite matching complexes have different face conditions. They neither give this induced-degree-at-most-one rook complex nor imply its seven degree-four generators. Related source records that could only be consulted through indexed descriptions, rather than complete papers, remain an originality risk.

## Limitations
This is a theorem for **exactly** \(1\le n\le6\), with no assertion for larger boards, other row counts, or analogous graph families. Its proof is a fully specified finite exhaustive Morse computation with a separate cross-check, not a closed-form recurrence or an infinite-family classification. Its novelty comparison is best-knowledge rather than a proof of global mathematical uniqueness. Independent external validation is not claimed.

## References
1. Rutuja Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150v1, first public 2026-05-24. https://arxiv.org/html/2605.25150v1
2. Arka Ghosh and S. Selvaraja, *Chordality and Shellability of Higher Independence Complexes*, arXiv:2505.06614, first public 2025-05-10. https://arxiv.org/abs/2505.06614
3. Andrés Carnero Bravo, *On independence complexes of graph products*, arXiv:2505.06457, first public 2025-05-09. https://arxiv.org/abs/2505.06457
4. Robin Forman, *Morse theory for cell complexes*, Advances in Mathematics **134** (1998), 90–145. Discrete-Morse CW homotopy theorem and gradient path chain complex.
