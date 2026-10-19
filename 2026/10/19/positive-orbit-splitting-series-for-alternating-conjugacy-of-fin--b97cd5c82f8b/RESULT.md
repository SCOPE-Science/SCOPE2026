# Positive orbit-splitting series for alternating conjugacy of finite transformations

## Finding
Let \(n\ge2\), let \(T_n\) be the monoid of all functions \(f:[n]\to[n]\), and let \(S_n\) and \(A_n\) act by relabeling, equivalently conjugation. A symmetric orbit **splits** when it is the union of two distinct alternating-group orbits. The theorem below classifies every splitting orbit by its functional digraph and gives a positive, recursively computable ordinary generating function for the number \(g_n\) of such orbits. The values for \(n=2,\ldots,9\) are
\[
(g_2,\ldots,g_9)=(1,4,9,20,45,111,276,666).
\]
The corresponding numbers of alternating-group orbits are
\[
(4,11,28,67,175,454,1227,3281).
\]
The novelty claimed here is the **parity-restricted structural classification and its positive nested generating series**, not the standard cycle-index or Burnside formula alone.

A finite rooted in-tree is called **even-stable** when every automorphism of the rooted tree induces an even permutation of all its vertices. This property holds exactly when (i) every immediate child rooted tree is even-stable, and (ii) each isomorphism type of a child tree of odd order occurs at most once. An even-order child type may have any multiplicity.

A connected functional digraph is represented by a directed cyclic word \((T_1,\ldots,T_\ell)\) of rooted in-trees, with each root on the directed cycle. Let \(p\) be its minimal cyclic period, let \(t=\ell/p\), and let \(w\) be the total number of vertices in one minimal repeating block of \(p\) rooted trees. The component is **even-stable** exactly when every \(T_i\) is even-stable and either \(t\) is odd or \(w\) is even. Finally, a functional digraph is even-stable exactly when all its connected components are even-stable and no isomorphism type of **odd-order connected component** occurs more than once. For \(n\ge2\), its symmetric orbit splits exactly when its functional digraph is even-stable.

Here is the precise all-degree enumeration. Write \(r_m\) for the number of even-stable unlabeled rooted in-trees of order \(m\), and set \(R(x)=\sum_{m\ge1}r_mx^m\). Its recursive equation is
\[
R(x)=x\left(\prod_{\substack{m\ge1\\m\text{ even}}}(1-x^m)^{-r_m}\right)
\left(\prod_{\substack{m\ge1\\m\text{ odd}}}(1+x^m)^{r_m}\right).
\]
The coefficient at degree \(m\) on the right depends only on \(r_1,\ldots,r_{m-1}\), so the equation uniquely specifies the series with zero constant term. Let \(\varphi\) and \(\mu\) be Euler's totient and the number-theoretic Möbius function. Define weighted cyclic-necklace and primitive-necklace series
\[
C_R(x)=\sum_{\ell\ge1}\frac1\ell\sum_{d\mid\ell}\varphi(d)R(x^d)^{\ell/d},\qquad
P_R(x)=\sum_{\ell\ge1}\frac1\ell\sum_{d\mid\ell}\mu(d)R(x^d)^{\ell/d}.
\]
Put \(P_R^{\mathrm{odd}}(x)=(P_R(x)-P_R(-x))/2\), and
\[
E(x)=C_R(x)-\sum_{j\ge1}P_R^{\mathrm{odd}}(x^{2j})=\sum_{m\ge1}e_mx^m.
\]
Then \(e_m\) counts even-stable connected functional digraphs of order \(m\), and the required positive generating series is
\[
\boxed{G(x)=\prod_{\substack{m\ge1\\m\text{ even}}}(1-x^m)^{-e_m}
\prod_{\substack{m\ge1\\m\text{ odd}}}(1+x^m)^{e_m}.}
\]
For every \(n\ge2\), \(g_n=[x^n]G(x)\); the total number of alternating orbits equals \(s_n+g_n\), where \(s_n\) is the standard number of unlabeled endofunctions on \(n\) points. The constant and linear coefficients of \(G(x)\) are bookkeeping terms only: \(A_0=S_0\) and \(A_1=S_1\) do not have index two.

