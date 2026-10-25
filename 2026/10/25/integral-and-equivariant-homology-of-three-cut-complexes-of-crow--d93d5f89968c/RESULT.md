# Integral and equivariant homology of three-cut complexes of crown graphs

## Finding
For every integer \(n\geq5\), let \(G_n\) be the *crown graph*: two labeled parts \(A=\{a_1,\ldots,a_n\}\), \(B=\{b_1,\ldots,b_n\}\), with every cross-edge except \(\{a_i,b_i\}\). Let \(X_n=\Delta_3(G_n)\) be the **ordinary** three-cut complex, whose facets are the complements of three-vertex subsets inducing disconnected subgraphs. Put
\[
  b_n=1+\frac{n(n-2)(n-3)(n-5)}4.
\]
Then all reduced integral homology groups are free, with
\[
 \widetilde H_k(X_n;\mathbb Z)\cong
 \begin{cases}
 \mathbb Z^{b_n},&k=2n-6,\\
 \mathbb Z^{n},&k=2n-4,\\
 0,&\text{otherwise}.
 \end{cases}
\]
In particular, the pure complex \(X_n\) is **not shellable**, for every \(n\ge5\). The first values of \(b_n\) are \(1,19,71,181\) for \(n=5,6,7,8\).

The full rational character of \(S_n\times C_2\) on both homology groups is also determined. A simultaneous permutation \(\sigma\in S_n\) relabels the two parts, and \(\varepsilon\in\{0,1\}\) records whether the two parts are exchanged. Write \(c_j\) for the number of cycles of length \(j\) in \(\sigma\). Define
\[
P(t)=1-t+\binom t2,\qquad
Q(t)=1-2t+4\binom t2-6\binom t3+6\binom t4,
\]
\[
T_0=Q(c_1)-2c_2P(c_1)+c_2(c_2-1),\qquad
T_1=1-2c_2+4\binom{c_2}{2}-2c_4.
\]
(As usual, \(\binom jk=0\) for \(0\le j<k\).) The character formulas are
\[
\operatorname{tr}\bigl((\sigma,\varepsilon)\mid\widetilde H_{2n-6}(X_n;\mathbb Q)\bigr)
=(-1)^{n\varepsilon}T_\varepsilon,
\]
\[
\operatorname{tr}\bigl((\sigma,\varepsilon)\mid\widetilde H_{2n-4}(X_n;\mathbb Q)\bigr)
=(-1)^{(n+1)\varepsilon}c_1.
\]

## Assumptions and scope
All graphs are finite simple undirected graphs. The ordinary cut-complex convention is the one from Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram, and Xue: facets are complements of **disconnected**, not connected, induced triples. Coefficients are integral for the group classification and rational for the representation characters. Here \(n\ge5\) is essential to the shellability argument; the four-pair graph is the three-cube and is **not** part of this new-family claim. No assertion is made about the full homotopy type of \(X_n\) or its integral representation decomposition.

## Proof
**1. Alexander dual and exact face classification.** Write \(L_n=X_n^\vee\), the combinatorial Alexander dual on the same \(2n\) vertices. From the facet definition, a vertex subset \(U\) is a face of \(L_n\) if and only if it contains no disconnected three-vertex induced subgraph. For any three vertices in one part the induced graph is disconnected; likewise, if two selected vertices lie in one part and the third lies in the other, the induced triple is disconnected precisely when that third vertex is the omitted matching partner of one of the two. Consequently, a face with at least three vertices has at most two vertices in each part and at most one vertex from every omitted matched pair. Conversely, each such subset does contain only connected induced triples. Every matched pair \(\{a_i,b_i\}\) is itself a face, but belongs to no triangle of \(L_n\).

Let \(B_n\) denote the multiple chessboard complex with two rows of capacity two and \(n\) columns of capacity one, where the chessboard squares are \(a_i\) and \(b_i\). We have the **equality of abstract simplicial complexes**
\[
L_n=B_n\cup \bigcup_{i=1}^{n}\{a_i,b_i\},
\]
where these last \(n\) one-simplices meet \(B_n\) only in their endpoints. This identification can alternatively be checked by explicitly classifying all disconnected triples of the crown graph.

**2. Shellable core and its exact top rank.** Theorem 4.4 of Jojić–Vrećica–Živaljević states that a multiple chessboard complex with row capacities \(k_1,\ldots,k_r\), column capacity one and \(m\ge\sum_i k_i+r-1\) columns is shellable. Here the criterion reads \(n\ge5\). The complex \(B_n\) is pure and three-dimensional: every face extends to a choice of two columns in each row (there are \(n\ge4\) columns). Hence shellability yields a homotopy type that is a wedge of three-spheres and, in particular, vanishing reduced integral homology below degree three and no torsion.

Directly choosing up to two squares in each row with different columns gives the face counts
\[
f_0=2n,\quad f_1=2n(n-1),\quad f_2=n(n-1)(n-2),\quad
f_3=\binom n2\binom{n-2}{2}.
\]
The reduced Euler characteristic therefore gives
\[
\operatorname{rank}\widetilde H_3(B_n;\mathbb Z)
=1-f_0+f_1-f_2+f_3
=1+\frac{n(n-2)(n-3)(n-5)}4=b_n.
\]

