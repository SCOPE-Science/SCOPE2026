# Exact triangle spectrum of the two-read deletion-confusability graph

## Finding

Let \(q\ge2\) and \(n\ge1\) be integers. On the vertex set \(\Sigma_q^n\), join distinct length-\(n\) words when their sets of distinct length-\(n-1\) single-deletion descendants intersect in at least two words. Write \(T_q(n)\) for the number of unordered triangles of this graph. Then

\[
T_q(n)=q(q-1)\sum_{\ell=4}^{n}(n-\ell+1)(\ell-3)q^{n-\ell},
\]

where an empty sum is zero. Equivalently, as a formal power series,

\[
\sum_{n\ge0}T_q(n)z^n=\frac{q(q-1)z^4}{(1-qz)^2(1-z)^2}.
\]

Every triangle has a unique description: select a common outside context, one interval of length \(\ell\ge4\), two different letters, and a cut strictly at least two positions from both ends of the interval; place opposite alternating phases on the interval to make two vertices, and form the third by splicing the prefix of one phase to the suffix of the other. There are precisely two distinct splice choices. In particular no triangle exists for \(n<4\).

## Assumptions and scope

The alphabet \(\Sigma_q\) has exactly \(q\) distinct labeled symbols. The deletion-descendant set \(D_1(x)=\{x_1\cdots x_{i-1}x_{i+1}\cdots x_n:1\le i\le n\}\) is a **set**, so repeated deletion outcomes are counted only once. The graph has an undirected edge \(xy\) if and only if \(x\ne y\) and \(|D_1(x)\cap D_1(y)|\ge2\); a triangle is an unordered set of three distinct pairwise adjacent words. The formula holds for all finite integers \(q\ge2\) and \(n\ge1\), without a probabilistic or asymptotic assumption. The standard Type-A edge characterization quoted below applies to arbitrary alphabets.

## Proof

**1. Edge characterization.** The Type-A confusability criterion in Cai–Kiah–Nguyen–Yaakobi, Proposition 9, states that two distinct words have at least two distinct common single-deletion descendants if and only if there are positions \(i<j\) and distinct letters \(a,b\) for which the two words agree outside \([i,j]\) and are opposite alternating phases on it:

\[
x[i:j]=aba\cdots,\qquad y[i:j]=bab\cdots.
\]

Their first and last differing positions are therefore exactly \(i,j\), uniquely specifying the **edge interval** \(I_{xy}=[i,j]\) of length at least two. The result is not restricted to a binary alphabet; the interval itself uses exactly two distinct symbols. The cited proposition proves necessity by comparing the two possible extreme deletion alignments and sufficiency by deleting opposite ends of the alternating interval. We use this published equivalence as an established lemma.

**2. No three distinct letters at one coordinate.** Let \(x,y,z\) be a triangle. Suppose their symbols at position \(t\) were pairwise different, say \(a,b,c\). Each of the three edge intervals \(I_{xy},I_{xz},I_{yz}\) contains \(t\), and, because each has length at least two, extends to \(t-1\) or \(t+1\) (with only the available direction at an endpoint). By pigeonhole, two intervals extend to the same neighboring position. Those two edges share one of the vertices, for instance \(x\). Alternation on the first edge forces the neighbor's symbol of \(x\) to equal \(b\), and alternation on the second forces it to equal \(c\). Since \(b\ne c\), this is impossible. Thus at every coordinate either all three symbols coincide or exactly two coincide.

**3. Interval geometry.** In the latter case precisely two of the three edge intervals contain that coordinate. In the former case none do. Therefore three nonempty integral intervals cover each position either zero or twice. Such a family necessarily consists of one long interval \([i,j]\) and two disjoint adjacent intervals \([i,s]\), \([s+1,j]\), for some \(i\le s<j\). To see this directly, at the first covered coordinate exactly two intervals start. If both ended together, the third interval could not be nonempty without covering a position once. Hence one of these two intervals ends first; at the next position the third interval begins (to maintain double coverage), while the other initial interval continues to the common right endpoint. This proves the asserted arrangement, up to permuting the three edges. All three edge intervals have length at least two, forcing \(i+1\le s\le j-2\) and \(j-i+1\ge4\). The longest interval is unique.

**4. Unique structural reconstruction.** Let \(x,y\) denote the endpoints of the unique long edge interval \([i,j]\). They are opposite alternating phases there. The third word \(z\) agrees with one of \(x,y\) on \([i,s]\), and with the other on \([s+1,j]\); outside \([i,j]\) all three agree. These are the two possible splices, and both give two shorter opposite-alternating edge intervals of lengths at least two, hence a triangle by Step 1. Conversely, Steps 2–3 show that every triangle has this form, and the long-edge uniqueness prevents counting the same triangle twice.