An independent signed finite formula makes the result directly computable without constructing trees. For a partition \(\lambda\vdash n\), denote by \(m_d(\lambda)\) the multiplicity of part \(d\), and let \(\ell(\lambda)\) be its number of parts. For \(n\ge2\),
\[
\boxed{g_n=\sum_{\lambda\vdash n}(-1)^{n-\ell(\lambda)}
\frac{\displaystyle\prod_{d\ge1}\left(\sum_{e\mid d}e\,m_e(\lambda)\right)^{m_d(\lambda)}}
{\displaystyle\prod_{d\ge1}d^{m_d(\lambda)}m_d(\lambda)!}.}
\]
Factors having exponent zero are interpreted as one. The positive Euler product explains the nonnegativity and the combinatorial meaning of this cancellation-heavy signed sum.

## Assumptions and scope
All sets are finite and unlabeled isomorphism classes are used only when explicitly stated. The alternating group acts by its usual even permutations of the \(n\) underlying vertices. Loops in functional digraphs (fixed points of the transformation) are permitted. Repeated rooted-tree and component types mean actual rooted or directed-graph isomorphism, respectively. Rotations, but **not reflections**, preserve the oriented directed cycle. The theorem concerns ordinary conjugation by permutations, not the broader natural-conjugacy equivalence studied for semigroups. All displayed infinite products and series are formal power series in \(\mathbb Z[[x]]\) or \(\mathbb Q[[x]]\), with finitely many terms contributing to every given coefficient.

## Proof
**Step 1: the subgroup criterion.** For an action of \(S_n\) on a set, an orbit splits on restriction to its normal index-two subgroup \(A_n\) if and only if the stabilizer of a representative is contained in \(A_n\). Here that stabilizer is precisely the vertex-permutation automorphism group of the functional digraph. This identifies splitting with the absence of odd digraph automorphisms, but does not by itself enumerate the objects.

**Step 2: rooted trees.** At a root, the automorphism group is assembled from the automorphism groups of the child trees and permutations of identical child copies. An odd internal automorphism extends to an odd automorphism of the whole tree. For an isomorphism type of child tree having \(m\) vertices, exchanging two copies changes parity by \((-1)^m\): the permutation is the product of \(m\) transpositions. Such swaps generate the symmetric group on equal copies. Hence exactly the recursive even-stability criterion stated above holds. Its multisets of allowed children contribute a factor \(1+x^m\) per odd-order type, since at most one copy is allowed, and \((1-x^m)^{-1}\) per even-order type. Grouping types by their orders proves the equation for \(R(x)\).

**Step 3: a cyclic component.** Internal automorphisms of any attached tree extend independently, so every attached tree must be even-stable. The group of allowed cycle rotations is cyclic of order \(t\), where \(t\) is the number of repetitions of the primitive cyclic word. The generator moves the \(t\) isomorphic copies of a primitive block of total size \(w\) cyclically. It therefore has permutation sign \((-1)^{w(t-1)}\): identify matching vertex positions coherently around the block cycle. Every alternative choice of these identifications differs by even internal rooted-tree automorphisms. Because the rotations are generated by this element, they are all even exactly when \(t\) is odd or \(w\) is even. This proves the component criterion, including the single-loop and pure-cycle boundary cases.

**Step 4: connected generating series.** Standard weighted necklace counting by rotation gives \(C_R\); Möbius inversion on the length-period divisor lattice gives \(P_R\), whose objects have a primitive cyclic word. The forbidden connected objects have a unique primitive word of **odd total order** repeated an **even number** \(2j\) of times. Their series is exactly \(\sum_{j\ge1}P_R^{\mathrm{odd}}(x^{2j})\), with no overcount because primitive periods are unique. Subtraction yields \(E\) with nonnegative integer coefficients \(e_m\).

**Step 5: disconnected generating series.** Every functional digraph decomposes uniquely as a multiset of connected ones. Its automorphism group includes the internal automorphism groups and the swaps of isomorphic components. A swap of equal connected components of order \(m\) has sign \((-1)^m\). Thus every odd-order component type may appear at most once, while any even-order type may repeat. For each of the \(e_m\) eligible types the generating factor is, respectively, \(1+x^m\) or \((1-x^m)^{-1}\). Multiplication proves the formula for \(G\), and Step 1 identifies its coefficients with the number of splitting symmetric orbits.

