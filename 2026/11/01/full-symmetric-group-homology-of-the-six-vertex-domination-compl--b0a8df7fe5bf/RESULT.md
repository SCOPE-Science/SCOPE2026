# Full symmetric-group homology of the six-vertex domination complex

## Finding
Let \(X=D_{6,3}\) be the simplicial complex on the fifteen edges of the complete graph on \([6]\): an edge set is a face precisely when the corresponding simple graph on all six labeled vertices has domination number at least three. The natural relabeling action of \(S_6\) on \(X\) has the following complete reduced rational homology representations:
\[
\begin{aligned}
\widetilde H_5(X;\mathbb Q)&\cong S^{(5,1)}\oplus S^{(4,2)}\oplus S^{(4,1,1)}\\
&\cong (V\otimes_{\mathbb Q}V)/\mathbf1,\\
\widetilde H_4(X;\mathbb Q)&\cong S^{(5,1)}\oplus2S^{(4,2)}\oplus S^{(4,1,1)}\oplus S^{(3,3)}\\
&\quad\oplus3S^{(3,2,1)}\oplus S^{(3,1,1,1)}\oplus S^{(2,2,2)}\\
&\quad\oplus S^{(2,2,1,1)}\oplus S^{(2,1,1,1,1)}.
\end{aligned}
\]
Here \(S^\lambda\) denotes the rational Specht module for the partition \(\lambda\vdash6\), \(V=S^{(5,1)}\) is the five-dimensional standard module, and \(\mathbf1=S^{(6)}\). All other reduced rational homology groups vanish. In particular, neither nonzero homology group has a trivial \(S_6\)-constituent, and the orbit space \(|X|/S_6\) has vanishing reduced rational homology in every degree.

The nonequivariant homotopy type \(X\simeq\bigvee^{115}S^4\vee\bigvee^{24}S^5\) was determined previously. The new assertion is the full representation in each degree, including the tensor-square structure of the top homology and the quotient consequence.

## Assumptions and scope
A simple undirected graph on the vertex set \([6]=\{1,\ldots,6\}\) includes isolated vertices. A dominating set \(T\) is a vertex set whose closed neighborhoods cover all six vertices; its domination number \(\gamma(G)\) is the least size of such a set. The simplicial vertices of \(X\) are unordered graph edges. A face with \(k\) graph edges has simplicial dimension \(k-1\), with the empty face understood as dimension \(-1\). Relabeling by each element of \(S_6\) permutes the fifteen simplicial vertices. Oriented chains use the increasing lexicographic edge order and the induced permutation sign.

The complex has \(4502\) nonempty faces and face vector \((15,105,455,1185,1647,915,180)\) in dimensions zero through six. Its integral homology is torsion-free, with Betti numbers \((1,0,0,0,115,24,0)\). The result concerns exactly this finite complex and its natural full relabeling action; it does not assert a uniform theorem for other graph orders or domination thresholds.

## Proof
**1. Integral chain complex.** Enumerate the \(2^{15}\) subsets of the fifteen possible graph edges, and retain exactly those for which no one- or two-vertex dominating set exists. Because a dominating singleton extends to a dominating pair, it is enough to test all fifteen pairs. The verifier implements two logically equivalent formulations of this test: unions of closed neighborhoods and intersections of their complements. It checks face closure, the face vector above, and the simplicial boundary-square identity on every face.

For the integer boundary \(\partial_d:C_d(X;\mathbb Z)\longrightarrow C_{d-1}(X;\mathbb Z)\), reduce signed columns in increasing face order against earlier normalized columns, always using the highest nonzero row as pivot. The verifier reconstructs the reduction from first principles and checks that **every nonzero pivot is \(+1\) or \(-1\)**. The complete ranks for \(d=1,\ldots,6\) are
\[
(14,91,364,821,711,180).
\]
The unit-pivot triangular reductions are integral basis changes and exhibit primitive images, so all integral homology is free. The alternating rank formula yields reduced homology only in degrees four and five, with respective ranks \(115\) and \(24\). In particular, \(\partial_6\) is injective.

**2. Exact action on the degree-five boundary image.** The same unit-pivot reduction gives an actual integral basis \(\{b_p\}\) of \(\operatorname{im}\partial_5\subset C_4(X;\mathbb Z)\), with a distinct highest nonzero row \(p\) and coefficient one in each \(b_p\). For a relabeling \(g\), map each oriented four-simplex in \(b_p\) by its induced signed edge permutation; reduce the result in the same basis. The trace of the resulting \(711\times711\) endomorphism is the sum of the coefficient of \(b_p\) in \(g b_p\). This uses only integer additions and subtractions, with no floating-point projection or homology-basis guesses.