**5. Count and generating function.** Fix \(\ell=j-i+1\). The interval's location has \(n-\ell+1\) choices, its outside context has \(q^{n-\ell}\) choices, and the unordered pair of alternating letters has \(\binom q2\) choices. The cut has \(\ell-3\) possibilities and the splice orientation two possibilities. The product equals \(q(q-1)(n-\ell+1)(\ell-3)q^{n-\ell}\). Summing \(4\le\ell\le n\) gives the formula. Finally, set \(m=n-\ell\ge0\) and \(r=\ell-4\ge0\). Summing the factors \(q^m(m+1)\) and \(r+1\) independently gives

\[
\sum_{n\ge0}T_q(n)z^n=q(q-1)z^4
\left(\sum_{m\ge0}(m+1)(qz)^m\right)
\left(\sum_{r\ge0}(r+1)z^r\right)
=\frac{q(q-1)z^4}{(1-qz)^2(1-z)^2}.
\]

## Verification

The included standalone Python program `verify_triangles.py` constructs the graph in two different ways: (i) directly enumerating distinct single-deletion descendant sets and testing pairwise intersection size at least two, and (ii) constructing all edges from the alternating-interval lemma. It compares the entire edge sets in sixteen small alphabet/length instances, then exhaustively counts and structurally classifies every triangle in nineteen instances, checking both the closed expression and the long-interval/two-short-interval normal form. The executed script reported `VERIFY_OK direct_edge_cases=16 triangle_structural_cases=19`. The separate direct edge computation reached \(q=2,n=7\), \(q=3,n=5\), and \(q=4,n=4\); the structural triangle census reached \(q=2,n=8\), \(q=3,n=6\), and \(q=4,n=5\). These finite checks are consistency tests, **not** substitutes for the all-parameter argument above. Reproduce with `python3 verify_triangles.py` using only the Python standard library.

## Relationship to prior work

Cai–Kiah–Nguyen–Yaakobi's Type-A characterization (Proposition 9) supplies the complete pairwise edge criterion, and is explicitly used rather than claimed as new. Chrisnata–Kiah–Yaakobi study the binary confusability graph and a covering family of cliques; their relevant graph-theoretic sections concern independence bounds and clique covers, not the exact all-alphabet triangle census. A published published-finding corpus item entitled *Exact edge count of the finite-alphabet two-read single-deletion reconstruction graph* gives the edge count and unique opposite-phase interval decomposition but not this three-vertex characterization or triangle count. A different published result counts triangles in the **ordinary binary one-read** single-deletion confusability graph (an edge requires at least one common descendant); it does not imply the result for the strictly smaller two-read graph. Matching numerical coefficients of the binary series to an unrelated integer sequence do not amount to an interpretation or proof for this graph.

## Limitations

The theorem counts triangles, not maximum cliques, chromatic numbers, code sizes, or higher-order cliques. It presumes the Type-A edge theorem, for which a full proof is in the cited primary literature; a self-contained rederivation of that established theorem is not claimed. The literature comparison cannot exclude an unindexed equivalent enumeration, especially one implicit in clique-cover constructions; the known pairwise results must not be mistaken for prior triangle counts. The finite verification is not infinite certification. No independent mathematical audit has been performed.

## References

1. Kui Cai, Han Mao Kiah, Tuan Thanh Nguyen, Eitan Yaakobi. *Coding for Sequence Reconstruction for Single Edits*. arXiv:2001.01376, first public preprint January 6, 2020. See Definition 8 and Proposition 9 for Type-A confusability. https://arxiv.org/abs/2001.01376
2. Johan Chrisnata, Han Mao Kiah, Eitan Yaakobi. *Optimal Reconstruction Codes for Deletion Channels*, arXiv:2004.06032v1 (April 13, 2020); expanded journal article *Correcting Deletions With Multiple Reads*, IEEE Transactions on Information Theory 68 (2022), 7141–7160. See Section IV on the two-read binary confusability graph and clique covers. https://arxiv.org/abs/2004.06032
3. *Exact edge count of the finite-alphabet two-read single-deletion reconstruction graph*. Published mathematical research record, identifier `2026/10/4/SCOPE-exact-edge-count-of-the-finite-alphabet-two-read-single-deletion--737fed325e91`.
4. *Exact triangle count in the binary single-deletion graph*. Published mathematical research record, identifier `2026/10/4/SCOPE-exact-triangle-count-in-the-binary-single-deletion-graph--a53aac659908` (a different, one-read graph).