**Step 6: independent signed count.** A permutation having cycle-type multiplicities \(m_d\) commutes with exactly \(\prod_d(\sum_{e\mid d}e\,m_e)^{m_d}\) endofunctions: each domain cycle of length \(d\) may send a distinguished point to any vertex on a target cycle whose length divides \(d\). In the symmetric group, the proportion of permutations with partition \(\lambda\) is the reciprocal of \(\prod_d d^{m_d}m_d!\), and their sign is \((-1)^{n-\ell(\lambda)}\). Apply Burnside to \(S_n\) and \(A_n\) and subtract. Since the alternating group has index two for \(n\ge2\), the difference equals precisely the number of split symmetric orbits. This proves the partition formula and independently checks the Euler-product interpretation.

## Verification
Run \(\texttt{python3 verify_parity.py}\) in the same directory. The packaged standard-library checker implements four separately organized tests: exact signed Burnside partition sums through order 15; coefficient extraction from the positive rooted-tree/necklace products through order 9; direct construction of canonical rooted trees, cyclic components, and component multisets through order 9; and exhaustive labeled enumeration of all \(n^n\) functions with actual symmetric and alternating conjugation, through order 5. All comparisons passed. The first even-stable rooted-tree counts for orders \(1\) through \(9\) are \(1,1,1,2,4,8,16,34,75\), and the eligible connected counts are \(1,1,3,5,11,22,51,117,268\). Computation verifies the listed small cases only; the infinite result follows from Steps 1–6.

## Relationship to prior work
Araújo, Bentz, Kinyon, Konieczny, Malheiro, and Mercier (2023, arXiv:2301.04252), especially Section 4.3, identify permutation conjugacy for transformations with isomorphism of their functional digraphs and compare it with other semigroup conjugacies. Akman and Akman (2018, DOI:10.3389/fams.2018.00028), Sections 2.1–2.4, develop the component, cyclic-block, and rooted-tree automorphism decompositions. Both provide important structural premises here, **not** the parity-restricted recursive generating series in the passages inspected. Defrain, Porreca, and Timofeeva (2023, arXiv:2302.13832), Sections 2–4, give canonical codes and polynomial-delay generation of ordinary functional-digraph isomorphism types; that algorithm does not distinguish parity of graph automorphisms. Bhunia, Kaur, and Singh (2017, arXiv:1705.06651) analyze alternating-group class splitting and centralizers of **permutations themselves**, not the alternating action on all transformations. OEIS A001372 supplies the classical total count \(s_n\) for symmetric conjugacy. The ordinary signed Burnside identity is a direct application of established orbit counting and is not presented as independently novel; the positive all-degree parity-restricted species and its explicit classification are the assessed addition.

## Limitations
The theorem does not classify conjugacy under a different subgroup, and it does not give closed asymptotics for \(g_n\). The positive recursion determines exact coefficients and splitting types but may be computationally more costly than the signed partition formula for large orders. The literature review cannot rule out an equivalent parity-restricted enumeration indexed elsewhere, and the structural automorphism decompositions are prior results. Independent mathematical audit has not been performed.

## References
1. S. Bhunia, D. Kaur, and A. Singh, *z-Classes and Rational Conjugacy Classes in Alternating Groups*, arXiv:1705.06651, first public version 2017-05-18, https://arxiv.org/abs/1705.06651.
2. D. D. Akman and F. F. Akman, *Spectral Functional-Digraph Theory, Stability, and Entropy for Gene Regulatory Networks*, Frontiers in Applied Mathematics and Statistics (2018), DOI:10.3389/fams.2018.00028, https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2018.00028/full.
3. J. Araújo, W. Bentz, M. Kinyon, J. Konieczny, A. Malheiro, and V. Mercier, *Conjugacy in Semigroups: the Partition and Brauer Diagram Monoids, Conjugacy Growth, and Partial Inner Automorphisms*, arXiv:2301.04252, first public version 2023-01-11, https://arxiv.org/abs/2301.04252.
4. O. Defrain, A. E. Porreca, and E. Timofeeva, *Polynomial-delay generation of functional digraphs up to isomorphism*, arXiv:2302.13832, first posted 2023-02-27, https://arxiv.org/abs/2302.13832.
5. OEIS, *A001372: Number of unlabeled mappings (mapping patterns)*, https://oeis.org/A001372.