**3. Extra edges and Alexander duality.** The connected and simply connected complex \(B_n\) acquires exactly \(n\) independent one-cycles upon adjoining the \(n\) matching edges, with no new higher-dimensional cells. For example, the long exact sequences of the pairs \((L_n,B_n)\) and the fact that \(B_n\) is connected give
\[
\widetilde H_1(L_n;\mathbb Z)=\mathbb Z^n,\qquad
\widetilde H_3(L_n;\mathbb Z)=\mathbb Z^{b_n},
\]
with all other reduced integral homology zero. The integral universal coefficient theorem shows that the cohomology groups of \(L_n\) have the same torsion-free ranks. Combinatorial Alexander duality on \(2n\) vertices gives
\[
\widetilde H_i(X_n;\mathbb Z)\cong\widetilde H^{2n-i-3}(L_n;\mathbb Z),
\]
proving the asserted complete integral homology classification. Every facet of \(X_n\) has \(2n-3\) vertices, so \(X_n\) is pure of dimension \(2n-4\). Since its reduced homology is nonzero in the strictly smaller dimension \(2n-6\), it cannot be shellable.

**4. Equivariant character.** For an automorphism \(g\) of a simplicial complex with homology concentrated in degree three, its degree-three character equals the **signed face sum**
\[
 \sum_{F\text{ face},\;gF=F}(-1)^{|F|}\operatorname{sgn}(g\mid F),
\]
with the empty face included. For the row-preserving action of \(\sigma\) on \(B_n\), only one- and two-cycles of \(\sigma\) can participate in a fixed face (each row holds at most two squares). If formal variables \(u,v\) mark the row sizes, the signed fixed-face contribution, truncated to degree at most two in each variable, is
\[
(1-u-v)^{c_1}(1-u^2-v^2)^{c_2}.
\]
Summing its permitted coefficients gives \(T_0\). Under row exchange, only two- and four-cycles of \(\sigma\) are allowable, giving the corresponding truncated product
\[
(1-2uv)^{c_2}(1-2u^2v^2)^{c_4},
\]
and hence \(T_1\). This determines the full \(S_n\times C_2\) character on \(\widetilde H_3(B_n;\mathbb Q)=\widetilde H_3(L_n;\mathbb Q)\).

The relative one-cycles \(\{a_i,b_i\}\) form a basis for \(H_1(L_n,B_n;\mathbb Q)\cong\widetilde H_1(L_n;\mathbb Q)\). Permuting labels permutes these classes; swapping parts reverses the orientation of each matched edge, multiplying the character by \(-1\). Thus its character is \((-1)^\varepsilon c_1\). Equivariant combinatorial Alexander duality relates the dual homology representations by tensoring with the orientation character of the full \(2n\)-vertex permutation. The simultaneous \(\sigma\)-action is even, while exchanging parts consists of \(n\) transpositions, so this orientation character is \((-1)^{n\varepsilon}\). Multiplying the two \(L_n\) characters by that factor proves both formulas for \(X_n\).

## Verification
The included standalone `CHECK.py` reconstructs every face of the crown three-cut complex and its Alexander dual, verifies the precise chessboard-plus-matching decomposition, and computes exact mod-\(101\) and mod-\(103\) homology ranks for the three first new parameters \(n=5,6,7\). It also checks, for *every* cycle type in \(S_n\) and both swap choices, exact signed simplex-permutation Lefschetz sums against the closed character formulas. The expected output ends in `CHECK_OK`. These finite checks are independent sanity checks of the combinatorial formula, **not** a substitute for the parameter-uniform shellability and duality proof.

## Relationship to prior work
The cut-complex definition, combinatorial duality framework, and previous analysis of other graph families are due to Bayer–Denker–Jelić Milutinović–Rowlands–Sundaram–Xue (2023 preprint; 2024 publication), extended by Bayer–Denker–Jelić Milutinović–Sundaram–Xue (2024 preprint). The necessary shellability of the multiple-chessboard core is Theorem 4.4 of Jojić–Vrećica–Živaljević (2014 preprint; 2015 revision); in particular the core's five-column instance is already understood. The previously documented \(n=4\) crown/three-cube cut-complex case is **excluded**. These ingredients do not themselves state the crown-graph decomposition, its all-\(n\ge5\) two-band integral three-cut homology, or the two complete \(S_n\times C_2\) homology characters established above.

## Limitations
The exact statements concern ordinary three-cut complexes with \(n\ge5\) and the specified natural symmetry. They do not determine the homotopy type or cup products of \(X_n\), do not classify integral representation extensions, and do not address other cut orders or graph modifications. An equivalent unindexed result cannot be excluded by literature searches alone. This mathematical argument has not undergone an independent audit.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (first posted 2023-04-26), https://arxiv.org/abs/2304.13675.
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram, L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158 (first posted 2024-07-11), https://arxiv.org/abs/2407.08158.
3. D. Jojić, S. T. Vrećica, R. T. Živaljević, *Multiple chessboard complexes and the colored Tverberg problem*, arXiv:1412.0386, Theorem 4.4, https://arxiv.org/abs/1412.0386.
