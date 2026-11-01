# An essential modular extension in seven-vertex matching homology

## Finding
Let \(M_7\) be the ordinary matching complex of the complete graph on seven vertices, and put \(k=\mathbb F_3\). The natural \(\mathfrak S_7\)-equivariant universal-coefficient short exact sequence in degree two is **nonsplit as a sequence of \(k[\mathfrak S_7]\)-modules**:
\[
0\longrightarrow H_2(M_7;\mathbb Z)\otimes k
\longrightarrow H_2(M_7;k)
\longrightarrow \operatorname{Tor}_1^{\mathbb Z}(H_1(M_7;\mathbb Z),k)
\longrightarrow 0.
\]
The left term has dimension \(20\), the middle term dimension \(21\), and the one-dimensional quotient is the sign representation \(k_{\mathrm{sgn}}\). In particular, there is no \(\mathfrak S_7\)-equivariant section from the sign quotient back to degree-two mod-three homology, although a nonequivariant linear section exists.

## Assumptions and scope
The vertex set of \(M_7\) consists of the \(21\) two-element subsets of \(\{1,\ldots,7\}\). A face is a collection of pairwise disjoint edges. Its maximal faces consist of three edges and have dimension two. The symmetric group acts by relabeling the seven vertices; chain orientations are determined by an arbitrary fixed total ordering of the edges. All homology is ordinary simplicial homology and coefficients carry the trivial action before induction by naturality.

## Proof
**1. Integral input and ranks.** Bouc's integral calculation gives \(\widetilde H_1(M_7;\mathbb Z)\cong\mathbb Z/3\), and the complex is connected. Its numbers of simplices in dimensions zero, one, and two are respectively \(21\), \(105\), \(105\): an oriented matching of two edges is chosen from four underlying vertices, and a matching of three edges from six. Thus its unreduced Euler characteristic is \(21-105+105=21\). As \(H_0\cong\mathbb Z\) and \(H_1\) has rank zero, its second Betti number is \(20\). There are no simplices in dimension three. Consequently \(H_2(M_7;\mathbb Z)=\ker\partial_2\subset C_2(M_7;\mathbb Z)\) is free abelian of rank \(20\).

**2. Torsion character.** An explicit nonzero generator of the order-three group \(H_1(M_7;\mathbb Z)\), as in the known matching-complex description, is represented (up to the usual join sign) by
\[
z=(\{1,2\}-\{1,3\})\wedge(\{4,5\}-\{4,6\}).
\]
Each parenthesized difference is a reduced zero-cycle on two matching-complex vertices; disjoint supports make their join a one-cycle. The transposition \((2\ 3)\) sends \(z\) to \(-z\), so it acts as multiplication by \(-1\) on \(H_1(M_7;\mathbb Z)\). Since the action is one-dimensional and all transpositions are conjugate and generate \(\mathfrak S_7\), the complete action is the sign character. The naturality of \(\operatorname{Tor}_1^{\mathbb Z}(-,k)\) sends multiplication by \(\pm1\) on \(\mathbb Z/3\) to the same scalar on \(k\). Hence the universal-coefficient quotient is \(k_{\mathrm{sgn}}\).

**3. The missing sign submodule.** Take any oriented maximal matching \(\sigma=(e_1,e_2,e_3)\). Exchange the two underlying graph vertices belonging to edge \(e_1\). This is an odd permutation \(t_\sigma\in\mathfrak S_7\) that fixes **each matching-complex vertex** \(e_1,e_2,e_3\), hence fixes the oriented simplex \(\sigma\) with positive sign. Suppose a chain \(c\in C_2(M_7;k)\) spans a sign subrepresentation. Writing \(a_\sigma\) for its \(\sigma\)-coordinate, the equation \(t_\sigma c=-c\) gives \(a_\sigma=-a_\sigma\). Because \(2\ne0\) in \(k\), \(a_\sigma=0\). This holds for each of the \(105\) maximal matchings, so \(C_2(M_7;k)\) contains **no nonzero sign submodule**. Since there are no three-simplices, \(H_2(M_7;k)=\ker\partial_2\) is a submodule of \(C_2(M_7;k)\), and likewise contains no sign submodule.

**4. Nonsplitting.** If the natural universal-coefficient sequence split equivariantly, its section would inject its sign-character quotient as a sign submodule of \(H_2(M_7;k)\), contradicting step 3. Therefore the extension is nonsplit. The universal coefficient theorem gives its middle dimension \(20+1=21\). This completes the proof.

## Verification
The included `verify_m7.py` reconstructs all \(21,105,105\) simplices, checks \(\partial_1\partial_2=0\), and computes boundary ranks \(20,84\) over \(\mathbb F_3\), giving dimensions one and \(21\) for degree-one and degree-two mod-three homology. It computes a nontrivial cohomology class and confirms a transposition acts on that class by \(-1\). Every one of the \(105\) facets is independently checked to admit the required odd pointwise stabilizer. These finite checks corroborate the exact conceptual proof; the established integral order-three theorem is used as a cited input, not inferred from finite-field ranks.

## Relationship to prior work
Bouc determined the integral order-three group and complex-homology symmetric-group characters. Shareshian and Wachs (initial public preprint September 3, 2004) explain the integral torsion and give a family of explicit low-degree generators; Jonsson studies integral exact sequences and the dimensions of homology over \(\mathbb Z/3\). These results determine the groups or portions of their characters, not whether the **natural equivariant universal-coefficient extension** splits. The new point is the incompatibility between the sign quotient and the oriented top-chain stabilizers, not a new computation of integral homology groups.

## Limitations
The theorem concerns the single first torsion-bearing complete-graph matching complex, the prime three, and this canonical degree-two short exact sequence. It does not assert that the full \(21\)-dimensional middle module is indecomposable, determine its complete modular composition series, or resolve higher matching complexes. The novelty assessment is limited by potentially unindexed equivalent modular-representation results; the scientific review is not independent certification.

## References
- John Shareshian and Michelle L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, first publicly posted September 3, 2004, arXiv:math/0409054, §§1–3 (particularly Bouc's theorem and Lemma 2.5), https://arxiv.org/abs/math/0409054.
- Jakob Jonsson, *Exact Sequences for the Homology of the Matching Complex*, Journal of Combinatorial Theory Series A 115 (2008), 1504–1526; arXiv:1203.5641, https://arxiv.org/abs/1203.5641.
- Serge Bouc, *Homologie de certains ensembles de 2-sous-groupes des groupes symétriques*, Journal of Algebra (1992); cited through Shareshian–Wachs's accessible statement of his result.
