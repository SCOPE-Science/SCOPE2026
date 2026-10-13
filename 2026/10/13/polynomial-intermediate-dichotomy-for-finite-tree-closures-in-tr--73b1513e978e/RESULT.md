# Polynomial–intermediate dichotomy for finite tree-closures in tree-plan generics

## Finding

Let \(\Gamma=(\Gamma,\lambda)\) be any finite tree plan in Mirabi's sense, with root labeled \(1\) and \(\lambda:\Gamma\to\{1,\infty\}\). Write \(M=\Gamma(\omega)\) for its countable colored rooted tree, and \(\operatorname{tcl}\) for Mirabi's closure: close downwards toward the root and then include every successor whose plan-node label is \(1\). Let \(a_n(\Gamma)\) be the number of color-preserving isomorphism types of finite nonempty \(\operatorname{tcl}\)-closed induced substructures of \(M\) with exactly \(n\) vertices. Put
\[
 F_\Gamma(z)=\sum_{n\ge1}a_n(\Gamma)z^n,
 \qquad A_\Gamma(N)=\sum_{1\le n\le N}a_n(\Gamma).
\]
For each plan node \(\sigma\), define \(F_\sigma(z)\) for rooted closed subtrees above one vertex colored \(\sigma\). If \(C_1(\sigma)\) and \(C_\infty(\sigma)\) are its singleton- and infinity-labeled immediate plan successors, respectively, then the exact recursive generating series is
\[
\boxed{
F_\sigma(z)=z\prod_{\tau\in C_1(\sigma)}F_\tau(z)
 \prod_{\tau\in C_\infty(\sigma)}
 \exp\!\left(\sum_{j\ge1}\frac{F_\tau(z^j)}j\right).}
\]
The recursion starts with \(F_\sigma(z)=z\) at every leaf, and \(F_\Gamma=F_{\langle\rangle}\).

There is a sharp growth dichotomy, determined solely by the position of infinity-nodes in the finite plan:

**Antichain case.** Suppose no two infinity-nodes lie on the same root-to-leaf path. Let \(I=\lambda^{-1}(\infty)\), \(d=|I|\), let \(s_0\) count the plan nodes whose entire root path is singleton-labeled, and let \(s_\sigma\) count all plan descendants of each \(\sigma\in I\), including \(\sigma\). Then
\[
\boxed{F_\Gamma(z)=z^{s_0}\prod_{\sigma\in I}(1-z^{s_\sigma})^{-1}.}
\]
Thus \(a_n(\Gamma)\) is eventually quasipolynomial, and for \(d\ge1\),
\[
\boxed{A_\Gamma(N)\sim\frac{N^d}{d!\prod_{\sigma\in I}s_\sigma}.}
\]
If \(d=0\), the closed tree has one possible finite type and \(A_\Gamma(N)=1\) for all sufficiently large \(N\).

**Nested case.** If some root-to-leaf path contains two infinity-nodes, then for constants \(c,C>0\) depending on the plan,
\[
\boxed{A_\Gamma(N)\ge\exp(c\sqrt N)\quad(N\ge C),
\qquad\log A_\Gamma(N)=o(N).}
\]
Consequently its cumulative finite-closure type spectrum grows strictly faster than every polynomial but strictly slower than every exponential. In particular \(F_\Gamma\) is not a rational function.

For the two-level plan consisting of a root and two successive infinity-nodes, the recursion gives
\[
F_\Gamma(z)=z\prod_{k\ge1}(1-z^k)^{-1},
\qquad a_n(\Gamma)=p(n-1),
\]
where \(p\) is the ordinary integer-partition function. This example has only \(1+m+m^2\) individual vertices in Mirabi's uniform finite approximation \(\Gamma(m)\), yet its closure-type spectrum has intermediate growth. The familiar partition identity is an ingredient, not a claim of novelty.

## Assumptions and scope

The ambient language \(\mathcal L_\Gamma\) contains the rooted-tree order, predecessor and meet, and a unary predicate \(P_\sigma\) for each plan node \(\sigma\). Isomorphisms must preserve these colors. Each finite \(\operatorname{tcl}\)-closed subset of \(M\), with the induced \(\mathcal L_\Gamma\)-structure, is being counted once up to isomorphism. All such sets contain the root. Closure is **Mirabi's tree closure**, not mere closure under the language's function symbols: the latter need not include every singleton-labeled child. The theorem does not identify this family with the author's special uniform approximants \(\Gamma(m)\), and does not count their labeled embeddings.

