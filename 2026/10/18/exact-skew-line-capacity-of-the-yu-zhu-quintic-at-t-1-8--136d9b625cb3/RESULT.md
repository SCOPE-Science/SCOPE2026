# Exact skew-line capacity of the Yu–Zhu quintic at \(t=-1/8\)

## Finding
Let \(X\subset\mathbb P^3_{\mathbb C}\) be the smooth quintic
\[
X:\quad (x_3-x_4)(x_1^4-3x_2^4)-6(x_3+x_4)x_1^2x_2^2
+x_3x_4\bigl(x_4^3+\tfrac18x_3^3\bigr)=0.
\]
Then **the largest collection of pairwise skew (mutually disjoint) projective lines on \(X\) has exactly \(18\) members**. In the labeling \(L_1,\ldots,L_{85}\) from Yu and Zhu, arXiv:2609.26862v1, Section 3.2, one such maximum collection is
\[
\{L_2,L_6,L_{38},L_{39},\ldots,L_{53}\}.
\]
This is an exact finite classification of the maximum, not merely a construction of eighteen skew lines.

## Assumptions and scope
The base field is \(\mathbb C\), and the member \(X=X_{-1/8}\) is fixed. Yu and Zhu prove that it is smooth and that the displayed labeled \(85\) lines are **all** its projective lines. This completeness is a cited premise, not an independently claimed result. Two distinct lines are skew if they have no common projective point. The result does not assert the same optimum for other parameters of the pencil, or for arbitrary curves on \(X\).

## Proof
**Exact incidence.** Each source line \(L_j\) is given by two linear equations; all \(85\) pairs of equations are reproduced in the standalone checker `artifacts/verify_skew_capacity.py`. Their coefficients belong to
\[
K=\mathbb Q(i,a,b),\quad i^2=-1,\quad a^4=2,\quad b^4=3.
\]
Indeed \(\sqrt3=b^2\), \(\sqrt[4]{12}=a^2b\), \(\sqrt[4]{18}=ab^2\), and \(\sqrt[4]{6}=ab\). These form a degree-\(32\) number field over \(\mathbb Q\): over \(\mathbb Q(i)\), the classes of \(2\) and \(3\) are independent of order four modulo fourth powers. Independence follows first from the valuation at the Gaussian prime \(3\), and then from the fact that \(\sqrt2\notin\mathbb Q(i)\). Kummer theory therefore supplies a basis \(i^e a^r b^s\) with \(0\le e<2\) and \(0\le r,s<4\). The checker represents each coefficient as an integer vector in this basis with exact reduction rules, not a floating-point approximation.

For lines defined by linear forms \((\ell_1,\ell_2)\) and \((m_1,m_2)\), their projective intersection is nonempty if and only if the determinant of the four coefficient rows vanishes. Expanding by the six \(2\times2\) minors gives the exact incidence test used in the checker. It yields \(850\) meeting pairs, every vertex has \(20\) neighbors, and the adjacent-pair common-neighbor census is \(530\) with three common neighbors and \(320\) with none. These independent consistency invariants agree with the previously published incidence-spectrum calculation.

**Lower bound.** The exact incidence matrix confirms that no two members of the displayed \(18\)-line set intersect, so the maximum is at least \(18\).

