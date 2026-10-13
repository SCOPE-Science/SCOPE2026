# Uniqueness of the optimum six-symbol length-two 2-separable code
## Finding
Every maximum \(\overline{2}\)-separable code of length \(2\) over a six-symbol alphabet has \(16\) codewords and belongs to one equivalence class under independent permutations of the six symbols in each coordinate and interchange of the two coordinates. Equivalently, every extremal \(C_4\)-free subgraph of \(K_{6,6}\) is the incidence graph of the Fano plane with one incident point-line pair deleted.

There are exactly \(64{,}800\) labeled maximum codes. For the natural action of \( (S_6\times S_6)\rtimes S_2\), whose order is \(1{,}036{,}800\), the maxima form one orbit and the stabilizer of each maximum has order \(16\).

One representative, writing a codeword as an ordered pair of symbols, is
\[
\{00,01,12,13,20,22,24,31,33,34,40,43,45,51,52,55\}.
\]

## Assumptions and scope
For a code \(C\subseteq Q^2\), where \(|Q|=6\), and a nonempty coalition \(X\subseteq C\), its descendant is the Cartesian product of the coordinate-symbol sets occurring in \(X\). The code is \(\overline{2}\)-separable when distinct coalitions of sizes at most \(2\) have distinct descendants.

Associate to \(C\) a bipartite graph with two labeled copies of \(Q\), putting an edge \(ij\) exactly when \((i,j)\in C\). Two distinct two-codeword coalitions have the same descendant exactly when their four codewords are the four corners of a \(2\times2\) rectangle. Hence \(C\) is \(\overline{2}\)-separable exactly when the associated bipartite graph is \(C_4\)-free. This is the length-two packing equivalence used in the cited separable-code literature.

## Proof
Let the six neighborhoods on one side of a \(C_4\)-free bipartite graph be blocks \(B_1,\ldots,B_6\) on a six-point set. Distinct blocks intersect in at most one point. If their sizes are \(d_1,\ldots,d_6\), then
\[
\sum_{i=1}^6 \binom{d_i}{2}\le \binom{6}{2}=15.
\]
If the graph had at least \(17\) edges, convexity makes the left side at least
\[
5\binom{3}{2}+\binom{2}{2}=16,
\]
a contradiction. Thus the maximum is at most \(16\), and the displayed representative attains \(16\).

Now assume equality. The only nondecreasing six-term degree sequences of sum \(16\) satisfying the pair bound are
\[
(1,3,3,3,3,3),\qquad(2,2,2,3,3,4),\qquad(2,2,3,3,3,3).
\]
The first would force five triples to cover all fifteen point-pairs exactly once. A point would then have to meet its other five points in pairs contributed two at a time by triples, which is impossible. For the second, the pair sum is again fifteen. A block of size four leaves only two outside points, so each of the two size-three blocks must contain both outside points; their intersection would then contain two points, contradicting \(C_4\)-freeness. Therefore every equality case has block-size multiset \( (3,3,3,3,2,2)\).

These six blocks cover exactly fourteen of the fifteen point-pairs, each once. Let \(\{a,b\}\) be the unique uncovered pair and call the other four points ordinary. If \(r_3(x)\) and \(r_2(x)\) count the triples and pairs containing a point \(x\), then every ordinary point satisfies
\[
2r_3(x)+r_2(x)=5,
\]
whereas \(a\) and \(b\) satisfy the same equation with right side \(4\). Since there are only two pair-blocks, each ordinary point must have \(r_3=2\) and \(r_2=1\). Thus the two pair-blocks form a perfect matching on the four ordinary points. They exhaust all pair-block incidences, so \(a\) and \(b\) each lie in exactly two triples and no pair-block.

No triple contains both \(a\) and \(b\). The two triples through \(a\) therefore determine one perfect matching on the four ordinary points, and the two triples through \(b\) determine a second. Neither can repeat the pair-block matching or each other, because no point-pair may occur twice. Since \(K_4\) has exactly three perfect matchings, these are precisely its three perfect matchings. This proves uniqueness up to relabeling.

Adding a seventh point to each of the two pair-blocks and adjoining the triple consisting of that new point with \(a\) and \(b\) produces seven triples on seven points in which every pair occurs once. This is the unique Steiner triple system on seven points, namely the Fano plane. Reversing the construction shows that every equality graph is the Fano incidence graph with one incident point-line pair deleted.

For the labeled count, choose the uncovered point-pair in \(\binom{6}{2}=15\) ways, choose the pair-block perfect matching on the other four points in \(3\) ways, assign the two remaining perfect matchings to the two labeled uncovered points in \(2\) ways, and label the six blocks in \(6!\) ways. Hence
\[
15\cdot3\cdot2\cdot6!=64{,}800.
\]
Side-preserving relabelings have order \( (6!)^2=518{,}400\), so the unique orbit has stabilizer order \(8\). Coordinate interchange preserves the single orbit and doubles the acting group, giving stabilizer order \(16\) in \( (S_6\times S_6)\rtimes S_2\).

## Verification
The standalone verifier `artifacts/verify_q6_separable.py` independently enumerates every row-multiset representation of a \(6\times6\) \(C_4\)-free matrix with \(16\) or \(17\) ones. It finds no \(17\)-edge case and exactly \(90\) row-sorted \(16\)-edge cases with labeled columns. It checks the degree profile, the unique uncovered pair, the Fano completion, the descendant definition for every maximum, the labeled count, and the full natural-group orbit.

The recorded replay output is in `artifacts/verification_output.txt`.

## Relationship to prior work
Cheng, Fu, Jiang, Lo, and Miao prove the equivalence between length-two \(\overline{2}\)-separable codes and \(C_4\)-free bipartite graphs, and their exact-value theorem gives \(M(\overline{2},2,6)=z(6;2)=16\). Their paper constructs optimal families and studies bounds, but the inspected full text does not classify all equality cases or count labeled maxima. The present finding supplies that missing equality structure.

A later paper on an augmented Zarankiewicz problem explicitly uses a \(16\)-edge \(C_4\)-free graph on \(6+6\) vertices as a base skeleton and treats classification of extremal \(6\times n\) \(C_4\)-free graphs as a more complicated issue; it does not provide the classification above.

## Limitations
The claim is only for alphabet size six and length two. It classifies maxima under the standard coordinate/symbol equivalence and does not assert a classification for larger alphabets or unbalanced bipartite graphs. A historically plausible 2000 source establishes small exact Zarankiewicz values; only its abstract and bibliographic metadata were accessible in this review, so an obscure equality-case classification there remains a residual literature risk. The mathematical classification itself is proved here and independently replayed by exhaustive finite verification.

## References
1. M. Cheng, H.-L. Fu, J. Jiang, Y.-H. Lo, and Y. Miao, “New bounds on \(\overline{2}\)-separable codes of length 2,” *Designs, Codes and Cryptography* 74 (2015), 31–40. DOI: 10.1007/s10623-013-9849-9. First published online 27 June 2013.
2. W. Goddard, M. A. Henning, and O. R. Oellermann, “Bipartite Ramsey numbers and Zarankiewicz numbers,” *Discrete Mathematics* 219 (2000), 85–95. DOI: 10.1016/S0012-365X(99)00370-2.
3. “New Lower Bounds for the Limited Augmented Zarankiewicz Number Based on Complete Graphs,” *Symmetry* 18 (2026), 1076. DOI: 10.3390/sym18071076.