A plan node \(\tau\) is a descendant of \(\sigma\) when the plan word \(\sigma\) is a prefix of \(\tau\). Products over empty child sets are \(1\). All series are ordinary formal power series with nonnegative integer coefficients; the exponential multiset operator is well defined because each \(F_\tau\) has zero constant coefficient.

## Proof

**1. Recursive classification.** Fix a concrete vertex of plan color \(\sigma\). A finite tree-closed subtree rooted there must contain every child whose plan color has label \(1\), and must contain with it a recursively tree-closed subtree. For an infinity-labeled child color \(\tau\), its parent has countably many indistinguishable \(\tau\)-children. A finite closed subtree may use any finite multiset of the rooted \(\tau\)-types. Different child colors are distinguished by the unary predicates, while children of the same color can be permuted independently. The resulting rooted types are therefore classified uniquely by one choice of each mandatory singleton child type and one multiset for each infinity child type. A multiset of objects with ordinary series \(f(z)=\sum_{k\ge1}b_kz^k\) has series \(\prod_{k\ge1}(1-z^k)^{-b_k}=\exp(\sum_{j\ge1}f(z^j)/j)\). Multiplying the child factors and the vertex weight \(z\) proves the recursion and its completeness by induction on the plan height.

**2. Antichain and exact degree.** If the infinity-nodes form an antichain, each has only singleton-labeled descendants. Every singleton descendant of any selected infinity-copy is forced by tree-closure; that copy contributes exactly \(s_\sigma\) vertices. All vertices above the first infinity-nodes, namely the \(s_0\) vertices, are always present exactly once. Independently for each \(\sigma\in I\), an arbitrary number \(k_\sigma\ge0\) of copies may be selected under its uniquely present singleton-labeled parent. The color predicates distinguish the different \(\sigma\), so the isomorphism type is exactly the vector \((k_\sigma)_{\sigma\in I}\) and its size is \(s_0+\sum_{\sigma\in I}s_\sigma k_\sigma\). This proves the rational generating function. Its poles lie at roots of unity, hence its coefficient sequence is eventually quasipolynomial. The number of nonnegative integer vectors satisfying \(\sum s_\sigma k_\sigma\le N-s_0\) is asymptotic to the Euclidean volume of the corresponding simplex, \(N^d/(d!\prod s_\sigma)\), by standard lattice-point/Riemann-sum estimates.

**3. Nested infinity-nodes give the lower bound.** Choose an infinity-node \(\alpha\) with only singleton-labeled strict ancestors and a strict infinity descendant \(\beta\), chosen with no infinity-node strictly between \(\alpha\) and \(\beta\). At the (compulsorily present) parent of \(\alpha\), arbitrarily many \(\alpha\)-branches may occur. Within any such branch, select no optional infinity successors except \(j\) copies of \(\beta\) at its forced ancestor. In each \(\beta\)-copy choose no optional infinity successors. All singleton successors are included as closure requires. There are fixed positive integers \(b,c\) such that these \(\alpha\)-branch types have pairwise distinct sizes \(b+cj\), for \(j=0,1,2,\ldots\). For each subset \(S\subseteq\{0,1,\ldots,k-1\}\), take one \(\alpha\)-branch of each selected type and no other optional branches. Different \(S\) yield nonisomorphic colored trees; all have at most \(O(k^2)\) vertices. Hence \(A_\Gamma(C_0 k^2)\ge2^k\) for some \(C_0\), implying \(A_\Gamma(N)\ge\exp(c_0\sqrt N)\) for sufficiently large \(N\). In particular no polynomial can bound the cumulative profile.

**4. Subexponential upper bound.** We show inductively that each \(F_\sigma(r)\) is finite for every real \(0<r<1\). It is immediate for leaves. Given this for all children, the multiset exponent \(\sum_{j\ge1}F_\tau(r^j)/j\) converges: its tail is \(O(\sum_{j\ge j_0}r^j/j)\), because \(F_\tau(t)=O(t)\) near \(t=0\). The finite child products therefore converge. For every \(0<r<1\), nonnegativity gives \(A_\Gamma(N)\le r^{-N}F_\Gamma(r)\), so \(\limsup_{N\to\infty}N^{-1}\log A_\Gamma(N)\le-\log r\). Letting \(r\uparrow1\) yields the asserted \(o(N)\). The superpolynomial lower bound, together with this upper bound, also rules out a rational generating function: a rational series with nonnegative coefficients, radius at least \(1\), and no exponential coefficient growth has at most polynomially growing cumulative coefficients (all poles have modulus at least \(1\)).