**Upper bound.** Let \(G\) be the graph of the \(85\) lines, with an edge when two lines meet. The following \(19\) sets of five vertices are cliques of \(G\) and together cover every vertex (each edge within each displayed set is tested exactly by the checker):
\[
\begin{aligned}
C_1&=\{1,2,3,4,5\},&C_2&=\{1,6,7,8,9\},\\
C_3&=\{18,22,50,64,75\},&C_4&=\{14,23,48,59,85\},\\
C_5&=\{18,24,52,62,77\},&C_6&=\{10,25,44,66,80\},\\
C_7&=\{19,26,49,67,73\},&C_8&=\{15,27,51,57,80\},\\
C_9&=\{19,28,47,69,71\},&C_{10}&=\{11,29,38,65,83\},\\
C_{11}&=\{20,30,43,54,84\},&C_{12}&=\{16,31,38,68,74\},\\
C_{13}&=\{20,32,45,56,82\},&C_{14}&=\{12,33,53,59,70\},\\
C_{15}&=\{17,34,42,63,72\},&C_{16}&=\{13,34,46,55,76\},\\
C_{17}&=\{21,35,39,60,81\},&C_{18}&=\{21,36,40,61,78\},\\
C_{19}&=\{21,37,41,58,79\}.&&
\end{aligned}
\]
A pairwise skew set contains at most one vertex from each clique, hence at most \(19\). If it had \(19\), it would have exactly one from each clique, and could contain **no vertex occurring in two or more covering cliques**: such a vertex consumes at least two clique capacities. Removing all multiply occurring vertices from the eight cliques with indices
\[\{4,8,10,12,14,15,16,18\}\]
leaves, in the same order, precisely
\[
\begin{gathered}
\{14,23,48,85\},\quad\{15,27,51,57\},\quad
\{11,29,65,83\},\quad\{16,31,68,74\},\\
\{12,33,53,70\},\quad\{17,42,63,72\},\quad
\{13,46,55,76\},\quad\{36,40,61,78\}.
\end{gathered}
\]
The checker exhausts all \(4^8=65{,}536\) choices of one vertex from each of these eight four-element sets. **Every choice contains a pair joined by an edge of \(G\)**. This is an exhaustive finite certificate, using the previously established exact incidence test; no \(19\)-line skew set exists. A separate exact bitset branch-and-color algorithm explores \(2{,}575\) nodes and independently certifies that no skew clique of size \(19\) exists in the complement graph. Hence the maximum is exactly \(18\).

## Verification
Run `python3 artifacts/verify_skew_capacity.py` using the Python standard library. The program reconstructs all \(85\) cited line equations over the exact \(32\)-dimensional coefficient basis, tests all \(\binom{85}{2}=3{,}570\) pairs, checks the incidence census and displayed witness, verifies the full \(19\)-clique cover, exhaustively rules out all \(65{,}536\) eight-block transversals, and independently searches the complement graph. Its successful final marker is `YU_ZHU_85_SKEW_MAXIMUM_EXACT_OK`. The program has no external data files, computer algebra package requirements, or numerical tolerance.

## Relationship to prior work
Yu and Zhu (2026) construct this \(85\)-line quintic, determine all its lines, and compute the rank of its line-intersection lattice. Their Section 5 constructs **different** smooth quintics with \(79\) lines and exhibits \(24\) mutually skew lines on some of those surfaces. It does not give a sharp skew-line maximum for \(X_{-1/8}\). A published mathematical note, *Integral spectrum of the 85-line incidence graph on the Yu--Zhu quintic*, independently computes the present graph's regularity, spectrum, and common-neighbor profile but does not state its independence number. A spectrum, even together with regularity and rank, does not in general determine an independence number. The contribution here is the sharp geometric capacity and an explicit compact covering-plus-exhaustion certificate, not the underlying line list, adjacency graph, or a new general graph algorithm. Miyaoka's general inequality gives a much weaker upper bound of \(30\) skew lines on a smooth quintic.

## Limitations
The result is for the named parameter only. Although the source gives the \(85\) line equations and proves their completeness, this work does not independently reprove the absence of additional lines. The exact finite search proves the stated upper bound once those source equations and their completeness are accepted; it does not establish an abstract upper bound for all quintics. A literature search, including an exact comparison with the published incidence-spectrum note, found no already stated value \(18\), but inaccessible or unpublished prior computations may exist. No independent external scientific audit has been performed.

## References
1. X. Yu and Z. Zhu, *A smooth quintic surface with 85 lines and Picard number 43*, arXiv:2609.26862v1 (first public 22 September 2026), Theorem 1.1, Section 3.2, Theorem 5.1. https://arxiv.org/html/2609.26862v1
2. *Integral spectrum of the 85-line incidence graph on the Yu--Zhu quintic* (2026), publicly available mathematical result, especially its RESULT.md: https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-integral-spectrum-of-the-85-line-incidence-graph-on-the-yu-zhu-q--067e669d2fbd/RESULT.md
3. Y. Miyaoka, *The maximal number of quotient singularities on surfaces with given numerical invariants*, Math. Ann. 268 (1984), as cited by Yu–Zhu for the general skew-line bound.