Since \(\partial_6\) is injective and equivariant, the degree-five homology character satisfies
\[
\chi_5(g)=\operatorname{tr}(g\mid C_5)-\operatorname{tr}(g\mid\operatorname{im}\partial_5)-\operatorname{tr}(g\mid C_6).
\]
The chain traces count simplices fixed setwise by \(g\), weighted by the sign of the induced permutation of their edge vertices. Represent the eleven conjugacy classes of \(S_6\) by permutations with cycle types
\[
(6),(5,1),(4,2),(4,1,1),(3,3),(3,2,1),(3,1,1,1),(2,2,2),(2,2,1,1),(2,1,1,1,1),(1^6).
\]
In this order, the exact computed degree-five traces are
\[
\chi_5=(0,-1,0,0,0,-1,3,0,0,8,24).
\]
The checker independently repeats the entire image-basis trace calculation with the degree-five columns processed in reverse order; both integral bases give the identical class traces.

**3. Character identification and degree four.** Let \(f(g)\) be the number of fixed points of the permutation \(g\) acting on \([6]\). The standard representation has character \(f(g)-1\). The values just obtained satisfy, on every conjugacy class,
\[
\chi_5(g)=(f(g)-1)^2-1.
\]
Thus \(\widetilde H_5(X;\mathbb Q)\cong (V\otimes V)/\mathbf1\), since rational representations of the finite group \(S_6\) are determined by characters. The classical decomposition of \(V\otimes V\) gives exactly the three Specht constituents stated above.

By equivariant Euler–Poincaré and the absence of other positive-degree homology,
\[
\chi_4(g)-\chi_5(g)=\sum_{d=0}^{6}(-1)^d\operatorname{tr}(g\mid C_d)-1.
\]
The resulting fourth-degree character on the same eleven classes is
\[
\chi_4=(0,0,-1,-1,-2,0,-2,3,3,3,115).
\]
Exact Murnaghan–Nakayama rim-hook recursion evaluates all eleven rational Specht characters. Taking scalar products with the eleven class characters yields the fourth-degree constituent multiplicities in the finding, all nonnegative integers. The dimensions sum to \(115\), and the three fifth-degree dimensions sum to \(24\).

**4. Orbit-space consequence.** Neither character contains the trivial constituent. The finite-group quotient of a simplicial complex (after barycentric subdivision to remove inversions) has rational homology equal to the invariant subspace of the rational homology upstairs. Therefore every reduced rational homology group of \(|X|/S_6\) is zero.

## Verification
Run `python3 artifacts/verify.py` using Python 3 without third-party packages. Its exact integer algorithm builds the entire complex, checks every boundary-square identity, computes the integral unit-pivot ranks, reconstructs signed group actions on chains and boundary images, evaluates every conjugacy-class trace, repeats the image-trace calculation using a second independent pivot ordering, and verifies the Specht multiplicities by rim-hook recursion. Successful execution prints `D63_S6_INTEGRAL_CHAIN_CHARACTER_VERIFIED` and the complete class and decomposition tables. The recorded output appears in `artifacts/verification_output.txt`.

## Relationship to prior work
González and Hoekstra-Mendoza introduced the complexes \(D_{n,k}\), proved a uniform two-sphere wedge theorem for \(D_{n,n-2}\), and explicitly noted only the Euler characteristic \(92\) for \(D_{6,3}\), which is consistent with \(1+115-24\). A later publicly available exact computation established the nonequivariant mixed-dimensional sphere wedge for \(D_{6,3}\), but it did not determine the \(S_6\)-homology actions. Another published representation theorem concerns \(\widetilde H_2(D_{n,n-2};\mathbb Q)\), a **different** filtration level; an adjacent-case calculation for \(D_{7,4}\) also supplies only nonequivariant homotopy information. Their conclusions neither contain nor imply the two characters in this result. Full source comparisons and residual bibliographic risks are recorded in `AUDIT.json` and `REVIEW.md`.

## Limitations
The theorem identifies **rational** \(S_6\)-modules and torsion-free integral groups but not their integral \(\mathbb Z[S_6]\)-lattice isomorphism classes. It neither proves that the orbit space is contractible nor gives its integral homology. The result is specific to six labeled graph vertices and domination threshold three. Search cannot exclude an unindexed equivalent character computation, and no independent external audit is asserted.

## References
1. J. González and T. I. Hoekstra-Mendoza, *On the homotopy type of complexes of graphs with bounded domination number*, arXiv:1901.07130 (first publicly posted 2019-01-22), *Contributions to Discrete Mathematics* 16 (2021), 153–174. https://arxiv.org/abs/1901.07130
2. *A mixed-dimensional sphere wedge for \(D_{6,3}\)*, publicly indexed mathematical record (2026), https://github.com/Resultary/2026/blob/main/2026/10/4/SCOPE-a-mixed-dimensional-sphere-wedge-for-d-6-3--55d89ec4bab2/RESULT.md .
3. *Stable Specht decomposition of \(H_2(D_{n,n-2};\mathbb Q)\)*, publicly indexed mathematical record (2026), https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-stable-specht-decomposition-of-h-2-d-n-n-2-mathbb-q--ab4fa03abdf7/RESULT.md .
4. *The domination complex \(D_{7,4}\) is a mixed-dimensional sphere wedge*, publicly indexed mathematical record (2026), https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-the-domination-complex-d-7-4-is-bigvee-811-s-4-vee-bigvee-84-s-5--e4e894a65756/RESULT.md .