The converse directions are covered: every plan either has an antichain of infinity-nodes or contains a comparable pair, and the empty infinity set is addressed separately.

## Verification

Run the bundled standard-library program `python3 verify.py`. It constructs actual finite colored tree plans \(\Gamma(2)\), enumerates all optional infinity-node selections and their **independently computed tree closures**, classifies the resulting finite structures by recursive color-preserving isomorphism invariants, and compares those classes with a separate bounded-multiset construction. It also computes the unbounded series by integer-arithmetic plethystic product, verifies the antichain rational formula on all \(4{,}283\) increasing-parent plan encodings through six nodes (including \(2{,}107\) antichain-label plans), and checks the two-infinity example against Euler's independently implemented pentagonal recurrence for partition numbers.

Recorded replay:

`VERIFY_OK 42474 exact assertions; 1444 labelled finite-node selections screened; 7 tree-plan shapes compared by direct isomorphism invariants; 4283 exhaustive small plans incl. 2107 antichain plans`

The finite checks are regression evidence for the structural recursion and small cases, not a proof of the asymptotic dichotomy; its general proof is given above.

## Relationship to prior work

Mirabi (2023, Sections 3–5) defines finite tree plans, \(\operatorname{tcl}\), colored generic trees and polynomial finite approximants, and establishes their model-theoretic properties. His counting polynomial \(P(\Gamma;m)=|\Gamma(m)|\) counts *vertices in the uniform finite approximants*, not isomorphism types of finite tree-closed subsets. The present recursive multiset series and its growth criterion address the latter, different invariant; indeed the depth-two infinity plan provides a direct polynomial-versus-partition contrast. The inspected primary full text has no generating-function or finite-closure-profile calculation of this kind.

Falque and Thiéry (2020) classify oligomorphic permutation groups with polynomial *subset-orbit* profiles and recover rational Hilbert series. This is broad relevant background on profile growth, but its counted objects are fixed-cardinality subsets of the full carrier rather than finite tree-closure hulls graded by their number of closure vertices, and it does not state the criterion or formula for Mirabi's tree plans. Classical unlabeled-tree and integer-partition generating functions explain the multiset step and some special cases; these combinatorial ingredients are not claimed as new. The novelty claim is restricted to the exact closure-spectrum calculus and uniform infinity-node comparability dichotomy in this specific semantic construction.

Candidate-specific searches for tree plans, tree-closure growth, profile series, nested infinity-nodes, oligomorphic wreath-product profiles, and restricted partitions did not locate an equivalent full theorem. An unindexed combinatorial derivation or a reformulation in the general theory of ages and Pólya species remains a real originality risk.

## Limitations

This is a result about the finite tree-closure operator of a colored generic tree, not about the number of arbitrary finite subsets, uncolored-tree isomorphism classes, first-order type counts, or the sizes \(|\Gamma(m)|\) of finite approximants. It does not give a sharp stretched-exponential exponent for nested plans, only the universal lower bound \(\exp(\Omega(\sqrt N))\) and a subexponential upper bound. The count at any single size can vanish for congruence reasons; the dichotomy and asymptotic formula are deliberately stated for the cumulative profile. No independent mathematical audit has been performed.

## References

1. Mostafa Mirabi, *Asymptotic Classes of Trees and \(\aleph_0\)-Categoricity*, arXiv:2307.07899v1, first posted 2023-07-15, https://arxiv.org/html/2307.07899v1 ; especially Definitions 3.0.1, 3.0.2, 3.0.5, Remark 3.0.6, and Section 5.1.
2. Justine Falque and Nicolas M. Thiéry, *Classification of \(P\)-Oligomorphic Groups, Conjectures of Cameron and Macpherson*, arXiv:2005.05296v2 (2020), https://arxiv.org/html/2005.05296v2 ; especially Sections 1.1–1.3 and 2.
3. Nicolas Broutin and Philippe Flajolet, *The Distribution of Height and Diameter in Random Non-plane Binary Trees*, Random Structures & Algorithms 41 (2012), 215–252, https://doi.org/10.1002/rsa.20393 ; cited only as background on generating functions for finite-height unlabelled trees, not as a source for the specific tree-plan theorem.
